import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MouseTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week 3 - (F1D022111 - ANDIKA)")
        self.setGeometry(100, 100, 600, 400)

        
        self.label = QLabel("x: 0, y: 0", self)
        self.label.move(50, 50)
        self.label.setStyleSheet("font-size: 14px; padding: 5px; background: lightgray; border-radius: 5px;")
        self.label.adjustSize()

        
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        
        x, y = event.x(), event.y()
        self.label.setText(f"x: {x}, y: {y}")
        self.label.adjustSize()

      
        if self.is_cursor_on_label(x, y):
            self.move_label_instantly()

    def is_cursor_on_label(self, x, y):
    
        label_x, label_y = self.label.pos().x(), self.label.pos().y()
        label_w, label_h = self.label.width(), self.label.height()

        return label_x <= x <= label_x + label_w and label_y <= y <= label_y + label_h

    def move_label_instantly(self):
      
        max_x = self.width() - self.label.width() - 10  
        max_y = self.height() - self.label.height() - 10  

        new_x = random.randint(10, max_x)
        new_y = random.randint(10, max_y)

        self.label.move(new_x, new_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTrackerApp()
    window.show()
    sys.exit(app.exec_())
