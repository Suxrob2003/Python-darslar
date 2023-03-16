


# # Moslashuvchan funksiyalar - yaratilgan funksiya uchun moslashuvchan argument berish orqali, istalgancha obyektlar va qiymatlar berish uchun islatiladi.

# # def city(*args):
# #     return args
# # a = city("Shahar1", "SHahar2","Shahar3",122312,123232)
# # print(a)
# # def shaxar(**kwars):
# #     return kwars
# # a= shaxar("qarshi ", "toshkent", "guliston")
# # print(a)
# ################################################################################################################




# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(1,2,4,5))


# def summa(*sonlar):
#     yigindi = 1
#     for son in sonlar:
#         yigindi*=son
#     return yigindi

# print(summa(1,5,5,2))

####################################################


# 1) summa deb nomlangan funksiya yaratiladi
# 2) *sonlar deb nomlangan argument yaratiladi
# 3) yigindi = 1 bu sonni 1 dan boshlab sanash uchun ishlatiladi
# 4) for operatori orqali son degan for o'zgaruvchi olinib, sonlar argumentidan oladi
# 5) yigindi*=son - bu yuqoridagi 1 dan boshlab, son deb olingan o'zgaruvchi ko'paytirib ketaveradi
# 6)return yigindi - bu yigindi deb nomlangan sonlarni qaytarish uchun ishlatiladi




#################



# def summa(*pullar):
#     ayirma= 1
#     for i in pullar:
#         ayirma*=i
#     return ayirma
# print(summa(11,2,3,4,5,5,6,6,7,5,3,3,5,56,433,5,))



############



def qarzlar(*berdim):
    berganlarim= 1000
    for i in berdim:
        berganlarim +=16000
    return berganlarim
print(qarzlar(120000,120000,532000,323000,122000))



###################




# # Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa, va bunday parametrlar 
# # soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs)./
# # **kwargs — keyword arguments (kalit so'zli argumentlar)
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
# print(avto2)
