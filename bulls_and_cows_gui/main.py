import random
import tkinter as tk
from collections import Counter
from pathlib import Path

# ================================
# Bulls and Cows GUI Game
# ================================
# Homework rule used here:
# Cows  = correct digit in the correct position.
# Bulls = correct digit, but in the wrong position.

WINDOW_WIDTH = 768
WINDOW_HEIGHT = 512
ASSET_DIR = Path(__file__).parent / "assets"


def make_magic_number() -> str:
    """Create a random 4-digit number."""
    return str(random.randint(1000, 9999))


def check_user_choice(user_choice: str, magic_number: str) -> tuple[int, int]:
    """Return cows and bulls for one user guess."""
    cows = 0

    for i in range(4):
        if user_choice[i] == magic_number[i]:
            cows += 1

    total_matching_digits = sum((Counter(user_choice) & Counter(magic_number)).values())
    bulls = total_matching_digits - cows

    return cows, bulls


class BullsAndCowsApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Bulls and Cows")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        self.magic_number = make_magic_number()
        self.attempts = 0
        self.history = []

        self.images = {}
        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            highlightthickness=0,
            bd=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.show_menu()

    def load_image(self, image_name: str) -> tk.PhotoImage:
        if image_name not in self.images:
            self.images[image_name] = tk.PhotoImage(file=ASSET_DIR / image_name)
        return self.images[image_name]

    def clear_screen(self):
        self.canvas.delete("all")
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()

    def set_background(self, image_name: str):
        image = self.load_image(image_name)
        self.canvas.create_image(0, 0, image=image, anchor="nw")

    def make_button(self, text: str, command, width: int = 14) -> tk.Button:
        return tk.Button(
            self.root,
            text=text,
            command=command,
            font=("Arial", 15, "bold"),
            bg="#4f8f36",
            fg="white",
            activebackground="#356827",
            activeforeground="white",
            relief="raised",
            bd=5,
            width=width,
            height=1,
            padx=12,
            pady=6,
            cursor="hand2",
        )

    def show_menu(self):
        self.clear_screen()
        self.set_background("menu_screen.png")

        play_button = self.make_button("PLAY", self.new_game, width=16)
        how_button = self.make_button("HOW TO PLAY", self.show_how_to_play, width=16)

        self.canvas.create_window(392, 370, window=play_button)
        self.canvas.create_window(392, 440, window=how_button)

    def new_game(self):
        self.magic_number = make_magic_number()
        self.attempts = 0
        self.history = []
        self.show_game()

    def show_game(self):
        self.clear_screen()
        self.set_background("game_screen.png")

        # Cover only old cow number "0"
        self.canvas.create_rectangle(
            315, 400, 350, 432,
            fill="#fff1d2",
            outline="#fff1d2"
        )

        # Cover only old bull number "2"
        self.canvas.create_rectangle(
            555, 400, 590, 432,
            fill="#fff1d2",
            outline="#fff1d2"
        )

        # Cover only old static Attempts text, not the whole button
        self.canvas.create_rectangle(
            625, 37, 735, 75,
            fill="#8b5429",
            outline="#8b5429"
        )

        self.attempts_text = self.canvas.create_text(
            680,
            56,
            text=f"Attempts: {self.attempts}",
            font=("Arial", 13, "bold"),
            fill="white",
        )

        # Main working input panel
        self.canvas.create_rectangle(
            188, 98, 580, 351,
            fill="#f8ecd0",
            outline="#b8844b",
            width=3
        )

        self.canvas.create_text(
            384,
            130,
            text="Enter 4-digit number:",
            font=("Arial", 18, "bold"),
            fill="#2e2118",
        )

        self.entry = tk.Entry(
            self.root,
            font=("Arial", 28, "bold"),
            justify="center",
            width=8,
            bd=4,
            relief="ridge",
        )

        self.canvas.create_window(384, 185, window=self.entry)
        self.entry.focus_set()
        self.entry.bind("<Return>", lambda event: self.check_guess())

        check_button = self.make_button("CHECK", self.check_guess, width=10)
        self.canvas.create_window(384, 250, window=check_button)

        self.error_text = self.canvas.create_text(
            384,
            315,
            text="",
            font=("Arial", 13, "bold"),
            fill="#8b1e1e",
        )

        # Only dynamic cow number
        self.cows_text = self.canvas.create_text(
            334,
            422,
            text="-",
            font=("Arial", 26, "bold"),
            fill="#2e6b25",
        )

        # Only dynamic bull number
        self.bulls_text = self.canvas.create_text(
            571,
            422,
            text="-",
            font=("Arial", 26, "bold"),
            fill="#8b3e1f",
        )

    def check_guess(self):
        user_choice = self.entry.get().strip()

        if len(user_choice) != 4 or not user_choice.isdigit():
            self.canvas.itemconfig(
                self.error_text,
                text="WRONG! Enter exactly 4 digits."
            )
            self.entry.delete(0, tk.END)
            return

        self.canvas.itemconfig(self.error_text, text="")

        self.attempts += 1
        cows, bulls = check_user_choice(user_choice, self.magic_number)

        self.canvas.itemconfig(
            self.attempts_text,
            text=f"Attempts: {self.attempts}"
        )

        if cows == 4:
            self.show_win()
            return

        self.canvas.itemconfig(self.cows_text, text=str(cows))
        self.canvas.itemconfig(self.bulls_text, text=str(bulls))

        self.entry.delete(0, tk.END)
        self.entry.focus_set()

    def show_win(self):
        self.clear_screen()
        self.set_background("win_screen.png")

        self.canvas.create_rectangle(145, 315, 625, 445, fill="#fff4d8", outline="#b8844b", width=4)
        self.canvas.create_text(
            384,
            355,
            text="YOU WON!",
            font=("Arial", 34, "bold"),
            fill="#3d812b",
        )
        self.canvas.create_text(
            384,
            405,
            text=f"Attempts made: {self.attempts}",
            font=("Arial", 20, "bold"),
            fill="#2e2118",
        )

        again_button = self.make_button("PLAY AGAIN", self.new_game, width=12)
        menu_button = self.make_button("MENU", self.show_menu, width=12)

        self.canvas.create_window(300, 470, window=again_button)
        self.canvas.create_window(470, 470, window=menu_button)

    def show_how_to_play(self):
        self.clear_screen()
        self.set_background("how_to_play_screen.png")

        # # Cover old text and print instructions matching this homework version.
        # self.canvas.create_rectangle(95, 118, 675, 410, fill="#fff1d2", outline="#b8844b", width=4)
        # self.canvas.create_text(
        #     384,
        #     70,
        #     # text="HOW TO PLAY",
        #     font=("Arial", 30, "bold"),
        #     fill="#4a2615",
        # )
        # self.canvas.create_text(
        #     384,
        #     155,
        #     text="1. The computer chooses a 4-digit number.",
        #     font=("Arial", 16, "bold"),
        #     fill="#2e2118",
        # )
        # self.canvas.create_text(
        #     384,
        #     205,
        #     text="2. Enter your 4-digit guess and press CHECK.",
        #     font=("Arial", 16, "bold"),
        #     fill="#2e2118",
        # )
        # self.canvas.create_text(
        #     384,
        #     265,
        #     text="Cows = correct digit in the correct position.",
        #     font=("Arial", 16, "bold"),
        #     fill="#2e6b25",
        # )
        # self.canvas.create_text(
        #     384,
        #     315,
        #     text="Bulls = correct digit, but in the wrong position.",
        #     font=("Arial", 16, "bold"),
        #     fill="#8b3e1f",
        # )
        # self.canvas.create_text(
        #     384,
        #     370,
        #     text="Win when you get 4 cows.",
        #     font=("Arial", 18, "bold"),
        #     fill="#2e2118",
        # )

        back_button = self.make_button("BACK", self.show_menu, width=12)
        self.canvas.create_window(348, 420, window=back_button)


if __name__ == "__main__":
    root = tk.Tk()
    app = BullsAndCowsApp(root)
    root.mainloop()
