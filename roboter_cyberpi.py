import cyberpi as cy
import mbot2 as pixu
import socket
import time

wlan_name = 'WLAN_NAME'
wlan_passwort = 'WLAN_PASSWORT'
computer_ip = "COMPUTER_IP"
port = 5000
geschwindigkeit = 20
drehgeschwindigkeit = 15


def senden(text):
    verbindung.sendall((text + "\n").encode())


def messwert(art):
    links = pixu.EM_get_angle("EM1")
    rechts = pixu.EM_get_angle("EM2")
    winkel = cy.get_yaw()
    senden(art + ";" + str(links) + ";" + str(rechts) + ";" + str(winkel))


verbindung = None
messen = False
pixu.EM_stop("all")

try:
    cy.console.clear()
    cy.console.println("Verbinde WLAN")
    cy.wifi.connect(wlan_name, wlan_passwort)
    versuche = 0
    while not cy.wifi.is_connect():
        time.sleep(1)
        versuche = versuche + 1
        if versuche == 30:
            raise OSError("WLAN nicht erreichbar")

    cy.console.clear()
    cy.console.println("WLAN verbunden")

    verbindung = socket.socket()
    verbindung.settimeout(5)
    adresse = socket.getaddrinfo(computer_ip, port)[0][-1]
    verbindung.connect(adresse)
    verbindung.settimeout(0.5)

    cy.console.clear()
    cy.console.println("Bereit am PC")

    while True:
        daten = verbindung.recv(1)
        if not daten:
            raise OSError("Verbindung unterbrochen")
        befehl = daten.decode()

        if cy.controller.is_press("b"):
            befehl = "E"

        if befehl == "E":
            pixu.EM_stop("all")
            time.sleep(0.2)
            if messen:
                messwert("E")
            else:
                senden("ENDE")
            break

        if befehl == "S" and not messen:
            pixu.EM_stop("all")
            messen = True
            cy.console.clear()
            cy.console.println("Messung laeuft")
        elif messen and befehl == "F":
            pixu.forward(geschwindigkeit)
        elif messen and befehl == "B":
            pixu.backward(geschwindigkeit)
        elif messen and befehl == "L":
            pixu.turn_left(drehgeschwindigkeit)
        elif messen and befehl == "R":
            pixu.turn_right(drehgeschwindigkeit)
        else:
            pixu.EM_stop("all")

        if messen:
            messwert("D")
        else:
            senden("BEREIT")

    cy.console.clear()
    cy.console.println("Messung beendet")

except OSError as fehler:
    pixu.EM_stop("all")
    cy.console.clear()
    cy.console.println("Verbindung gestoppt")
    print(fehler)

finally:
    pixu.EM_stop("all")
    if verbindung is not None:
        verbindung.close()