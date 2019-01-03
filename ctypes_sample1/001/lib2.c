#include <stdlib.h>

char *result;

char *reverse_bytes(int n, char *buf) {
  int i;

  result = (char *)malloc(sizeof(char)*(n+1));
  for (i=0; i<n; i++) {
    result[i] = buf[n-i-1];
  }
  result[n] = '\0';
  return result;
}

void free_result(void) {
  free(result);
}
