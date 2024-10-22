from threading import Thread, Lock
from mpi4py import MPI
import sys

class Game:
    def __init__(self):
        self.comm = MPI.COMM_WORLD

        self.rank = self.comm.Get_rank()
        self.size = self.comm.Get_size()

        self.role = None  # rola gracza
        self.pair_id = None # id gracza z pary
        self.pair_number = None # numer pary

        self.lamport_clock = 0

        self.game_request_array = []  #[N/2]
        self.game_timestamp_array = [] #[N]

        self.roles_request_array = [] #[N]
        self.roles_timestamp_array = None #[N]

        self.pistols = None #liczba piostoletow P

        self.shot = None                                    # nowe
        self.dodge = None
        self.everyone_finished_round = []
        self.everyone_started_new_round = []
        self.results = []

        self.wins = 0 #liczba wygranych gracza/procesu

        self.mutex = Lock()
        
        self.start_round_mutex = Lock()
        self.results_mutex = Lock()
        self.pair_req_ready_mutex = Lock()
        self.game_req_ready_mutex = Lock()
        self.pair_id_mutex = Lock()
        self.looking_for_vctm_mutex = Lock()
        self.shot_mutex = Lock()
        self.dodge_mutex = Lock()


def myPrint(data):
    sys.stdout.write(f"{data}\n")
    sys.stdout.flush()

class Packet:
    def __init__(self, tag, id, timestamp):
        self.tag = tag
        self.id = id
        self.timestamp = timestamp
        self.data = None

    # def packetData(self):
    #     return (f"tag: {self.tag}, id: {str(self.id)}, timestamp: {str(self.timestamp)}")



