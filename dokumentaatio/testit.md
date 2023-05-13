# Testaus  
Ohjelmaa testataan automatisoidusti unittestilla. Järjestelmätestaus tehty manuaalisesti Linux-ympäristössä noudattamalla [Käyttöohjetta](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md).

### Testien suorittaminen
```console
poetry run invoke test
```

### Testikattavuusraportin luonti 
```console
poetry run invoke coverage-report
```

# Ajastimen testaus  
Ajastinta testataan [TestTimerservice](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/tests/timer_service_test.py)-luokalla. Luokan setUp-metodissa alustetaan [Timer](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/entities/Timer.py)-olio, sekä [TimerService](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/services/timer_service.py)-olio, jolle tämä annetaan.

# Repositorio-luokkien testaus  
[TodoRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/repositories/todo_repo.py)-luokkaa testataan [TestTodoRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/tests/todo_repo_test.py)-luokalla. Luokan setUp-metodissa kutsutaan [TodoRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/repositories/todo_repo.py)-luokkaa parametrilla test=True, jotta voidaan käyttää testaamiseen tarkoitettuja tietokantatauluja.  

[UserRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/repositories/user_repo.py)-luokkaa testataan [TestUserRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/tests/user_repo_test.py)-luokalla. Luokan setUp-metodissa kutsutaan [UserRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/repositories/user_repo.py)-luokkaa myös parametrilla test=True, jotta voidaan käyttää testaamiseen tarkoitettuja tietokantatauluja. 

# Testikattavuusraportti
![testikattavuusraportti](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/img/coverage_report.png)
