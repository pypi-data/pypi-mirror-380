#include "test.cuh"

#include <cstdlib>
#include <cinttypes>

ShapeFunc g_ShapeFunctions[kMaxSolutionFunctions]{};
const char *g_ShapeFunctionNames[kMaxSolutionFunctions]{};

int AddShapeFunction(const std::size_t idx, const ShapeFunc func, const char *name) {
  if (idx >= kMaxSolutionFunctions) {
    std::exit(EXIT_FAILURE);
  }

  if (g_ShapeFunctions[idx] != nullptr) {
    std::exit(EXIT_FAILURE);
  }

  if (func == NULL) {
    std::exit(EXIT_FAILURE);
  }

  g_ShapeFunctions[idx] = func;
  g_ShapeFunctionNames[idx] = name ? name : "Unknown function name";

  return static_cast<int>(idx);
}

__global__ void polluteCaches(float *buffer, const std::size_t bufferSize) {
  const int tid = blockIdx.x * blockDim.x + threadIdx.x;
  const int stride = blockDim.x * gridDim.x;

  const int prime1 = 31;
  const int prime2 = 67;

  float sum = 0.0f;
  for (std::size_t i = tid; i < bufferSize; i += stride) {
    const std::size_t idx1 = (i * prime1) % bufferSize;
    const std::size_t idx2 = (i * prime2) % bufferSize;

    // Read-modify-write to ensure memory operations aren't optimized away
    sum += buffer[idx1];
    buffer[idx2] = sum;

    const std::size_t idx3 = (bufferSize - 1 - i) % bufferSize;
    sum += buffer[idx3];
  }

  if (sum == 0.0f) {
    buffer[tid % bufferSize] = sum;
  }
}

void CleanGPUCache() {
  const std::size_t bufferSize = 256 * 1024 * 1024 / sizeof(float);
  float *d_buffer;
  cudaMalloc(&d_buffer, bufferSize * sizeof(float));

  cudaMemset(d_buffer, 0, bufferSize * sizeof(float));

  int blockSize = 256;
  int gridSize = min(1024, (int)((bufferSize + blockSize - 1) / blockSize));

  polluteCaches<<<gridSize, blockSize>>>(d_buffer, bufferSize);
  cudaDeviceSynchronize();
  cudaFree(d_buffer);
}

SOLUTION_DECL(0);
SOLUTION_DECL(1);
SOLUTION_DECL(2);
SOLUTION_DECL(3);
SOLUTION_DECL(4);
SOLUTION_DECL(5);
SOLUTION_DECL(6);
SOLUTION_DECL(7);
SOLUTION_DECL(8);
SOLUTION_DECL(9);

void RegisterSolutions() {
  REGISTER_SOLUTION(0, "Basic implementation");
  REGISTER_SOLUTION(1, "Improved atomics");
  REGISTER_SOLUTION(2, "Added async data copy");
  REGISTER_SOLUTION(3, "Added simple shared memory");
  REGISTER_SOLUTION(4, "Less work for diameters");
  REGISTER_SOLUTION(5, "SOA implementation");
  REGISTER_SOLUTION(6, "SOA reduced atomics");
  REGISTER_SOLUTION(7, "Reduced memory reads");
  REGISTER_SOLUTION(8, "Reduced memory reads with no atomics");
  REGISTER_SOLUTION(9, "Reduced memory reads - single dim");
}
