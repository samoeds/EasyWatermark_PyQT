import sys
import time

from PIL import Image, ImageDraw, ImageFont
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox

FILEPATH = "C:/Users/samoe/Desktop/watermark_test"

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("watermark.ui", self)
        self.browse = self.findChild(QtWidgets.QPushButton, 'browse')
        self.browse_entry = self.findChild(QtWidgets.QLineEdit, 'browse_entry')
        self.watermark_entry = self.findChild(QtWidgets.QLineEdit, 'watermark_entry')
        self.browse.clicked.connect(self.browse_files)

        self.watermark = self.findChild(QtWidgets.QPushButton, 'watermark')
        self.watermark.clicked.connect(self.do_watermark)

        self.show()

    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", FILEPATH, "Image files (*.PNG *.jpeg)")
        self.browse_entry.setText(fname[0])

    def show_message_box(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        retval = msg.exec()

    def do_watermark(self):
        file = self.browse_entry.text()
        text = self.watermark_entry.text()

        if len(text) == 0:
            text = self.watermark_entry.placeholderText()

        with Image.open(file).convert("RGBA") as pic:

            txt = Image.new("RGBA", pic.size, (255, 0, 0, 0))

            fnt = ImageFont.truetype("arial.ttf", 70)
            d = ImageDraw.Draw(txt)


            x, y = 10, 10
            width, height = pic.size
            step_x, step_y = 400, 90

            for i in range(0, height, step_y):
                for j in range(0, width, step_x):
                    d.text((j, i), text, font=fnt, fill=(255, 255, 255, 50))

            out = Image.alpha_composite(pic, txt)

            out.save(FILEPATH + '/watermark_done.png')

            # need to try open this file if exist - need to add end symbol to the name

            out.show()
            time.sleep(5)

            # need to ask user in message box to open the directory with this file

            self.show_message_box("Information", "Done")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()  # MAKE WINDOW VISIBLE
    app.exec()  # EVENT LOOP


if __name__ == '__main__':
    main()