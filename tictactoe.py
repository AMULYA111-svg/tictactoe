import tkinter as tk
from tkinter import messagebox

# ---------- COLORS ----------
BG_COLOR = "#1b0d1a"
CARD_COLOR = "#2a1430"
BOX_COLOR = "#4a2954"
BOX_HOVER = "#5a3366"
TEXT_COLOR = "#ffeaf4"
SUBTEXT_COLOR = "#d6a9c3"
X_COLOR = "#ff5ca8"
O_COLOR = "#ffb3d9"
WIN_COLOR = "#ff4f87"
DRAW_COLOR = "#ffd166"
BTN_COLOR = "#8e2f5d"
BTN_HOVER = "#b03d74"
RESET_COLOR = "#612440"
RESET_HOVER = "#7c3052"


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Python GUI")
        self.root.geometry("560x720")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0
        self.buttons = []

        self.create_ui()

    def create_ui(self):
        title = tk.Label(
            self.root,
            text="TIC TAC TOE",
            font=("Segoe UI", 24, "bold"),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        title.pack(pady=(18, 4))

        subtitle = tk.Label(
            self.root,
            text="Python GUI Game",
            font=("Segoe UI", 11),
            bg=BG_COLOR,
            fg=SUBTEXT_COLOR
        )
        subtitle.pack(pady=(0, 12))

        score_frame = tk.Frame(self.root, bg=CARD_COLOR)
        score_frame.pack(padx=18, pady=10, fill="x")

        self.x_label = tk.Label(
            score_frame,
            text="Player X : 0",
            font=("Segoe UI", 12, "bold"),
            bg=CARD_COLOR,
            fg=X_COLOR,
            pady=14
        )
        self.x_label.grid(row=0, column=0, padx=16)

        self.draw_label = tk.Label(
            score_frame,
            text="Draws : 0",
            font=("Segoe UI", 12, "bold"),
            bg=CARD_COLOR,
            fg=DRAW_COLOR,
            pady=14
        )
        self.draw_label.grid(row=0, column=1, padx=16)

        self.o_label = tk.Label(
            score_frame,
            text="Player O : 0",
            font=("Segoe UI", 12, "bold"),
            bg=CARD_COLOR,
            fg=O_COLOR,
            pady=14
        )
        self.o_label.grid(row=0, column=2, padx=16)

        self.status_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Segoe UI", 16, "bold"),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        self.status_label.pack(pady=16)

        board_frame = tk.Frame(self.root, bg=BG_COLOR)
        board_frame.pack(pady=6)

        for i in range(9):
            btn = tk.Button(
                board_frame,
                text="",
                font=("Segoe UI", 24, "bold"),
                width=5,
                height=2,
                bg=BOX_COLOR,
                fg=TEXT_COLOR,
                activebackground=BOX_HOVER,
                activeforeground=TEXT_COLOR,
                bd=0,
                relief="flat",
                cursor="hand2",
                command=lambda i=i: self.make_move(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=8, pady=8)
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_leave(b))
            self.buttons.append(btn)

        control_frame = tk.Frame(self.root, bg=BG_COLOR)
        control_frame.pack(pady=22)

        restart_btn = tk.Button(
            control_frame,
            text="Restart Round",
            font=("Segoe UI", 11, "bold"),
            bg=BTN_COLOR,
            fg="white",
            activebackground=BTN_HOVER,
            activeforeground="white",
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
            command=self.reset_board
        )
        restart_btn.grid(row=0, column=0, padx=8)
        restart_btn.bind("<Enter>", lambda e: restart_btn.config(bg=BTN_HOVER))
        restart_btn.bind("<Leave>", lambda e: restart_btn.config(bg=BTN_COLOR))

        reset_btn = tk.Button(
            control_frame,
            text="Reset Score",
            font=("Segoe UI", 11, "bold"),
            bg=RESET_COLOR,
            fg="white",
            activebackground=RESET_HOVER,
            activeforeground="white",
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
            command=self.reset_all
        )
        reset_btn.grid(row=0, column=1, padx=8)
        reset_btn.bind("<Enter>", lambda e: reset_btn.config(bg=RESET_HOVER))
        reset_btn.bind("<Leave>", lambda e: reset_btn.config(bg=RESET_COLOR))

        footer = tk.Label(
            self.root,
            text="Built with Python & Tkinter",
            font=("Segoe UI", 9),
            bg=BG_COLOR,
            fg=SUBTEXT_COLOR
        )
        footer.pack(side="bottom", pady=12)

    def on_hover(self, button):
        if button["text"] == "" and not self.game_over:
            button.config(bg=BOX_HOVER)

    def on_leave(self, button):
        if button["text"] == "" and not self.game_over:
            button.config(bg=BOX_COLOR)

    def make_move(self, index):
        if self.board[index] != "" or self.game_over:
            return

        self.board[index] = self.current_player

        if self.current_player == "X":
            self.buttons[index].config(text="X", fg=X_COLOR, bg=CARD_COLOR)
        else:
            self.buttons[index].config(text="O", fg=O_COLOR, bg=CARD_COLOR)

        winner = self.check_winner()

        if winner:
            self.game_over = True
            for i in winner:
                self.buttons[i].config(bg=WIN_COLOR, fg="white")

            if self.current_player == "X":
                self.x_score += 1
            else:
                self.o_score += 1

            self.update_score()
            self.status_label.config(
                text=f"🎉 Congratulations! Player {self.current_player} Wins!",
                fg=WIN_COLOR
            )

            play_again = messagebox.askyesno(
                "Congratulations!",
                f"🎉 Congratulations Player {self.current_player}!\n\nYou won the game.\n\nDo you want to play again?"
            )

            if play_again:
                self.reset_board()

            return

        if "" not in self.board:
            self.game_over = True
            self.draw_score += 1
            self.update_score()
            self.status_label.config(text="It's a Draw!", fg=DRAW_COLOR)

            play_again = messagebox.askyesno(
                "Draw Game",
                "It's a draw!\n\nDo you want to play again?"
            )

            if play_again:
                self.reset_board()

            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s Turn", fg=TEXT_COLOR)

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return (a, b, c)
        return None

    def update_score(self):
        self.x_label.config(text=f"Player X : {self.x_score}")
        self.o_label.config(text=f"Player O : {self.o_score}")
        self.draw_label.config(text=f"Draws : {self.draw_score}")

    def reset_board(self):
        self.board = [""] * 9
        self.game_over = False
        self.current_player = "X"
        self.status_label.config(text="Player X's Turn", fg=TEXT_COLOR)

        for btn in self.buttons:
            btn.config(text="", bg=BOX_COLOR, fg=TEXT_COLOR)

    def reset_all(self):
        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0
        self.update_score()
        self.reset_board()



if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()