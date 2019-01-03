#include <stdlib.h>
#include <wchar.h>

wchar_t *result;

wchar_t *reverse_str(int n, wchar_t *buf) {
  int i;

  result = (wchar_t *)malloc(sizeof(wchar_t)*(n+1));
  for (i=0; i<n; i++) {
    result[i] = buf[n-i-1];
  }
  result[n] = L'\0';
  return result;
}

void free_result(void) {
  free(result);
}
