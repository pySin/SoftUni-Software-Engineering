# Tic Tac Toe TK
import tkinter as tk


def start_game(window, player_one):
    pass


def start_screen():
    window = tk.Tk()
    window.geometry('240x240')
    window.title("Tic Tac Toe")
    # window.configure(bg="white")

    tk.Label(window, text="First player name: ", bg="blue").pack()
    player_one = tk.Entry(window)
    player_one.pack()

    tk.Button(window, text="Start game", command=lambda: start_game(window, player_one)).pack()

    window.mainloop()


if __name__ == "__main__":
    start_screen()


