import tkinter as tk
from tkinter import messagebox
import random

PUZZLES = {
    "Easy": [
        {
            "solution": [
                ['C', 'A', 'T', '_', 'M', '_'],
                ['A', '_', '_', '_', 'A', '_'],
                ['R', '_', 'R', 'A', 'T', 'S'],
                ['T', '_', '_', '_', '_', '_'],
                ['_', 'D', 'O', 'G', '_', '_'],
                ['_', '_', '_', '_', '_', '_'],
            ],
            "clue_numbers": {
                (0, 0): 1,
                (2, 2): 4,
                (4, 1): 3,
                (0, 4): 2,
            },
            "across_clues": {
                1: "A small pet that says meow (3 letters)",
                3: "A loyal pet (3 letters)",
                4: "Plural of a common rodent (4 letters)",
            },
            "down_clues": {
                1: "3,1,18,20 guess the word using these numbers (4 letters)",
                2: "Thing used on floor in houses (3 letters)",
            }
        },
        {
            "solution": [
                ['B', 'I', 'R', 'D', '_', '_'],
                ['_', '_', 'O', '_', '_', '_'],
                ['_', '_', 'S', 'E', 'A', '_'],
                ['_', 'H', 'E', 'A', 'R', 'T'],
                ['_', '_', '_', '_', '_', 'E'],
                ['_', '_', '_', '_', '_', 'A'],
            ],
            "clue_numbers": {
                (0, 0): 1,
                (3, 5): 2,
                (2, 2): 3,
                (0, 2): 4,
                (3, 1): 5
            },
            "across_clues": {
                1: "A flying animal that starts with B (4 letters)",
                3: "Large body of salt water (3 letters)",
                5: "Organ that pumps blood (5 letters)",
            },
            "down_clues": {
                2: "Common drink (3 letters)",
                4: "Flowering plant with a thorny stem (4 letters)"
            }
        }
    ],
    "Medium": [
        {
            "solution": [
                ['P', 'I', 'A', 'N', 'O', '_'],
                ['_', '_', 'S', '_', 'T', '_'],
                ['_', '_', 'S', '_', 'H', '_'],
                ['_', '_', 'A', '_', 'E', '_'],
                ['_', 'S', 'M', 'A', 'R', 'T'],
                ['_', '_', '_', '_', 'S', '_'],
            ],
            "clue_numbers": {
                (0, 0): 1,
                (0, 2): 2,
                (4, 1): 3,
                (0, 4): 4,
            },
            "across_clues": {
                1: "A keyboard musical instrument (5 letters)",
                3: "Intelligent or clever (5 letters)",
            },
            "down_clues": {
                2: "Indian state with Brahmaputra River (5 letters)",
                4: "Remaing people or things(6 letters)",
            }
        },
        {
            "solution": [
                ['G', 'U', 'I', 'T', 'A', 'R'],
                ['_', '_', 'T', '_', '_', '_'],
                ['_', '_', 'A', '_', '_', '_'],
                ['_', '_', 'L', 'U', 'C', 'K'],
                ['_', '_', 'Y', 'O', 'G', 'A'],
                ['_', '_', '_', '_', '_', '_'],
            ],
            "clue_numbers": {
                (0, 0): 1,
                (0, 2): 2,
                (3, 2): 3,
                (4, 2): 4

            },
            "across_clues": {
                1: "String instrument (6 letters)",
                4: "Exercise for mind and body(4 letters)",
            },
            "down_clues": {
                2: "Home of colosseum and Roman Empire(5 Letters)",
                3: "Good fortune or chance(4 Letters)",
            }
        }
    ],
    "Hard": [
        {
            "solution": [
                ['_', '_', 'N', '_', '_', '_'],
                ['_', '_', 'I', '_', 'P', '_'],
                ['B', 'A', 'L', 'L', 'E', 'T'],
                ['_', '_', 'E', 'O', 'A', '_'],
                ['_', '_', '_', 'A', 'R', '_'],
                ['_', '_', '_', 'N', '_', '_'],
            ],
            "clue_numbers": {
                (2, 0): 1,
                (0, 2): 2,
                (1, 4): 3,
                (2, 3): 4
            },
            "across_clues": {
                1: "Dance genre that tells stories through movement(6 letters)",
            },
            "down_clues": {
                2: "World's longest river(4 letters)",
                3: "A fruit used for cooking and baking(4 letters)",
                4: "Provide financial help (4 letters)",
            }
        },
        {
            "solution": [
                ['S', 'O', 'C', 'C', 'E', 'R'],
                ['_', '_', '_', '_', 'A', '_'],
                ['_', 'K', 'I', 'N', 'G', '_'],
                ['_', '_', '_', '_', 'L', '_'],
                ['_', '_', 'G', 'E', 'E', 'K'],
                ['_', '_', '_', '_', '_', '_'],
            ],
            "clue_numbers": {
                (0, 0): 1,
                (0, 4): 2,
                (2, 1): 3,
                (4, 2): 4
            },
            "across_clues": {
                1: "For which sport is FIFA world cup is given(6 letters)",
                3: "A chess piece which cannot be captured",
                4: " Tech enthusiast (4 letters)"
            },
            "down_clues": {
                2: "Bird that start with letter E and Ends with E(5 letters)",
            }
        }
    ]
}


class CrosswordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Crossword Puzzle Game")
        self.root.geometry("450x750")
        self.root.configure(bg='skyblue')
        self.entries = {}
        self.answers = {}
        self.clue_numbers = {}
        self.across_clues = {}
        self.down_clues = {}
        self.level = None
        self.confetti_running = False
        self.confetti_items = []

        # Frames for UI parts
        self.level_frame = tk.Frame(self.root, bg='skyblue')
        self.grid_frame = None
        self.buttons_frame = None
        self.clues_frame = None
        self.congrats_frame = None

        self.level_frame.pack(pady=20)
        tk.Label(self.level_frame, text="Select Difficulty Level:",
                 font=("Arial", 14, "bold"), bg='skyblue').pack(pady=10)

        self.level_buttons = {}
        levels = ["Easy", "Medium", "Hard"]
        for lvl in levels:
            btn = tk.Button(self.level_frame, text=lvl, font=('Arial', 12, 'bold'),
                            bg='darkorange', fg='white',
                            command=lambda l=lvl: self.select_level(l))
            btn.pack(side='left', padx=10)
            self.level_buttons[lvl] = btn

        self.start_button = tk.Button(self.root, text="Start Game", font=('Arial', 14, 'bold'),
                                      bg='green', fg='white', command=self.start_game)
        self.start_button.pack(pady=15)
        self.start_button.config(state='disabled')

    def select_level(self, level):
        self.level = level
        # Highlight selected button
        for lvl, btn in self.level_buttons.items():
            btn.config(bg='darkorange', fg='white')
        self.level_buttons[level].config(bg='forestgreen', fg='white')
        # Enable start button
        self.start_button.config(state='normal')

    def start_game(self):
        if not self.level:
            messagebox.showwarning("Warning", "Please select a difficulty level first!")
            return
        self.level_frame.pack_forget()
        self.start_button.pack_forget()

        # Pick random puzzle
        puzzle = random.choice(PUZZLES[self.level])
        self.solution = puzzle["solution"]
        self.size = len(self.solution)
        self.clue_numbers = puzzle["clue_numbers"]
        self.across_clues = puzzle["across_clues"]
        self.down_clues = puzzle["down_clues"]

        self.entries.clear()
        self.answers.clear()

        self.grid_frame = tk.Frame(self.root, bg='skyblue')
        self.grid_frame.pack(pady=10)
        self.draw_grid()

        self.buttons_frame = tk.Frame(self.root, bg='skyblue')
        self.buttons_frame.pack(pady=10)
        self.draw_buttons()

        self.clues_frame = tk.Frame(self.root, bg='skyblue')
        self.clues_frame.pack(pady=10, fill='x')
        self.show_clues()

    def draw_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        for i in range(self.size):
            for j in range(self.size):
                letter = self.solution[i][j]
                if letter == '_':
                    frame = tk.Frame(self.grid_frame, width=50, height=50, bg='black')
                    frame.grid(row=i, column=j, padx=1, pady=1)
                    continue

                frame = tk.Frame(self.grid_frame, width=50, height=50, bg='white', highlightbackground="black", highlightthickness=1)
                frame.grid_propagate(False)
                frame.grid(row=i, column=j, padx=1, pady=1)

                number = self.clue_numbers.get((i, j))
                if number:
                    number_label = tk.Label(frame, text=str(number), font=("Arial", 7), bg='white')
                    number_label.place(x=2, y=0)

                var = tk.StringVar()
                entry = tk.Entry(frame, textvariable=var, font=('Arial', 18), justify='center', bg='lightyellow')
                entry.place(x=0, y=12, width=50, height=38)
                self.entries[(i, j)] = entry
                self.answers[(i, j)] = letter

    def draw_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        self.check_btn = tk.Button(self.buttons_frame, text="Check Answers", command=self.check_answers,
                                   bg='green', fg='white', font=('Arial', 12, 'bold'))
        self.check_btn.grid(row=0, column=0, padx=10)

        self.show_btn = tk.Button(self.buttons_frame, text="Show Answers", command=self.show_answers,
                                  bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.show_btn.grid(row=0, column=1, padx=10)

        self.reset_btn = tk.Button(self.buttons_frame, text="Reset Puzzle", command=self.reset_puzzle,
                                   bg='red', fg='white', font=('Arial', 12, 'bold'))
        self.reset_btn.grid(row=0, column=2, padx=10)

    def show_clues(self):
        for widget in self.clues_frame.winfo_children():
            widget.destroy()

        lbl_across = tk.Label(self.clues_frame, text="Across Clues:", font=('Arial', 16, 'bold'), bg='skyblue')
        lbl_across.pack(anchor='w', padx=10)
        for num, clue in sorted(self.across_clues.items()):
            lbl = tk.Label(self.clues_frame, text=f"{num}. {clue}", font=('Arial', 15), bg='skyblue', anchor='w')
            lbl.pack(fill='x', padx=20)

        lbl_down = tk.Label(self.clues_frame, text="Down Clues:", font=('Arial', 16, 'bold'), bg='skyblue', pady=10)
        lbl_down.pack(anchor='w', padx=10)
        for num, clue in sorted(self.down_clues.items()):
            lbl = tk.Label(self.clues_frame, text=f"{num}. {clue}", font=('Arial', 15), bg='skyblue', anchor='w')
            lbl.pack(fill='x', padx=20)

    def check_answers(self):
        correct = 0
        total = len(self.answers)
        all_correct = True
        for pos, entry in self.entries.items():
            user_answer = entry.get().strip().upper()
            if user_answer == self.answers[pos]:
                entry.config(bg='lightgreen')
                correct += 1
            else:
                entry.config(bg='salmon')
                all_correct = False

        if all_correct:
            self.show_congratulations_fullpage()
        else:
            messagebox.showinfo("Result", f"You got {correct} out of {total} correct!")

    def show_answers(self):
        for pos, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, self.answers[pos])
            entry.config(bg='lightblue')

    def reset_puzzle(self):
        # Clear full page congrats if any
        if self.congrats_frame:
            self.confetti_running = False
            self.congrats_frame.destroy()
            self.congrats_frame = None

        # Recreate game UI
        self.grid_frame.destroy()
        self.buttons_frame.destroy()
        self.clues_frame.destroy()

        puzzle = random.choice(PUZZLES[self.level])
        self.solution = puzzle["solution"]
        self.size = len(self.solution)
        self.clue_numbers = puzzle["clue_numbers"]
        self.across_clues = puzzle["across_clues"]
        self.down_clues = puzzle["down_clues"]

        self.entries.clear()
        self.answers.clear()

        self.grid_frame = tk.Frame(self.root, bg='skyblue')
        self.grid_frame.pack(pady=10)
        self.draw_grid()

        self.buttons_frame = tk.Frame(self.root, bg='skyblue')
        self.buttons_frame.pack(pady=10)
        self.draw_buttons()

        self.clues_frame = tk.Frame(self.root, bg='skyblue')
        self.clues_frame.pack(pady=10, fill='x')
        self.show_clues()

    def show_congratulations_fullpage(self):
        # Remove old frames (puzzle + clues + buttons)
        if self.grid_frame:
            self.grid_frame.destroy()
            self.grid_frame = None
        if self.buttons_frame:
            self.buttons_frame.destroy()
            self.buttons_frame = None
        if self.clues_frame:
            self.clues_frame.destroy()
            self.clues_frame = None

        # Create congrats full page frame
        self.congrats_frame = tk.Frame(self.root, bg='white')
        self.congrats_frame.pack(fill='both', expand=True)

        label = tk.Label(self.congrats_frame, text="🎉 Congratulations! 🎉",
                         font=("Arial", 28, "bold"), fg='darkgreen', bg='white')
        label.pack(pady=40)

        message = tk.Label(self.congrats_frame, text="You solved the crossword puzzle!",
                           font=("Arial", 18), bg='white')
        message.pack(pady=10)

        canvas = tk.Canvas(self.congrats_frame, bg='white', highlightthickness=0)
        canvas.pack(fill='both', expand=True)

        width = self.root.winfo_width() or 450
        height = self.root.winfo_height() or 750

        canvas.config(width=width, height=height - 200)

        # Confetti setup
        colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange','gold']
        self.confetti_items = []
        for _ in range(100):
            x = random.randint(0, width)
            y = random.randint(-height, 0)
            size = random.randint(5, 10)
            color = random.choice(colors)
            oval = canvas.create_oval(x, y, x + size, y + size, fill=color, outline='')
            speed = random.uniform(2, 5)
            self.confetti_items.append([oval, x, y, size, speed])

        self.confetti_running = True

        def animate_confetti():
            if not self.confetti_running:
                canvas.delete("all")
                return
            for item in self.confetti_items:
                oval, x, y, size, speed = item
                y += speed
                if y > height:
                    y = random.randint(-height, 0)
                    x = random.randint(0, width)
                item[1] = x
                item[2] = y
                canvas.coords(oval, x, y, x + size, y + size)
            self.root.after(30, animate_confetti)

        animate_confetti()

        # Add a button to restart the game
        restart_btn = tk.Button(self.congrats_frame, text="Play Again", font=("Arial", 16, "bold"),
                                bg='green', fg='white', command=self.restart_from_congrats)
        restart_btn.pack(pady=30)

    def restart_from_congrats(self):
        # Stop confetti and remove congrats frame
        self.confetti_running = False
        if self.congrats_frame:
            self.congrats_frame.destroy()
            self.congrats_frame = None

        # Show level select again
        self.level_frame.pack(pady=20)
        self.start_button.pack(pady=15)
        self.start_button.config(state='disabled')
        # Reset buttons highlight
        for lvl, btn in self.level_buttons.items():
            btn.config(bg='darkorange', fg='white')
        self.level = None


if __name__ == "__main__":
    root = tk.Tk()
    game = CrosswordGame(root)
    root.mainloop()
