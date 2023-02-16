import matplotlib.pyplot as plt
import matplotlib.pyplot
import matplotlib.dates
import numpy as np
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit


# For Task 2E
def plot_water_levels(station, dates, levels):
    """Displays a plot (using Matplotlib) of the water level data against time for a station"""
    plt.plot(dates, levels)
    plt.tight_layout()

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=30)
    plt.title(station.name)

    plt.show()


# For Task 2F
def plot_water_level_with_fit(station, dates, levels, p):
    """ A function that plots the water level data and the best-fit polynomial"""
    poly, d0 = polyfit(dates, levels, p)

    plt.plot(dates, levels)

    ds = matplotlib.dates.date2num(dates)

    x1 = np.linspace(ds[0], ds[-1], 30)
    plt.plot(x1, poly(x1-d0))

    plt.axhline(y=station.typical_range[0])
    plt.axhline(y=station.typical_range[1])

    plt.tight_layout()

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=30)
    plt.title("Station" + station.name)

    plt.show()
