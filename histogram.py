import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class HistogramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Histogram Example")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        canvas = self.create_histogram_canvas()
        layout.addWidget(canvas)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_histogram_canvas(self):
        fig = Figure()
        ax = fig.add_subplot(111)

        data = [10, 30, 50, 70, 90]  # Your data values here
        categories = ["Category1", "Category2", "Category3", "Category4", "Category5"]

        ax.bar(categories, data)

        canvas = FigureCanvas(fig)
        canvas.draw()

        return canvas


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HistogramWindow()
    window.show()
    sys.exit(app.exec_())
