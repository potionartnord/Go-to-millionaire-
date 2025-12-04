from tkinter import *
from timer import *
from threading import Timer
from math import *


argent = 0
revenu = 0
clicks = 1

def atrv(price, value , id, id2, px, py) :
    global argent
    global clicks
    if id2 == id:
        id.place_forget()
    if argent >= price :
        argent -= price
        clicks = value
        click(clicks)
        id2.place(x=px, y=py)
        id.place_forget()

 
def click(value):
    global argent 
    argent += value
    bu1.config(text="+" + str(value)+ "$")
    li1.config(text=str(argent) + " $")

    if argent >= 1000000:
        show_frame(page_de_fin)

def passif(eta, value, price, id, id2, px, py):
    global argent
    global revenu

    if id2 == id:
        id.place_forget()

    if not eta and argent >= price: 
        argent -= price
        revenu += value
        li2.config(text=str(revenu) + "$/sec")
        auto_click(value)  
        id.place_forget() 
        id2.place(x=px, y=py) 

def auto_click(value):
    global argent
    argent += value
    li1.config(text=str(argent) + "$")

    if argent >= 1000000:
        show_frame(page_de_fin)
        return
    
    Timer(1.0, lambda: auto_click(value)).start()


def show_frame(frame):
    frame.tkraise()
    
# fermeture de la fenêtre  
def quitter():
    global root
    root.destroy()

# configuration de la fenetre 
root = Tk()
root.geometry("400x500")
root.title("Go to the million $")
root.config(background="#121414")
root.resizable(height=False,width=False)

page_accueil = Frame(root, bg="#121414")
page_jeu = Frame(root, bg="#121414")
page_de_fin = Frame(root, bg="#121414")
page_concepte = Frame(root, bg="#121414")

for frame in (page_accueil, page_jeu, page_de_fin, page_concepte):
    frame.place(relwidth=1, relheight=1)

Label(page_accueil, text="Go to the million $", font=("Arial", 25, "bold"), bg="#121414", fg="white").pack(pady=50)

Button(page_accueil, text="Start", font=("Arial", 20),
       bg="white", fg="#121414",command=lambda: show_frame(page_jeu),width=15).place(x=85 ,y=200)

Button(page_accueil, text="Concept", font=("Arial", 20),
       bg="white", fg="#121414",command=lambda: show_frame(page_concepte),width=10).place(x=120 ,y=400)

Label(page_concepte, text="The goal is to generate one million dollars through various improvements.", font=("Arial", 15),
       fg="white", bg="#121414",wraplength=350,
    justify="center").pack(pady=50)

Button(page_concepte, text="Start", font=("Arial", 20),
       bg="white", fg="#121414",command=lambda: show_frame(page_jeu),width=15).place(x=85 ,y=200)

Label(page_de_fin, text="WIN", font=("Arial", 25,"bold"),
       fg="white", bg="#121414", width=15).pack(pady=50)

Label(page_de_fin, text="You are millionaire", font=("Arial", 20),
       fg="white", bg="#121414", width=15).place(x=85 ,y=200)

Button(page_de_fin, text="Leave", font=("Arial", 20),
       bg="white", fg="#121414",command= quitter,width=15).place(x=85 ,y=300)

# bouton 1 (click de cookie à la main)
bu1 = Button(page_jeu, command=lambda: click(clicks), text="+ 1$ ",  font=('arial', 20),bg='white', fg="#121414", bd=False, height=1, width=7)
bu1.place(x=200,y=200, anchor="center")

