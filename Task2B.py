from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)


list = []
for station in stations_level_over_threshold(stations, 0.8):
    name = station[0].name
    relative_water_level = station[1]
    list.append((name, relative_water_level))

print()
print("Stations and their relative water level, in descending order:")
for i in list[:10]:
    print(i)

print()
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")


