from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)
    # Retrieving the 5 max water level stations
    all_levels = []
    for i in stations:
        if i.latest_level is None:
            continue
        else:
            all_levels.append(i.latest_level)

    all_levels.sort(reverse=True)
    max_levels = all_levels[0:5]

    max_level_stations = []

    for i in stations:
        for j in max_levels:
            if j == i.latest_level:
                max_level_stations.append(i)

    #    print(max_level_stations)

    # Get data for past 2 days for the max level stations
    dt = 2
    for i in max_level_stations:
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        # Plot a graph of water level against time for the 5 stations
        plot_water_level_with_fit(i, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
