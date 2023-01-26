# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


# Function for Task 1B
def stations_by_distance(stations, p):
    """ ENTER SOMETHING HERE  """
    station_distance = []
    for i in stations:
        distance = haversine(i.coord, p)
        station_distance.append((i, distance))

    x = sorted_by_key(station_distance, 1)

    return x

