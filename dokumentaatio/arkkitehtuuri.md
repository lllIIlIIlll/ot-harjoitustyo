# Arkkitehtuurikuvaus  
### Koodin pakkausrakenne  
```mermaid
classDiagram
   src --> ui
   ui --> repositories
   ui --> services
   ui --> entities
   repositories --> entities
   services --> entities
```  
- ui sisältää käyttöliittymän koodin.
- repositories mahdollistaa entities luokkien tietokantatoiminnot.
- services sisältää luokan jonka avulla ui voi manipuloida entities kansion ajastin luokkaa.
- entities sisältää muut sovelluksen käyttämät luokat.  
### Luokkakaavio  
```mermaid
classDiagram
   App ..> ui
   ui ..> "1" Timer
   ui ..> repositories
   ui ..> User
   repositories --> UserRepo
   repositories --> TodoRepo
   UserRepo --> entities
   TodoRepo --> entities
   ui .. TimerServices
   TimerServices "1" -- "1" Timer
   User "1" .. "1" Timer
   User "1" .. "*" Todo
   entities -- User
   entities -- Todo
```  
### Sovelluslogiikka  
Sovelluksen käyttöliittymän toiminnallisuudesta vastaa:  
[TimerService](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/services/timer_service.py), joka hallinnoi ajastimen toimintoja.  
[TodoRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/reporitories/todo_repo.py), joka mahdollistaa todojen lisäyksen, muokkaamisen ja poistamisen.  
[UserRepo](https://github.com/lllIIlIIlll/ot-harjoitustyo/blob/master/src/reporitories/user_repo.py), joka mahdollistaa kirjautumisen ja rekisteröitymisen.  
### Sekvenssikaavio  
```mermaid
sequenceDiagram
  participant User
  participant ui
  participant Todo
  participant TodoRepo
  User ->> ui: _create_todo()
  ui ->> ui:  new_todo.get() from input field
  ui ->> Todo: Create new Todo instance
  Todo ->> ui: new Todo
  ui ->> TodoRepo: TodoRepo.create_todo(Todo)
  TodoRepo ->> ui: True
  ui ->> ui: Update todo list
```