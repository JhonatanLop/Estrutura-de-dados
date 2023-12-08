#include <stdio.h>
#include <stdlib.h>

typedef struct doc{
  char nome;
  struct doc *next;
} doc;

typedef struct pilha{
  doc *document;
  int tamanho;
} pilha;

// cria pilha de documentos
void init_pilha_doc(pilha *p){
  doc *head = (doc *)malloc(sizeof(doc));
  head->next = NULL;
  p->document = head;
  p->tamanho = 0;
}

void push_doc(pilha *p, char valor) {
  doc *new_doc = (doc *)malloc(sizeof(doc));
  new_doc->nome = valor;
  new_doc->next = p->document;
  p->document = new_doc;
  p->tamanho++;
}

int remove_doc(pilha *p){
  if (p->tamanho > 0)
  {
    doc *lixo = p->document;
    p->document = p->document->next;
    printf("%c", lixo->nome);
    free(lixo);
  }
}

//printa a pilha
void print(pilha*p){
  doc *act = p->document;
  while (act->next != NULL)
  {
    printf("\n%c", act->nome);
    act = act->next;
  }
  printf("\n%c", act->nome);
}

int main(int argc, char const *argv[]){
  pilha *documents = (pilha *)malloc(sizeof(pilha));

  char doc1 = 'A';
  char doc2 = 'B';
  char doc3 = 'C';
  char doc4 = 'D';

  push_doc(documents, doc1);
  push_doc(documents, doc2);
  push_doc(documents, doc3);
  push_doc(documents, doc4);

  printf("\nprintado pilha:");
  print(documents);
  
  printf("\nremovendo documento:");
  remove_doc(documents);
  
  printf("\nprintado pilha:");
  print(documents);

  printf("\nadicionando documento:");
  char doc5 = 'E';
  push_doc(documents,doc5);
  
  printf("\nprintado pilha:");
  print(documents);
}
