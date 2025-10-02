#ifndef IMPROVED_SHAPE_CUH
#define IMPROVED_SHAPE_CUH

#include "tables.cuh"
#include <cstddef>

static __global__ void ShapeKernelSharedMemory(
    const char *mask, const int *size, const int *strides,
    const double *spacing, double *surfaceArea, double *volume,
    double *vertices, unsigned long long *vertex_count, size_t max_vertices) {

    // Calculate global thread indices
    const int ix = blockIdx.x * blockDim.x + threadIdx.x;
    const int iy = blockIdx.y * blockDim.y + threadIdx.y;
    const int iz = blockIdx.z * blockDim.z + threadIdx.z;

    /* Load data to shared memory */
    __shared__ int8_t s_triTable[128][16];
    __shared__ double s_vertList[12][3];
    __shared__ int8_t s_gridAngles[8][3];

    const int tid = threadIdx.x + threadIdx.y * blockDim.x + threadIdx.z * blockDim.x * blockDim.y;
    const int blockSize = blockDim.x * blockDim.y * blockDim.z;

    // Load triTable (have threads load multiple elements)
    for (int i = tid; i < 128*16; i += blockSize) {
        const int row = i / 16;
        const int col = i % 16;
        s_triTable[row][col] = d_triTable[row][col];
    }

    // Load vertList
    for (int i = tid; i < 12*kVertexPosSize3D; i += blockSize) {
        const int row = i / kVertexPosSize3D;
        const int col = i % kVertexPosSize3D;
        s_vertList[row][col] = d_vertList[row][col];
    }

    // Load gridAngles
    for (int i = tid; i < 8*kVertexPosSize3D; i += blockSize) {
        const int row = i / kVertexPosSize3D;
        const int col = i % kVertexPosSize3D;
        s_gridAngles[row][col] = d_gridAngles[row][col];
    }

    __syncthreads();

    // Bounds check: Ensure the indices are within the valid range for cube
    // origins
    if (iz >= size[0] - 1 || iy >= size[1] - 1 || ix >= size[2] - 1) {
        return;
    }

    // --- Calculate Cube Index ---
    unsigned char cube_idx = 0;
    for (int a_idx = 0; a_idx < 8; a_idx+=2) {
        // Calculate the linear index for each corner of the cube
        const int corner_idx_1 = (iz + s_gridAngles[a_idx][0]) * strides[0] +
                         (iy + s_gridAngles[a_idx][1]) * strides[1] +
                         (ix + s_gridAngles[a_idx][2]) * strides[2];

        const int corner_idx_2 = (iz + s_gridAngles[a_idx + 1][0]) * strides[0] +
                         (iy + s_gridAngles[a_idx + 1][1]) * strides[1] +
                         (ix + s_gridAngles[a_idx + 1][2]) * strides[2];

        cube_idx |= (1 << a_idx) * (mask[corner_idx_1] != 0);
        cube_idx |= (1 << (a_idx + 1)) * (mask[corner_idx_2] != 0);
    }

    // --- Symmetry Optimization & Skipping ---
    int sign_correction = 1;
    if (cube_idx & 0x80) {
        // If the 8th bit (corresponding to point p7) is set
        cube_idx ^= 0xff; // Flip all bits
        sign_correction = -1; // Correct sign for volume calculation
    }

    // Skip cubes entirely inside or outside (index 0 after potential flip)
    if (cube_idx == 0) {
        return;
    }

    // --- Store Vertices for Diameter Calculation ---
    // Store vertices on edges 6, 7, 11 if the corresponding points (bits 6, 4, 3)
    // are set in the *potentially flipped* cube_idx, matching the C code logic.
    const int num_new_vertices =
        ((cube_idx & (1 << 6)) != 0) +
        ((cube_idx & (1 << 4)) != 0) +
        ((cube_idx & (1 << 3)) != 0);

    if (num_new_vertices > 0) {
        unsigned long long start_v_idx =
                atomicAdd(vertex_count, (unsigned long long) num_new_vertices);

        if (start_v_idx + num_new_vertices >= max_vertices) {
            // If overflow occurs, the vertex_count will exceed max_vertices, handled in
            // host code.

            return;
        }

        double* p_table = vertices + start_v_idx * kVertexPosSize3D;

        // Check bit 6 (original point p6, edge 6) using potentially flipped cube_idx
        if (cube_idx & (1 << 6)) {
            static constexpr int kEdgeIdx = 6;

            p_table[0] = (((double) iz) + s_vertList[kEdgeIdx][0]) * spacing[0];
            p_table[1] = (((double) iy) + s_vertList[kEdgeIdx][1]) * spacing[1];
            p_table[2] = (((double) ix) + s_vertList[kEdgeIdx][2]) * spacing[2];

            p_table += 3;
        }

        // Check bit 4 (original point p4, edge 7) using potentially flipped cube_idx
        if (cube_idx & (1 << 4)) {
            static constexpr int kEdgeIdx = 7;

            p_table[0] = (((double) iz) + s_vertList[kEdgeIdx][0]) * spacing[0];
            p_table[1] = (((double) iy) + s_vertList[kEdgeIdx][1]) * spacing[1];
            p_table[2] = (((double) ix) + s_vertList[kEdgeIdx][2]) * spacing[2];

            p_table += 3;
        }

        // Check bit 3 (original point p3, edge 11) using potentially flipped cube_idx
        if (cube_idx & (1 << 3)) {
            static constexpr int kEdgeidx = 11;

            p_table[0] = (((double) iz) + s_vertList[kEdgeidx][0]) * spacing[0];
            p_table[1] = (((double) iy) + s_vertList[kEdgeidx][1]) * spacing[1];
            p_table[2] = (((double) ix) + s_vertList[kEdgeidx][2]) * spacing[2];
        }

    }

    // --- Process Triangles for Surface Area and Volume ---
    double local_SA = 0;
    double local_Vol = 0;

    int t = 0;
    // Iterate through triangles defined in d_triTable for the current cube_idx
    while (s_triTable[cube_idx][t * kVertexPosSize3D] >= 0) {
        double p1[kVertexPosSize3D], p2[kVertexPosSize3D], p3[kVertexPosSize3D]; // Triangle vertex coordinates
        double v1[kVertexPosSize3D], v2[kVertexPosSize3D], cross[kVertexPosSize3D]; // Vectors for calculations

        // Get vertex indices from the table
        int v_idx_1 = s_triTable[cube_idx][t * kVertexPosSize3D];
        int v_idx_2 = s_triTable[cube_idx][t * kVertexPosSize3D + 1];
        int v_idx_3 = s_triTable[cube_idx][t * kVertexPosSize3D + 2];

        // Calculate absolute coordinates for each vertex
        for (int d = 0; d < kVertexPosSize3D; ++d) {
            p1[d] = (((double) (d == 0 ? iz : (d == 1 ? iy : ix))) +
                     s_vertList[v_idx_1][d]) *
                    spacing[d];
            p2[d] = (((double) (d == 0 ? iz : (d == 1 ? iy : ix))) +
                     s_vertList[v_idx_2][d]) *
                    spacing[d];
            p3[d] = (((double) (d == 0 ? iz : (d == 1 ? iy : ix))) +
                     s_vertList[v_idx_3][d]) *
                    spacing[d];
        }

        // Volume contribution: (p1 x p2) . p3 (adjust sign later)
        cross[0] = (p1[1] * p2[2]) - (p2[1] * p1[2]);
        cross[1] = (p1[2] * p2[0]) - (p2[2] * p1[0]);
        cross[2] = (p1[0] * p2[1]) - (p2[0] * p1[1]);
        local_Vol += cross[0] * p3[0] + cross[1] * p3[1] + cross[2] * p3[2];

        // Surface Area contribution: 0.5 * |(p2-p1) x (p3-p1)|
        for (int d = 0; d < kVertexPosSize3D; ++d) {
            v1[d] = p2[d] - p1[d]; // Vector from p1 to p2
            v2[d] = p3[d] - p1[d]; // Vector from p1 to p3
        }

        cross[0] = (v1[1] * v2[2]) - (v2[1] * v1[2]);
        cross[1] = (v1[2] * v2[0]) - (v2[2] * v1[0]);
        cross[2] = (v1[0] * v2[1]) - (v2[0] * v1[1]);

        double mag_sq =
                cross[0] * cross[0] + cross[1] * cross[1] + cross[2] * cross[2];
        local_SA += 0.5 * sqrt(mag_sq); // Add area of this triangle

        t++; // Move to the next triangle for this cube
    }

    // Atomically add the calculated contributions for this cube to the global
    // totals
    atomicAdd(surfaceArea, local_SA);
    atomicAdd(volume,
              sign_correction * local_Vol); // Apply sign correction for volume
}

#endif //IMPROVED_SHAPE_CUH
