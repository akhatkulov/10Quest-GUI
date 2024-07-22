import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox, QRadioButton, QGroupBox
from PyQt5.QtGui import QColor
from random import shuffle


questions = [
    {
        'question': 'Python dasturlash tilining muhim xususiyati nima?',
        'options': ['Yorliq', 'Obyektga yo‘naltirilgan', 'O‘rtacha', 'Tarmoq'],
        'correct_answer': 1
    },
    {
        'question': 'PyQt5 nima uchun ishlatiladi?',
        'options': ['Grafik interfeyslar yaratish', 'Ma’lumotlar tuzatish', 'Skript dasturlash', 'Boshqalar'],
        'correct_answer': 0
    },
    {
        'question': 'Qt qanday tilida yozilgan?',
        'options': ['C++', 'Java', 'Python', 'JavaScript'],
        'correct_answer': 0
    },
    {
        'question': 'PyQt5 kutubxonasida qanday widgetlar mavjud?',
        'options': ['Button, Label, Edit', 'List, Dictionary', 'Array, String', 'Float, Integer'],
        'correct_answer': 0
    },
    {
        'question': 'PyQt5 bilan qaysi OS larda ishlay olamiz?',
        'options': ['Linux', 'Windows', 'MacOS', 'Hammasi'],
        'correct_answer': 3
    },
    {
        'question': 'PyQt5 kutubxonasida qanday metodlar mavjud?',
        'options': ['Text, Image', 'Graphics, Animation', 'Layout, Event', "Hammasi tog'ri"],
        'correct_answer': 3
    },
    {
        'question': 'PyQt5 ichida qanday layoutlar ishlatiladi?',
        'options': ['Horizontal, Vertical, Grid', 'List, Tuple, Dictionary', 'Float, Integer, String', "To'gri javob jo'q"],
        'correct_answer': 0
    },
    {
        'question': 'PyQt5 kutubxonasida foydalaniladigan ma’lumotlar turi nima?',
        'options': ['SQL, NoSQL', 'Array, String', 'List, Tuple', 'String, Number'],
        'correct_answer': 2
    },
    {
        'question': 'PyQt5 widgetlari qanday xususiyatlar bilan aniqlanadi?',
        'options': ['Class, Object', 'Attributes, Methods', 'Variables, Function', "To'gri javob jo'q"],
        'correct_answer': 1
    },
    {
        'question': 'PyQt5 dasturlash qaysi dasturlash tilida amalga oshiriladi?',
        'options': ['Python, C++', 'Java, JavaScript', 'C#, Ruby', 'Python, Java'],
        'correct_answer': 0
    }
]

class QuizGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('akhatkulov')
        self.setGeometry(100, 100, 600, 400)
        
        self.current_question = 0
        self.score = 0
        
        self.initUI()
        
    def initUI(self):
        self.question_label = QLabel()
        self.option_buttons = []
        self.result_label = QLabel()
        self.next_button = QPushButton('Keyingisi')
        
        layout = QVBoxLayout()
        layout.addWidget(self.question_label)

        group_box = QGroupBox()
        vbox = QVBoxLayout()
        for i in range(4):
            option_button = QRadioButton()
            self.option_buttons.append(option_button)
            vbox.addWidget(option_button)
        group_box.setLayout(vbox)
        layout.addWidget(group_box)
        
        layout.addWidget(self.result_label)
        layout.addWidget(self.next_button)
        
        self.setLayout(layout)
        
        self.show_question()
        
        self.next_button.clicked.connect(self.next_question)
        
    def show_question(self):
        self.result_label.setText('')
        question_data = questions[self.current_question]
        self.question_label.setText(question_data['question'])
        
        options = question_data['options']

        shuffle(options)
        for i in range(4):
            self.option_buttons[i].setText(options[i])
        
    def check_answer(self):
        selected_option = -1
        for i in range(4):
            if self.option_buttons[i].isChecked():
                selected_option = i
                break
        
        correct_option = questions[self.current_question]['correct_answer']
        
        if selected_option == correct_option:
            self.score += 1
            self.result_label.setText('To\'g\'ri!')
            self.result_label.setStyleSheet('color: green')
        else:
            self.result_label.setText('Noto\'g\'ri!')
            self.result_label.setStyleSheet('color: red')
        

        for button in self.option_buttons:
            button.setEnabled(False)
        
    def next_question(self):

        self.check_answer()

        self.current_question += 1
        
        if self.current_question < len(questions):
            self.show_question()

            for button in self.option_buttons:
                button.setEnabled(True)
                button.setChecked(False)
            self.result_label.setText('')
            self.result_label.setStyleSheet('color: black')
        else:
            self.show_result()
        
    def show_result(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Natijalar')
        msg_box.setText(f"Siz {len(questions)} savoldan {self.score} ta to'g'ri javob berdingiz!")
        msg_box.exec_()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = QuizGame()
    

    game.setAutoFillBackground(True)
    p = game.palette()
    p.setColor(game.backgroundRole(), QColor(240, 240, 240))  
    game.setPalette(p)
    

    game.setStyleSheet("""
        QLabel {
            color: black;
            font-size: 18px;
        }
        QRadioButton {
            color: black;
            font-size: 16px;
        }
        QPushButton {
            background-color: #4CAF50; /* Green */
            color: white;
            font-size: 18px;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049; /* Darker green */
        }
        """)
    
    game.show()
    sys.exit(app.exec_())
