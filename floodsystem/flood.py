from floodsystem.stationdata import update_water_levels


def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    list_stations_and_relative_level = []
    for station in stations:
        rel_water_level = station.relative_water_level()
        if rel_water_level is not None:
            tuple_stations_and_relative_level = (station, rel_water_level)
            list_stations_and_relative_level.append(tuple_stations_and_relative_level)
        sorted_list_stations_and_relative_level = sorted(list_stations_and_relative_level, key=lambda x: x[1])
        reversed_sorted_list_stations_and_relative_level = sorted_list_stations_and_relative_level[::-1]
    return reversed_sorted_list_stations_and_relative_level


def stations_highest_rel_level(stations, N):
    update_water_levels(stations)
    list_stations_and_relative_level = []
    for station in stations:
        rel_water_level = station.relative_water_level()
        if rel_water_level is not None:
            tuple_stations_and_relative_level = (station, rel_water_level)
            list_stations_and_relative_level.append(tuple_stations_and_relative_level)
        sorted_list_stations_and_relative_level = sorted(list_stations_and_relative_level, key=lambda x: x[1])
        reversed_sorted_list_stations_and_relative_level = sorted_list_stations_and_relative_level[::-1]
    return reversed_sorted_list_stations_and_relative_level[:N]




















