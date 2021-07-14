# Wortschatz

SS2021 Semesterprojekt von Victoria Bremer, Annekathrin Kolb, Kevin Liu und Isabel Pfalzgraf

Betriebsanleitung:

<img width="382" alt="Bildschirmfoto 2021-07-14 um 23 10 21" src="https://user-images.githubusercontent.com/58940110/125693444-3a574a0c-2980-4016-b7db-394cea24b5e7.png">

Die LED mit den zwischengeschalteten Widerständen mit den Pins(26) verbinden, und das andere Ende mit GND. 
Nun kann man entscheiden, ob man per Netzwerk-Scan die IP-Adresse des Raspberrys ermittelt und über SSH auf ihn zugreift oder man den PI selbst an einen Bildschirm mit Maus und Tastatur anschließt. Ist der PI nun angeschaltet navigiert man in den Ordner (/path/to/repository) und führt mit Node.js die Datei(server.js) aus.
Im Browser die IP-Adresse des Raspberrys öffnen, damit man sich mit dem Server (Socket.io und express) verbinden kann. 
Hier ist ein Input Feld, dass einen String an ein Python Skript weitergibt. Nun platziert man eine RFID-Karte auf dem Reader damit die RFID-Karte mit dem String beschreiben kann. Dabei leuchtet eine LED auf. 
Ist die Karte beschrieben worden, kann man den Server (mit Strg+C) stoppen und mit dem beigelegten Skript (read-after-writeRfid.py) überprüfen, was auf der RFID-Karte steht. 
Dieses Skript ruft man über python3 auf. Nun kann die eben beschriebene RFID-Karte wieder auf den Reader gelegt werden und die Karte wird ausgelesen. 

Die IP Adresse des Raspberry Pis muss in der client.js mit der eigenen IPv4-Adresse ausgetauscht werden!

<img width="473" alt="Bildschirmfoto 2021-07-14 um 23 09 45" src="https://user-images.githubusercontent.com/58940110/125693354-d58cfbf1-e691-457c-95bc-09b7cf7a5282.png">

Inventarliste Wortschatz:

1 Steckplatine
1 Raspberry 3 Modell B Plus
2 MicroSD-Karten
1 RC522-RFID-Karten
Farbige LEDs
1 330-Ohm-Widerstand
10 Jumper-Kabel Male-Female
Micro-USB-Netzteil
Mini-HDMI-HDMI-Adapter
RFID-Tags oder Karten

