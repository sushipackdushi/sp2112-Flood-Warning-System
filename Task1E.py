from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
stations = build_station_list()


def run():
    print()
    print("Rivers by number of stations:")
    print(rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print()
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()


