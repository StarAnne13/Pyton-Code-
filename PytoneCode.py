import random
Karakterler=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
Uzunluk=int(input("Uzunluğu Giriniz Yeni sifre oluşturmak için"))
sifre=""
for i in range(Uzunluk):
    sifre+=random.choice(Karakterler)
print(sifre)
