Algorytm dla projektu „montownia”\
cel zadania:
W montowni, na pojedynczym stanowisku, wykonywana jest prosta operacja złożenia produktu końcowego, którego główne komponenty A i B dostarczane są przez
dwóch niezależnych dostawców. Komponenty składowe A i B trafiają do magazynu,
który może pomieścić w sumie N komponentów. Dostawcy w dowolnym momencie
dostarczają komponenty, a ich obiór może być wstrzymany gdy magazyn będzie wypełniony. Montaż polega na: pobraniu z magazynu pojedynczej sztuki komponentu A,
pobraniu pojedynczej sztuki komponentu B i złożeniu ich w produkt końcowy.
Rozważ sytuację jak wyżej, ale w wersji uogólnionej, gdzie funkcjonuje kilku dostawców komponentu A, kilku dostawców komponentu B oraz kilka stanowisk do montażu. Każde stanowisko do montażu wykonuje działania jak w wersji podstawowej i
wszystkie one mogą pracować jednocześnie.


N – liczba miejsc w magazynie
Struktury użyte w projekcie:
- magazyn jako tablica długości N;
- tablica wolnych indeksów długości N+2(dwa ostatnie miejsca zawierają informację z
którego miejsca w tablicy pobrać zlecenie i w które wstawić nowe)
- tablica z indeksami elementów gotowych do pobrania(jedna dla każdego typu produktu)
każda długości N+1(co najwyżej N-1 elementów danego typu jednocześnie w magazynie + 2
miejsca informacyjne jak wyżej).
Semafory:
- Sa, Sb = N – 1 liczba dostępnych miejsc dla produktów zabezpieczająca przed
zapełnieniem całego magazynu produktem jednego typu;
- Sp = N ogranicza liczbę dostawców w jednym momencie do N;
- Sca, Scb = 0 udostępniają informację o tym czy konsument może pobrać produkt
danego typu;
- Sw = 1 chroni dostęp do tablicy indeksów z wolnymi miejscami
- Sza, Szb = 1 chronią dostępu do tablic z indeksami miejsc zajętych przez
produkt danego typu.
Algorytm dla dostawcy produktu A:
while(1):
P(Sa);
P(Sp);
P(Sw);
Modyfikacja tablicy wolnych indeksów;
V(Sw);
Wykonanie pracy;
P(Sza);
Modyfikacja tablicy gotowych produktów A;
V(Sza);
V(Sca);
Algorytm dla dostawcy produktu B:
while(1):
P(Sb);
P(Sp);
P(Sw);
Modyfikacja tablicy wolnych indeksów;
V(Sw);
Wstawianie elementu(wykonywanie pracy);
P(Szb);
Modyfikacja tablicy gotowych produktów A;
V(Szb);
V(Scb);
Algorytm dla konsumenta:
While(1):
P(Sca);
P(Sza);
Modyfikacja tablicy Gotowych elementów A;
V(Sza);
Pobieranie elementu A(wykonywanie pracy);
P(Sw);
Modyfikacja tablicy wolnych indeksów;
V(Sw);
V(Sa);
V(Sp);
P(Scb);
P(Szb);
Modyfikacja tablicy Gotowych elementów B;
V(Szb);
Pobieranie elementu B(wykonywanie pracy);
P(Sw);
Modyfikacja tablicy wolnych indeksów;
V(Sw);
V(Sb);
V(Sp);
Implementacja programowa zawiera jeden semafor więcej, pozwalający wypisywać aktualny
stan magazynu. Program przedstawia pracę 4 dostawców oraz 3 konsumentów. 0 w
magazynie oznacza puste miejsce, 1 produkt A, 2 produkt B.