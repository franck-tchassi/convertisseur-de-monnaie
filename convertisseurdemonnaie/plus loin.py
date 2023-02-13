# Importation de librairies
from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates
from tkinter import messagebox




def Converts():
    currency_1 = initial_devise.get()
    currency_2 = final_devise.get()
    c = CurrencyRates()
    somme_argent = float(amount.get())
    e4 = c.convert(currency_1, currency_2, somme_argent)
    value_conv.config(text=e4)

def clear_all():
    e1.delete(0, END)
    e2.delete( END)
    e3.delete(0, END)
    


    
# Début de l'affichage
main = Tk()
currency = ['EUR', 'USD', 'CAD', 'CNY', 'DKK','FCFA']
main.title("Convertisseur de devises")
main.resizable(False, False)
conv = ttk.Frame(main, borderwidth=2, relief="ridge", padding="10 10 5 5")
conv.grid(column=0, row=0)
conv.columnconfigure(0, weight=1)
conv.rowconfigure(0, weight=1)

initial_devise = StringVar()
e2 = ttk.Combobox(conv, textvariable=initial_devise, width=17)
e2.state(["readonly"])
e2['values'] = currency 
e2.grid(column=1, row=1)
e2.set([0])

final_devise = StringVar()
e3 = ttk.Combobox(conv,textvariable=final_devise, width=17)
e3.state(["readonly"])
e3['values'] = currency
e3.grid(column=1, row=2)
e3.set([1])

print_result = StringVar()
amount_enter = StringVar()
amount = StringVar()

label = ttk.Label(conv, text="Quantité:", padding="10")
label.grid(column=0, row=0)

label = ttk.Label(conv, text="De:", padding="10")
label.grid(column=0, row=1)

label = ttk.Label(conv, text="à:", padding="10")
label.grid(column=0, row=2)

label = ttk.Label(conv, text="value_conv:", padding="10")
label.grid(column=1, row=4)

e1 = ttk.Entry(conv,textvariable=amount, width=20)
e1.grid(column=1, row=0)

convertir = ttk.Button(conv, text='Convertir', command=Converts)
convertir.grid(column=1, row=3)

value_conv = ttk.Label(conv)
value_conv.grid(column=1, row=4)

clear = ttk.Button(conv, text='clear_all', command=clear_all)
clear.grid(column=2, row=5)

label = ttk.Label(conv, textvariable=print_result, padding="10")
label.grid(column=1, row=6)
main.mainloop()