 
from tkinter import *

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def toggle_theme():
    is_dark = window.cget("bg") == "#2A2E32"
    theme_bg = "#2A2E32" if not is_dark else "#F5F5F5"
    theme_fg = "white" if not is_dark else "black"
    button_bg = "#3E4347" if not is_dark else "#F0F0F0"
    button_fg = "white" if not is_dark else "black"
    listbox_tasks.config(bg=theme_bg, fg=theme_fg)
    entry_task.config(bg=button_bg, fg=theme_fg)
    button_add_task.config(bg=button_bg, fg=button_fg)
    button_delete_task.config(bg=button_bg, fg=button_fg)
    button_toggle_theme.config(bg=button_bg, fg=button_fg)
    window.config(bg=theme_bg)

# Create main window
window = Tk()
window.title("To-Do List App")
window.geometry("600x600")
window.resizable(True, True)

# Create GUI elements
frame_tasks = Frame(window)
frame_tasks.pack(fill=BOTH, expand=True)

listbox_tasks = Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(window, width=50)
entry_task.pack(pady=10)

button_add_task = Button(window, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = Button(window, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_toggle_theme = Button(window, text="Toggle theme", width=48, command=toggle_theme)
button_toggle_theme.pack(pady=10)

# Increase font size to 14
font_style = ("TkDefaultFont", 14)
listbox_tasks.config(font=font_style)
entry_task.config(font=font_style)
button_add_task.config(font=font_style)
button_delete_task.config(font=font_style)
button_toggle_theme.config(font=font_style)

# Set dark mode to dark grey
listbox_tasks.config(bg="#2A2E32", fg="white")
entry_task.config(bg="#3E4347", fg="white")
button_add_task.config(bg="#3E4347", fg="white")
button_delete_task.config(bg="#3E4347", fg="white")
button_toggle_theme.config(bg="#3E4347", fg="white")
window.config(bg="#2A2E32")

# Run the main event loop
window.mainloop()
