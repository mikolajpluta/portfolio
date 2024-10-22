from variables import Packet, myPrint
from mpi4py import MPI
from threading import Thread
from tools import *


# def send_data(GAME, data, dest):
#     GAME.comm.send(data, dest=dest)

def sort_key(tab):
    if tab is None:
        return (float('inf'), float('inf'))
    return (tab[1], tab[0])
    

def com_thread(GAME):

    while True:

        #odbior pakietu
        packet = GAME.comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)

        GAME.mutex.acquire()

        #aktualizacja 
        GAME.lamport_clock = max(GAME.lamport_clock, packet.timestamp) + 1
        GAME.roles_timestamp_array[packet.id] = packet.timestamp

        if packet.tag == "PAIR_REQ":

            myPrint(f"{GAME.rank}: otzymalem PAIR_REQ od {packet.id} w momencie {GAME.lamport_clock}")

            #wstawienie i posortowanie requestu
            index = GAME.roles_request_array.index(None)
            GAME.roles_request_array[index] = [packet.id, packet.timestamp]
            GAME.roles_request_array = sorted(GAME.roles_request_array, key=sort_key)

            #wyslanie ACK
            mySend(GAME, "PAIR_ACK", packet.id)

            #sprawdzenie czy wlasny req jest w kolejce
            if packet.id == GAME.rank and any(element is not None and element[0] == GAME.rank for element in GAME.roles_request_array):
                GAME.pair_req_ready_mutex.release()


        elif packet.tag == "PAIR_ACK":
            myPrint(f"{GAME.rank}: otzymalem PAIR_ACK od {packet.id} w momencie {GAME.lamport_clock}")

        elif packet.tag == "LOOKING_FOR_VICTIM":
            if GAME.role == "VICTIM" and packet.data == GAME.pair_number:
                GAME.pair_id = packet.id
                GAME.looking_for_vctm_mutex.release()

        elif packet.tag == "HELLO_MY_KILLER":
            if GAME.role == "KILLER":
                GAME.pair_id = packet.id
                GAME.pair_id_mutex.release()
        
        elif packet.tag == "GAME_REQ":
            if GAME.role == "KILLER":  #tylko killerzy ubiegaja sie o sekcje krytyczna
                myPrint(f"{GAME.rank}: otzymalem GAME_REQ od {packet.id} w momencie {GAME.lamport_clock}")

                #aktualizacja 
                GAME.game_timestamp_array[packet.id] = packet.timestamp

                #wstawienie i posortowanie requestu
                index = GAME.game_request_array.index(None)
                GAME.game_request_array[index] = [packet.id, packet.timestamp]
                GAME.game_request_array = sorted(GAME.game_request_array, key=sort_key)

                #wyslanie ACK
                mySend(GAME, "ACK", packet.id)

                if packet.id == GAME.rank and any(element is not None and element[0] == GAME.rank for element in GAME.game_request_array):
                    GAME.game_req_ready_mutex.release()

        
        elif packet.tag == "GAME_ACK":
            myPrint(f"{GAME.rank}: otzymalem GAME_ACK od {packet.id} w momencie {GAME.lamport_clock}")
            #aktualizacja
            GAME.game_timestamp_array[packet.id] = packet.timestamp
        
        elif packet.tag == "GAME_RELEASE":
            GAME.game_timestamp_array[packet.id] = packet.timestamp
            for i in range(len(GAME.game_request_array)):
                if GAME.game_request_array[i] != None and GAME.game_request_array[i][0] == packet.id:
                    del GAME.game_request_array[i]
                    break
        
        elif packet.tag == "SHOOT":
            if packet.data == 0:
                GAME.shot = 0
            else:
                GAME.shot = 1
            GAME.shot_mutex.release()
        
        elif packet.tag == "DODGE":
            if packet.data == 0:
                GAME.dodge = 0
            else:
                GAME.dodge = 1
            GAME.dodge_mutex.release()

        elif packet.tag == "RESULT":
            if len(GAME.results) < GAME.size:
                GAME.results.append([packet.id, packet.data])
            else:
                for i in range(GAME.size):
                    if GAME.results[i][0] == packet.id:
                        GAME.results[i] = [packet.id, packet.data]
                        break

            #aktualizacja przy idebraniu wynikow
            GAME.everyone_finished_round[packet.id] = 1

            #sprawdzenie czy przyszyly wszystkie wyniki
            if sum(GAME.everyone_finished_round) == GAME.size:
                GAME.results_mutex.release()
        
        elif packet.tag == "NEW_ROUND":
            #aktualizacja zeby sprawdzic czy wszyscy zaczelki runde
            GAME.everyone_started_new_round[packet.id] = 1

            #sprawdz czy moza zaczac runde
            if sum(GAME.everyone_started_new_round) == GAME.size:
                GAME.start_round_mutex.release()

        GAME.mutex.release()         
        
            