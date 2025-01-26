import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import os
import tempfile
import ollama

def capture_screenshot():
    try:
        # Create a temporary directory
        temp_dir = tempfile.gettempdir()
        screenshot_path = os.path.join(temp_dir, "screenshot.jpg")
        
        # Capture the primary monitor's screenshot
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path, "JPEG")
        
        # Display success message
        messagebox.showinfo("Success", f"Screenshot saved at: {screenshot_path}")
        
        # Call ollama to analyze the image
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': 'Whats up? Like the image?',
                'images': [screenshot_path]
            }]
        )
        
        # Show response in a messagebox
        messagebox.showinfo("Ollama Response", response)
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the tkinter UI
root = tk.Tk()
root.title("Screenshot and Analyze")

# Add a button to capture a screenshot
capture_button = tk.Button(root, text="Capture Screenshot", command=capture_screenshot)
capture_button.pack(pady=20)

# Run the tkinter main loop
root.mainloop()
