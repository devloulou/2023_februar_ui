"""
Általában 5 fázisa van 1 fejlesztésnek: Software Life Cycle
HLD - High Level Design
LLD - Low Level Design
Implementáció
Test
Deploy


Requirements specikáció:

Menü rendszer, ami a funkciókat tartalmazza és vezérli az app működését
Az appnak képesnek kell lennie MongoDB-ben tárolni és felolvasni az adatokat
Az appnak képesnek kell lennie mappákból felolvasni a filmek neveit
és letölteni a hozzájuk tartozó meta adatokat -API-on keresztül
Az appnak képesnek kell lennie arra, hogy a letöltöt metaadatokat grafikusan megjelenítse
Az appnak a már előzőleg letöltött adatokat képesnek kell lennie felolvasni és megjeleníteni
Az appnak képesnek kell lennie a megjelenített poster-ekre
kattintva az egyes filmek adatait megjeleníteni
Az appnak képesnek kell lennie  a "Popular" filmek metaadatait külön kezelve letöltenie


2 funckió:
mappa felolvasása
Popular moviek letöltése

Ezek közös pontjai: metaadat letöltés
                    képek kiírása file-ba
                    adatok letárolása MongoDB-be
                    A már letöltött adatok kiolvasása MongoDB-ből


"""