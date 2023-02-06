from haversine import haversine
from .utils import sorted_by_key  #noqa


def test_stations_by_distance(stations, p):
    """ Returns a sorted list of (station, distance) tuples, where distance (float) is the distance of the station
    (MonitoringStation) from the coordinate p  """

    station_distance = []

    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))

    x = sorted_by_key(station_distance, 1)

    return x
