#include "test.cuh"
#include "square_launcher.cuh"

// ------------------------------
// CUDA Kernels
// ------------------------------

#include "shape/soa_shape.cuh"
#include "volumetry/reduced_reads.cuh"

// ------------------------------
// Host wrapper
// ------------------------------

SOLUTION_DECL(8) {
    return CUDA_SQUARE_LAUNCH_SOLUTION(
        ShapeKernelSharedMemorySoa,
        VolumetryKernelSoaMatrixBasedFullAtomics
    );
}
