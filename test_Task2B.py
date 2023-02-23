from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()


def test_for_stations_level_over_threshold():
    for station in stations_level_over_threshold(stations, 0.8):
        relative_water_level = station[1]
        if relative_water_level > 0.8:
            return True, print("No errors found")
        else:
            return False, print("Error found")
        assert relative_water_level > 0.8


test_for_stations_level_over_threshold()
