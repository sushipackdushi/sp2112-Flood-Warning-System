from floodsystem import geo, plot
from floodsystem import station
from floodsystem.station import MonitoringStation
from datetime import datetime, timedelta


# Builds a list of made up stations for testing


station1 = MonitoringStation('s_id1', 'm_id1', 'station1', (1, 1), (0, 1), 'river1', 'town1')
station2 = MonitoringStation('s_id2', 'm_id2', 'station2', (2, 2), (1, 2), 'river2', 'town2')
station3 = MonitoringStation('s_id3', 'm_id3', 'station3', (3, 3), (None, 3), 'river3', 'town3')
station4 = MonitoringStation('s_id4', 'm_id4', 'station4', (4, 4), (4, 3), 'river3', 'town4')

stations = [station1, station2, station3, station4]


def test_stations_by_distance():
    """Test for Task 1B"""

    x = geo.stations_by_distance(stations, (0, 0))
    assert x == [('station1', 157.2495984740402), ('station2', 314.47523947196964),
                 ('station3', 471.65293997288967),
                 ('station4', 628.7586658391518)]

    # checks if the function output which is a list matches the expected list


def test_stations_within_radius():
    """Test for Task 1C"""
    x = geo.stations_within_radius(stations, (0, 0), 315)
    # Radius of 4 from this point should only include first 2 stations
    assert x == ["station1", "station2"]


def test_plot_water_levels():
    """Test for Task 2E"""

    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
         datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
         datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    plot.plot_water_levels(station1, t, level)
    assert True




