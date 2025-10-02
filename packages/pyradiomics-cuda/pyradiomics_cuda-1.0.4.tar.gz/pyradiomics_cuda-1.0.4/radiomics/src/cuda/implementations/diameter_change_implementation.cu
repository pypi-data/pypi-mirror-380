#include "test.cuh"
#include "basic_launcher.cuh"

// ------------------------------
// CUDA Kernels
// ------------------------------

#include "shape/basic_implementation.cuh"
#include "volumetry/improved_atomic_implementation.cuh"

// ------------------------------
// Host wrapper
// ------------------------------

SOLUTION_DECL(1) {
    return CUDA_BASIC_LAUNCH_SOLUTION(
        ShapeKernelBasic,
        VolumetryKernelLocalAccumulatorWithAtomicFinal
    );
}