# bouton 2 (auto click 1/sec)
bu2 = Button(page_jeu, command=lambda: passif(False, 1,15.0, bu2, bu4, 60, 400), text=" +1$/sec (15$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)
bu2.place(x=60, y=400)

# bouton 3 (+2 au click à la main)
bu3 = Button(page_jeu, command=lambda: atrv(30.0, 2, bu3, bu6, 60, 300), text=" +2/click (30$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)
bu3.place(x=60,y=300)

# bouton 6 (+5 au click à la main)
bu6 = Button(page_jeu, command=lambda: atrv(50.0, 5, bu6, bu7, 60, 300), text=" +5/click (50$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 7 (+8 au click à la main)
bu7 = Button(page_jeu, command=lambda: atrv(75.0, 8, bu7, bu8, 60, 300), text=" +8/click (75$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 8 (+10 au click à la main)
bu8 = Button(page_jeu, command=lambda: atrv(100.0, 10, bu8, bu9, 60, 300), text=" +10/click (100$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 9 (+15 au click à la main)
bu9 = Button(page_jeu, command=lambda: atrv(200.0, 15, bu9, bu14, 60, 300), text=" +15/click (200$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 14 (+20 au click à la main)
bu14 = Button(page_jeu, command=lambda: atrv(500.0, 20, bu14, bu15, 60, 300), text=" +20/click (500$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 15 (+25 au click à la main)
bu15 = Button(page_jeu, command=lambda: atrv(700.0, 25, bu15, bu26, 60, 300), text=" +25/click (700$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 26 (+50 au click à la main)
bu26 = Button(page_jeu, command=lambda: atrv(1000.0, 50, bu26, bu27, 60, 300), text=" +50/click (1,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 27 (+100 au click à la main)
bu27 = Button(page_jeu, command=lambda: atrv(1800.0, 100, bu27, bu28, 60, 300), text=" +100/click (1,800$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 28 (+200 au click à la main)
bu28 = Button(page_jeu, command=lambda: atrv(3000.0, 200, bu28, bu29, 60, 300), text=" +200/click (3,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 29 (+400 au click à la main)
bu29 = Button(page_jeu, command=lambda: atrv(3500.0, 400, bu29, bu30, 60, 300), text=" +400/click (3,500$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 30 (+800 au click à la main)
bu30 = Button(page_jeu, command=lambda: atrv(4000.0, 800, bu30, bu33, 60, 300), text=" +800/click (4,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 33 (+100 au click à la main)
bu33 = Button(page_jeu, command=lambda: atrv(50000.0, 1000, bu33, bu34, 60, 300), text=" +1,000/click (50,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 34 (+100 au click à la main)
bu34 = Button(page_jeu, command=lambda: atrv(100000.0, 5000, bu34, bu35, 60, 300), text=" +5,000/click (100,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 35 (+100 au click à la main)
bu35 = Button(page_jeu, command=lambda: atrv(150000.0, 10000, bu35, bu36, 60, 300), text=" +10,000/click (150,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)

# bouton 36 (+100 au click à la main)
bu36 = Button(page_jeu, command=lambda: atrv(200000.0, 15000, bu36, bu36, 60, 300), text=" +15,000/click (200,000$)",  font=('arial', 20),bg='white', fg='#121414', border=False, height=1, width=19)




# button 4 (passif +2/sec)
bu4 = Button(page_jeu, command=lambda: passif(False, 2,100.0, bu4, bu5, 60, 400), text=" +2$/sec (100$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 5 (passif +10/sec)
bu5 = Button(page_jeu, command=lambda: passif(False, 10,500.0, bu5, bu10, 60, 400), text=" +10$/sec (500$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 10 (passif +12/sec)
bu10 = Button(page_jeu, command=lambda: passif(False, 12,520.0, bu10, bu11, 60, 400), text=" +12$/sec (520$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 11 (passif +14/sec)
bu11 = Button(page_jeu, command=lambda: passif(False, 14,560.0, bu11, bu12, 60, 400), text=" +14$/sec (560$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 12 (passif +16/sec)
bu12 = Button(page_jeu, command=lambda: passif(False, 16,580.0, bu12, bu13, 60, 400), text=" +16$/sec (580$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 13 (passif +18/sec)
bu13 = Button(page_jeu, command=lambda: passif(False, 18,600.0, bu13, bu16, 60, 400), text=" +18$/sec (600$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 16 (passif +27/sec)
bu16 = Button(page_jeu, command=lambda: passif(False, 27,1000.0, bu16, bu17, 60, 400), text=" +27$/sec (1,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 17 (passif +20/sec)
bu17 = Button(page_jeu, command=lambda: passif(False, 20,1200.0, bu17, bu18, 60, 400), text=" +20$/sec (1,200$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 18 (passif +20/sec)
bu18 = Button(page_jeu, command=lambda: passif(False, 20,1400.0, bu18, bu19, 60, 400), text=" +20$/sec (1,400$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 19 (passif +20/sec)
bu19 = Button(page_jeu, command=lambda: passif(False, 20,1600.0, bu19, bu20, 60, 400), text=" +20$/sec (1,600$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 20 (passif +20/sec)
bu20 = Button(page_jeu, command=lambda: passif(False, 20,1800.0, bu20, bu21, 60, 400), text=" +20$/sec (1,800$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 21 (passif +20/sec)
bu21 = Button(page_jeu, command=lambda: passif(False, 20,2000.0, bu21, bu22, 60, 400), text=" +20$/sec (2,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 22 (passif +100/sec)
bu22 = Button(page_jeu, command=lambda: passif(False, 100,3500.0, bu22, bu23, 60, 400), text=" +100$/sec (3,500$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 23 (passif +200/sec)
bu23 = Button(page_jeu, command=lambda: passif(False, 200,6000.0, bu23, bu24, 60, 400), text=" +200$/sec (6,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 24 (passif +500/sec)
bu24 = Button(page_jeu, command=lambda: passif(False, 500,10000.0, bu24, bu25, 60, 400), text=" +500$/sec (10,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 25 (passif +1,000/sec)
bu25 = Button(page_jeu, command=lambda: passif(False, 1000,15000.0, bu25, bu31, 60, 400), text=" +1,000$/sec (15,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 31 (passif +5,000/sec)
bu31 = Button(page_jeu, command=lambda: passif(False, 1000,100000.0, bu31, bu32, 60, 400), text=" +5,000$/sec (100,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# button 32 (passif +5,000/sec)
bu32 = Button(page_jeu, command=lambda: passif(False, 1000,175000.0, bu32, bu32, 60, 400), text=" +10,000$/sec (175,000$)",  font=('arial', 20),bg='white', fg='#121414', border='1px',borderwidth='1px', height=1, width=19)

# label 1(nombre de cookie total)
li1 = Label(page_jeu, text=str(argent) + "$", font=('arial', 20),fg='white', bg='#121414') 
li1.place(x=200, y=250, anchor="center")

# label 2 (revenu passif)
li2 = Label(page_jeu, text=str(revenu) + "$/sec", font=('arial', 20),fg='white', bg='#121414')
li2.place(x=163 , y=120)

# initialisation de la fenetre 
show_frame(page_accueil)

root.mainloop()