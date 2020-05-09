# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:29:03 2020

@author: User
"""

from abc import ABC, abstractmethod #abstract metod

class Virus(ABC): #abstract class
    @abstractmethod
    def belirtileri(self): #abstract metod
        pass
    
    @abstractmethod
    def bulası_olum(self): #abstract metod
        pass
    
    def bilgiler(self,olum_oranı): #metod
        pass
        
class Sars(Virus): #subclass

    def __init__(self):
        print("Virüsün türü: Sars")
        
    def belirtileri(self): #abstract metod
        pass
        
    def bulası_olum(self): #abstract metod
        pass    
    
    def bilgiler(self): #metod
        print("Ölüm Oranı: ", self.__olum_oranı)
        print("Bulaşan kişi: Ali")
        
    def getOlum_oranı(self): #olum_oranı nı donduruyoruz
        return self.__olum_oranı
    
    def setOlum_oranı(self, oran): #olum_oranı nı giriyoruz
        self.__olum_oranı = oran

class Mers(Virus): #subclass
     
    def __init__(self):
        print("Virüsün türü: Mers")
        
    def belirtileri(self): #abstract metod
        pass
        
    def bulası_olum(self): #abstract metod
        pass    
    
    def bilgiler(self): #metod
        print("Ölüm Oranı: ", self.__olum_oranı)
        print("Bulaşan kişi: Cenk")
        
    def getOlum_oranı(self): #olum_oranı nı donduruyoruz
        return self.__olum_oranı
    
    def setOlum_oranı(self, oran): #olum_oranı nı giriyoruz
        self.__olum_oranı = oran
 
class Korona(Virus): #subclass
     
     def __init__(self):
        print("Virüsün türü: Korona")
        
     def belirtileri(self): #abstract metod
        pass
        
     def bulası_olum(self): #abstract metod
        pass    
    
     def bilgiler(self): #metod
        print("Ölüm Oranı: ", self.__olum_oranı)
        print("Bulaşan kişi: Ahmet")
        
     def getOlum_oranı(self): #olum_oranı nı donduruyoruz 
        return self.__olum_oranı
    
     def setOlum_oranı(self, oran): #olum_oranı nı giriyoruz
        self.__olum_oranı = oran

        
sars = Sars() #nesneyi tanımlıyoruz
sars.setOlum_oranı(10) #olum_oranı nı veriyoruz
sars.bilgiler() #bilgileri çağırıyoruz ve yazdırıyoruz

print("***************************") #çıktı görüntüsü için

korona = Korona() #nesneyi tanımlıyoruz
korona.setOlum_oranı(20) #olum_oranı nı veriyoruz
korona.bilgiler() #bilgileri çağırıyoruz ve yazdırıyoruz   

print("***************************") #çıktı görüntüsü için
   
mers = Mers() #nesneyi tanımlıyoruz
mers.setOlum_oranı(30) #olum_oranı nı veriyoruz
mers.bilgiler() #bilgileri çağırıyoruz ve yazdırıyoruz    
        