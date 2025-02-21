import customtkinter as tk

main_window = tk.CTk(fg_color="#808080")
main_window.resizable(False, False)
WIDTH = 454
HEIGHT = 469

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

x = screen_width / 2 - WIDTH / 2
y = screen_height / 2 - HEIGHT / 2

main_window.title("Музыкальный плеер")
main_window.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")