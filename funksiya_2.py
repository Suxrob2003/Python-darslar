
# Pythonda Funksiyalar

# Funksiya bu - bir nechta Python buyruqlarini ma'lum bir vazifa ostida ishlatadigan obyektlar va argumentlar jamlanmasi

# Funksiyaning kalit so'zi def deb nomlanadi    

# salomlash - funksiyaninig nomi


# def salomlash():
#     print("Salom")
#     print("drger")
#     print("erge")
#     print("erger")
#     print("erg")
# salomlash()

# talaba funksiyasi orqali ism, familiya, yosh, manzil, guruh
# def talaba(ism , familiya, yosh ,manzil,guruh):
#     print(familiya.title(),ism.title(), yosh ,manzil.title(),guruh.title())
# talaba("suxrob" , "shoimov" ,"21 yoshda"," qarshi shaxrida yashaydi!"," guruhi :python dasturlash" )
# def talaba(ism, familiya):
#     print(familiya, ism)

# talaba("G'ulomov" ,"Aziz")


#####################################################



# Avtomobillar jadvalini shakllantirish. Bunda avtomobil modeli, nomi, rangi, narxi, yili

# def avtomobillar(model, nom, narx):
#     avto = {
#         'model':model,
#         'nom':nom,
#         'narx':narx
#     }
#     return avto
# # return funksiyasi berilgan argument o'zgaruvchilarini obyektning o'ziga qaytaradi(printning konsolga yozmaydigan varianti)

# a = avtomobillar('GM','Gentra',15000000)
# b = avtomobillar('USA','Tesla',7500052165)
# print(a,b)












# def kitob_dokoni(kitob_nomi , aftir , chiqgan_yili , narxi ):
#     kitob={ 'Kitob nomi':kitob_nomi,
#            'Yozuvchi': aftir,
#            "Chiqgan yili": chiqgan_yili ,
#            'Sotuvdagi narxi': narxi ,
#     }
#     return kitob
# a = kitob_dokoni('alkimyogar'.title(),'deo pavlo'.title(),2019 ,150000)
# b = kitob_dokoni('al jabr val-muqobala'.title() , 'al=xorazmiy'.title() ,1500, "sotuvda yo'q!".title())
# print(a)
# print(b)



######################################################



print("Avtoomobillar")
def avtomobillar(model, nom, narx):
    avto = {
        'model':model,
        'nom':nom,
        'narx':narx
    }
    return avto


# a = avtomobillar('GM','Gentra',15000000)
# b = avtomobillar('USA','Tesla',7500052165)
# print(a,b)

avtolar = []
while True:
    model = input("Modelini kiiting = ")
    nom = input("Nominin kiriting = ")
    narx = input("Narx kiriting = ")
    avtolar.append(avtomobillar(model,nom, narx))
    javob = input("Yana qo'shmoqchimisiz H/Y")
    if javob == 'y' or 'Y':
        break
    else:
        print(avtolar)
