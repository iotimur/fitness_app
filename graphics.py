from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure
import sys
import test_graphic
import numpy as np


class Hystogram_classic(QWidget):
    def __init__(self, parent=None):
        super(Hystogram_classic, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)

        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)


class Circle_hystogram(QWidget):
    def __init__(self, parent=None):
        super(Circle_hystogram, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)

        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)


class MainWidget(QMainWindow, test_graphic.Ui_MainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.pushButton.clicked.connect(self.plot_widget)

    def plot_widget(self):
        self.matplotlibwidget_upper.axis.clear()
        x = np.random.random(10)
        y = np.random.random(10)
        txts = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
        self.matplotlibwidget_upper.axis.scatter(x, y)
        for index, txt, in enumerate(txts):
            self.matplotlibwidget_upper.axis.annotate(txt, (x[index], y[index]))
        self.matplotlibwidget_upper.canvas.draw()

        self.matplotlibwidget_downer.axis.clear()
        x = np.random.random(10)
        y = np.random.random(10)
        txts = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
        self.matplotlibwidget_downer.axis.scatter(x, y)
        for index, txt, in enumerate(txts):
            self.matplotlibwidget_downer.axis.annotate(txt, (x[index], y[index]))
        self.matplotlibwidget_downer.canvas.draw()

    def init_widgets(self):
        self.matplotlibwidget_upper = Circle_hystogram()
        self.layoutvertical_upper = QVBoxLayout(self.widget)
        self.layoutvertical_upper.addWidget(self.matplotlibwidget_upper)

        self.matplotlibwidget_downer = Hystogram_classic()
        self.layoutvertical_down = QVBoxLayout(self.widget_2)
        self.layoutvertical_down.addWidget(self.matplotlibwidget_downer)

