#   +5594984088618 

# Importing all Libraries
import os # Manage files
import pyautogui # Control PC
import subprocess # Run File
import pywhatkit as kit # Intergration with WhatsApp
from time import sleep # Pause during the program

# Creation Graphical Interface:
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from threading import Thread
from tkinter import messagebox
from tkinter import filedialog
import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# DEFINE FUNCTIONS:

# Collecting file path
def collect_path():
    file = filedialog.askopenfilename()
    return file

phone_number = ''
def save_number(entry_number):
    global phone_number
    number = entry_number.get()
    if number:
        messagebox.showinfo("PHONE NUMBER", f"PHONE NUMBER ADD: {number}")
        janela.destroy()
    else:
        messagebox.showerror("Erro", "Por favor, insira um número de telefone válido.")
    phone_number = number
    


# Start work automation
def start_job():
    global selected_minutes
    selected_minutes = int(spinbox.get()) # Funciton "spinbox.get" capture the value of spinbox
    # Obtenha o caminho do arquivo após o usuário ter selecionado os minutos
    file_path = collect_path() # Calling the function collect-path()
    
    # Start working after the selected time
    def run_job():
            # Menssage for user
            ttk.Label(frm, text="", font=my_font,  foreground= 'red').grid(column=2, row=6)
            ttk.Label(frm, text="LOADING FILE...", font=my_font,  foreground= 'red').grid(column=2, row=7)
            sleep(2)
            messagebox.showinfo(title='Confirmation',message='Successfully Executed!')

            # Close Graphical Interface
           
            pyautogui.hotkey("alt", "F4")
            pyautogui.hotkey("win", "m")


            while True:
                here = os.getcwd() 
                name_img = 'img.jpg'
                img_path = os.path.join(here, name_img)

                # This little piece of code ensures that a single screenshot exists in the specified directory
                if os.path.exists(img_path):
                   os.remove(img_path)


                # Open File
                subprocess.run(file_path, shell=True)
                sleep(5)
                
                # MAX Window
                #pyautogui.hotkey('win', 'up')
                #sleep(1)
                # Screenshot from the file
                pyautogui.screenshot(img_path)
                sleep(2)
                #Close File
                pyautogui.hotkey("alt", "F4")
                sleep(2)

                # Open Browser / Web Page / WhatsApp Web
                # Phone Number for sent a image (is necessary iclude code from the Country)
                

                # Senting the Image
                kit.sendwhats_image(phone_number, img_path,"Hello! You Received an Image")
                sleep(10)

                # MENSSAGE FOR THE USER:
                #pyautogui.write()
                #sleep(1)
                #pyautogui.press('enter')
                #sleep(1)
                
                # FEEDBAK: FOR READ THIS MENSSAGE, ACESS THE TERMINAL!
                try:
                    subprocess.Popen(['xdg-open', img_path])
                except Exception as e:
                    print(f"Erro ao abrir o arquivo: {e}")
                sleep(5)

                # Close the Browser tab
                pyautogui.hotkey("alt", "f4")

                # Wait the time selected by the user to restart the process
                # -30 Subtract the time necessary for load program
                sleep(selected_minutes*60-35)

    thread = Thread(target=run_job) #Call function run_job()
    thread.start() #Start funcion run_job()


#Creating Graphical Interface:
def add_phone():
    global janela
    janela = tk.Tk()
    janela.geometry('500x300')
    janela.title("CAPTURE NUMBER")
    janela.maxsize(500, 300)

    # Rótulo e entrada para o número de telefone
    label_numero = tk.Label(janela, text="              WRITE YOUR PHONE NUMBER:", font=("Helvetica", 12), foreground='blue')
    label_numero.grid(column=1, row=1)

    tk.Label(janela, text="").grid(column =1, row=2)

    row2 = tk.Label(janela, text="                   Exemple Format Phone Number: +55 94 991234 5432").grid(column =1, row=3)
    tk.Label(janela, text="").grid(column =1, row=4)

   
    entry_numero = tk.Entry(janela, width=25, font=("Helvetica", 12))
    entry_numero.grid(column=1, row=8)
    row4 = tk.Label(janela, text=" ").grid(column =1, row=7)
    row5 = tk.Label(janela, text=" ").grid(column =1, row=9)


    # Botão para salvar o número
    btn_save = tk.Button(janela, text="SAVE NUMBER", command=lambda: save_number(entry_numero))
    btn_save.grid(column=1, row=10)


    # Inicia o loop da interface gráfica
    janela.mainloop()

root = Tk()
root.title('AUTOJO')
frm = ttk.Frame(root, padding=10)
frm.grid()
root.geometry('700x400') # Defining the Dimensions of the window
root.maxsize(700, 400)

my_font = ("Helvetica", 18) # Standardizing Font

# Menssage user reception
ttk.Label(frm, text="WELCOME JOBBOT\n", font=my_font, foreground= 'blue',justify='center',underline=20).grid(column=2, row=2, columnspan=2)

#Spinbox Configuration
ttk.Label(frm, text="          Select Minutes:", font=my_font, justify='right').grid(column=1, row=3)
spinbox = Spinbox(frm, from_=1, to=60, width=5, font=my_font)
spinbox.grid(column=2, row=3)
ttk.Label(frm, text="", font=my_font).grid(column=2, row=4)

#Add phone number
add_phone = ttk.Button(frm, text='ADD NUMBER', command=add_phone, width=25, padding=10)
add_phone.grid(column=2, row = 5)
ttk.Label(frm, text="", font=my_font).grid(column=2, row=6)

# Botão para iniciar o trabalho
start_button = ttk.Button(frm, text="SELECT FILE", command=start_job, width=25, padding=10)
start_button.grid(column=2, row=7)

root.mainloop()
