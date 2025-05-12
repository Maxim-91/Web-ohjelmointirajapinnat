# NÄIN SAAT PROJEKTIN PÄÄLLE

## Luo virtualenv riippuvuuksia varten
* Jos käytät Pycharmia, se saattaa luoda virtualenvin automaattisesti
* python/3 tarkoittaa, että macilla toimii python3 ja windowsilla python

- Suorita terminaalissa komento: python/3 -m venv .venv

## Aktivoi virtualenv

Jos virtualenv ei ole aktiivinen aktivoi se näin

### Windows

.venv\Scripts\activate

### Mac

source .venv/bin/activate

## Asenna riippuvuudet

python/3 -m pip install -r requirements.txt

## Käynnistä ja käytä palvelinta

### Käynnistys

uvicorn main:app

main:app tarkoitaa, että FastAPI-instanssi on nimeltään app ja se sijaitsee tiedostossa main.py

Palvelin käynnistyy oletuksena portissa 8000, jos se ei ole sinulla jo varattu
Jos se on varattu, voit asettaa toisen portin: uvicorn main:app --port porttinumerotahan

### Käyttö

Kun palvelin käynnistyy mene osoitteeseen http://localhost:portti/docs






