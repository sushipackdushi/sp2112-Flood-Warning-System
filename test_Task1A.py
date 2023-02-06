from haversine import haversine
from floodsystem.utils import sorted_by_key  #noqa
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    """ Returns a sorted list of (station, distance) tuples, where distance (float) is the distance of the station
    (MonitoringStation) from the coordinate p  """

    x = build_station_list()
    station_distance = []

    for station in x:
        distance = haversine(station.coord, (0, 0))
        station_distance.append((station, distance))

    x = sorted_by_key(station_distance, 1)

    return x
