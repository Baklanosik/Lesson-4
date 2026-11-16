from pathlib import Path
import sys

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Plotter")
        self.resize(800, 600)

        self.months_list = []
        self.rainfall_list = []
        self.filename = None

        self.load_button = QPushButton("Load Data")
        self.load_button.setObjectName("loadButton")
        self.load_button.clicked.connect(self.load_data)

        self.figure = Figure(facecolor="#0f172a")
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setObjectName("plotCanvas")
        self.axes = self.figure.add_subplot(111)

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)
        layout.addWidget(self.load_button)
        layout.addWidget(self.canvas)

        central_widget = QWidget()
        central_widget.setObjectName("appRoot")
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
        self.axes.set_facecolor("#111c31")
        self.axes.bar(self.months_list, self.rainfall_list, color="#38bdf8")
        self.axes.set_title(self.filename or "Monthly Rainfall", color="#e2e8f0")
        self.axes.tick_params(colors="#a7b5ca")
        self.axes.grid(axis="y", color="#334155", alpha=0.6)
        for spine in self.axes.spines.values():
            spine.set_color("#334155")

        self.canvas.draw_idle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = Path(__file__).resolve().with_name("style.qss")
    app.setStyleSheet(stylesheet.read_text(encoding="utf-8"))
    window = PlotWindow()
    window.show()
    sys.exit(app.exec())
