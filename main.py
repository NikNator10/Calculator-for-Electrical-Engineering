import math

func = int(
  input(
    "Folgende Möglichkeiten: \n1. Herkömlicher Taschenrechner \n2. HWE-spezifische Rechnungen\n3. Verlauf anzeigen\nWelche Funktion willst du nutzen?\nDeine Eingabe: "
  ))

if func == 1:  #basic-calculator
  funcbc = int(
    input(
      "Wähle deine Funktion aus.\nAus folgenden Funktionen kannst du wählen:\n1. Additionen/Subtraktionen/Multiplikationen/Divisionen\n2. Wurzel berechnen\n3. Winkelfunktionen (nur RADIAN)\n4. Lass dir Pi (π) als Zahl anzeigen\nWähle deine gewünschte Funktion aus: "
    ))
  if funcbc == 1:  # ----> normale Rechenaufgaben
    print("Zahlen eingeben:", end="")
    from calculations import basiccalc

  elif funcbc == 2:  #Wurzel
    sqrt = int(
      input("Gib die Zahl ein, aus der die Wurzel gezogen werden soll:"))
    anssqrt = math.sqrt(sqrt)
    print("Die Wurzel deiner Zahl", sqrt, "ist", anssqrt)

  elif funcbc == 3:  #Winkelfunktionen
    funcbcwink = int(
      input(
        "Welche Winkelfunktion möchtest du ausrechnen?\n1. Sinus\n2. Cosinus\n3. Tangens\n4. Cotangens\nWähle deine gewünschte Funktion aus: "
      ))
    if funcbcwink == 1:
      winkfunc = "Sinus"
      sin = int(input("Gib das Verhältnis deiner Zahlen ein:"))
      anssin = math.sin(sin)
      print("Die Winkelfunktion", winkfunc, "lautet bei deiner Zahl", sin,
            "lautet", anssin)

    elif funcbcwink == 2:
      winkfunc = "Cosinus"
      cos = int(input("Gib das Verhältnis deiner Zahlen ein:"))
      anscos = math.cos(cos)
      print("Die Winkelfunktion", winkfunc, "lautet bei deiner Zahl", cos,
            "lautet", anssin)

    elif funcbcwink == 3:
      winkfunc = "Tangens"
      tan = int(input("Gib das Verhältnis deiner Zahlen ein:"))
      anstan = math.tan(tan)
      print("Die Winkelfunktion", winkfunc, "lautet bei deiner Zahl", sin,
            "lautet", anssin)

    elif funcbcwink == 4:
      winkfunc = "Cotangens"
      cot = int(input("Gib das Verhältnis deiner Zahlen ein:"))
      anscot = math.cot(cot)
      print("Die Winkelfunktion", winkfunc, "lautet bei deiner Zahl", sin,
            "lautet", anssin)

    else:
      print("Ungültige Eingabe")

  elif funcbc == 4:  #Pi als Zahl
    print("Pi (π) als Zahl lautet", math.pi)
  else:
    print("Ungültige Eingabe")

elif func == 2:  #HWE-Rechner
  funchwe = int(
    input(
      "Folgende Möglichkeiten:\n1. Wattsekunden in kWh\n2. kWh in Wattsekunden\nDeine Eingabe: "
    ))
  if funchwe == 1:
    wskwh = float(
      input(
        "Wie viele Wattsekunden möchtest du in kWh umwandeln?\nDeine Eingabe: "
      ))
    wskwhans = wskwh / 3600000
    print("Deine", wskwh, "Wattsekunden sind", wskwhans, "kWh")
  if funchwe == 2:
    kwhws = float(
      input(
        "Wie viele kWh möchtest du in Wattsekunden umwandeln?\nDeine Eingabe: "
      ))
    kwhwsans = kwhws * 3600000
    print("Deine", kwhws, "kWh sind", kwhwsans, "Wattsekunden")

elif func == 3:
  print("Noch in Arbeit")

else:
  print("Ungültige Eingabe")

#-----------------------------------------------------------------#
