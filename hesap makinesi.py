print("Hesap Makinesi")

sayi1 = float(input("Birinci Sayiyi Girin."))
islem = input("islem sec(+, -, *, /)")
sayi2 = float(input("İkinci Sayiyi Girin"))

if islem == "+":
    sonuc = sayi1+sayi2

elif islem == "-":
    sonuc = sayi1-sayi2

elif islem == "*":
    sonuc = sayi1*sayi2

elif islem == "/":
    if sayi2 == 0:
        print("Bir Sayiyi Sifira Bolemezsin")

    else:
        print(sayi1/sayi2)

else:
    print("Gecersiz Islem")

if islem in ("+", "-", "*", "/") or (islem == "/" and sayi2 != 0):
    print("sonuc:", sonuc)