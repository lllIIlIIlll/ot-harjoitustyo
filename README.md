# StudyTimer  
StudyTimer on sovellus, jonka avulla voi rytmittää opiskelua. Käyttäjä voi määrittää opiskelulle ja tauolle tarkoitetun ajan. Opiskelulle määritetyn ajan loppuessa sovellus ilmoittaa äänimerkillä tauon alkamisesta ja ajastin aloittaa tauolle määritetyn ajan laskemisen. Tämä sykli toistuu kunnes käyttäjä laittaa sovelluksen tauolle. Sovelluksessa on myös todo-lista, jonka avulla voi seurata opiskelutavoitteiden valmistumista.

## Dokumentaatio  
[Vaatimusmäärittely](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)


[Arkkitehtuuri](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivi invoke taskit

### Suorittaminen  
```console
poetry run invoke start
```

### Testaus  
```console
poetry run invoke test
```

### Testikattavuus  
```console
poetry run invoke coverage-report
```

### Pylint  
```console
poetry run invoke lint
```