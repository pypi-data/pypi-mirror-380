import os
import pandas as pd
from datetime import datetime, date, time


def get_smn_stations_info(full_description=False):
    """ 
    Get information about the meteorological measurements stations from the SwissMetNet (SMN) network.

    ARGUMENTS: 
        - full_description (boolean, default=False): if True, then all available metadata is returned ; by default
                                                     a selection of the most relevant metadata is returned 

    RETURNS: a pd.DataFrame with the list of all stations from the SMN network and their description.
    """
    URL = "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_stations.csv"
    smn_stations = pd.read_csv(URL, delimiter=';', encoding='iso-8859-1')

    if full_description:
        return smn_stations
    else:
        essential_info = smn_stations[[
            'station_abbr', 'station_name', 'station_canton',
            'station_type_en', 'station_data_since', 'station_height_masl',
            'station_coordinates_lv95_east', 'station_coordinates_lv95_north',
            'station_coordinates_wgs84_lat', 'station_coordinates_wgs84_lon'
        ]]
        return essential_info


def get_meteo_parameters_info(full_description=False, lookup=None, language='fr'):
    """ 
    Get information about all available meteorological parameters.

    ARGUMENTS: 
        - full_description (boolean, default=False): if True, then all available metadata is returned ; by default
                                                     a selection of the most relevant metadata is returned
        - lookup (string, optional): allows to filter according to a group of parameters (temperature, precipitation, wind...)
                                     only parameters that contain the lookup string are then returned. The lookup is case-insensitive,
                                     but sensitive to accents. 
        - language ('fr' or 'en', default='fr'): whether the lookup and the output should be in french ('fr') or english ('en')

    RETURNS: a pd.DataFrame with the list of all available meteorological parameters and their description.
    """
    URL = "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_parameters.csv"
    meteo_parameters = pd.read_csv(URL, delimiter=';', encoding='iso-8859-1')

    if lookup is not None:
        if language == 'en':
            meteo_parameters = meteo_parameters.query('parameter_group_en.str.contains(@lookup, case=False)')
        else:
            meteo_parameters = meteo_parameters.query('parameter_group_fr.str.contains(@lookup, case=False)')
   
    if full_description:
        return meteo_parameters
    else:
        essential_info = meteo_parameters[[
            'parameter_shortname', 'parameter_description_' + language,
            'parameter_group_' + language, 'parameter_granularity',
            'parameter_decimals', 'parameter_datatype', 'parameter_unit'
        ]]
        return essential_info


def get_parameters_by_station(sta, full_description=False, lookup=None, language='fr'):
    """ 
    Get information about all available meteorological parameters for a given meteorological station.

    ARGUMENTS:
        - sta (string): the SwissMetNet meteorological station (e.g. GVE, CGI, PAY,...)
        - full_description (boolean, default=False): if True, then all available metadata is returned ; by default
                                                     a selection of the most relevant metadata is returned
        - lookup (string, optional): allows to filter according to a group of parameters (temperature, precipitation, wind...)
                                     only parameters that contain the lookup string are then returned. The lookup is case-insensitive,
                                     but sensitive to accents. 
        - language ('fr' or 'en', default='fr'): whether the lookup and the output should be in french ('fr') or english ('en')

    RETURNS: a pd.DataFrame with the list of all available meteorological parameters for 'sta' and their description.
    """
    URL = "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_datainventory.csv"
    data_inventory = pd.read_csv(URL, delimiter=';', encoding='iso-8859-1')
    sta_params = data_inventory.loc[data_inventory['station_abbr'] == sta]

    if full_description:
        pass
    else:
        sta_params = sta_params[['station_abbr', 'parameter_shortname', 'data_since', 'data_till']]

    output = pd.merge(
        sta_params,
        get_meteo_parameters_info(full_description, lookup, language),
        how='inner',
        on='parameter_shortname')
    return output


def get_param_description(shortname, language='fr'):
    """ 
    Get description of a meteorological parameter from its shortname.

    ARGUMENTS: 
        - shortname (string): the parameter shortname (e.g. rre150h0) as provided by get_meteo_parameters_info()
        - language ('fr' or 'en', default='fr') for the output parameter description

    RETURNS: a string describing the meteorological parameter.
    """
    all_param_info = get_meteo_parameters_info(full_description=False, language=language)
    par_row = all_param_info[all_param_info['parameter_shortname'] == shortname]
    if len(par_row) == 0:
        raise ValueError(f"No entry found for parameter {shortname} !")
    elif len(par_row) > 1:
        raise ValueError(f"Multiple entries found for parameter {shortname} !")
    else:
        par_row.index
        param_description = par_row['parameter_description_' + language].get(par_row.index[0])
        return param_description
    

