from random import randint
from secrets import choice
import string
from tkinter import *



number_chars = 2

def generate_password():
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_chars) for x in range(number_chars))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    

backgroud_color = "#83a2ad"

# Création de la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background=backgroud_color)

# Création de la frame principale
frame = Frame(window, bg=backgroud_color)

#creation d'une image
width = 300
height = 300
image = PhotoImage(file="password-image.png")
canvas = Canvas(frame, width=width, height=height, bg=backgroud_color, bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# Création d'une sous frame
right_frame = Frame(frame, bg=backgroud_color)

# Créer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg=backgroud_color, fg="white")
label_title.pack()

# Créer un input
password_entry = Entry(right_frame, font=("Helvetica", 15), bg=backgroud_color, fg="white", bd=1, highlightthickness=0)
password_entry.pack(pady=10)

# Créer le bouton de génération de mot de passe
generate_button = Button(right_frame,  text="Générer", font=("Helvetica", 15), bg="white", fg=backgroud_color, bd=1, highlightthickness=0, command=generate_password)

generate_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

# Création d'une barre de menu
menu_bar = Menu(window)

# Création d'un premier menu
file_menu  = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Ajouter le menu a la fenetre
window.config(menu=menu_bar)


window.mainloop()
