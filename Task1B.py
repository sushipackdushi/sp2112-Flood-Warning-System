from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    x = stations_by_distance(stations, (52.2053, 0.1218))
    a = []
    for i in x:
        a.append([(i[0].river, i[0].town, i[1])])

    closest_stations = [a[:9]]
    furthest_stations = [a[-10:]]
    print(f"Closest Stations: {closest_stations}")
    print(f"Furthest Stations: {furthest_stations}")


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