def check_parameter_availability(shortname, sta):
    """ 
    Check the availability of a meteorological parameter at a given station.

    ARGUMENTS: 
        - shortname (string): the parameter shortname (e.g. rre150h0) as provided by get_meteo_parameters_info()
        - sta (string): the SwissMetNet meteorological station (e.g. GVE, CGI, PAY,...)

    RETURNS: a boolean.
    """
    sta_params = get_parameters_by_station(sta)
    par_row = sta_params[sta_params['parameter_shortname'] == shortname]
    
    if len(par_row) == 1:
        return True
    else:
        return False


def get_smn_data(sta, granularity, past_type=None, historical_period=None):
    """
    Get data from a remote csv file into a pd.DataFrame

    ARGUMENTS:
        - sta (string): nat_abbr_tx abbreviation
        - granularity (string): 10 minutes - 't' ; hourly - 'h' ; daily - 'd' ; monthly - 'm' ; yearly - 'y'
        - past_type (string): one of 'now', 'recent' or 'historical'
        - historical_period (string): one of '1980-1989', ..., '2020-2029'
    
    RETURNS: a pd.DataFrame with the content of the retrieved csv file
    """

    BASE_URL_SMN = "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn"

    if granularity in ['d', 'h', 't'] and past_type is None:
        raise ValueError(f"For granularity '{granularity}', 'past_type' must be provided !")
    if granularity in ['m', 'y'] and past_type is not None:
        print(f"For granularities 'm' (monthly) and 'y' (yearly), argument 'past_type' is useless and ignored.")

    # the basename of the file associated with given location and time granularity
    url_suffix_base = f"ogd-smn_{sta.lower()}_{granularity}"

    if granularity == 'd':
        if past_type in ['recent', 'historical']:
            url_suffix = '_'.join([url_suffix_base, past_type])
        else:
            raise ValueError(f"Not allowed past type '{past_type}' for granularity '{granularity}' !")
    elif granularity in ['t', 'h']:
        if past_type == 'historical':
            if historical_period is not None:
                url_suffix = '_'.join([url_suffix_base, past_type, historical_period])
            else:
                raise ValueError("Argument 'historical_period' must be provided !")
        else:
            url_suffix = '_'.join([url_suffix_base, past_type])
    else:
        url_suffix = url_suffix_base

    url = os.path.join(BASE_URL_SMN, sta.lower(), url_suffix + '.csv')
    #print(url)

    try:
        # in production, please check if a local copy of the files already exists. If so, please
        # send the ETag of the local resource (that you got in the response when initially
        # requesting the resource) in an If-None-Match header. The server will only send the file,
        # if the remote version is newer than your local file. This avoids unnecessary traffic.
        # (also check here: https://data.geo.admin.ch/api/stac/static/spec/v1/apitransactional.html#tag/Data/operation/getAssetObject)
        df = pd.read_csv(
            url,
            delimiter=';',
            parse_dates=['reference_timestamp'],
            date_format={'reference_timestamp': '%d.%m.%Y %H:%M'}
        )
        
        return df
    # too broad exception, I know. Please use better error handling in production ;-)
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None


def sanitize_smn_data(df):
    """
    ARGUMENTS:
        - df (pd.DataFrame): The input DataFrame.

    RETURNS:
        pd.DataFrame: A new DataFrame with cleaned data.
    """

    df_cleaned = df.rename(columns={'reference_timestamp': 'time'})
        
    return df_cleaned


