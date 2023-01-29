from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def river_list():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    x = sorted(rivers)
    print("number of rivers with at least one monitoring station:", len(rivers))
    print(x[:10])

if __name__ == "__main__":
    print()
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    river_list()