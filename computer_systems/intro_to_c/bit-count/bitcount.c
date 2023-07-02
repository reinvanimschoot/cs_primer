#include <assert.h>
#include <stdio.h>

int bitcount(unsigned n)
{
    int c = 0;

    while (n)
    {
        n &= (n - 1);
        c++;
    }

    return c;
}

int main()
{
    assert(bitcount(0) == 0);
    assert(bitcount(1) == 1);
    assert(bitcount(3) == 2);
    assert(bitcount(8) == 1);
    // harder case:
    assert(bitcount(0xffffffff) == 32);
    printf("OK\n");
}
