#Aufgabe_3_1 Zinsen Arithmetische Operatoren I
K1=float(input("Geben Sie Ihr Kapital ein: "))
Zinssatz=float(input("Geben Sie Ihr Zinssatz in Prozentzahl ein: "))
K_in_1Jahr=K1*Zinssatz/100
print("Zinsen für ein Jahr ",round(K_in_1Jahr,2))

#Aufgabe_3_2  Energieverbrauch
Fernseher=3*1*3 #Jeden Tag
Herd=2*2 #4 Mal pro Woche
Tel_Router=4*2 #Jeden Tag
Heizung=20*8 #170 Tage im Jahr
energie_jahr=(Fernseher*365+Herd*52*4+Tel_Router*365+Heizung*170)*0.3
print("Energieverbrauch im Jahr ist: ", energie_jahr," Euro")

#Aufgabe_3_2  Aufgabe
TG=30 #pro Monat
Wartesteuer=0.07
Summe_1=170+170*0.07
Monate=Summe_1//30+1
print("Gesamtwert ist ",Summe_1," Euro und zahlen wir ",int(Monate),"_Monate")
