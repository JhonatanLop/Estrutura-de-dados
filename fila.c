#include <stdio.h>
#include <stdlib.h>

// Estrutura principal
typedef struct cel
{
  int conteudo;
  struct cel *next;
} cel;

// Insere conteudo na fila
void fazer_pedido(int conteudo, cel **fim, cel **init)
{
  cel *new = (cel *)malloc(sizeof(cel));
  new->conteudo = conteudo;
  new->next = NULL;

  // Se estiver vazia
  if (*init == NULL)
  {
    *init = new;
    *fim = new;
  }
  else
  { // Se não estiver vazia
    (*fim)->next = new;
    *fim = new;
  }
}

// Remover e retornar o primeiro elemento da fila
int entregar_pedido(cel **init)
{
  if (init == NULL)
  {
    printf("Sem conteudos na fila\n");
    exit(1);
  }
  else
  {
    int command = (*init)->conteudo;
    cel *p = *init;
    *init = (*init)->next;
    free(p);
    return command;
  }
}

// Imprimir a fila
void PrintLista(cel *init)
{
  cel *p = init;
  while (p != NULL)
  {
    printf("<- | pedido %d | ", p->conteudo);
    p = p->next;
  }
  printf("\n");
}

// Liberar a memória
void LiberarLista(cel **init)
{
  while (*init != NULL)
  {
    cel *p = *init;
    *init = (*init)->next;
    free(p);
  }
}

// Função principal
int main(void)
{
  cel *init = NULL;
  cel *fim = NULL;

  fazer_pedido(1, &fim, &init);
  fazer_pedido(2, &fim, &init);
  fazer_pedido(3, &fim, &init);
  fazer_pedido(4, &fim, &init);
  fazer_pedido(5, &fim, &init);
  fazer_pedido(6, &fim, &init);
  fazer_pedido(7, &fim, &init);
  fazer_pedido(8, &fim, &init);
  fazer_pedido(9, &fim, &init);

  PrintLista(init);

  entregar_pedido(&init);
  entregar_pedido(&init);

  PrintLista(init);

  LiberarLista(&init);
  return 0;
}