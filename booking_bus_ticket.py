# parent class
class Yolculuk():
    def __init__(self, sefer_bilgisi): 
        self.sefer_bilgisi = sefer_bilgisi
        
# child class        
class Yolcu(Yolculuk):
    # yolcu bilgilerini alır tutar
    def __init__(self, sefer_bilgisi, ad, soyad, numara):
        super().__init__(sefer_bilgisi)
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

# child class        
class Bilet(Yolcu):
    # yolcu bilgilerini alır tutar
    def __init__(self, sefer_bilgisi, ad, soyad, numara):
        super().__init__(sefer_bilgisi, ad, soyad, numara)
    
    # yolcu bilgilerini gösterir       
    def bilgiler(self):
        print("""
        Sefer Bilgisi: {}      
        Ad: {}
        Soyad: {}
        T.C. Kimlik Numarası: {}  
        """.format(self.sefer_bilgisi, self.ad, self.soyad, self.numara))

# Bilet class ın dan obje olusturduk bilet1 adında bilgileri verik 
bilet1 = Bilet("Seydişehir-Konya","Nilay","Soytop",12345678910)
# bilet1 in icerisindeki bilgileri gostermesini istedik ve bilgileri cagirdik
bilet1.bilgiler()