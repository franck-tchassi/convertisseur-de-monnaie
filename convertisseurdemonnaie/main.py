from tkinter import*
from forex_python.converter import CurrencyRates
from tkinter import ttk
from tkinter import messagebox


currency = ['CAD','USD','EUR', "CNY", "DKK", "FCFA"]
def converts():
    currency_1 = e2.get()
    currency_2 = e3.get()
    c = CurrencyRates()
    somme_argent = float(e1.get())
    e4 = c.convert(currency_1, currency_2, somme_argent)
    label4.config(text=e4)

    with open("save_data.txt", "w") as f:
        f.write(f"Enter amount: {somme_argent}\nconvert from: {currency_1}\nconvert to: {currency_2}\nrésultat: {e4}")

    
    



def clear_all(): 
    e2.delete(0, END) 
    e3.delete(0, END)
    e1.delete(0, END)
    
     
    


 



root = Tk()
root.title("Currency Converter")
root.geometry("370x400")
root.config(background="green")
devise_name = StringVar(root)
combo_1 = StringVar(root)
combo_2 =  StringVar(root)



label1 = Label(root, text="Enter amount:", bg="green")
label1.grid(row=0, column=0)

e1 = Entry(root, textvariable=devise_name)
e1.grid(row=0, column=1)


label2 = Label(root, text="convert from:",bg="green")
label2.grid(row=1, column=0)

e2 = ttk.Combobox(root, textvariable=combo_1)
e2['value'] = (currency)
e2.grid(row=1, column=1)



label3 = Label(root, text="convert to:",bg="green")
label3.grid(row=2, column=0)

e3 = ttk.Combobox(root, textvariable=combo_2)
e3['value'] = (currency)
e3.grid(row=2, column=1)


label4 = Label(root, text="resul-convertion",bg="green")
label4.grid(row=3, column=1)



convert_button = Button(root, text="convert", command=converts,bg="red" )
convert_button.grid(row=4, column=1)


btn_effacer = Button(root, text="clear_all", command=clear_all,bg="red").grid(row=5, column=1)








root.mainloop()


