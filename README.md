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
