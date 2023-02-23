from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.datafetcher import fetch_latest_water_level_data

stations = build_station_list()
update_water_levels(stations)


def test_for_update_water_levels():
    for station in stations:
        if type(station.latest_level) == float:
            return print("No errors found")
        assert type(station.latest_level) == float


test_for_update_water_levels()