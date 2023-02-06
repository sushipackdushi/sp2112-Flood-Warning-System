from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem import geo

# Test if stations can be sorted by distance


def test_stations_by_distance():
    # Create some stations

    station1 = MonitoringStation("s_id1", "m_id1", "stn1", (1, 1), (0, 1), "river1", "town1")
    station2 = MonitoringStation("s_id2", "m_id2", "stn2", (2, 2), (1, 2), "river2", "town2")
    station3 = MonitoringStation("s_id3", "m_id3", "stn3", (3, 3), (None, 3), "river3", "town3")

    test_stations = [station1, station2, station3]

    x = geo.stations_by_distance(test_stations, (52.2053, 0.1218))

    assert x == [('station1', 157.2495984740402), ('station2', 314.47523947196964), ('station3', 417.65293997288967)]

