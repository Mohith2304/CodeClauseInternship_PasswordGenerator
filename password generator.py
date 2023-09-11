import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and configure widgets
length_label = tk.Label(app, text="Password Length:")
length_entry = tk.Entry(app)
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
result_label = tk.Label(app, text="Generated Password: ")

# Place widgets in the window
length_label.pack()
length_entry.pack()
generate_button.pack()
result_label.pack()

# Start the Tkinter event loop
app.mainloop()
