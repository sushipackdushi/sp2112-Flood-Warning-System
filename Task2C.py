from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

list = []


def run():
    for station in stations_highest_rel_level(stations, 10):
        name = station[0].name
        relative_water_level = station[1]
        list.append((name, relative_water_level))

    print()
    print("Nth highest relative water levels and their stations: ")
    print("N=10")
    print()
    for i in list:
        print(i)


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
