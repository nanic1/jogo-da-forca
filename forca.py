import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from random import choice

#========== VARIAVEIS ==========
palavras = ['goiaba', 'banana', 'guarana', 'uva', 'maca', 'limao', 'laranja', 'melancia', 'pera', 'morango', 'abacaxi', 'melao']
palavra = choice(palavras)
letraUsuario = []
chances = 7
ganhou = False

tela = ctk.CTk()
tela.geometry("800x600")
tela.resizable(width=False, height=False)

vitoria_derrota_Label = Label(tela, text="", anchor=CENTER, font=("Arial 30 bold"))
vitoria_derrota_Label.pack(padx=10, pady=0)

instrucoesLabel = Label(tela, text="Jogo da forca", font=("Verdana 40 bold"), anchor=CENTER)
instrucoesLabel.place(x=200, y=55)

letraEntrada = ctk.CTkEntry(tela, placeholder_text="Digite uma letra", font=("Verdana", 30), height=40,width=260)
letraEntrada.place(x=275, y=150)

letras = Label(tela, text="aaa", font=("Verdana 25"), anchor=CENTER)
letras.pack(padx=10, pady=260)

buscarButao = ctk.CTkButton(tela, text="Enter", font=("Verdana", 30))
buscarButao.place(x=330, y=220)

def buscar():
    while True:
        for letra in palavra:
            if letra in letraUsuario:
                letraEntrada



        if ganhou:
            vitoria_derrota_Label.configure(text="Voce venceu!")
        else:
            vitoria_derrota_Label.configure(text="Você perdeu. >:")



tela.mainloop()