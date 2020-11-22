#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

import os

"""
## insert
lb.insert(0, "First item")
lb.insert(0, "Second item")
lb.insert(tk.END, content.get())

## delete
lb.delete(tk.ACTIVE)  # delete the on on top
lb.delete(0)  # delete the one on top

listbox.delete(0, tk.END) # delete all items
listbox.delete(tk.ANCHOR) # delete selected items

## select multiple items
lb = tk.Listbox(win, selectmode=tk.EXTENDED)

## get the selected item
cs = lb.curselection()[0]

## binding
lb.bind("<<ListboxSelect>>", lambda x: my_func())

## loop
items = ["first", "second", "third"]
for item in items:
    lb.insert(tk.END, item)
"""

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self, title, icon, theme):
        super().__init__()
        self.style = ttk.Style(self)
        self.resizable(False, False)
        self.title(title)
        self.iconbitmap(icon)
        self.style.theme_use(theme)

        self.init_UI()
        self.retrieve_data()

    # INITIALIZER ==============================
    @classmethod
    def create_app(cls, app):
        return cls(app['title'], app['icon'], app['theme'])

    #===========================================
    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.fieldset = ttk.LabelFrame(self.main_frame, text='Add List Item:')
        self.fieldset.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.entry_text = tk.StringVar()
        self.entry = ttk.Entry(self.fieldset, textvariable=self.entry_text)
        self.entry.focus()
        self.entry.pack(side=tk.LEFT, anchor=tk.W, fill=tk.X, expand=True, ipady=5)

        button_add_item = ttk.Button(self.fieldset,text='Add', command=self.meth_add_item)
        button_add_item.pack(side=tk.LEFT, anchor=tk.W)

        self.listbox = tk.Listbox(self.main_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button_delete = ttk.Button(self.main_frame,text='Delete All', command=self.meth_delete_all_item)
        button_delete.pack(side=tk.LEFT, anchor=tk.W)

        button_delete_selected = ttk.Button(self.main_frame,text='Delete Selected', command=self.meth_delete_selected_item)
        button_delete_selected.pack(side=tk.LEFT, anchor=tk.W)

        button_quit_save = ttk.Button(self.main_frame,text='Quit & Save', command=self.meth_quit_save)
        button_quit_save.pack(side=tk.LEFT, anchor=tk.W)

    # METHODS -----------------------------------
    def meth_add_item(self):
        self.listbox.insert(tk.END, self.entry_text.get())
        self.stored_data.append(self.entry_text.get())
        self.entry_text.set('')
        self.entry.focus_set()

    def meth_delete_all_item(self):
        self.listbox.delete(0, tk.END)
        self.stored_data = []

    def meth_delete_selected_item(self):
        selected = self.listbox.get(self.listbox.curselection())
        self.listbox.delete(tk.ANCHOR)
        self.stored_data.pop(self.stored_data.index(selected))

    def meth_quit_save(self):
        with open('save.txt', 'w', encoding='utf-8') as file:
            for data in self.stored_data:
	            file.write(f'{data}\n')
        self.destroy()

    def retrieve_data(self):
        self.stored_data = []
        try:
            if 'save.txt' in os.listdir():
                with open('save.txt', 'r', encoding='utf-8') as file:
                    for data in file:
                        self.listbox.insert(tk.END, data.strip())
                        self.stored_data.append(data.strip())
                print(self.stored_data)
        except:
            pass


#===========================
# Start GUI
#===========================

def main(config):
    app = App.create_app(config)
    app.mainloop()

if __name__ == '__main__':
    main({
        'title' : 'Todo List Version 1.0',
        'icon' : 'python.ico',
        'theme' : 'clam'
        })