#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Problem {
  char name;
  int right;
  int time;
  int n_wrong;
  int penalty;
} typedef prob;

void create_new_problem(prob *new_problem, char name) {
  new_problem->name = name;
  new_problem->right = 0;
  new_problem->time = 0;
  new_problem->n_wrong = 0;
  new_problem->penalty = 0;
}

int main() {
  int n = 0, time;
  prob *plist = NULL;
  int total_penalty = 0;
  int n_right = 0;

  while (1) {
    scanf("%d", &time);
    getchar();
    if (time == -1)
      break;

    int isexist = 0;
    char name;
    char state[6];
    scanf("%c %s", &name, state);
    getchar();

    prob *current_log = NULL;

    for (int i = 0; i < n; i++) {
      if (plist[i].name == name) {
        isexist = 1;
        current_log = plist + i;
        break;
      }
    }

    if (isexist == 0) {
      plist = (prob *)realloc(plist, sizeof(prob) * (n + 1));
      create_new_problem(plist + n, name);
      current_log = plist + n;
      n++;
    }

    if (strcmp(state, "right") == 0) {
      current_log->right = 1;
      current_log->time = time;
      current_log->penalty = current_log->n_wrong * 20 + current_log->time;
    } else {
      current_log->n_wrong++;
    }
  }
  
  for (int i = 0; i < n; i++) {
    if ((plist + i)->right == 1) {
      total_penalty += (plist + i)->penalty;
      n_right++;
    }
  }
  printf("%d %d", n_right, total_penalty);

  return 0;
}