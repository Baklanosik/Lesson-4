import sys

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget


class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Plotter")
        self.resize(800, 600)

        self.months_list = []
        self.rainfall_list = []

        self.filename = None

        self.load_button = QPushButton("Load Data")
        self.load_button.clicked.connect(self.load_data)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)

        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.canvas)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Data File",
            "",
            "Data Files (*.csv *.txt);;All Files (*)",
        )
        if filename:
            with open(filename, 'r') as f:
                next(f)
                for line in f:
                    parts = line.split(",")
                    self.months_list.append(parts[0])
                    self.rainfall_list.append(int(parts[1]))
            self.draw_graph()

    def draw_graph(self):
        self.axes.clear()
        self.axes.bar(self.months_list, self.rainfall_list)
        self.axes.set_title(self.filename)

        self.canvas.draw_idle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlotWindow()
    window.show()
    sys.exit(app.exec())
