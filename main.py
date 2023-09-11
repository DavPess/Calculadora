import tkinter as tk
from tkinter import *



root = Tk()
root.title('Calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

numero1 = ''
numero2 = ''
divisao = FALSE
multiplica = FALSE
soma = FALSE
subtracao = FALSE

root.configure(background='#282828')
#Input de entrada (Entry são widgets que permitem que o usuário insira texto)
e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER) #FLAT = relevo // bold = negrito
#Como o nome sugere, ele vai dividir o container em uma grade (grid em inglês), 
# assim podemos posicionar os elementos dividino o Frame, por exemplo, em x linhas e y linhas.
e.grid(
    row= 0, #linha
    column= 0, #coluna
    columnspan= 4, 
    pady= 2
)
#Funções operadores
def botao_click(num):
    e.insert(END, num)

def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)
    
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_soma():
    global numero1
    global soma
    soma = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_limpa(limpa):
    e.delete(0, END)
    
#responsável por fazer todas as operações.
def botao_igual(resultado):
    global soma
    global multiplica
    global divisao
    global subtracao
    numero2 = e.get()
    e.delete(0, END)
    if soma == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        soma = FALSE
    if multiplica == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisao = FALSE
    
divide = Button(root, 
                text = '÷',
                padx= '40',
                pady= '20',
                command= botao_divisao, #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
divide.grid(row=0, column=4)
#primeira fileira
um = Button(root, 
                text = '1',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(1), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
um.grid(row=1, column=1)
dois = Button(root, 
                text = '2',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(2), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )

dois.grid(row=1, column=2)
tres = Button(root, 
                text = '3',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(3), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
tres.grid(row=1, column=3)
multiplicacao = Button(root, 
                text = 'x',
                padx= '41',
                pady= '20',
                command= botao_multiplica, #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
multiplicacao.grid(row=1, column=4)
#segunda fileira
quatro = Button(root, 
                text = '4',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(4), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
quatro.grid(row=2, column=1)
cinco = Button(root, 
                text = '5',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(5), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
cinco.grid(row=2, column=2)
seis = Button(root, 
                text = '6',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(6), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
seis.grid(row=2, column=3)
menos = Button(root, 
                text = '-',
                padx= '43',
                pady= '20',
                command= botao_subtracao, #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
menos.grid(row=2, column=4)
#terceira fileira
sete = Button(root, 
                text = '7',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(7), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
sete.grid(row=3, column=1)
oito = Button(root, 
                text = '8',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(8), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
oito.grid(row=3, column=2)
nove = Button(root, 
                text = '9',
                padx= '40',
                pady= '20',
                command= lambda: botao_click(9), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
nove.grid(row=3, column=3)
mais = Button(root, 
                text = '+',
                padx= '41',
                pady= '20',
                command= botao_soma, #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
mais.grid(row=3, column=4)
#quarta fileira
zero = Button(root, 
                text = '0',
                padx= '91',
                pady= '20',
                command= lambda: botao_click(0), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
zero.grid(row=4, column=1, columnspan=2)
resultado = Button(root, 
                text = '=',
                padx= '40',
                pady= '20',
                command= lambda: botao_igual('='), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
resultado.grid(row=4, column=3)

limpa = Button(root, 
                text = 'C',
                padx= '40',
                pady= '20',
                command= lambda: botao_limpa('C'), #função, ao ser cliclado, gera uma ação para retornar algo
                fg= '#FFFFFF',
                activeforeground= '#FFFFFF', #Quando clicar no botão, a cor será alterada.
                bg= '#320064',
                activebackground= '#240046', 
                relief=FLAT,
                font= ('futura', 12, 'bold')
                )
limpa.grid(row=4, column=4)


#enquanto a janela estiver aberta, espera algum tipo de açõa.
root.mainloop()