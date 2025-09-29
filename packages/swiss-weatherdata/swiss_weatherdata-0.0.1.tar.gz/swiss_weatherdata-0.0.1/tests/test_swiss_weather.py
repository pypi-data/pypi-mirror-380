import swiss_weather.gbm as gbm
import pandas as pd


def test_get_smn_stations_info():

    df = gbm.get_smn_stations_info(full_description=False)
    nrows = df.shape[0]
    assert nrows > 1, "Empty DataFrame retrieved"


def test_get_smn_measures():

    df_expected = pd.read_pickle('tests/test_data_tre200h0_rre150h0_PAY.pickle')
    df = gbm.get_smn_measures(sta='PAY', parameters=['tre200h0', 'rre150h0'], beg='201001150600', end='201003011800')
    assert df_expected.equals(df), "Problem with data retrieval"


