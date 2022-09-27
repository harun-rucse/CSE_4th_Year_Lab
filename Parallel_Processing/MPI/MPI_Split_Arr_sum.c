#include<stdio.h>
#include<mpi.h>

int main(int argc, char **argv) {
    int rank, N=12;
    int section = N/4;
    int subArr[200];

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if(rank == 0) {
        printf("Give 12 random values: \n");
        int values[12] = {1,2,3,4,5,6,7,8,9,10,11,12};

        MPI_Send(values, section, MPI_INT, 1, 10, MPI_COMM_WORLD);
        MPI_Send(values + section, section, MPI_INT, 2, 10, MPI_COMM_WORLD);
        MPI_Send(values + 2*section, section, MPI_INT, 3, 10, MPI_COMM_WORLD);
        MPI_Send(values + 3*section, section, MPI_INT, 4, 10, MPI_COMM_WORLD);

        int total = 0;
        for(int i=0; i<4; i++) {
            int value;
            MPI_Recv(&value, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, MPI_STATUSES_IGNORE);
            total += value;
        }
        printf("from %d rank total sum is: %d\n", rank, total);
    } else {
        MPI_Recv(&subArr, section, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, MPI_STATUSES_IGNORE);
        int sum = 0;
        for(int i=0; i<4; i++) {
            sum += subArr[i];
        }
        printf("from %d rank: %d is sum\n", rank, sum);
        MPI_Send(&sum, 1, MPI_INT, 0, 10, MPI_COMM_WORLD);
    }


    MPI_Finalize();
}
