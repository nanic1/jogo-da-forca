import tkinter as tk
from tkinter import messagebox
import random
import customtkinter as ctk

#========== VARIAVEIS E LISTAS ==========
palavras = ['goiaba', 'banana', 'guarana', 'uva', 'maca', 'limao', 'laranja', 'melancia', 'pera', 'morango', 'abacaxi', 'melao']
palavra = random.choice(palavras).upper()
letraUsuario = set()
chances = 7

#========== FUNÇÕES ==========
def atualizar_palavra_oculta():
    resultado = ''
    for letra in palavra:
        if letra in letraUsuario:
            resultado += letra + ' '
        else:
            resultado += '_ '
    palavra_label.config(text=resultado)

def verificar_vitoria():
    if all(letra in letraUsuario for letra in palavra):
        messagebox.showinfo("Parabéns!", "Você ganhou!")
        tela.quit()

def processar_letra():
    global chances
    letra = letra_entry.get().upper()
    letra_entry.delete(0, 'end')
    
    if letra in letraUsuario:
        messagebox.showwarning("Atenção", "Você já tentou essa letra.")
    else:
        letraUsuario.add(letra)
        if letra not in palavra:
            chances -= 1
            desenhar_forca()
            if chances == 0:
                messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era '{palavra}'.")
                tela.quit()
        else:
            atualizar_palavra_oculta()
            verificar_vitoria()

def desenhar_forca():
    partes_forca[chances].config(fg='red')

#========== TELA ==========
tela = tk.Tk()
tela.title("Jogo da Forca")
tela.geometry("800x600")

#========== WIDGETS ==========
palavra_label = tk.Label(tela, text='', font=('Arial', 24))
palavra_label.pack(pady=20)

letra_entry = ctk.CTkEntry(tela, font=('Arial', 18))
letra_entry.pack(pady=20)

botao_letra = ctk.CTkButton(tela, text="Tentar Letra", command=processar_letra, font=('Arial', 20))
botao_letra.pack(pady=20)

#========== DESENHO FORCA ==========
partes_forca = [
    tk.Label(tela, text='  |  ', font=('Arial', 18)),
    tk.Label(tela, text='  O  ', font=('Arial', 18)),
    tk.Label(tela, text=' /|\\ ', font=('Arial', 18)),
    tk.Label(tela, text=' / \\ ', font=('Arial', 18)),
    tk.Label(tela, text='  |  ', font=('Arial', 18)),
    tk.Label(tela, text=' / \ ', font=('Arial', 18)),
    tk.Label(tela, text='|    |', font=('Arial', 18)),
]

for parte in partes_forca:
    parte.pack()

atualizar_palavra_oculta()
tela.mainloop()
