import tkinter as tk
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, tk.END)
    e1.insert(tk.END, selected_tuple[1])
    e2.delete(0, tk.END)
    e2.insert(tk.END, selected_tuple[2])
    e3.delete(0, tk.END)
    e3.insert(tk.END, selected_tuple[3])
    e4.delete(0, tk.END)
    e4.insert(tk.END, selected_tuple[4])


def view_command():
    list1.delete(0, tk.END)
    for item in backend.view():
        list1.insert(tk.END, item)


def search_command():
    for item in backend.search(nazev_text.get(), autor_text.get(), rok_text.get(), ISBN_text.get()):
        list1.insert(tk.END, item)


def insert_command():
    backend.insert(nazev_text.get(), autor_text.get(), rok_text.get(), ISBN_text.get())
    list1.delete(0, tk.END)
    list1.insert(0, (nazev_text.get(), autor_text.get(), rok_text.get(), ISBN_text.get()))


def update_command():
    backend.update(selected_tuple[0], nazev_text.get(), autor_text.get(), rok_text.get(), ISBN_text.get())


def delete_command():
    backend.delete(selected_tuple[0])


window = tk.Tk()

window.wm_title("Knihovna")

l1 = tk.Label(window, text="Název")
l1.grid(row=0, column=0)

l2 = tk.Label(window, text="Autor")
l2.grid(row=0, column=2)

l3 = tk.Label(window, text="Rok")
l3.grid(row=1, column=0)

l4 = tk.Label(window, text="ISBN")
l4.grid(row=1, column=2)

nazev_text = tk.StringVar()
e1 = tk.Entry(window, textvariable=nazev_text)
e1.grid(row=0, column=1)

autor_text = tk.StringVar()
e2 = tk.Entry(window, textvariable=autor_text)
e2.grid(row=0, column=3)

rok_text = tk.StringVar()
e3 = tk.Entry(window, textvariable=rok_text)
e3.grid(row=1, column=1)

ISBN_text = tk.StringVar()
e4 = tk.Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

list1 = tk.Listbox(window)
list1.grid(row=3, column=0, rowspan=5, columnspan=2)

sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = tk.Button(window, text="Zobrazit vše", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = tk.Button(window, text="Hledat", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = tk.Button(window, text="Přidat", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = tk.Button(window, text="Aktualizovat", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = tk.Button(window, text="Smazat", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = tk.Button(window, text="Zavřít", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
