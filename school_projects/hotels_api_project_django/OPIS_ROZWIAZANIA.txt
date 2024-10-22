zadanie:
Create small project to serve REST API using Django Rest Framework.
At first you should define your reality which you represents in 3-4 sample models. Your models should have:
at least one relation one-to-many between models
at least one relation many-to-many between models
custom User model with type field
In the next step you should prepare REST API to serve data from your models. Your REST API should have:
endpoint to log in by user (it would be nice to give user about his type after log in)
public endpoint to serve data from your models with all related objects
private endpoint (only for superusers) to create entry with nested objects
private endpoint (only for owners) to update entry with nested objects

projekt jest prostą aplikacją pozwalającą na zarządzanie hotelami,
w bazie danych znajduje się już kilka przykładowych obiektów w tym:
-6 uzytkownikow na potrzeby testow, username user<nr> np, user1, a hasło każdego to 123
	uzytkownicy 1 i 2 maja typ "guest", 3 i 4 - "owner", a 5 i 6 to "admin"
-system udostepnia endpoint /hotels który udostepnia dane na temat hoteli
-endpoint /login umozliwia zalogowanie sie uzytkownika, oraz zwraca informację o jego typie
-endpoint /hotels/admin umozliwia uzytkownikom typu "admin" na dodawanie nowych hoteli
-endpoint /hotels/owner/<nr> umożliwa wascicielowi hotelu na edycje wlasciwosci hotelu (nr to id hotelu)
