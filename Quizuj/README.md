# Czym jest Quizuj?
Quizuj to lokalna gra wieloosobowa w stylu teleturnieju telewizyjnego wykonana dla [ClueRoom](https://clueroom.pl), która wkrótce zostanie uruchomiona.  
W jej skład wchodzi szereg aplikacji mających na celu nie tylko wywołanie wrażenia przebywania w teleturnieju telewizyjnym u graczy, ale także umożliwienie dostosowania rozgrywki do własnych potrzeb oraz łatwego zarządzania nią.<br>
całość wykonywana była w dwuosobowym zespole.

## Demo
Poniżej znajdują się linki do filmów z prezentacją części możliwości systemu, ze względu na to, że gra nie została jeszcze uruchomiona są to tylko przykładowe materiały nagrane w środowisku testowym. Materiały audiowizualne są w większosci przykładowe i mogą być niespójne z treścią.
[Przykładowa rozgrywka](https://drive.google.com/file/d/1PuAiMXAukl8R1tOKSpCVBrLW_-XguNG0/view?usp=sharing)<br>
[Prezentacja panelu administracyjnego](https://drive.google.com/file/d/1rx1je96pVc3pkTb6nU1PKGjGBas5di4z/view?usp=sharing)


## Zawartość i możliwości

### Dostępne gry
Specjalnie dostosowany pokój do gry pozwala graczom na rywalizację w grach o czterech charakterystykach:
- **Wiedza** – gracze wybierają jedną spośród czterech odpowiedzi na zadane pytanie.
- **Muzyka** – gracze odpowiadają na pytania muzyczne.
- **Gra statystyczna** – uczestnicy starają się odgadnąć, co odpowiedzieli ankietowani.
- **Gra słowna** – gracze kręcą kołem i odgadują hasła.
- Każda rozgrywka zakończona jest prezentacją statystyk graczy w aktualnie rozgrywanym scenariuszu (możliwość bicia rekordów).

### Możliwości
- **Rozgrywka** - od 2 do 6 graczy, każdy gracz wybiera stanowisko składające się z dotykowego panelu gracza, oraz ekranu punktów z przodu. Dzięki panelowi gracza uczestnik może wchodzić w interakcję z grą. W pomieszczeniu znajduje się również ekran główny prezentujący zawartość kotrą widzą wszyscy gracze.
- Specjalnie zaprojektowany panel administracyjny udostępnia:
    * zarządzanie rozgrywką, w tym:
        + uruchomienie rozgrywki, zatrzymanie, wznowienie, reset;
        + śledzenie stanu każdej aplikacji, stanowiska oraz zewnętrznych procesorów sterujących multimediami w czasie rzeczywistym;
        + możliwość przywrócenia stanu rozgrywki w razie awarii;
    * zarządzanie scenariuszami:
        + możliwość modyfikowania i tworzenia własnych scenariuszy rozgrywki, co pozwala na dostosowanie m.in. treści pytań i odpowiedzi, dźwięków audio, czasów rozgrywki, doboru gier i ich kolejności;
        + dostosowanie opcjonalnych dialogów i reakcji na zdarzenia zachodzące w grze;
        + dostosowanie bonusów zdobywanych w trakcie rozgrywki;
        + dostosowanie filmów instruktażowych przed grą;
        + eksport i import scenariuszy w dedykowanym formacie plików;
    * możliwość wykonania kopii zapasowej aktualnych scenariuszy;
    * możliwość zdalnego włączania i wyłączania całego systemu za pomocą panelu administratora.
- **API**
    * system udostępnia szereg sygnałów, które wysyłane są do miejsca wskazanego w pliku konfiguracyjnym i zawierają informację o aktualnie wykonanych akcjach – sygnały te mogą zostać wykorzystane np. do obsługi dodatkowych multimediów w pokoju gry;
    * system udostępnia interfejs umożliwiający interakcję z grami z urządzeń zewnętrznych, np. fizyczne przyciski umożliwiające graczom wybór odpowiedzi lub możliwość zakręcenia fizycznym kołem fortuny.

## Wykorzystane technologie
Aplikacje składające się na system to aplikacje desktopowe wykonane z wykorzystaniem technologii webowych.
Wykorzystane technologie:
 - React
 - Electron
 - Node.js
 - Express
 - Websockets
 - MongoDB
 - Python

## Zakres prac
Zakres pracy obejmował nie tylko wytworzenie systemu, ale również pełną konfigurację środowiska końcowego, w tym:<br>
konfigurację sieci, konfigurację systemów Linux (dedykowany tryb kiosku, obsługa wielu ekranów dotykowych i inne), konfigurację systemów Windows oraz wykonanie dokumentacji technicznej(w tym instrukcja konfiguracji, instrukcja dla użytkowników i dokumentacja kodu)