def get_smn_measures(sta, parameters, beg=None, end=None, description_lang='fr'):
    """
    ARGUMENTS:
        - sta (string): the SwissMetNet meteorological station (e.g. GVE, CGI, PAY,...)
        - parameters (list): the requested meteorological parameters -- a list of strings corresponding 
                             to the parameter_shortname as given by get_parameters_by_station(sta)
        - beg/end (datetime or string, default=None): the start/end of the measurement period -- datetime object or string in format "AAAAMMDDHHmm".
                                                      If 'beg'=None, then all available data from the beginning of the recordings is retrieved.
                                                      If 'end'=None, then data until the latest available record is retrieved.
                                                      Thus, if both are None, the time series of all available recordings is retrieved.
        - language ('fr' or 'en', default='fr'): in which language the description of the parameters should be printed to stout : 
        		                                 french ('fr') or english ('en')

    RETURNS: pd.DataFrame : a dataframe with requested meteorlogical data
    """
    
    if beg is not None:
        if isinstance(beg, datetime):
            pass
        else:
            beg = datetime.strptime(beg, '%Y%m%d%H%M')

    if end is not None:
        if isinstance(end, datetime):
            pass
        else:
            end = datetime.strptime(end, '%Y%m%d%H%M')
    
    if beg is None and end is None:
        print(f"Retrieving all available measurements")
    else:
        if beg is None:
            print(f"Retrieving measurements at {sta} from the beginning of measurement to {end.strftime('%d-%m-%Y %H:%M')}")
        elif end is None:
            print(f"Trying to retrieve measurements at {sta} from {beg.strftime('%d-%m-%Y %H:%M')} to latest available timestamp")
        else:
            print(f"Trying to retrieve measurements at {sta} from {beg.strftime('%d-%m-%Y %H:%M')} to {end.strftime('%d-%m-%Y %H:%M')}")

    # names of the columns that will be returned in output dataframe:
    cols = ['time', 'nat_abbr_tx']
    for p in parameters:
        cols.append(p)

    # get and print out info about requested parameters:
    df_params_by_sta = get_parameters_by_station('GVE')
    param_granu_list = []
    is_any_data_available = False
    for param in parameters:
        param_row = df_params_by_sta.loc[df_params_by_sta['parameter_shortname'] == param]
        param_granu = param_row['parameter_granularity'].item().lower()
        param_granu_list.append(param_granu)
        param_description = param_row[f"parameter_description_{description_lang}"].item()
        param_avail_since = datetime.strptime(param_row['data_since'].item(), '%d.%m.%Y %H:%M')
        print(
            f"Retrieving data for parameter {param}: \n"
            f"\t description ({description_lang}) : {param_description} \n"
            f"\t time granularity: {param_granu} \n"
            f"\t data available since {param_avail_since.strftime('%d-%m-%Y %H:%M')}"
        )
        if end is None or (end is not None and end > param_avail_since):
            is_any_data_available = True

    if not is_any_data_available:
        raise ValueError("No measurement is available for the requested period of time.")

    if not all([i == param_granu_list[0] for i in param_granu_list]):
        raise ValueError('Requested parameters are not available at the same time granularity')
    
    # retrieve all needed files containing the data and concatenate them:        
    if param_granu in ['m', 'y']: # for these granularities, there is a single file with all the data
        df = get_smn_data(sta, param_granu)
    else:
        today_start = datetime.combine(date.today(), time())
        df_list = []
        if beg is None or beg.year < today_start.year: # if historical measures are requested
            if param_granu in ['h', 't']:
                HIST_BATCHES = {
                    'h': [1980, 1990, 2000, 2010, 2020, 2030],
                    't': [2000, 2010, 2020, 2030]   
                }
                batch_beg_idx = 0
                if beg is not None:
                    if beg.year > HIST_BATCHES[param_granu][0]:
                        # returns the last index smaller than beg.year
                        batch_beg_idx = [i for i,b in enumerate(HIST_BATCHES[param_granu]) if b < beg.year][-1]

                batch_end_idx = len(HIST_BATCHES[param_granu]) - 1
                if end is not None:
                    if end.year < HIST_BATCHES[param_granu][-1]:
                        # returns the first index greater than end.year
                        batch_end_idx = [i for i,b in enumerate(HIST_BATCHES[param_granu]) if b > end.year][0]

                for batch_idx in range(batch_beg_idx, batch_end_idx):
                    batch_beg_year = HIST_BATCHES[param_granu][batch_idx]
                    batch_suffix = f"{str(batch_beg_year)}-{str(batch_beg_year + 9)}"
                    df_list.append(get_smn_data(sta, param_granu, 'historical', batch_suffix))
            else:
                df_list.append(get_smn_data(sta, param_granu, 'historical'))

            if end is None:
                df_list.append(get_smn_data(sta, param_granu, 'recent'))
                if param_granu in ['h', 't']:
                    df_list.append(get_smn_data(sta, param_granu, 'now'))
            else:
                if end.year >= today_start.year:
                    df_list.append(get_smn_data(sta, param_granu, 'recent'))
                    if end >= today_start and param_granu in ['h', 't']:
                        df_list.append(get_smn_data(sta, param_granu, 'now'))
        else:
            if beg < today_start:
                df_list.append(get_smn_data(sta, param_granu, 'recent'))
                if end is None or end >= today_start:
                    if param_granu in ['h', 't']:
                        df_list.append(get_smn_data(sta, param_granu, 'now'))
            else:
                if param_granu in ['h', 't']:
                    df_list.append(get_smn_data(sta, param_granu, 'now'))

        df = pd.concat(df_list)
    
    df = sanitize_smn_data(df)
    # add a column with station abbreviation:
    df['nat_abbr_tx'] = sta
    # keep only requested parameters, as well as 'time' and 'nat_abbr_tx' columns:
    df_param = df[cols]

    if beg is not None and end is not None:
        df_filtered = df_param.loc[(df_param['time'] >= beg) & (df_param['time'] <= end)] # time as usual column
    else:
        if beg is not None:
            df_filtered = df_param.loc[df_param['time'] >= beg] # time as usual column
        elif end is not None:
            df_filtered = df_param.loc[df_param['time'] <= end]
        else:
            df_filtered = df_param
    
    df_filtered.reset_index(inplace=True, drop=True)

    return df_filtered
