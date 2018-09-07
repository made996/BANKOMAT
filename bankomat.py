import tkinter as tk
from tkinter import *
import os
standardni_limit = 150
    

class okno:
    

    def __init__(self, master):
        self.zgodovina = []
        self.vec_dvigov = []
        self.vec_pologov = []
        self.pretvorbe = []
        self.limit = standardni_limit
        kuna=''
        dolar =''
        funt = ''
        cny = ''
        self.stanje = DoubleVar(master, value=0)
        self.vnos = DoubleVar(master, value=0)

        self.master = master
        self.frame = tk.Frame(self.master)
    
#PODMENU -shrani, odpri, osveži
        menu = Menu(master)
        master.config(menu = menu)
        pod_menu = Menu(menu)
        menu.add_cascade(label = 'DATOTEKA', menu = pod_menu)
        pod_menu.add_command(label = 'ODPRI ', command =self.odpri_sledenje )
        pod_menu.add_command(label = 'OSVEŽI', command =self.osvezi )
        pod_menu.add_command(label = 'SHRANI DATOTEKO', command = self.shrani_stanje)


        
        
#prvo tekstovno okno - oblike Label
        self.text1 = tk.Label(self.frame, text = "VPIŠITE ZNESEK: ")
        self.text1.grid(row = 2, column = 0 )
        Label(master,text='Vaše Stanje:').grid(row=4,column=0)
        label_stanje=Label(master, textvariable=self.stanje)
        label_stanje.grid(row=4,column=1)
        
        
        



        

#prvo vnosno okno - Entry
        self.vnos = tk.Entry(self.frame)
        self.vnos.grid(row = 2, column = 2)
        self.gumb_polog = tk.Button(self.frame, text = "POLOG", command = self.polozi)
        self.gumb_polog.grid(row = 4, column = 0)
        self.gumb_dvig = tk.Button(self.frame, text = "DVIG", command = self.dvigni)
        self.gumb_dvig.grid(row = 4, column = 1)
        self.gumb_pretvori_HRK = tk.Button(self.frame, text = 'PRETVORI v HRK', command = self.pretvori_HRK)
        self.gumb_pretvori_HRK.grid(row = 5, column = 0)
        self.gumb_pretvori_USD = tk.Button(self.frame, text = 'PRETVORI v USD', command = self.pretvori_USD)
        self.gumb_pretvori_USD.grid(row = 5, column = 1)
        self.gumb_pretvori_GBP = tk.Button(self.frame, text = 'PRETVORI v GBP', command = self.pretvori_GBP)
        self.gumb_pretvori_GBP.grid(row = 5, column = 2)
        self.gumb_pretvori_CNY = tk.Button(self.frame, text = 'PRETVORI v CNY', command = self.pretvori_CNY)
        self.gumb_pretvori_CNY.grid(row = 5, column = 3)
        self.podokno1 = tk.Button(self.frame, text = "Vsi pologi", command = self.odpri_vse_pologe)
        self.podokno1.grid(row = 6, column = 0)
        self.podokno2 = tk.Button(self.frame, text = "Vsi dvigi", command = self.odpri_vse_dvige)
        self.podokno2.grid(row = 6, column = 1)
        self.podokno3 = tk.Button(self.frame, text = "Vse transakcije", command = self.odpri_vse_transakcije)
        self.podokno3.grid(row = 6, column = 2)
        self.frame.grid()

    def dvigni(self) :
        vrednost = float(self.vnos.get()) #vzame vpisan znesek iz polja
        if self.stanje.get() + self.limit - vrednost >= 0 : 
            self.stanje.set(self.stanje.get()-vrednost) #shrani novo stanje neodvisno od limita v množico 
            self.vec_dvigov.append(vrednost*(-1)) # doda v seznam vseh dvigov koliko smo dvignili 
            self.zgodovina.append(vrednost*(-1)) # doda vrednost dviga v seznam zgodovina, kjer se beležijo vsi dvigi in vsi pologi, ločimo jih po prredzanku
            return self.stanje.get()
        return False

    def polozi(self):
       vrednost = float(self.vnos.get())
       self.stanje.set(self.stanje.get()+vrednost)
       if True :
           self.vec_pologov.append(vrednost)
           self.zgodovina.append(vrednost)
       return self.stanje.get()
    
    def pretvori_HRK(self):
        kuna = ''
        znesek = float(self.vnos.get())
        kuna = kuna + str(round(znesek * 7.44, 2))
        self.HRK = tk.Label(self.frame, text = 'HRK : ' +'     ' +    kuna)
        self.HRK.grid(row = 7, column =0)

    
        
        

    def pretvori_USD(self):
        dolar = ''
        znesek = float(self.vnos.get())
        dolar = dolar + str( round(znesek * 1.17, 2))
        self.USD = tk.Label(self.frame, text = 'USD : ' +'     ' +    dolar)
        self.USD.grid(row = 8, column =0)
        
    def pretvori_GBP(self):
        funt=''
        znesek = float(self.vnos.get())
        funt = funt + str(round(znesek * 0.91, 2))
        self.GBP = tk.Label(self.frame, text = 'GBP : ' +'     ' +    funt)
        self.GBP.grid(row = 9, column =0)
        
    def pretvori_CNY(self):
        cny=''
        znesek = float(self.vnos.get())
        cny = cny + str(round(znesek * 7.69, 2))
        self.CNY = tk.Label(self.frame, text = 'CNY : ' +'     ' +    cny)
        self.CNY.grid(row =10, column =0)


    def osvezi(self):
        self.stanje.set(0) 
        self.vnos.delete(0,END)
        self.vnos.insert(0,0)
        self.zgodovina.clear()
        self.vec_dvigov.clear()
        self.vec_pologov.clear()


    def odpri_sledenje(self):
       with open ('sledenje_stanja.txt','r', encoding='utf8') as dat2:
           self.zgodovina.clear()
           self.vec_dvigov.clear()
           self.vec_pologov.clear()
           self.stanje.set(0)
           
           podatki = dat2.read().strip()
           podatki = podatki.split('\n')## --> seznam nizov, hočemo seznam intov
           sez_podatki = []

           for x in podatki :
               sez_podatki.append(int(float(x))) ##--> zdaj imamo seznam intov

           for element in sez_podatki :
               self.zgodovina.append(element)#podatke iz shranjene datoteke shrani kot zgodoovino

           for element in sez_podatki : # podatke nam še shhrani ločeno na dvige in pologe 
               if element < 0 :
                   self.vec_dvigov.append(element)
               else :
                   self.vec_pologov.append(element)

           for element in sez_podatki : #self.stanje nastavi na tistoo iz sledenja
               self.stanje.set(sum(self.zgodovina))
            
               
        
