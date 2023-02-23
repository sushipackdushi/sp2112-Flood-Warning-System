from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)


def test_for_stations_level_over_threshold():
    if len(stations_highest_rel_level(stations, 10)) == 10:
        return True, print("No errors found")
    else:
        return False, print("Error found")
    assert len(stations_highest_rel_level(stations, 10)) == 10


test_for_stations_level_over_threshold
