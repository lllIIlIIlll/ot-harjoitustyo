```mermaid
classDiagram
Pelilauta "1" --> "40" Ruutu
Pelilauta "1" -- "2-8" Pelaaja
Pelilauta "1" -- "2" Nopat
Ruutu "1" -- "1" Pelinappula
Pelaaja "1" -- "1" Pelinappula

class Ruutu {
    seuraava = Ruutu+1
}
```