# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  #noqa
from haversine import haversine #Unit


# Function for Task 1B
def stations_by_distance(stations, p):
    """ ENTER SOMETHING HERE  """
    station_distance = []

    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))

    x = sorted_by_key(station_distance, 1)

    return x

# function for task 1D
def rivers_with_station(stations):

    list_of_rivers = []

    for station in stations:
        river = station.river
        list_of_rivers.append(river)

    return set(list_of_rivers)
