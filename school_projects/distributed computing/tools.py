from threading import Thread, Lock
from variables import Packet, myPrint

def send_data(GAME, data, dest):
    GAME.comm.send(data, dest=dest)

def myBroadcast(GAME, tag, data=None):
    GAME.mutex.acquire()
    packet = Packet(tag, GAME.rank, GAME.lamport_clock)
    packet.data = data
    for dest in range(GAME.size):
        thread = Thread(target=send_data, args=(GAME, packet, dest,))
        thread.start()
    GAME.lamport_clock += 1
    GAME.mutex.release()

def wait_for_condition(GAME, condition):
        GAME.mutex.acquire()
        if condition:
            GAME.mutex.release()
            return True
        GAME.mutex.release()
        return False

def mySend(GAME, tag, dest, data=None):
    packet = Packet(tag, GAME.rank, GAME.lamport_clock)
    packet.data = data
    thread = Thread(target=send_data, args=(GAME, packet, dest,))
    thread.start()
    GAME.lamport_clock += 1

