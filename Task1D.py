from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
stations = build_station_list()
rivers = rivers_with_station(stations)


def run():
    x = sorted(rivers)
    y = len(rivers)
    print("Number of rivers with at least one monitoring station:", y)
    print("First 10 river:", x[:10])
    print()

    station_river = stations_by_river(stations)
    river_aire = station_river["River Aire"]
    river_cam = station_river["River Cam"]
    river_thames = station_river["River Thames"]

    river_aire_station_names = station_names_from_stations(river_aire)
    river_cam_station_names = station_names_from_stations(river_cam)
    river_thames_station_names = station_names_from_stations(river_thames)

    print("Stations located on River Aire:", river_aire_station_names)
    print("Stations located on River Cam:", river_cam_station_names)
    print("Stations located on River Thames:", river_thames_station_names)


def station_names_from_stations(stations):
    station_names = []
    for station in stations:
        name = station.name
        station_names.append(name)
    return sorted(station_names)


if __name__ == "__main__":
    print()
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
