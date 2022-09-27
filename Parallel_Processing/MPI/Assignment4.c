#include<stdio.h>
#include<mpi.h>

int main(int argc, char **argv) {
    int rank, a, b;

    a = 5;
    b = 2;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        printf("Sum(a,b) = %d\n", a+b);
    } else if (rank == 1) {
        printf("Subtraction(a,b) = %d\n", a-b);
    } else if (rank == 2) {
        printf("Multiply(a,b) = %d\n", a*b);
    } else if(rank == 3) {
        printf("Division(a,b) = %.2f\n", (double) a/b);
    }

    MPI_Finalize();
}