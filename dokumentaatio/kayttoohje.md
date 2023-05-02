# Käyttöohje  
### Asennus  
Riippuvuuksien asennus komennolla:  
```console
poetry install
```  
### Käynnistys   
```console
poetry run invoke start
```  
### 1. Luo käyttäjä  
- Sovellus avautuu kirjautumisnäkymään, jossa on painike rekisteröytymistä varten.
- Mikäli näytölle ei tullut lomakkeen tallentamisen jälkeen virheestä ilmoittavaa viestiä ja ohjelma palasi kirjautumisnäkymään, käyttäjän luonti onnistui ja voit kirjautua sisään.
### 2. Kirjaudu sisään  
- Syötä luomasi käyttäjänimi ja salasana. Kirjatumisen onnistuessa sovelluksen päänäkymä ilmaantuu.
### 3. Sovelluksen käyttäminen  
- Ensimmäisenä sivun yläreunassa on ulos kirjautumista varten punainen "Log out"-painike.
- Tämän alapuolella näytetään status ja ajastin.
- Ajastimen alapuolella on ajastimen hallinnointia varten painikkeet.
- "Timer Settings"-painikkeesta voi konfiguroida opiskelulle ja tauolle ajat.
- Todoja lisätään kirjoittamalla todo ikkunan alareunassa oleva tekstikenttään ja painamalla "Create Todo".
- Sivun alareunassa on myös mahdollisuus muokata valittua todoa kirjoittamalla uusi todo ja vaihtamalla se tällä hetkellä valittuun todoon kohdasta "Edit Selected".
- Viimeisenä toimintona on valitun todon poistaminen kohdasta "Delete Todo".