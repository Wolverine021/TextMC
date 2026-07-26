```
██████╗███████╗██╗  ██╗████████╗███╗   ███╗ ██████╗
╚═██╔═╝██╔════╝╚██╗██╔╝╚══██╔══╝████╗ ████║██╔════╝
  ██║  █████╗   ╚███╔╝    ██║   ██╔████╔██║██║     
  ██║  ██╔══╝   ██╔██╗    ██║   ██║╚██╔╝██║██║     
  ██║  ███████╗██╔╝ ██╗   ██║   ██║ ╚═╝ ██║╚██████╗
  ╚═╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝
```
Tekstualna simulacija Minecraft inventara i craftinga.

## Znacajke

- Interaktivan CLI meni - craftanje, jelo, koristenje alata, prikaz statova, sve iz terminala
- Sistem inventara s dodavanjem/uklanjanjem predmeta
- Tri tipa predmeta koji nasljeduju baznu klasu `Predmet`: `Blok`, `Alat`, `Hrana`
- Fleksibilan crafting sistem - recepti odreduju i materijale i tip/statove predmeta koji nastaje
- Health/Hunger sistem (`Stats` klasa)
- Recepti se ucitavaju iz vanjskog `recepti.json` fajla
- Stanje igre (inventar + statovi) se sprema/ucitava iz `user.json` - napredak se ne gubi izmedu pokretanja
- Custom exceptions za sve vrste gresaka (nedovoljno materijala, pun inventar, nepostojeci recept/predmet, itd.)

## Pokretanje

```bash
python MC.py
```

Pri pokretanju izabires ucitati postojecu igru (`user.json`) ili zapoceti novu.

## Struktura

- `MC.py` - glavni kod (klase i CLI meni)
- `recepti.json` - definicije crafting recepata
- `user.json` - spremljeno stanje igre (generira se/azurira kroz igru)
