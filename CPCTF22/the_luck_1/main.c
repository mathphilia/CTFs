#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  srand(time(NULL));
  int result = rand();
  int predict;
  printf("Please predict the result: ");
  scanf("%d", &predict);
  if (predict == result) {
    printf("Good luck!\n");
    printf("%s\n", getenv("FLAG"));
  } else {
    printf("You are wrong!\n");
    printf("The result is %d!\n", result);
  }
  printf("good bye...\n");
}
