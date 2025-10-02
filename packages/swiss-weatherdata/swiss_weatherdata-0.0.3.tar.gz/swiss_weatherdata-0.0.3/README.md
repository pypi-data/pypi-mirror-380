# Overview

This package provides a set of convenience tools to seamlessly download meteorological data collected and made available to the public as Open Government Data (OGD) by the Federal Office for Meteorology and Climatology MeteoSwiss. More information about the Open Data from MeteoSwiss is available [here](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html).

Currently, the data available through this interface concerns ground-base measurements (gbm) coming from the MeteoSwiss [automatic weather stations network](https://opendatadocs.meteoswiss.ch/a-data-groundbased/a1-automatic-weather-stations) SwissMetNet (SMN).

**Important notice:**

This package was not developed and is not suppported by MeteoSwiss. It however relies on the [MeteoSwiss Open Data API](https://opendatadocs.meteoswiss.ch/) which allows public access to meteorological data provided by the Federal Office for Meteorology and Climatology, and which can be used independently of this package.

# Installation

```
pip install swiss-weatherdata
```

# Usage

Import all functions at once:

```
import swiss_weatherdata.gbm as gbm
```


## Information about weather stations and meteorological parameters

Get information about all SwissMetNet (SMN) weather stations in a `pd.DataFrame`:

```
gbm.get_smn_stations_info()
```
Look for a meteorological parameter:

```
gbm.get_meteo_parameters_info()
```

The `lookup` argument allows to filter meteorological parameters by category, e.g., the following lists all parameters related to Wind:

```
gbm.get_meteo_parameters_info(lookup='wind', language='en')
```

Same output but in french:

```
gbm.get_meteo_parameters_info(lookup='vent', language='fr')
```

Currently, meteorological parameters are grouped into the following categories:

| language='en' | language='fr' |
| -------- | ------- |
| Wind  | Vent    |
| Evaporation | évaporation     |
| Radiation    | Rayonnement    |
| Snow | neige |
| Pressure | Pression |
| Humidity | Humidité |
| Precipitation | Précipitations |
| Sunshine | Ensoleillement |
| Temperature | Température |


Get the parameter description from its shortname:

```
gbm.get_param_description(shortname='rre150d0', language='fr')
```

Get the list of available parameters for a given weather station. For example, at Genève-Cointrin (GVE):


```
gbm.get_parameters_by_station('GVE')
```
### Time-granularity of recordings

Recordings are generally available at different time granularities: 10 minutes, hourly, daily, monthly or yearly. 

Each parameter has its own granularity, as specified in the output of `get_meteo_parameters_info()`, for instance:

| parameter_shortname | parameter_description_en |
| -------- | ------- |
| tre200s0 | 'Air temperature 2 m above ground; current value' |
| tre200h0 | 'Air temperature 2 m above ground; hourly mean' |
| tre200d0 | 'Air temperature 2 m above ground; daily mean' |
| tre200m0 | 'Air temperature 2 m above ground; monthly mean' |
| tre200y0 | 'Air temperature 2 m above ground; annual mean' |


## Download recordings from a given weather station:

The function `get_smn_measures()` downloads data recorded at a given weather station for several meteorological parameters and for a specified period. It returns data organized in a Pandas `pd.DataFrame`.

**Example 1:** get daily maximum temperature and daily sum of precipitation recorded at Genève-Cointrin from May 15. 2025 and to the latest available record:

```
df = gbm.get_smn_measures(
    sta='GVE',
    parameters=['tre200dx', 'rka150d0'],
    beg='202405150000'
)
```

**Example 2:** get hourly mean temperature and hourly sum of precipitation recorded at Payerne from January 15. 2010 at 06:00 UTC to March 1. 2010 at 18:00 UTC:

```
df = gbm.get_smn_measures(
    sta='PAY',
    parameters=['tre200h0', 'rre150h0'],
    beg='201001150600',
    end='201003011800'
)
```

# Examples

All previous examples are available in a [Jupyter Notebook](https://github.com/ptitmatheux/swiss_weatherdata/tree/master/docs) on GitHub.