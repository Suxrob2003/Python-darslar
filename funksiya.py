# funksiya bu = malum bir vazifani bajaradigan , shartlar o'zgaruvchilar va obyektlar bilan ishlaydigan ko'rinishdir 


# funksiyaning kalit so'zi - def

# def - bu funksiyaning belgisi
# salom - bu funksiyaning o'zgaruvchisi
# def salom():
#     # salom() - qavs bu funksiyaning argumenti
#     print("Assalomu alaykum")
# salom()


######################################################


# def raqamlarni_kiriting() :
#     print("1","2","3","4","5","6","7","8","9","0")
# raqamlarni_kiriting()
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('suxrob')


######################################################


# hisoblash - bu funksiyaning  nomi. uning ichidagi son1, son2 esa- uning agrumentlari deyiladi. Ya'ni vazifasi - huddi o'zgaruvchi yaratgandek, yaratiladi

# def hisoblash(son1, son2, son3):
#     print(son1,son2, son3)
# hisoblash(1,23,10)



####################################################


# def ism_sharif(ism, familiya):
#     print(f'Foydalanuvchining ismi = {ism.title()}, {familiya.title()}')
# ism_sharif("Azizbek","G'ulomov")




# Vazifa - ism, sharif, yosh, manzil, universiter ma'lumotlarini talaba degan funksiya orqali to'ldiring
def talaba(ism , sharif ,yosh ,manzil ,universitet malumotlari):
    print(f'{ism} , {sharif}, yosh , manzil , universitet malumotlari !, {ism.title()} , {sharif.title()}')
talaba("suxrob", "otabek o'g'li","21","qarshi shaxar", "neft va gaz fakulteti 3-kurs ")

