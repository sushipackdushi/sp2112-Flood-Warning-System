import matplotlib as plt
import matplotlib.dates
import numpy as np


def polyfit(dates, levels, p):
    """Fits a polynomial to the dates and levels for a particular station"""
    float_dates = plt.dates.date2num(dates)

    d0 = float_dates[0]
    float_dates -= d0

    p_coeff = np.polyfit(float_dates, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0


