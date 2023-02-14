import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """Displays a plot (using Matplotlib) of the water level data against time for a station"""
    plt.plot(dates, levels)
    plt.tight_layout()

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.show()

