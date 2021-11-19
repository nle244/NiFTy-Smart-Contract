import tkinter as tk
from tkinter import filedialog as fd

filetypes = (
    ('image files', '*.jpg *.png'),
    ('All files', '*.*')
)

root = tk.Tk()
root.withdraw()

filename = fd.askopenfilename(
    title='Open a file',
    initialdir='/',
    filetypes=filetypes)
