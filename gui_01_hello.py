import tkinter as tk
# Commit Test
# calendar green test

count = 0

def increment():
    global count
    count += 2
    label.config(text=f"Count: {count}")

def reset():
    global count
    count = 100
    label.config(text=f"Count: {count}")

root = tk.Tk()
root.title("Counter App")

label = tk.Label(root, text="Count: 0", font=("Arial", 26))
label.pack(padx=100, pady=50)

inc_button = tk.Button(root, text="Increment", command=increment)
inc_button.pack(padx=10, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(padx=10, pady=(0, 10))

root.mainloop()
