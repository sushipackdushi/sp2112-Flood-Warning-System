# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Method (function) for Task 1F (part 1):
    def typical_range_consistent(self):
        """ Checks if a station object the typical high/low range data for consistency. Returns False if data is
        inconsistent and True if it is consistent"""

        if self.typical_range is None:
            return False

        low, high = self.typical_range

        if low is None or high is None or low > high:
            return False

        return True

    # Method for Task 2B
    def relative_water_level(self):

        if self.typical_range is None:
            return False

        if self.latest_level is None or self.typical_range is None:
            return None

        else:
            low, high = self.typical_range
            relative_water_level = (self.latest_level-low)/(high - low)
            return relative_water_level




# Function for Task 1F (part 2):
def inconsistent_typical_range_stations(stations):
    """Given a list of station objects, returns a list of stations that have inconsistent data"""
    inconsistent_list = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_list.append(station.name)

    return sorted(inconsistent_list)

