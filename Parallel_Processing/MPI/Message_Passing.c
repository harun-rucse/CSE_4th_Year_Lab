#include <stdio.h>
#include <mpi.h>
#include<string.h>

#define MAX 100

int main(int argc, char **argv) {
    int rank;
    char message[MAX];

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        strcpy(message, "Hello world!");
        MPI_Send(&message, strlen(message)+1, MPI_CHAR, 1, 1, MPI_COMM_WORLD);
        printf("Message send from master process: %s\n", message);
    }
    else if(rank == 1) {
        char msg[MAX];
        MPI_Recv(&msg, MAX, MPI_CHAR, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Message received: %s\n", msg);
    }

    MPI_Finalize();
}