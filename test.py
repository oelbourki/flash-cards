import asyncio
import tkinter as tk

async def async_function():
    # Do some async task here
    await asyncio.sleep(1)
    # Update GUI elements here
    label.config(text="Async function finished")

async def on_button_click():
    # Start async function
    await asyncio.create_task(async_function())

# Create tkinter window
root = tk.Tk()
root.geometry("200x100")

# Create label and button
label = tk.Label(root, text="Click the button to start async function")
label.pack()
button = tk.Button(root, text="Start async function", command=lambda: asyncio.create_task(on_button_click()))
button.pack()

# Start asyncio event loop in tkinter main loop
asyncio.ensure_future(asyncio.gather(asyncio.sleep(0))) # Ensure the loop is running
root.mainloop()
