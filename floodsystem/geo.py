# Copyright (C) 2018 Garth N. Wells

# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from .utils import sorted_by_key  #noqa
from haversine import haversine #Unit


# Function for Task 1B
def stations_by_distance(stations, p):
    """ Returns a sorted list of (station, distance) tuples, where distance (float) is the distance of the station
    (MonitoringStation) from the coordinate p  """

    station_distance = []

    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))

    x = sorted_by_key(station_distance, 1)

    return x


# Function for Task 1C
def stations_within_radius(stations, centre, r):
    """ Returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x"""
    final_list = []

    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            final_list.append(station.name)

    final_list = sorted(final_list)

    return final_list


# function for task 1D part 1
def rivers_with_station(stations):
    """ Write description of function here"""

    list_of_rivers = []

    for station in stations:
        river = station.river
        list_of_rivers.append(river)

    return set(list_of_rivers)


# function for task 1D part 2
def stations_by_river(stations):
    """ Write description here"""

    dict_stations_by_river = {}

    for station in stations:
        river = station.river
        if river in dict_stations_by_river:
            existing_list = dict_stations_by_river[river]
            existing_list.append(station)
            dict_stations_by_river[river] = existing_list
        else:
            dict_stations_by_river[river] = [station]

    return dict_stations_by_river


# function for task 1E
def rivers_by_station_number(stations, N):
    rivers_and_their_stations = stations_by_river(stations)
    for river in rivers_and_their_stations:
        rivers_and_their_stations[river] = len(rivers_and_their_stations[river])

    tuple_river_and_their_station = tuple(rivers_and_their_stations.items())

    sorted_tuples = sorted(tuple_river_and_their_station, key=lambda x: x[1])

    reversed_tuple = sorted_tuples[::-1]

    final_tuple = reversed_tuple[:N]

    while final_tuple[N-1][1] == reversed_tuple[N][1]:
        final_tuple = reversed_tuple[:N+1]
        N = N + 1

    return final_tuple
    #dictionary created (river: station 1, station 2 ......)
    #change station names --> numbers (use for loop to iterate through then set station names into len(station names)
    #convert dict into list of tuples


    #Nth entry; if there are more rivers with the same number of stations as the N th entry, include these rivers in the list
    #1 check for the number of station
    #2 if final_tuple[] = reverse
