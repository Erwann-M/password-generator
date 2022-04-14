from functools import partial
from secrets import choice
import pyperclip
import string
from tkinter import *

class GeneratorSystem:
    
    def __init__(self):
        self.number_chars = 2

    def generate_password(self):
        all_chars = string.ascii_letters + string.punctuation + string.digits
        
        self.password = "".join(choice(all_chars) for x in range(int(self.number_chars)))
        password_entry.delete(0, END)
        password_entry.insert(0, self.password)
        
    def change_number_chars(self, number):
        self.number_chars = number
        label_number_chars.config(text="de: " + str(self.number_chars) + " caractères")
        
    def copy_password(self):
        pyperclip.copy(self.password)
        
    def get_number_chars(self):
        return self.number_chars
    

backgroud_color = "#83a2ad"
newPassword = GeneratorSystem()


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
image = PhotoImage(file="assets/password-image.png")
canvas = Canvas(frame, width=width, height=height, bg=backgroud_color, bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)


# Création d'une sous frame
right_frame = Frame(frame, bg=backgroud_color)


# Créer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg=backgroud_color, fg="white")
label_title.pack()


# Information du nombre de caractère
label_number_chars = Label(right_frame, text="de: " + str(newPassword.get_number_chars()) + " caractères", font=("Helvetica", 20), bg=backgroud_color, fg="white")
label_number_chars.pack()


# Créer un input
password_entry = Entry(right_frame, font=("Helvetica", 15), bg=backgroud_color, fg="white", bd=1, highlightthickness=0)
password_entry.pack(pady=10)


# Créer le bouton de génération de mot de passe
generate_button = Button(right_frame,  text="Générer", font=("Helvetica", 15), bg="white", fg=backgroud_color, bd=1, highlightthickness=0, command=newPassword.generate_password)
generate_button.pack(fill=X, pady=10)

# Bouton pour copier le mot de passe
copy_button = Button(right_frame,  text="Copier le MDP", font=("Helvetica", 15), bg="white", fg=backgroud_color, bd=1, highlightthickness=0, command=newPassword.copy_password)
copy_button.pack(fill=X)


right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

# Création d'une barre de menu
menu_bar = Menu(window)

# Création d'un premier menu
file_menu  = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=newPassword.generate_password)
file_menu.add_command(label="Quitter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Création du menu de choix du nombre de caractere
select_number_menu = Menu(menu_bar, tearoff=0)
for x in range(6, 21):
    
    select_number_menu.add_command(label=x, command=partial(newPassword.change_number_chars, x))

menu_bar.add_cascade(label="Nombre de caractère", menu=select_number_menu)

# Ajouter le menu a la fenetre
window.config(menu=menu_bar)


window.mainloop()
