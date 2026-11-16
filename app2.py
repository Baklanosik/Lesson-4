import sys

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget


class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Plotter")
        self.resize(800, 600)

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
            self.filename = filename

    def draw_graph(self, x_values, y_values):
        self.axes.clear()
        self.axes.plot(x_values, y_values)
        self.axes.set_xlabel("X")
        self.axes.set_ylabel("Y")
        self.axes.grid(True)
        self.canvas.draw_idle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlotWindow()
    window.show()
    sys.exit(app.exec())
