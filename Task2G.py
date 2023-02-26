from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_distance, stations_within_radius, stations_by_river, rivers_with_station, \
    rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)

    # Ask user to enter the threshold number– this value is used as the cut-off for deciding how many at-risk stations
    # there are.

    n = int(input("Enter the number of stations to set as threshold: "))

    if n <= 0:
        raise ValueError("Error, N must be an integer greater than 0")

    # Retrieve stations with no data available and report to user
    empty_data_stations = []

    for i in stations:
        if i.latest_level is None:
            empty_data_stations.append(i.name)

    print(f"Warning: The data for the following stations is currently available:"
          f" {empty_data_stations} ")
    print("Monitor these stations manually")

    list = []

    for station in stations_highest_rel_level(stations, n):
        town = station[0].town
        relative_water_level = station[1]
        list.append((town, relative_water_level))

    print()
    print(f"{n}th highest relative water levels and their towns: ")
    print()

    severe_list = []
    high_list = []
    moderate_list = []
    low_list = []

    for i in list:
        if i[1] > 1.5:
            severe_list.append(i[0])
        elif i[1] > 1.2:
            high_list.append(i[0])
        elif i[1] > 1:
            moderate_list.append(i[0])
        elif i[1] < 1:
            low_list.append(i[0])

    print(f"Severe risk of flooding in these towns: {severe_list}")
    print(f"High risk of flooding in these towns: {high_list}")
    print(f"Moderate risk of flooding in these towns: {moderate_list}")
    print(f"Low risk of flooding in these towns: {low_list}")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

