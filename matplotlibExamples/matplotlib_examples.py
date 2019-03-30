from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy import arange, sin, pi
import numpy as np


def signalSubPlots():
    t = arange(0.0, 1.0, 0.01)

    fig = figure(1)

    ax1 = fig.add_subplot(311)
    ax1.plot(t, sin(2*pi*t))
    ax1.set_title('Signal 1')
    ax1.tick_params(
        axis='both',          # changes apply to the x-axis
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off)

    ax2 = fig.add_subplot(312)
    ax2.plot(t, sin(2*2*pi*t))
    ax2.set_title('Signal 2')
    ax2.tick_params(
        axis='both',          # changes apply to the x-axis
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off)


    ax3 = fig.add_subplot(313)
    ax3.plot(t, sin(2*2*2*pi*t))
    ax3.set_title('Signal 3')
    ax3.tick_params(
        axis='both',          # changes apply to the x-axis
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off)

    show()

def circlePlot():
    # x**2  + y**2 = r**2
    r1 = 2
    r2 = 1
    x1 = np.linspace(-r1, r1, 1000)
    x2 = np.linspace(-r2, r2, 1000)
    y1 = np.sqrt(-x1**2+r1**2)
    y2 = np.sqrt(-x2**2+r2**2)
    fig2 = figure(2)
    plt.plot(x1, y1, 'g', label='outer')
    plt.plot(x1, -y1, 'g')
    plt.plot(x2, y2, 'r', label='inner')
    plt.plot(x2, -y2, 'r')
    plt.gca().set_aspect('equal')
    plt.legend()

    plt.show()

#signalSubPlots();
circlePlot();

