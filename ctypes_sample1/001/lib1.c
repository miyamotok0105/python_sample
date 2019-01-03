#include <stdlib.h>

char *result;

char *reverse_bytes(int n, char *buf) {
  int i;

  /* サイズ決めてメモリ確保 */
  result = (char *)malloc(sizeof(char)*(n));
  for (i=0; i<n; i++) {
    /* ひっくり返して入れる */
    result[i] = buf[n-i-1];
  }
  return result;
}

void free_result(void) {
  /* メモリ解放 */
  free(result);
}
