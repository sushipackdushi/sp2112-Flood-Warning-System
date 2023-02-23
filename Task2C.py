from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

list = []
for station in stations_highest_rel_level(stations, N):
    name = station[0].name
    relative_water_level = station[1]
    list.append((name, relative_water_level))

print(stations_highest_rel_level(stations, 9))