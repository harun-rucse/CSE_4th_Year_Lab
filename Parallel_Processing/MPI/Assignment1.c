#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int num_procs, rank;
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    MPI_Get_processor_name(processor_name, &name_len);

    printf("I'm from processor %s, rank %d out of %d process\n", processor_name, rank, num_procs);

    MPI_Finalize();
}