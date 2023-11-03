# Import the modules
import tkinter as tk
import pyautogui
import pyperclip
from pynput import mouse

# Create a tkinter window
root = tk.Tk()
root.title("Mouse Position")
# Make the window stay on top
root.wm_attributes("-topmost", 1)

# Create a label to display the mouse position
label = tk.Label(root, font=("Arial", 15))
label.pack()

# Define a function to update the label with the mouse position
def update_label():
    # Get the current mouse coordinates
    x, y = pyautogui.position()
    # Format the position as a string
    pos = f"X: {x}, Y: {y}"
    # Update the label text
    label.config(text=pos)
    # Repeat the function after 50 milliseconds
    root.after(50, update_label)

# Define a function to copy the position to the clipboard when right-clicked
def copy_position(x, y, button, pressed):
    # If the right button is pressed, copy the position to the clipboard
    if button == mouse.Button.right and pressed:
        # Get the current mouse coordinates
        x, y = pyautogui.position()
        # Format the position as a string
        pos = f"X: {x}, Y: {y}"
        # Copy the position to the clipboard
        pyperclip.copy(pos)

# Create a mouse listener to handle mouse events
listener = mouse.Listener(on_click=copy_position)
# Start the listener
listener.start()

# Call the function for the first time
update_label()

# Start the tkinter main loop
root.mainloop()
