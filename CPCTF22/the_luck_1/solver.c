#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    long now;
    scanf("%ld", &now);
    srand(now);
    int result = rand();
    int predict;
    printf("%d", result);
} 
