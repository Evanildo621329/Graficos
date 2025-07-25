from tkinter import *
from tkinter import ttk

def cadastrar_aluno():
    tv.insert('', 'end', values=(Vnome.get(), Vemail.get(), Vcurso.get()))
    
    Vnome.delete(0, 'end')
    Vcurso.delete(0, 'end')
    Vemail.delete(0, 'end')
    
               
app = Tk()
app.title("ADS - Fecaf")
app.geometry("600x450")

lbnome = Label(app, text="Nome")
Vnome = Entry(app)

lbemail = Label(app, text="E-mail")
Vemail = Entry(app)

lbcursos = Label(app, text="Curso")
Vcurso = Entry(app)


tv = ttk.Treeview(app, columns=("nome", "email", "curso"), show='headings')

tv.column('nome', minwidth=0, width=250)
tv.column('email', minwidth=0, width=210)
tv.column('curso', minwidth=0, width=100)

tv.heading('nome', text='Nome')
tv.heading('email', text='E-mail')
tv.heading('curso', text='Curso')

btncadastrar = Button(app, text="Cadastrar", command=cadastrar_aluno)

lbnome.grid(column=0, row=0, sticky='w')
Vnome.grid(column=0, row=1,)

lbemail.grid(column=1, row=0, sticky='w')
Vemail.grid(column=1, row=1)

lbcursos.grid(column=2, row=0, sticky='w')
Vcurso.grid(column=2, row=1)    

btncadastrar.grid(column=3, row=1)

tv.grid(column=0, row=2, columnspan=8,)

app.mainloop() 