import tkinter as tk
from tkinter import messagebox

### Инициализация главного окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

### Глобальные переменные
current_player = "X"
buttons = []
player_choice = None
scores = {"X": 0, "O": 0}

### Виджеты для интерфейса
choice_frame = tk.Frame(window)
choice_frame.pack(pady=10)

score_label = tk.Label(window, text="X: 0  |  O: 0", font=("Arial", 12))
score_label.pack()

reset_button = tk.Button(window, text="Новая игра", command=lambda: reset_game())
reset_button.pack(pady=5)


### Функция проверки победителя
def check_winner():
    # Проверка строк
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Проверка диагоналей
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


### Функция проверки ничьи
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True


### Обработчик клика по клетке
def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "" or not player_choice:
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        scores[current_player] += 1
        update_score()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_board()
    elif check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_board()
    else:
        current_player = "O" if current_player == "X" else "X"


### Сброс игрового поля
def reset_board():
    for row in buttons:
        for btn in row:
            btn.config(text="")


### Полный сброс игры
def reset_game():
    global current_player
    reset_board()
    current_player = "X"
    if player_choice == "O":
        current_player = "O"


### Обновление счета
def update_score():
    score_label.config(text=f"X: {scores['X']}  |  O: {scores['O']}")


### Выбор символа игрока
def choose_symbol(symbol):
    global player_choice, current_player
    player_choice = symbol
    current_player = symbol
    for btn in [x_btn, o_btn]:
        btn.config(state=tk.DISABLED)


### Создание кнопок выбора символа
x_btn = tk.Button(choice_frame, text="Играть за X", command=lambda: choose_symbol("X"))
x_btn.pack(side=tk.LEFT, padx=5)

o_btn = tk.Button(choice_frame, text="Играть за O", command=lambda: choose_symbol("O"))
o_btn.pack(side=tk.LEFT, padx=5)

### Создание игрового поля
game_frame = tk.Frame(window)
game_frame.pack(pady=10)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

### Запуск главного цикла
window.mainloop()
