# Maturaarbeit-Pixu
Python-Programme und Messdaten zur Flächenbestimmung mit Pixu (mBot2)
# Maturaarbeit – Flächenbestimmung mit Pixu (mBot2)

**Milica Popovic**

Kantonale Maturitätsschule für Erwachsene Zürich (KME)

Maturaarbeit | November 2026

## 1. Projektbeschreibung

Im Rahmen meiner Maturaarbeit untersuche ich, wie sich der Flächeninhalt einer ebenen Figur anhand der Trajektorie eines mobilen Roboters bestimmen lässt.

Dazu verwende ich den Makeblock mBot2, den ich «Pixu» genannt habe. Der Roboter wird über einen Laptop ferngesteuert und erfasst während der Fahrt die Drehwinkel seiner beiden Antriebsräder sowie den Gyrowinkel.

Aus diesen Sensordaten werden mithilfe der Odometrie die Positionen des Roboters berechnet. Die aufeinanderfolgenden Positionen bilden eine polygonale Annäherung der gefahrenen Trajektorie. Der eingeschlossene Flächeninhalt wird anschliessend mit der Gaussschen Flächenformel (Shoelace-Formel) bestimmt.

Zur Überprüfung des Verfahrens wurden drei Referenzflächen mit bekannten Seitenlängen jeweils dreimal abgefahren. Die berechneten Flächeninhalte wurden mit den Referenzwerten verglichen.

## 2. Inhalt des Repositorys

### Roboter- und Laptopprogramme

- **`roboter_cyberpi.py`**: Python-Programm für den CyberPi des mBot2. Es empfängt Fahrbefehle, steuert die Motoren, liest die Sensorwerte aus und überträgt sie über WLAN/TCP.
- **`laptop_auswertung.py`**: Python-Programm für die Fernsteuerung, den Empfang der Sensordaten, die Positionsberechnung, die Anwendung der Shoelace-Formel sowie die Speicherung und grafische Darstellung der Messungen.

### Ordner `Messdaten`

Enthält die Messdaten der Versuchsreihe, geordnet nach Referenzfläche und Versuch.

Bei jeder Messung erzeugt das Laptopprogramm folgende Dateien:

- **`messdaten.csv`**: Sensorwerte und berechnete Positionskoordinaten
- **`ergebnis.txt`**: Berechneter Flächeninhalt, Schliessabstand und Anzahl gespeicherter Messpunkte
- **`trajektorie.png`**: Grafische Darstellung der berechneten Trajektorie

### Ordner `Abbildungen_Codes`

Enthält die Python-Codes zur Erstellung der mathematischen und technischen Abbildungen der Maturaarbeit. Die Dateinamen ermöglichen die Zuordnung zu den jeweiligen Abbildungsnummern.

Die fertigen Abbildungen sind bereits in der schriftlichen Maturaarbeit enthalten und werden deshalb hier nicht nochmals separat bereitgestellt.

## 3. Technische Umsetzung

**Verwendete Hardware:**
- Makeblock mBot2 mit CyberPi
- Motorencoder der beiden Antriebsräder
- Gyrosensor
- Laptop

**Verwendete Software:**
- Python
- mBlock
- PyCharm
- Matplotlib

Die Kommunikation zwischen Pixu und dem Laptop erfolgt über eine TCP-Verbindung im WLAN.

Die veröffentlichten Programme enthalten Platzhalter für die Netzwerkzugangsdaten. Für eine eigene Ausführung müssen WLAN-Name, Passwort, IP-Adresse und die übereinstimmende Portnummer entsprechend konfiguriert werden.

## 4. Hinweise zur Auswertung

Die berechneten Positionskoordinaten beruhen auf den Encoder- und Gyrosensordaten. Sie stellen eine Schätzung der gefahrenen Trajektorie dar und keine unabhängig gemessene Position.

Die Versuche wurden manuell gesteuert. Die ermittelten Flächenabweichungen berücksichtigen daher das gesamte Messverfahren einschliesslich möglicher Abweichungen bei der Fahrt entlang der Referenzbegrenzung.

Die ausführliche Beschreibung der mathematischen Grundlagen, der Versuchsdurchführung und der Ergebnisse befindet sich in der schriftlichen Maturaarbeit.
