# Erstes Beispiel für eine Flask-Anwendung (Backend)
1. Erstelle eine VENV
Erzeuge dir eine venv mit dem Befehl `python -m venv <Name der Venv>`.
Danach wollen wir die VENV aktivieren
Auf MacOS/Linux
```bash
source <Name der Venv>/bin/activate
```
Auf Windows in der Git Bash
```bash
source <Name der Venv>/Scripts/activate
```
2. Installation von Flask
Installiere dir mithilfe des Befehls `pip install flask` das Flask-Modul.
Es werden Pakete installiert.
3. Festhalten der Abhängigkeiten in einer requirements.txt
Damit deine Kollegen auch wissen, welche Abhängigkeiten (Module und Pakete) dein Projekt hat, schreibe sie in eine requirements.txt
```bash
pip freeze > requirements.txt
```
4. Initialisiere Git-Repository
- Initialisiere ein Git-Repository mit `git init`
- Lege eine .gitignore an, in der du den Namen deines venv-Ordners reinschreibst, damit diese nicht mit versioniert bzw. gepushed wird
- Überprüfe mit `git status`, ob der venv-Ordner mit getracked wird
- Adde deine Veränderungen mit `git add .` und committe sie mit `git commit -m "added venv with flask dependency"`
- Wenn wir das pushen wollen auf Github, lege erst ein Repository auf Github an und dann füge per `git remote add origin <Link zum Github-Repo>` den Remote-Branch hinzu und mach dann ein `git push -u origin <Angabe des Branches>`, damit wir den upstream einmal hinzufügen. 
Achtung: Wir müssen nach dem Hinzufügen des Remote-Branches immer erst den Upstream hinzufügen mit -u origin ..
5. Erstelle die flask-App
- Lege eine neue Python-Datei im Terminal an mit `touch app.py` 
6. Schreibe Flask-Anwendung
```python
from flask import Flask

app = Flask(__name__)

# Route definieren
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
```
- from flask import Flask: Importiert von unserem flask-Modul die Flask-Klasse
- app = Flask(__name__): Erzeuge Instanz (Objekt) der Flask-Klasse. Achtung: __name__ ist eine spezielle Python-Variable. die den Namen des aktuellen Moduls enthält.
- @app.route('/'): Dekorator, der Flask mitteilt, welche URL die nachstehende Funktion auslöst
- def hello_world(): Funktion, die ausgeführt wird, sobald die Route aufgerufen wird
- return 'Hello, World!': Die Antwort, die dann an den Client gesendet wird
- if __name__ == '__main__': Stelle sicher, dass Server läuft wenn das Skript ausgeführt wird
- app.run(debug=True):Starte den Server (Developement-Server) im Debug-Modus. Debug für mehr Informationen, die uns der Server gibt


---
## Wie starte ich das Ganze bei mir selbst? 
Setting: Das Repository liegt gerade in unserer Organisation (ts-25-01) auf dem Github-Account. Wie kann ich das nun bei mir lokal laufen lassen?
1. Gehe auf den Link des Github-Repositories
2. Forke dir das Github-Repository, damit eine Kopie davon bei dir auf dem Github-Account liegt. Drücke dazu auf den Button Fork, wähle dann deinen Github Account aus und dann auf Bestätigen
3. Klone dir das neue (geforkte) Repository 
4. Du hast das Repository nun lokal vorliegen.
5. Jetzt musst du für das geklonte Projekt eine venv anlegen. Diese muss auch aktiviert werden. Dann müssen die Abhängigkeiten in der venv installiert werden mit `pip install -r requirements.txt`
6. Jetzt könnt ihr mit `python app.py` die Anwendung laufen lassen
7. Ihr könnt außerdem auch Veränderungen an der app.py vornehmen. Wenn ihr das festhalten wollt, könnt ihr das wieder adden, committen und pushen. 

