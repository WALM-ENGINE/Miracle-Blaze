from game.engine import config

eng = {
    'settings': 'Settings',
    'exit': 'Exit',
    'play': 'Play',
    'fullscreen': 'Fullscreen mode',
    'sound': 'Sound',
    'on': 'ON',
    'off': 'OFF',
    'lang': 'Language',
    'ru-ru': 'RU',
    'en-us': 'EN',
    'pause': 'Pause',
    'continue': 'Continue ',
    'main menu': 'Main menu', 
    'speak': 'Speak',
    'controls': 'Controls',
    'up': 'Up',
    'down': 'Down',
    'left': 'Left',
    'right': 'Right',
    'change': 'Change',
    'presskey' : 'Нажмите клавишу',
    'abilities': 'Abilities',
    'attack': 'Attack',
    'wabani_voites': [['Hello. (Wabani)', ' ', ' ', ' ', ' ']],
    'anonymous_voites': [['I woke up in some kind of cell. At first though', 'it was unfamiliar, but I began my journey.', '(Anonymous)', ' ', ' '],
                         
                        ["In my dream I saw her, but didn't recognize ", 'her, even though in at the beginning of the ', 'journey, she met with me and helped me','understand where I was. (Anonymous)', ' '],
                        
                        ['Soon her silhouette began to appear so', 'frequently to flicker by, until at the end of', "my journey I couldn't remember who she was.", '(Anonymous)', ' ']

                        ]
}
rus = {
    'settings': 'Настройки',
    'exit': 'Выход',
    'play': 'Играть',
    'fullscreen' : 'Полноэкранный режим',
    'sound': 'Звук',
    'on': 'Вкл',
    'off': 'Выкл',
    'lang': 'Язык',
    'ru-ru': 'RU',
    'en-us': 'EN',
    'pause': 'Пауза',
    'continue': 'Продолжить ',
    'main menu': 'Главное меню',
    'controls': 'Управление',
    'speak': 'Разговоры',
    'up': 'Вверх',
    'down': 'Вниз',
    'left': 'Влево',
    'right': 'Вправо',
    'change': 'Изменить',
    'presskey': 'Press key',
    'abilities': 'Способности',
    'attack': 'Атака',
    'wabani_voites': [['Привет. (Вабани)', ' ', ' ', ' ', ' ']],
    'anonymous_voites': [['Я проснулся в какой-то камере. Хоть поначалу', 'было непривычно, однако я начал свой путь.', '(Aнонимус)', ' ', ' '],
                         
                        ['Во сне я увидел её, но не узнавал, хотя в ', 'начале пути она встретилась со мной ', 'и помогла понять, где я нахожусь. (Анонимус)',' ', ' '],
                        
                        ['Вскоре её силуэт настолько часто начал', 'мелькать, пока в конце моего странствия ', 'я не вспомнил, кто она. (Анонимус)', ' ', ' ']

                        ]
}

if config.language == 'rus':
    lofig = rus
elif config.language == 'eng':
    lofig = eng

def get_localize(localize: str):
    return lofig[localize]