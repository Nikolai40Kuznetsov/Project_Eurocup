import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QMessageBox, QSpinBox, QTabWidget, QTextEdit,
                             QGroupBox, QRadioButton, QButtonGroup, QCheckBox,
                             QGridLayout)
from PyQt5.QtCore import Qt, QTimer


class SalaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_balance = 0.0
        self.current_balance = 0.0
        self.week_number = 1
        self.seasonal_rewards_added = False  # Флаг, были ли уже добавлены награды на 48 неделе
        self.transfer_amount = 0.0  # Сумма трансфера для текущей недели
        
        # Словари для хранения матчей
        self.cup_matches = []      # Кубковые матчи
        self.league_matches = []    # Матчи лиги
        self.euro_matches = []      # Еврокубковые матчи
        
        self.initUI()
        
    def initUI(self):
        # Настройка главного окна (шире и немного ниже)
        self.setWindowTitle('Учет зарплат и матчей')
        self.setGeometry(150, 150, 1000, 650)
        
        # Центральный виджет с вкладками
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        # Создаем вкладки
        self.create_main_page()      # Первая страница (учет зарплат)
        self.create_matches_page()    # Вторая страница (матчи)
        
        # Таймер для проверки матчей при смене недели
        self.match_check_timer = QTimer()
        self.match_check_timer.timeout.connect(self.check_week_matches)
        
    def create_main_page(self):
        """Создает главную страницу с учетом зарплат (двухколоночный макет)"""
        main_page = QWidget()
        main_layout = QVBoxLayout(main_page)
        
        # Область для уведомлений о матчах (на всю ширину)
        notification_group = QGroupBox("Уведомления о матчах")
        notification_layout = QVBoxLayout()
        
        self.notification_display = QTextEdit()
        self.notification_display.setReadOnly(True)
        self.notification_display.setMaximumHeight(60)
        self.notification_display.setStyleSheet('background-color: #fff3cd; color: #856404;')
        
        notification_layout.addWidget(self.notification_display)
        notification_group.setLayout(notification_layout)
        main_layout.addWidget(notification_group)
        
        # Информация о трансферных окнах
        transfer_info_group = QGroupBox("Информация о трансферных окнах")
        transfer_info_layout = QVBoxLayout()
        
        transfer_info_label = QLabel("❄ Зимнее трансферное окно: с 17 по 21 неделю\n☀ Летнее трансферное окно: с 37 по 51 неделю")
        transfer_info_label.setStyleSheet('color: #0066cc; font-weight: bold; padding: 5px;')
        transfer_info_label.setAlignment(Qt.AlignCenter)
        
        transfer_info_layout.addWidget(transfer_info_label)
        transfer_info_group.setLayout(transfer_info_layout)
        main_layout.addWidget(transfer_info_group)
        
        # Создаем сетку для двух колонок
        grid_layout = QGridLayout()
        
        # Первая колонка (0-й столбец)
        # Поле для номера недели
        week_label = QLabel('Текущая неделя:')
        week_label.setFixedWidth(150)
        self.week_display = QSpinBox()
        self.week_display.setRange(1, 52)
        self.week_display.setValue(1)
        self.week_display.setReadOnly(True)
        self.week_display.setButtonSymbols(QSpinBox.NoButtons)
        self.week_display.setStyleSheet('background-color: #f0f0f0;')
        self.week_display.setFixedWidth(200)
        
        grid_layout.addWidget(week_label, 0, 0)
        grid_layout.addWidget(self.week_display, 0, 1)
        
        # Поле для ввода зарплаты
        salary_label = QLabel('Зарплата:')
        salary_label.setFixedWidth(150)
        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText('Введите сумму зарплаты')
        self.salary_input.setFixedWidth(200)
        
        grid_layout.addWidget(salary_label, 1, 0)
        grid_layout.addWidget(self.salary_input, 1, 1)
        
        # Поле для спонсорской помощи
        sponsor_label = QLabel('Спонсорская помощь:')
        sponsor_label.setFixedWidth(150)
        self.sponsor_input = QLineEdit()
        self.sponsor_input.setPlaceholderText('Введите сумму помощи')
        self.sponsor_input.setText('0')
        self.sponsor_input.setFixedWidth(200)
        
        grid_layout.addWidget(sponsor_label, 2, 0)
        grid_layout.addWidget(self.sponsor_input, 2, 1)
        
        # Поле для сезонных наград
        rewards_label = QLabel('Сезонные награды:')
        rewards_label.setFixedWidth(150)
        self.rewards_input = QLineEdit()
        self.rewards_input.setPlaceholderText('0')
        self.rewards_input.setEnabled(False)
        self.rewards_input.setStyleSheet('background-color: #f0f0f0;')
        self.rewards_input.setFixedWidth(200)
        
        grid_layout.addWidget(rewards_label, 3, 0)
        grid_layout.addWidget(self.rewards_input, 3, 1)
        
        # Вторая колонка (2-й столбец)
        # Поле для стартового баланса
        start_balance_label = QLabel('Стартовый баланс:')
        start_balance_label.setFixedWidth(150)
        self.start_balance_input = QLineEdit()
        self.start_balance_input.setPlaceholderText('Введите стартовый баланс')
        self.start_balance_input.setFixedWidth(215)
        
        grid_layout.addWidget(start_balance_label, 0, 2)
        grid_layout.addWidget(self.start_balance_input, 0, 3)
        
        # Кнопка установки стартового баланса (увеличенная)
        self.set_start_button = QPushButton('Установить стартовый баланс')
        self.set_start_button.clicked.connect(self.set_start_balance)
        self.set_start_button.setFixedWidth(250)
        self.set_start_button.setFixedHeight(40)
        self.set_start_button.setStyleSheet('padding: 5px 10px;')
        
        grid_layout.addWidget(QLabel(''), 1, 2)  # Пустой label для выравнивания
        grid_layout.addWidget(self.set_start_button, 1, 3)
        
        # Поле для текущего баланса
        current_balance_label = QLabel('Текущий баланс:')
        current_balance_label.setFixedWidth(150)
        self.current_balance_display = QLineEdit()
        self.current_balance_display.setReadOnly(True)
        self.current_balance_display.setText('0.00')
        self.current_balance_display.setStyleSheet('background-color: #f0f0f0;')
        self.current_balance_display.setFixedWidth(200)
        
        grid_layout.addWidget(current_balance_label, 2, 2)
        grid_layout.addWidget(self.current_balance_display, 2, 3)
        
        # Третья строка - Поле для трансферов (на всю ширину двух колонок)
        transfer_label = QLabel('Трансферы (положительное или отрицательное число):')
        transfer_label.setFixedWidth(425)
        self.transfer_input = QLineEdit()
        self.transfer_input.setPlaceholderText('Введите сумму трансфера')
        self.transfer_input.setFixedWidth(275)
        
        grid_layout.addWidget(transfer_label, 4, 0, 1, 2)  # Занимает 2 колонки
        grid_layout.addWidget(self.transfer_input, 4, 2, 1, 2)  # Занимает 2 колонки
        
        # Добавляем сетку в основной макет
        main_layout.addLayout(grid_layout)
        
        # Кнопка "Следующая неделя" (на всю ширину, увеличенная)
        self.next_week_button = QPushButton('Следующая неделя')
        self.next_week_button.clicked.connect(self.next_week)
        self.next_week_button.setEnabled(False)
        self.next_week_button.setMinimumHeight(50)
        self.next_week_button.setStyleSheet('font-size: 14px; font-weight: bold; padding: 8px;')
        main_layout.addWidget(self.next_week_button)
        
        main_layout.addStretch()
        
        # Добавляем страницу в виджет вкладок
        self.tab_widget.addTab(main_page, "Учет зарплат")
        
    def create_matches_page(self):
        """Создает страницу для ввода матчей (двухколоночный макет)"""
        matches_page = QWidget()
        matches_layout = QVBoxLayout(matches_page)
        
        # Инструкция (на всю ширину)
        instruction_label = QLabel("Используйте пресеты или введите номера недель вручную (через запятую или пробел):")
        instruction_label.setWordWrap(True)
        instruction_label.setStyleSheet('color: #666; padding: 5px;')
        matches_layout.addWidget(instruction_label)
        
        # Создаем сетку для двух колонок
        grid_layout = QGridLayout()
        
        # Левая колонка (0-й столбец) - Пресеты для матчей лиги
        league_preset_group = QGroupBox("Пресеты для матчей лиги")
        league_preset_layout = QVBoxLayout()
        
        preset_label = QLabel("Выберите количество команд в лиге:")
        league_preset_layout.addWidget(preset_label)
        
        # Группа радио-кнопок для выбора пресета лиги
        league_buttons_layout = QVBoxLayout()
        self.league_preset_group = QButtonGroup()
        
        self.preset_10_teams = QRadioButton("10 команд")
        self.preset_12_teams = QRadioButton("12 команд")
        self.preset_league_custom = QRadioButton("Свой вариант")
        self.preset_league_custom.setChecked(True)
        
        self.league_preset_group.addButton(self.preset_10_teams)
        self.league_preset_group.addButton(self.preset_12_teams)
        self.league_preset_group.addButton(self.preset_league_custom)
        
        league_buttons_layout.addWidget(self.preset_10_teams)
        league_buttons_layout.addWidget(self.preset_12_teams)
        league_buttons_layout.addWidget(self.preset_league_custom)
        
        league_preset_layout.addLayout(league_buttons_layout)
        
        # Кнопка применения пресета лиги (увеличенная)
        apply_league_preset_button = QPushButton('Применить пресет лиги')
        apply_league_preset_button.clicked.connect(self.apply_league_preset)
        apply_league_preset_button.setMinimumHeight(40)
        apply_league_preset_button.setStyleSheet('padding: 5px;')
        league_preset_layout.addWidget(apply_league_preset_button)
        
        league_preset_group.setLayout(league_preset_layout)
        grid_layout.addWidget(league_preset_group, 0, 0)
        
        # Правая колонка (1-й столбец) - Пресеты для еврокубков
        euro_preset_group = QGroupBox("Пресеты для еврокубков (можно выбрать несколько)")
        euro_preset_layout = QVBoxLayout()
        
        euro_label = QLabel("Выберите стадии еврокубков:")
        euro_preset_layout.addWidget(euro_label)
        
        # Чекбоксы для различных стадий еврокубков
        self.euro_qualification = QCheckBox("Квалификация (недели 38, 40, 42, 44, 46, 48, 50, 52)")
        self.euro_autumn = QCheckBox("Евроосень (недели 6, 8, 10, 12, 14, 16)")
        self.euro_playoff = QCheckBox("Стыковые матчи (недели 22, 24)")
        self.euro_spring = QCheckBox("Евровесна (недели 26, 28, 30, 32, 36)")
        
        euro_preset_layout.addWidget(self.euro_qualification)
        euro_preset_layout.addWidget(self.euro_autumn)
        euro_preset_layout.addWidget(self.euro_playoff)
        euro_preset_layout.addWidget(self.euro_spring)
        
        # Кнопка применения пресетов еврокубков (увеличенная)
        apply_euro_preset_button = QPushButton('Применить выбранные пресеты еврокубков')
        apply_euro_preset_button.clicked.connect(self.apply_euro_presets)
        apply_euro_preset_button.setMinimumHeight(40)
        apply_euro_preset_button.setStyleSheet('padding: 5px;')
        euro_preset_layout.addWidget(apply_euro_preset_button)
        
        euro_preset_group.setLayout(euro_preset_layout)
        grid_layout.addWidget(euro_preset_group, 0, 1)
        
        # Добавляем сетку с пресетами
        matches_layout.addLayout(grid_layout)
        
        # Создаем вторую сетку для полей ввода
        input_grid = QGridLayout()
        
        # Кубковые матчи
        cup_group = QGroupBox("Кубковые матчи")
        cup_layout = QVBoxLayout()
        
        cup_label = QLabel("Недели кубковых матчей:")
        self.cup_matches_input = QTextEdit()
        self.cup_matches_input.setPlaceholderText("Пример: 5, 10, 15, 20")
        self.cup_matches_input.setMaximumHeight(80)
        
        cup_layout.addWidget(cup_label)
        cup_layout.addWidget(self.cup_matches_input)
        cup_group.setLayout(cup_layout)
        input_grid.addWidget(cup_group, 0, 0)
        
        # Матчи лиги
        league_group = QGroupBox("Матчи лиги")
        league_layout = QVBoxLayout()
        
        league_label = QLabel("Недели матчей лиги:")
        self.league_matches_input = QTextEdit()
        self.league_matches_input.setPlaceholderText("Пример: 3, 8, 12, 18, 25")
        self.league_matches_input.setMaximumHeight(80)
        
        league_layout.addWidget(league_label)
        league_layout.addWidget(self.league_matches_input)
        league_group.setLayout(league_layout)
        input_grid.addWidget(league_group, 0, 1)
        
        # Еврокубковые матчи
        euro_group = QGroupBox("Еврокубковые матчи")
        euro_layout = QVBoxLayout()
        
        euro_label = QLabel("Недели еврокубковых матчей:")
        self.euro_matches_input = QTextEdit()
        self.euro_matches_input.setPlaceholderText("Пример: 7, 14, 21, 28")
        self.euro_matches_input.setMaximumHeight(80)
        
        euro_layout.addWidget(euro_label)
        euro_layout.addWidget(self.euro_matches_input)
        euro_group.setLayout(euro_layout)
        input_grid.addWidget(euro_group, 1, 0)
        
        # Кнопка сохранения и отображение сохраненных матчей (увеличенная)
        save_button = QPushButton('Сохранить расписание матчей')
        save_button.clicked.connect(self.save_matches)
        save_button.setMinimumHeight(50)
        save_button.setStyleSheet('font-weight: bold; padding: 8px;')
        input_grid.addWidget(save_button, 1, 1)
        
        matches_layout.addLayout(input_grid)
        
        # Список сохраненных матчей (на всю ширину)
        saved_group = QGroupBox("Сохраненные матчи")
        saved_layout = QVBoxLayout()
        
        self.saved_matches_display = QTextEdit()
        self.saved_matches_display.setReadOnly(True)
        self.saved_matches_display.setMaximumHeight(80)
        
        saved_layout.addWidget(self.saved_matches_display)
        saved_group.setLayout(saved_layout)
        matches_layout.addWidget(saved_group)
        
        matches_layout.addStretch()
        
        # Добавляем страницу в виджет вкладок
        self.tab_widget.addTab(matches_page, "Расписание матчей")
    
    def apply_league_preset(self):
        """Применяет выбранный пресет для матчей лиги"""
        if self.preset_10_teams.isChecked():
            # Пресет для 10 команд (недели 1-39 с шагом 2)
            weeks = list(range(1, 40, 2))
            weeks_text = ', '.join(map(str, weeks))
            self.league_matches_input.setPlainText(weeks_text)
        
        elif self.preset_12_teams.isChecked():
            # Пресет для 12 команд (недели 1-47 с шагом 2)
            weeks = list(range(1, 48, 2))
            weeks_text = ', '.join(map(str, weeks))
            self.league_matches_input.setPlainText(weeks_text)
        
        # Если выбран "Свой вариант", ничего не делаем
    
    def apply_euro_presets(self):
        """Применяет выбранные пресеты для еврокубков"""
        all_weeks = []
        
        if self.euro_qualification.isChecked():
            all_weeks.extend([38, 40, 42, 44, 46, 48, 50, 52])
        
        if self.euro_autumn.isChecked():
            all_weeks.extend([6, 8, 10, 12, 14, 16])
        
        if self.euro_playoff.isChecked():
            all_weeks.extend([22, 24])
        
        if self.euro_spring.isChecked():
            all_weeks.extend([26, 28, 30, 32, 36])
        
        # Убираем дубликаты и сортируем
        all_weeks = sorted(list(set(all_weeks)))
        
        if all_weeks:
            weeks_text = ', '.join(map(str, all_weeks))
            self.euro_matches_input.setPlainText(weeks_text)
        else:
            self.euro_matches_input.clear()
    
    def parse_weeks_input(self, text):
        """Преобразует введенный текст в список чисел"""
        weeks = []
        # Заменяем запятые на пробелы и разбиваем
        for part in text.replace(',', ' ').split():
            try:
                week = int(part.strip())
                if 1 <= week <= 52:
                    weeks.append(week)
            except ValueError:
                pass
        return sorted(list(set(weeks)))  # Убираем дубликаты и сортируем
    
    def save_matches(self):
        """Сохраняет введенные расписания матчей"""
        # Получаем тексты из полей ввода
        cup_text = self.cup_matches_input.toPlainText().strip()
        league_text = self.league_matches_input.toPlainText().strip()
        euro_text = self.euro_matches_input.toPlainText().strip()
        
        # Парсим недели
        self.cup_matches = self.parse_weeks_input(cup_text)
        self.league_matches = self.parse_weeks_input(league_text)
        self.euro_matches = self.parse_weeks_input(euro_text)
        
        # Обновляем отображение сохраненных матчей
        saved_text = "Сохраненное расписание:\n"
        if self.cup_matches:
            saved_text += f"🏆 Кубковые матчи: недели {', '.join(map(str, self.cup_matches))}\n"
        if self.league_matches:
            saved_text += f"⚽ Матчи лиги: недели {', '.join(map(str, self.league_matches))}\n"
        if self.euro_matches:
            saved_text += f"🌍 Еврокубки: недели {', '.join(map(str, self.euro_matches))}\n"
        
        if not (self.cup_matches or self.league_matches or self.euro_matches):
            saved_text = "Расписание пусто. Добавьте номера недель для матчей."
        
        self.saved_matches_display.setText(saved_text)
        
        # Проверяем матчи на текущей неделе
        self.check_week_matches()
    
    def check_week_matches(self):
        """Проверяет, есть ли матчи на текущей неделе"""
        matches_on_week = []
        
        if self.week_number in self.cup_matches:
            matches_on_week.append("🏆 КУБКОВЫЙ МАТЧ")
        
        if self.week_number in self.league_matches:
            matches_on_week.append("⚽ МАТЧ ЛИГИ")
        
        if self.week_number in self.euro_matches:
            matches_on_week.append("🌍 ЕВРОКУБКОВЫЙ МАТЧ")
        
        # Обновляем уведомление
        if matches_on_week:
            notification = f"⚠ На этой неделе ({self.week_number}): " + ", ".join(matches_on_week)
            self.notification_display.setText(notification)
            self.notification_display.setStyleSheet('background-color: #d4edda; color: #155724; font-weight: bold;')
        else:
            self.notification_display.setText("✅ На этой неделе матчей нет")
            self.notification_display.setStyleSheet('background-color: #fff3cd; color: #856404;')
    
    def set_start_balance(self):
        """Устанавливает стартовый баланс (без message box)"""
        try:
            start_text = self.start_balance_input.text().strip()
            
            if not start_text:
                # Просто игнорируем пустой ввод
                self.start_balance_input.setPlaceholderText('Введите стартовый баланс!')
                return
            
            self.start_balance = float(start_text)
            self.current_balance = self.start_balance
            
            self.current_balance_display.setText(f'{self.current_balance:.2f}')
            self.next_week_button.setEnabled(True)
            
            self.start_balance_input.setReadOnly(True)
            self.set_start_button.setEnabled(False)
            self.start_balance_input.setStyleSheet('background-color: #f0f0f0;')
            
        except ValueError:
            # Просто показываем ошибку в поле ввода
            self.start_balance_input.setText('')
            self.start_balance_input.setPlaceholderText('Ошибка! Введите число')
    
    def next_week(self):
        """Обработчик нажатия кнопки следующая неделя (без message box)"""
        try:
            # Проверяем, наступила ли 48 неделя
            if self.week_number == 48 and not self.seasonal_rewards_added:
                rewards_text = self.rewards_input.text().strip()
                
                # Если поле пустое, используем 0
                if not rewards_text:
                    rewards = 0
                else:
                    try:
                        rewards = float(rewards_text)
                        if rewards < 0:
                            rewards = 0
                    except ValueError:
                        rewards = 0
                
                # Добавляем награды к балансу (даже если 0)
                self.current_balance += rewards
                self.seasonal_rewards_added = True
                
                # Сбрасываем поле и делаем его недоступным
                self.rewards_input.clear()
                self.rewards_input.setEnabled(False)
                self.rewards_input.setStyleSheet('background-color: #f0f0f0;')
            
            salary_text = self.salary_input.text().strip()
            
            if not salary_text:
                # Подсвечиваем поле при ошибке
                self.salary_input.setStyleSheet('border: 2px solid red;')
                self.salary_input.setPlaceholderText('Введите сумму зарплаты!')
                return
            
            salary = float(salary_text)
            
            if salary <= 0:
                self.salary_input.setStyleSheet('border: 2px solid red;')
                self.salary_input.setText('')
                self.salary_input.setPlaceholderText('Зарплата > 0!')
                return
            
            # Сбрасываем стиль поля зарплаты
            self.salary_input.setStyleSheet('')
            
            # Вычитаем зарплату
            self.current_balance -= salary
            
            # Проверяем спонсорскую помощь
            if self.week_number % 4 == 1:
                sponsor_text = self.sponsor_input.text().strip()
                if sponsor_text:
                    try:
                        sponsor_amount = float(sponsor_text)
                        if sponsor_amount > 0:
                            self.current_balance += sponsor_amount
                    except ValueError:
                        # Игнорируем ошибку в спонсорской помощи
                        pass
            
            # Проверяем и применяем трансферы
            transfer_text = self.transfer_input.text().strip()
            if transfer_text:
                try:
                    transfer_amount = float(transfer_text)
                    if transfer_amount != 0:
                        self.current_balance += transfer_amount
                        # Визуально отмечаем примененный трансфер
                        self.transfer_input.setStyleSheet('border: 2px solid green;')
                        # Сбрасываем стиль через таймер
                        QTimer.singleShot(1000, lambda: self.transfer_input.setStyleSheet(''))
                except ValueError:
                    # Подсвечиваем поле при ошибке
                    self.transfer_input.setStyleSheet('border: 2px solid red;')
                    self.transfer_input.setText('')
                    self.transfer_input.setPlaceholderText('Некорректная сумма!')
                    return
            
            # Очищаем поле трансферов после применения
            self.transfer_input.clear()
            
            # Увеличиваем номер недели
            self.week_number += 1
            if self.week_number > 52:
                self.week_number = 1
                # Сбрасываем флаг сезонных наград для нового сезона
                self.seasonal_rewards_added = False
            
            # Обновляем отображение
            self.week_display.setValue(self.week_number)
            self.current_balance_display.setText(f'{self.current_balance:.2f}')
            
            # Проверяем, наступила ли 48 неделя
            if self.week_number == 48:
                self.rewards_input.setEnabled(True)
                self.rewards_input.setStyleSheet('background-color: white;')
                self.rewards_input.setPlaceholderText('0')
                self.rewards_input.clear()
                self.seasonal_rewards_added = False
            else:
                self.rewards_input.setEnabled(False)
                self.rewards_input.setStyleSheet('background-color: #f0f0f0;')
                self.rewards_input.setPlaceholderText('0')
            
            # Проверяем матчи на новой неделе
            self.check_week_matches()
            
        except ValueError:
            # Обрабатываем ошибку преобразования числа
            self.salary_input.setStyleSheet('border: 2px solid red;')
            self.salary_input.setText('')
            self.salary_input.setPlaceholderText('Введите число!')
    
    def keyPressEvent(self, event):
        """Обработка нажатия клавиш"""
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.focusNextChild()


def main():
    app = QApplication(sys.argv)
    window = SalaryApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()