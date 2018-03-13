# -*- encoding: utf-8 -*-

# Področje, na katerega lahko rišemo lomljeno črto.
# S pritiskom na levi gumb začnemo risati novo lomljeno črto,
# z desnim gumbom nadaljujemo prejšnjo črto.

from tkinter import *


class Risalnik():
    def __init__(self, master):
        # Trenutna točka, od koder bomo nadaljevali lomljeno
        # črto. Na začetku je ni.
        self.tocka = None
        self.debelina = 5
        self.barva = 'black'

        self.kajRisemo = 'PROSTOROCNA_CRTA'  # OVAL
        self.pravokotnikOgrodje = None
        self.pravokotnik = None
        self.vmesniLik = None

        # Naredimo področje za risanje
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

        # Registiramo se za premike miške
        self.canvas.bind("<B1-Motion>", self.nadaljuj_crto)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.tipka_pritisnjena)
        self.canvas.bind("<Button-1>", self.zacni_risanje)
        self.canvas.bind("<ButtonRelease-1>", self.izklopi_risanje)

        menu = Menu(master)
        menuNarisiLik = Menu(menu, tearoff=0)

        root.config(menu=menu)
        menu.add_cascade(label='Nariši lik', menu=menuNarisiLik)
        menuNarisiLik.add_command(label='Lik 1')
        menuNarisiLik.add_command(label='Lik2')
        menuNarisiLik.add_command(label='Lik3')


    def zacni_risanje(self, event):
        if self.kajRisemo== 'PROSTOROCNA_CRTA':
            return

        if self.kajRisemo=='OVAL':
            self.tocka=(event.x,event.y)
            self.pravokotnikOgrodje=self.canvas.create_rectangle(event.x,event.y,event.x,event.y)

        if self.kajRisemo == 'PRAVOKOTNIK':
            self.tocka = (event.x, event.y)
            self.pravokotnik = self.canvas.create_rectangle(event.x, event.y, event.x, event.y)
            return
        if self.kajRisemo == 'OZNACEVANJE':
            najblizjiId = self.canvas.find_closest(event.x, event.y)
            print(event.x, event.y, najblizjiId)
            return
        
    def nadaljuj_crto(self, event):
        '''Nadaljuj lomljeno črto.'''
        if self.kajRisemo == 'PROSTOROCNA_CRTA':
            if self.tocka is not None:
                (x, y) = self.tocka
                self.canvas.create_line(x, y, event.x, event.y,
                                        width=self.debelina, capstyle=ROUND, fill=self.barva)
                self.tocka = (event.x, event.y)
            else:
                self.tocka = (event.x, event.y)
            return
        if self.kajRisemo == 'OVAL':
            if self.tocka is not None:
                (xMin, yMin) = self.tocka
                self.canvas.coords(self.pravokotnikOgrodje, xMin, yMin, event.x, event.y)
                self.canvas.coords(self.vmesniLik, xMin, yMin, event.x, event.y)
        if self.kajRisemo == 'PRAVOKOTNIK':
            if self.tocka is not None:
                (xMin, yMin) = self.tocka
                self.canvas.coords(self.pravokotnik, xMin, yMin, event.x, event.y)
            return 

    def izklopi_risanje(self, event):
        if self.kajRisemo == 'PROSTOROCNA_TOCKA':
            if self.tocka == None:
                return
        if self.kajRisemo =='OVAL':
            (xMin,yMin)=self.tocka
            self.canvas.create_oval(xMin,yMin,event.x,event.y)
            self.tocka=None
            return

        if self.kajRisemo == 'PRAVOKOTNIK':
            (xMin, yMin) = self.tocka 
            self.canvas.coords(self.pravokotnik, xMin, yMin, event.x, event.y)
            self.tocka = None
            self.pravokotnik = None
            return


    def tipka_pritisnjena(self, event):
        if event.char == '+':
            self.debelina += 1
        if event.char == '-' and self.debelina > 1:
            self.debelina -= 1
        if event.char == 'c':
            self.barva = 'black'
        if event.char == 'm':
            self.barva = '#4ba5f4'
        if event.char == 'd':
            self.canvas.delete(ALL)
        if event.char == 'k':
            if self.kajRisemo == 'PROSTOROCNA_CRTA':
                self.kajRisemo = 'OVAL'
            elif self.kajRisemo == 'OVAL':
                self.kajRisemo = 'PROSTOROCNA_CRTA'
            print(self.kajRisemo)

            # Glavnemu oknu rečemo "root" (koren), ker so grafični elementi

        if event.char == 'p':
            self.kajRisemo = 'PROSTOROCNA_CRTA'
        if event.char == 'o':
            self.kajRisemo = 'OVAL'
        if event.char == 'z':
            self.kajRisemo = 'OZNACEVANJE'
        #popravi, kot zgoraj
        #if event.char == 'k':
        #    self.kajRisemo = 'PRAVOKOTNIK'
        print(self.kajRisemo)
                
            
            
# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi

# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Risalnik(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()