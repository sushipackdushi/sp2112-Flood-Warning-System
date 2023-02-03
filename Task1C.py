from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    x = stations_within_radius(stations, (52.2053, 0.1218), 10)
    print(x)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
