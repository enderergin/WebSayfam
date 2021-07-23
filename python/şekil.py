sekil = input("hangi şekli öğrenmeliyim ")

if (sekil == "dortgen"):
    print("kenarları sırayla giriniz")
    a = int (input("kenar-1:"))
    b = int (input("kenar-2:"))
    c = int (input("kenar-3:"))
    d = int (input("kenar-4:"))
    if (a == b and a == c and a == d):
        print("kare")
    elif ( a == c and d == b):

        print("dikdörtgen")
    else:
        print("dörtgen")

elif ( sekil == "üçgen"):
    a = int(input("kenar-1:"))
    b = int(input("kenar-2:"))
    c = int(input("kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(c+b) > a ):
        if (a == b and a == c and c == b ):
            print("eş kenar")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("ikiz kenar ")
        else:
            print("çeşitkenar")

    else:
        print("üçgen belirtmiyor")

else:
            print("geçersiz şekil")
