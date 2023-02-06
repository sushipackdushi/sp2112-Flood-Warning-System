from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)

print()
print("Test for number of rivers")


def test_for_no_of_rivers():
    y = len(sorted(rivers))
    if type(y) == int:
        return print("1) No errors for number of stations")
    assert type(y) == int


test_for_no_of_rivers()


def station_names_from_stations(stations):
    station_names = []
    for station in stations:
        name = station.name
        station_names.append(name)
    return sorted(station_names)


print()
print("Test if list is alphabetical")


def test_if_list_is_alphabetical():
    station_river = stations_by_river(stations)
    river_aire = station_river["River Aire"]
    river_aire_station_names = station_names_from_stations(river_aire)
    for i in range(len(river_aire_station_names)-1):
        if river_aire_station_names[i] > river_aire_station_names[i+1]:
            return False, print("1)list is not alphabetical")

    return True, print("1)list is alphabetical")
    assert river_aire_station_names[i] > river_aire_station_names[i+1]


test_if_list_is_alphabetical()


def test_if_list_is_alphabetical2():
    non_alphabetical_list = ["apple", "cow", "boy"]
    for i in range(len(non_alphabetical_list)-1):
        if non_alphabetical_list[i] > non_alphabetical_list[i+1]:
            return False, print("2)list is not alphabetical")

    return True, print("2)list is alphabetical")
    assert non_alphabetical_list[i] > non_alphabetical_list[i+1]


test_if_list_is_alphabetical2()

#print(river_aire_station_names)
#print(test_if_list_is_alphabetical(river_aire_station_names))
#print(non_alphabetical_list)
#print(test_if_list_is_alphabetical(non_alphabetical_list))
