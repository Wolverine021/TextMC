██████╗███████╗██╗  ██╗████████╗███╗   ███╗ ██████╗
╚═██╔═╝██╔════╝╚██╗██╔╝╚══██╔══╝████╗ ████║██╔════╝
  ██║  █████╗   ╚███╔╝    ██║   ██╔████╔██║██║ 
  ██║  ██╔══╝   ██╔██╗    ██║   ██║╚██╔╝██║██║ 
  ██║  ███████╗██╔╝ ██╗   ██║   ██║ ╚═╝ ██║╚██████╗
  ╚═╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝

# TextMC

Tekstualna simulacija Minecraft inventara i craftinga

## Značajke
- Sistem inventara s dodavanjem/uklanjanjem predmeta
- Tri tipa predmeta koji nasljeđuju baznu klasu: Blok, Alat, Hrana
- Crafting sistem koji provjerava materijale prije izrade predmeta
- Health/Hunger sistem (Stats klasa)
- Recepti se učitavaju iz vanjskog JSON fajla
- Custom exceptions za rukovanje greškama (nedovoljno materijala, pun inventar, itd.)

## Pokretanje
```bash
python textmc.py
```

## Struktura
- `textmc.py` - glavni kod (klase i logika)
- `recepti.json` - definicije crafting recepata
