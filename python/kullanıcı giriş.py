Kullanıcı ="ender"
Parola = 1234
Kullanıcı_adı = input("Kullanıcı giriniz " )
Parola_giriş= int(input("parola giriniz " ))
if (Kullanıcı !=Kullanıcı_adı and Parola == Parola_giriş) :
	print("kullanıcı adı hatalı " )

elif (Kullanıcı==Kullanıcı_adı and Parola != Parola_giriş) :
	print("Parola yanlış " )

elif (Kullanıcı !=Kullanıcı_adı and Parola != Parola_giriş) :
	print("Hatalı giriş " )
else:
	print("Giriş başarılı" )



