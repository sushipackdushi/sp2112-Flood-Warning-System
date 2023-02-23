from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


stations = build_station_list()

print()
print("Test for 1E:")


def test_for_1e():
    if len(rivers_by_station_number(stations, 9)) >= 9:
        return True, print("No errors found")
    else:
        return False, print("Error found")
    assert len(rivers_by_station_number(stations, 9)) >= 9


test_for_1e()


