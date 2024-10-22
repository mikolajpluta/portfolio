from variables import *
from main_thread import main_thread
from com_thread import com_thread
from threading import Thread, Lock
from tools import *
import sys
import time

# def wait_for_condition(GAME, condition):
#         GAME.mutex.acquire()
#         if condition:
#             GAME.mutex.release()
#             return True
#         GAME.mutex.release()
#         return False

GAME = Game()

def main(N, P):

    #ustawienie wartosci poczatkowych
    global GAME

    GAME.role = None
    GAME.pair_id = None
    GAME.pair_number = None

    GAME.game_request_array = [None] * (N // 2)
    GAME.game_timestamp_array = [None] * N

    GAME.roles_request_array = [None] * N
    GAME.roles_timestamp_array = [None] * N

    GAME.everyone_finished_round = [0] * N
    GAME.everyone_started_new_round = [0] * N

    GAME.shot = None
    GAME.dodge = None

    GAME.pistols = int(P)

    GAME.start_round_mutex.acquire()
    GAME.results_mutex.acquire()
    GAME.pair_req_ready_mutex.acquire()
    GAME.pair_id_mutex.acquire()
    GAME.looking_for_vctm_mutex.acquire()
    GAME.shot_mutex.acquire()
    GAME.game_req_ready_mutex.acquire()
    GAME.dodge_mutex.acquire()


    l_com_thread = Thread(target=com_thread, args=(GAME,))
    l_main_thread = Thread(target=main_thread, args=(GAME,))
    
    l_com_thread.start()
    #czekanie az watek komunikacjyjny wystartuje
    time.sleep(0.1)
    
    #broadcast NEW_ROUND
    myBroadcast(GAME, "NEW_ROUND")

    #oczxekiwanie az wszystkie instancj zaczna runde
    GAME.start_round_mutex.acquire()

    #start wątku glowneog i oczekiwanie nnna zakonczenie
    l_main_thread.start()
    l_main_thread.join()

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python program.py arg1 arg2")
    else:
        P = sys.argv[1]
        cycles = sys.argv[2]

    for _ in range(int(cycles)):
        myPrint(f"{GAME.rank}: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        main(GAME.size, P)
        GAME.start_round_mutex.release()
        # czekanie az wszytskie wyniki przyjda
        GAME.results_mutex.acquire()
        GAME.results_mutex.release()
        GAME.pair_req_ready_mutex.release()
        GAME.pair_id_mutex.release()
        GAME.looking_for_vctm_mutex.release()
        GAME.shot_mutex.release()
        GAME.game_req_ready_mutex.release()
        GAME.dodge_mutex.release()
    
    myPrint(f"{GAME.rank}: wyniki: {GAME.results}")
