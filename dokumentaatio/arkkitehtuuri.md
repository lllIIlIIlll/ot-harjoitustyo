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