#shranila bo vse transakcije
    def shrani_stanje (self):
        with open ('sledenje_stanja.txt','w', encoding='utf8') as dat :
           for znesek in self.zgodovina :
               print(znesek,file = dat)
        dat.close()


        

    
#tle unesš svojo funkcijo polog in jo prirediš tku da bo pač brala un entry
#in z njim nardila nevemkaj
#
#s tm poberš input
        


    def odpri_vse_pologe(self):
        self.odpri_vse_pologe = tk.Toplevel(self.master)
        self.app = podokno1(self.odpri_vse_pologe)
        self.odpri_vse_pologe.title("Vsi pologi")
        pologi = ''
        for znesek in self.zgodovina :
            if znesek > 0 :
                polog = str(znesek)
                pologi = pologi + polog + '\n'
        Message(self.odpri_vse_pologe, text=pologi).pack()
      
    def odpri_vse_dvige(self):
        self.odpri_vse_dvige = tk.Toplevel(self.master)
        self.app = podokno2(self.odpri_vse_dvige)
        self.odpri_vse_dvige.title("Vsi dvigi")
        dvigi = ''
        for znesek in self.zgodovina :
            if znesek < 0 :
                dvig = str(znesek) + '\n'
                dvigi = dvigi + dvig
        Message(self.odpri_vse_dvige , text=dvigi).pack()


    def odpri_vse_transakcije(self):
        self.odpri_vse_transakcije = tk.Toplevel(self.master)
        self.app = podokno3(self.odpri_vse_transakcije)
        self.odpri_vse_transakcije.title("Vse transakcije")
        zgodovina = ''
        for znesek in self.zgodovina :
            vse = str(znesek)
            zgodovina = zgodovina + vse +  '\n'
        Message(self.odpri_vse_transakcije, text=zgodovina).pack()

    

class podokno1:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

class podokno2:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

class podokno3:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
def main(): 
    root = tk.Tk()
    app = okno(root)
    root.mainloop()

if __name__ == '__main__':
    main()
