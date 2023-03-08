
berechnung = int(input("Folgende Möglichkeiten: \n1. Normale Rechnungen \n2. HWE-spezifische Rechnungen \nWas wollen Sie berechen?\nIhre Eingabe: "))


if 1 < berechnung > 2:
  print("Ungültige Eingabe")
  

elif berechnung == 1: #basic-calculator
  from calculations import addieren
  from calculations import subtrahieren
  from calculations import multiplizieren
  from calculations import dividieren

elif berechnung == 2:
  print("Noch in Arbeit")






#-----------------------------------------------------------------#