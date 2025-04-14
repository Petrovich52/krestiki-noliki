import tkinter as tk
from tkinter import messagebox, font

# Инициализация окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("350x500")
window.configure(bg="#f0f0f0")

# Шрифты
custom_font = font.Font(family="Helvetica", size=14, weight="bold")
button_font = font.Font(family="Arial", size=20)
title_font = font.Font(family="Verdana", size=16, weight="bold")

# Глобальные переменные
current_player = "X"
buttons = []
player_choice = None
scores = {"X": 0, "O": 0}
game_round = 1
max_wins = 3


# Основные функции
def choose_symbol(symbol):
    global player_choice, current_player
    player_choice = symbol
    current_player = symbol
    x_btn.config(state=tk.DISABLED, bg="#95a5a6")
    o_btn.config(state=tk.DISABLED, bg="#95a5a6")


def reset_board():
    global current_player
    for row in buttons:
        for btn in row:
            btn.config(text="", bg="white", fg="black")
    current_player = player_choice if player_choice else "X"


def reset_game():
    global current_player, game_round, scores, player_choice
    reset_board()
    current_player = "X"
    player_choice = None
    game_round = 1
    scores = {"X": 0, "O": 0}
    update_score()
    round_label.config(text=f"Раунд: {game_round}")
    x_btn.config(state=tk.NORMAL, bg="#e74c3c")
    o_btn.config(state=tk.NORMAL, bg="#3498db")


def update_score():
    x_score.config(text=f"X: {scores['X']}")
    o_score.config(text=f"O: {scores['O']}")


def check_winner():
    # Проверка строк и столбцов
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


def on_click(row, col):
    global current_player, game_round

    if buttons[row][col]['text'] != "" or not player_choice:
        return

    buttons[row][col]['text'] = current_player
    buttons[row][col].config(fg="#e74c3c" if current_player == "X" else "#3498db")

    if check_winner():
        scores[current_player] += 1
        update_score()
        if scores[current_player] >= max_wins:
            messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил в матче!")
            reset_game()
        else:
            messagebox.showinfo("Раунд окончен", f"Игрок {current_player} победил в раунде!")
            game_round += 1
            round_label.config(text=f"Раунд: {game_round}")
            reset_board()
    elif all(btn["text"] != "" for row in buttons for btn in row):
        messagebox.showinfo("Раунд окончен", "Ничья!")
        game_round += 1
        round_label.config(text=f"Раунд: {game_round}")
        reset_board()
    else:
        current_player = "O" if current_player == "X" else "X"


# Интерфейс
header_frame = tk.Frame(window, bg="#f0f0f0")
header_frame.pack(pady=10)

title_label = tk.Label(header_frame, text="КРЕСТИКИ-НОЛИКИ", font=title_font, bg="#f0f0f0", fg="#333")
title_label.pack()

# Счетчики
score_frame = tk.Frame(window, bg="#f0f0f0")
score_frame.pack(pady=5)
x_score = tk.Label(score_frame, text="X: 0", font=custom_font, bg="#f0f0f0", fg="#e74c3c")
x_score.pack(side=tk.LEFT, padx=10)
o_score = tk.Label(score_frame, text="O: 0", font=custom_font, bg="#f0f0f0", fg="#3498db")
o_score.pack(side=tk.LEFT, padx=10)

round_label = tk.Label(window, text=f"Раунд: {game_round}", font=custom_font, bg="#f0f0f0")
round_label.pack(pady=5)

# Кнопки выбора
control_frame = tk.Frame(window, bg="#f0f0f0")
control_frame.pack(pady=10)
x_btn = tk.Button(control_frame, text="Играть за X", font=custom_font, bg="#e74c3c", fg="white",
                  command=lambda: choose_symbol("X"))
x_btn.pack(side=tk.LEFT, padx=5)
o_btn = tk.Button(control_frame, text="Играть за O", font=custom_font, bg="#3498db", fg="white",
                  command=lambda: choose_symbol("O"))
o_btn.pack(side=tk.LEFT, padx=5)

# Игровое поле 3x3
game_frame = tk.Frame(window, bg="#f0f0f0")
game_frame.pack(pady=10)
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=button_font, width=5, height=2,
                        bg="white", relief="ridge", borderwidth=3,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса (зеленая, под полем)
reset_button = tk.Button(window, text="Новая игра", font=custom_font,
                         bg="#2ecc71", fg="white", command=reset_game)
reset_button.pack(pady=15)

window.mainloop()