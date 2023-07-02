#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define ALPHABET_MASK 0x3ffffff

bool ispangram(char *s)
{
  int alphabet = 0;

  char c;

  while (*s)
  {
    c = tolower(*s);

    if (isalpha(c))
      alphabet |= (1 << (c - 'a'));

    s++;
  }

  return alphabet == ALPHABET_MASK;
}

int main()
{
  size_t len;
  ssize_t read;
  char *line = NULL;
  while ((read = getline(&line, &len, stdin)) != -1)
  {
    if (ispangram(line))
      printf("%s", line);
  }

  if (ferror(stdin))
    fprintf(stderr, "Error reading from stdin");

  free(line);
  fprintf(stderr, "ok\n");
}
