from variables import Packet, myPrint
from mpi4py import MPI
from threading import Thread
from tools import *
import time
import random

def play(GAME):
    READY_TO_ENTER_CRITICAL_SECTION = True
    PLACE_IN_QUEUE = 0

    #broadcast GAME_REQ
    myBroadcast(GAME, "GAME_REQ")

    #oczekiwanie az wlasny GAME_REQ pojawi sie w tablicy
    GAME.game_req_ready_mutex.acquire()

    #sprawdzanie czy moze wejsc do sekcji krytycznej
    while True:
        time.sleep(0.1)
        #teraz bedziemy spreawdac tylko timestampy KILLEROW, nie wiemy kotre procesy nimi sa wiec musimy sprawdzic czy 
        #polowa tablicy jest wypelnona wartosciami innym niz None
        cntr = GAME.game_timestamp_array.count(None)
        if cntr != GAME.size/2:
            continue

        #zgromadzenie numerów procesów kotrych timestampy trzeba sprwdzic
        ranks = []
        for j in range(len(GAME.game_timestamp_array)):
            if GAME.game_timestamp_array[j] != None:
                ranks.append(j)
        i = 0

        while i < len(GAME.game_request_array) and GAME.game_request_array[i][0] != GAME.rank:
            ranks.remove(GAME.game_request_array[i][0])
            i += 1
        # if GAME.game_request_array[i][0] == GAME.rank:
        #     ranks.remove(GAME.rank)

        PLACE_IN_QUEUE = i
        
        #sprawdzenie czy wybrane procesy przysłąły wiadomości nowsze niż timestamp naszego requestu
        for rank in ranks:
            if GAME.game_timestamp_array[rank] == None or GAME.game_timestamp_array[rank] < GAME.game_request_array[i][1]:
                READY_TO_ENTER_CRITICAL_SECTION = False
                break
        
        # ostateczny warunek wejscia do sekcji krytycznej
        if READY_TO_ENTER_CRITICAL_SECTION and PLACE_IN_QUEUE < GAME.pistols:
            break
        
    #sekcja krytyczna
    myPrint(f"{GAME.rank} wchodze do sekcji krytycznej")
    time.sleep(random.random() * 3)     #praca

    #wyslij SHOOT:
    GAME.shot = random.randint(0, 1)
    GAME.mutex.acquire()
    mySend(GAME, "SHOOT", GAME.pair_id, GAME.shot)
    GAME.mutex.release()

    #czekaj na wynik od pary
    GAME.dodge_mutex.acquire()
    
    #sprawdz wynik rozgrywki
    if GAME.shot == GAME.dodge:
        GAME.wins += 1
        myPrint(f"{GAME.rank}: OFIARA TRAFIONA")
    else:
        myPrint(f"{GAME.rank}: OFIARA ZROBILA UNIK")
    
    #broadcast GAME_RELEASE
    myBroadcast(GAME, "GAME_RELEASE")


def main_thread(GAME):

    READY_TO_ENTER_CRITICAL_SECTION = True
    PLACE_IN_QUEUE = -1
    
    #broadcast PAIR_REQ
    myBroadcast(GAME, "PAIR_REQ")

    #oczekiwanie az wlasny PAIR_REQ pojawi sie w tablicy
    GAME.pair_req_ready_mutex.acquire()

    #sprawdzanie czy moze wejsc do sekcji krytycznej
    while True:
        time.sleep(0.1)

        #zgromadzenie numerów procesów kotrych timestampy trzeba sprwdzic
        ranks = [i for i in range(len(GAME.roles_request_array))]
        i = 0

        while i < len(GAME.roles_request_array) and GAME.roles_request_array[i][0] != GAME.rank:
            ranks.remove(GAME.roles_request_array[i][0])
            i += 1
        if GAME.roles_request_array[i] != None and GAME.roles_request_array[i][0] == GAME.rank:
            ranks.remove(GAME.rank)

        #sprawdzenie czy wybrane procesy przysłały wiadomości nowsze niż timestamp naszego requestu
        for rank in ranks:
            if GAME.roles_timestamp_array[rank] == None or GAME.roles_timestamp_array[rank] < GAME.roles_request_array[i][1]:
                READY_TO_ENTER_CRITICAL_SECTION = False
                break

        #Ostateczny waunek wejscia do sekcji kryrtcznej
        if READY_TO_ENTER_CRITICAL_SECTION:
            PLACE_IN_QUEUE = i
            break

    #sekcja krytyczna doboru pary
    if PLACE_IN_QUEUE % 2 == 0:
        GAME.role = "KILLER"
        GAME.pair_number = PLACE_IN_QUEUE // 2
    else:
        GAME.role = "VICTIM"
        GAME.pair_number = PLACE_IN_QUEUE // 2

        
    time.sleep(0.1) # opoznienie zeby wyswietlło sie razem
    myPrint(f"{GAME.rank}: moja rola to {GAME.role} a numer pary to {GAME.pair_number}")


    if GAME.role == "KILLER":
        # #broadcast LOOKING_FOR_VICTIM
        myBroadcast(GAME, "LOOKING_FOR_VICTIM", GAME.pair_number)

        #oczekuj na odbior id swojej pary
        GAME.pair_id_mutex.acquire()

        #wypisanie swojej pary:
        time.sleep(0.1)
        myPrint(f"{GAME.rank}: moja para to: {GAME.pair_id}")

        # rozgrywka
        play(GAME)

    else:
        #oczekuj na LOOKING_FOR_VICTIM
        GAME.looking_for_vctm_mutex.acquire()
        
        #wysklij HELLO_MY_KILLER:
        GAME.mutex.acquire()
        mySend(GAME, "HELLO_MY_KILLER", GAME.pair_id)
        GAME.mutex.release()

        #oczekuj na strzal
        GAME.shot_mutex.acquire()

        #odeslij unik
        GAME.dodge = random.randint(0, 1)
        GAME.mutex.acquire()
        mySend(GAME, "DODGE", GAME.pair_id, GAME.dodge)
        GAME.mutex.release()

        #sprawdznie wyniku
        if GAME.shot != GAME.dodge:
            GAME.wins += 1
            myPrint(f"{GAME.rank}: ZROBILEM UNIK")
        else:
            myPrint(f"{GAME.rank}: ZOSTAŁEM POSTRZELONY")

    #rozgloszenie wynikow
    myBroadcast(GAME, "RESULT", GAME.wins)
    return