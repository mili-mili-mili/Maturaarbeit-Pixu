import socket
import math
import csv
import tkinter as tk
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

port = 8180
Rad_Umfang = 20.2
vorzeichen_rechts = -1


def position_berechnen(x, y, richtung, alt, neu):
    links = (neu[0] - alt[0]) / 360 * Rad_Umfang
    rechts = vorzeichen_rechts * (neu[1] - alt[1]) / 360 * Rad_Umfang
    weg = (links + rechts) / 2

    drehung = neu[2] - alt[2]
    if drehung > 180:
        drehung = drehung - 360
    elif drehung < -180:
        drehung = drehung + 360

    mitte = math.radians(richtung + drehung / 2)

    x = x + weg * math.cos(mitte)
    y = y + weg * math.sin(mitte)

    return x, y, richtung + drehung


def shoelace_formel(punkte):
    geschlossen = punkte + [punkte[0]]
    summe = 0
    for i in range(len(punkte)):
        summe = summe + geschlossen[i][0] * geschlossen[i + 1][1]
        summe = summe - geschlossen[i + 1][0] * geschlossen[i][1]
    return abs(summe) / 2


def starten():
    global befehl
    befehl = "S"
    startknopf.config(state="disabled")


def beenden():
    global befehl
    befehl = "E"


def taste_druecken(ereignis):
    global taste
    if ereignis.keysym == "Escape":
        beenden()
    elif ereignis.keysym in ("Up", "Down", "Left", "Right"):
        taste = ereignis.keysym


def taste_loslassen(ereignis):
    global taste
    if ereignis.keysym == taste:
        taste = ""


def anhalten(ereignis):
    global taste
    taste = ""


def empfangen():
    global puffer
    while b"\n" not in puffer:
        daten = verbindung.recv(1024)
        if not daten:
            raise OSError("Verbindung unterbrochen")
        puffer = puffer + daten
    zeile, puffer = puffer.split(b"\n", 1)
    return zeile.decode().strip()


def aktualisieren():
    global verbindung, befehl, messen, abgeschlossen, alt, x, y, richtung
    try:
        if verbindung is None:
            if befehl == "E":
                fenster.destroy()
                return
            try:
                verbindung, adresse = server.accept()
            except BlockingIOError:
                fenster.after(100, aktualisieren)
                return
            verbindung.settimeout(0.8)
            status.config(text="Pixu verbunden. Auf Start klicken.")
            startknopf.config(state="normal")

        if messen and befehl != "E":
            befehl = "X"
            if taste == "Up":
                befehl = "F"
            elif taste == "Down":
                befehl = "B"
            elif taste == "Left":
                befehl = "L"
            elif taste == "Right":
                befehl = "R"

        verbindung.sendall(befehl.encode())
        antwort = empfangen()
        if befehl == "S":
            messen = True

        teile = antwort.split(";")
        if teile[0] in ("D", "E"):
            if len(teile) != 4:
                raise ValueError("Falsches Datenformat")
            neu = []
            for wert in teile[1:]:
                zahl = float(wert)
                neu.append(zahl)
            if alt is not None:
                x, y, richtung = position_berechnen(x, y, richtung, alt, neu)
            alt = neu
            punkte.append((x, y))
            tabelle.writerow(neu + [x, y, richtung])
            datei.flush()
            status.config(text="x: " + str(round(x, 2)) + " cm   y: " + str(round(y, 1)) + " cm   Winkel: " + str(
                round(richtung, 1)))

        if teile[0] == "E" or antwort == "ENDE":
            abgeschlossen = True
            fenster.destroy()
            return
    except (OSError, ValueError) as fehler:
        print("Messung abgebrochen:", fehler)
        fenster.destroy()
        return

    fenster.after(50, aktualisieren)


ordner = Path(__file__).resolve().parent / "Messungen"
ordner = ordner / datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
ordner.mkdir(parents=True)
datei = open(ordner / "messdaten.csv", "w", newline="", encoding="utf-8")
tabelle = csv.writer(datei, delimiter=";")
tabelle.writerow(["encoder_links_grad", "encoder_rechts_grad", "yaw_grad", "x_cm", "y_cm", "richtung_grad"])

server = socket.socket()
verbindung = None
puffer = b""
befehl = "W"
taste = ""
messen = False
abgeschlossen = False
punkte = []
alt = None
x = 0
y = 0
richtung = 0

fenster = tk.Tk()
fenster.title("Pixu – Flächenmessung")
status = tk.Label(fenster, text="Warte auf Pixu...", width=65)
status.pack(pady=15)
startknopf = tk.Button(fenster, text="Start", command=starten, state="disabled")
startknopf.pack()
tk.Button(fenster, text="Ende und Auswertung", command=beenden).pack(pady=10)
tk.Label(fenster, text="Pfeiltasten: fahren   Escape: beenden").pack()
fenster.bind("<KeyPress>", taste_druecken)
fenster.bind("<KeyRelease>", taste_loslassen)
fenster.bind("<FocusOut>", anhalten)
fenster.protocol("WM_DELETE_WINDOW", beenden)

try:
    server.bind(("0.0.0.0", port))
    server.listen(1)
    server.setblocking(False)
    fenster.after(100, aktualisieren)
    fenster.mainloop()

finally:
    if verbindung is not None:
        verbindung.close()
    server.close()
    datei.close()

print("Messdaten:", ordner)

if abgeschlossen and len(punkte) >= 3:
    flaeche = shoelace_formel(punkte)
    schliessfehler = math.sqrt(x ** 2 + y ** 2)
    with open(ordner / "ergebnis.txt", "w", encoding="utf-8") as ergebnis:
        text = "Fläche: " + str(round(flaeche, 2)) + " cm²\n"
        text = text + "Abstand zum Start: " + str(round(schliessfehler, 2)) + " cm\n"
        text = text + "Messpunkte: " + str(len(punkte))
        ergebnis.write(text)
    print(text)

    xs = []
    ys = []
    for punkt in punkte:
        xs.append(punkt[0])
        ys.append(punkt[1])

    plt.plot(xs, ys, color="#C40062", label="Pixus Trajektorie")
    plt.plot([xs[-1], xs[0]], [ys[-1], ys[0]], "--", color="#E36A9D", label="Schliesskante")
    plt.fill(xs, ys, color="#F3B8D0", alpha=0.35)
    plt.scatter(xs[0], ys[0], color="#C40062", label="Start")
    plt.scatter(xs[-1], ys[-1], color="#E36A9D", label="Ende")
    plt.xlabel("x in cm")
    plt.ylabel("y in cm")
    plt.title("Gemessene Fläche: " + str(round(flaeche, 2)) + " cm²")
    plt.axis("equal")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(ordner / "trajektorie.png", dpi=200)
    plt.show()
else:
    print("Keine vollständige Messung mit mindestens drei Punkten.")
