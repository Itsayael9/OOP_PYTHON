import tkinter as tk 
app = tk.Tk()
label = tk.Label(app,text="here is a label : ",font=("Arial",16))
label.config(state=tk.NORMAL)
label.pack(pady=20)

entry = tk.Entry(app)
entry.pack(pady=20)

check1= tk.Checkbutton(app,text="python")
check2 = tk.Checkbutton(app,text="js")
check1.pack()
check2.pack()

liste= tk.Listbox(app)
liste.pack()

liste.insert(0," 1st element")
liste.insert(1," 2nd element")
liste.insert(2," 3rd element")

liste.select_set(2)
label = tk.Label(app,text="selectioner un element dans la liste")
label.pack()

radio1 = tk.Radiobutton(app,text="html ").pack()
radio2 = tk.Radiobutton(app,text="css ").pack()




app.mainloop()






