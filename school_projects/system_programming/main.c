#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <semaphore.h>
#include <time.h>
#define N 10


int warehouse[N];
int empty[N+2];
int ready_A[N+1];
int ready_B[N+1];

sem_t Sa, Sb, Sp, Sca, Scb, Sw, Sza, Szb, prnt;

void print_status(){
    printf("stan magazynu: ");
    for(int i=0; i<N; i++) printf("%d ", warehouse[i]);
    printf("\n");
}

void* producer_A(void* info) {
    int index;
    int work_time;
    while(1){
        work_time = rand() % 3 + 1;

        sem_wait(&Sa);
        sem_wait(&Sp);

        sem_wait(&Sw);
        index = empty[empty[N]];
        empty[N] = (empty[N] + 1) % N;
        sem_post(&Sw);

        warehouse[index] = 1;

        sem_wait(&prnt);
        print_status();
        sem_post(&prnt);

        sleep(work_time);

        sem_wait(&Sza);
        ready_A[ready_A[N]] = index;
        ready_A[N] = (ready_A[N] + 1) % N-1;
        sem_post(&Sza);

        sem_post(&Sca);
    }
    return NULL;
}

void* producer_B(void* info) {
    int index;
    int work_time;
    while(1){
        work_time = rand() % 3 + 1;

        sem_wait(&Sb);
        sem_wait(&Sp);

        sem_wait(&Sw);
        index = empty[empty[N]];
        empty[N] = (empty[N] + 1) % N;
        sem_post(&Sw);

        warehouse[index] = 2;

        sem_wait(&prnt);
        print_status();
        sem_post(&prnt);

        sleep(work_time);

        sem_wait(&Szb);
        ready_B[ready_B[N]] = index;
        ready_B[N] = (ready_B[N] + 1) % N-1;
        sem_post(&Szb);

        sem_post(&Scb);
    }
    return NULL;
}

void* consumer(void* info) {
    int index;
    int work_time;
    while(1){
        work_time = rand() % 1 + 1;

        sem_wait(&Sca);
        sem_wait(&Sza);
        index = ready_A[ready_A[N-1]];
        ready_A[N-1] = (ready_A[N-1] + 1) % N-1;
        sem_post(&Sza);

        sleep(work_time);
        warehouse[index] = 0;
        sem_wait(&prnt);
        print_status();
        sem_post(&prnt);

        sem_wait(&Sw);
        empty[empty[N+1]] = index;
        empty[N+1] = (empty[N+1] + 1) % N+1;
        sem_post(&Sw);
        sem_post(&Sa);
        sem_post(&Sp);

        sem_wait(&Scb);
        sem_wait(&Szb);
        index = ready_B[ready_B[N-1]];
        ready_B[N-1] = (ready_B[N-1] + 1) % N-1;
        sem_post(&Szb);

        sleep(work_time);
        warehouse[index] = 0;
        sem_wait(&prnt);
        print_status();
        sem_post(&prnt);

        sem_wait(&Sw);
        empty[empty[N+1]] = index;
        empty[N+1] = (empty[N+1] + 1) % N+1;
        sem_post(&Sw);
        sem_post(&Sb);

        sem_post(&Sp);
    }
    return NULL;
}


int main() {
    srand(time(NULL));

    for(int i=0; i<N; i++) empty[i] = i;
    empty[N] = 0;
    empty[N+1] = 0;

    for(int i=0; i<N; i++) warehouse[i] = 0;

    sem_init(&Sa, 0 ,N-1);
    sem_init(&Sb, 0 ,N-1);
    sem_init(&Sp, 0 ,N);
    sem_init(&Sca, 0 ,0);
    sem_init(&Scb, 0 ,0);
    sem_init(&Sw, 0 ,1);
    sem_init(&Sza, 0 ,1);
    sem_init(&Szb, 0 ,1);
    sem_init(&prnt, 0 ,1);

    pthread_t worker_A_1, worker_A_2, worker_B_1, worker_B_2, consumer_1, consumer_2, consumer_3;

    pthread_create(&worker_A_1, NULL, producer_A, NULL);
    pthread_create(&worker_A_2, NULL, producer_A, NULL);

    pthread_create(&worker_B_1, NULL, producer_B, NULL);
    pthread_create(&worker_B_2, NULL, producer_B, NULL);

    pthread_create(&consumer_1, NULL, consumer, NULL);
    pthread_create(&consumer_2, NULL, consumer, NULL);
    pthread_create(&consumer_3, NULL, consumer, NULL);

    pthread_join(worker_A_1, NULL);
    pthread_join(worker_A_2, NULL);
    pthread_join(worker_B_1, NULL);
    pthread_join(worker_B_2, NULL);

    pthread_join(consumer_1, NULL);
    pthread_join(consumer_2, NULL);
    pthread_join(consumer_3, NULL);

    return 0;
}