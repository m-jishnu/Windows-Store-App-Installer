import subprocess
import tkinter as tk
from tkinter import filedialog

try:
    def select_file():
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File")

        subprocess.run(f"powershell -Command Add-AppxPackage {filename}")

    # Create the root window
    window = tk.Tk()

    # Set window title
    window.title('file Installer')

    # icon set
    # window.iconbitmap('C:/Users/Desktop/icon.ico')

    label = tk.Label(window,
                     text="file Installer V1.0",
                     fg="blue")

    label.config(font=("Courier", 12))

    button_explore = tk.Button(window,
                               text="Select File",
                               command=select_file)

    button_exit = tk.Button(window,
                            text="Exit",
                            command=window.destroy)

    label_credits = tk.Label(window,
                             text="By TechoZ",
                             fg="blue")

    label_credits.config(font=("Courier", 12))

    label.grid(column=0, row=0, padx=100, pady=10)

    button_explore.grid(column=0, row=1, padx=10, pady=10)

    button_exit.grid(column=0, row=2, padx=10, pady=2)

    label_credits.grid(column=0, row=3, padx=10,
                       sticky='E', columnspan=True)

    window.mainloop()

except:
    import traceback
    traceback.print_exc()
    input("Press Enter to end...")