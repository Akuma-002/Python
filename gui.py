from tkinter import *
from tkintertable import TableCanvas, TableModel, Button

root = Tk()
root.title("Tkinter Table Example")
root.geometry("500x300")

# Create a frame for the table
frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

# Sample data
data = {
    'row1': {'Name': 'Alice', 'Age': 25, 'Country': 'USA'},
    'row2': {'Name': 'Bob', 'Age': 30, 'Country': 'UK'},
    'row3': {'Name': 'Charlie', 'Age': 22, 'Country': 'Canada'}
}

# Create the table model
model = TableModel()
model.importDict(data)

# Create TableCanvas inside the frame
table = TableCanvas(frame, model=model, editable=True)
bu = Button()
bu.show()

root.mainloop()
