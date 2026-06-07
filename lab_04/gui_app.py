import sys
from pathlib import Path
from PyQt6.QtWidgets import (
 QApplication,
 QLabel,
 QPushButton,
 QTextEdit,
 QVBoxLayout,
 QWidget,
)
from src.robot_state import RobotState
from src.serial_utils import SerialPortFixture
from src.serial_utils import SerialPortWrite
from src.experiment_runner import run_experiment_from_serial

OUTPUT_DIR = Path(__file__).parent / 'results'
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Symulator robota mobilnego")
        self.resize(700, 430)
        self.label = QLabel(
        "Komendy sterowania (v_left,v_right,duration):"
        )
        self.commands_textbox = QTextEdit()
        self.commands_textbox.setPlaceholderText(
        "Wpisz komendy, np.\n"
        "0.10,0.10,1.0\n"
        "0.25,0.25,1.0\n"
        "0.20,0.50,2.0"
        )
        self.button = QPushButton("Uruchom eksperyment")
        self.status_label = QLabel("Status: oczekiwanie na komendy")
        self.button.clicked.connect(self.run_experiment)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.commands_textbox)
        layout.addWidget(self.button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def run_experiment(self) -> None:
        commands_text = self.commands_textbox.toPlainText().strip()
        if not commands_text:
            self.status_label.setText(
                "Status: wpisz co najmniej jedną komendę."
            )
            return

        serial_port = SerialPortFixture()
        SerialPortWrite(serial_port, commands_text + "\n")

        try:
            summary = run_experiment_from_serial(
                serial_port=serial_port,
                initial_state=RobotState(0.0, 0.0, 0.0),
                wheel_base=0.5,
                dt=0.05,
                output_dir=OUTPUT_DIR / "gui_experiment",
            )
        except ValueError as error:
            self.status_label.setText(f"Status: błąd danych - {error}")
            return

        self.status_label.setText(
            "Status: zapisano wyniki. "
            f"Długość drogi: {summary['path_length']:.3f} m"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())