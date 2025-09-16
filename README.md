En Windows:
py -m venv venv
venv\Scripts\activate.bat  # para sistemas basados en Windows
pip install -r requirements.txt

En Debian/Ubuntu:
En sistemas Debian/Ubuntu, se necesita instalar el paquete python3-venv
usando el siguiente comando:

    sudo apt install python3.{X}-venv

Dónde X es la version de Python 3 que se usa.
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt