ad_soyad = input("Ad ve soyad giriniz: ")
vize = float(input("Vize notunuzu giriniz: "))
while vize < 0 or vize > 100:
    vize = float(input("Lütfen geçerli bir not değeri giriniz : "))
final = float(input("Final notunuzu giriniz: "))
while final < 0 or final > 100:
    final = float(input("Lütfen geçerli bir not değeri giriniz : "))
devam = input("Devamsızlık durmunuzu girniz(evet/hayır) :")

while devam != "evet" and devam != "hayır":
    devam = input("Devam cevabınız hatalı, lütfen tekrar giriniz: ")

ort = vize*0.4 + final*0.6

if (ort>=50) and (devam == 'hayır') :
    durum = 'Gecti'
elif (devam == 'evet'):
    durum = 'Devamsızlıktan kaldı'
else :
    
    durum = 'Kaldı'

if devam == 'hayır' :
    if ort >= 90:
        harf_notu = "AA"
    elif ort >= 80:
        harf_notu = "BA"
    elif ort >= 70:
        harf_notu = "BB"
    elif ort >= 60:
        harf_notu = "CB"
    elif ort >= 50:
        harf_notu = "CC"
    else:
        harf_notu = "FF"


print("Öğrenci adı : ",ad_soyad)
print("Vize notu : ",vize)
print("Final notu : ",final)
print("Devmsızlık durumu : ",devam)

print("----SONUC----")

print("Ortalama : ",ort)
print("Durum : ",durum)
if durum == 'Devamsızlıktan kaldı':
    print("Harf notu hesaplanamaz")
else :    
    print("Harf notu :",harf_notu)

if (ort>=90) or (final>=95):
    print("Çok başarılı")
