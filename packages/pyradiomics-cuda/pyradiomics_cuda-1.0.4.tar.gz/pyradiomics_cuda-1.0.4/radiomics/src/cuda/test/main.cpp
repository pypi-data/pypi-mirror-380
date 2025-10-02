#include <assert.h>
#include <framework.h>
#include <async_stream.cuh>
#include <stdlib.h>

int main(const int argc, const char **argv) {
    /* Initialize stream to remove penalty in tests */
    [[maybe_unused]] const int result = AsyncInitStreamIfNeeded();
    assert(result == 0);

    ParseCLI(argc, argv);
    RunTests();
    FinalizeTesting();
    return EXIT_SUCCESS;
}
