import matplotlib.pyplot as plt


class BodePlotMatplotlib():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xscale("log")
        self.ax.set_yscale("log")

    def add_trace(self, f, c):
        self.ax.plot(f, abs(c))

    def show(self):
        plt.show()


class TimeWaveformsMatplotlib():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
                    title='About as simple as it gets, folks')
        self.ax.grid()

    def add_trace(self, f, c):
        self.ax.plot(f, abs(c))

    def show(self):
        plt.show()
