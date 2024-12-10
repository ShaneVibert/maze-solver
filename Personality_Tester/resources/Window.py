import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")

root.title("Personality Tester")

label = tk.Label(root, text="Welcome to the Personality Test!")
label.pack(pady = 20)

root.mainloop()