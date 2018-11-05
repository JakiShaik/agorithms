#include<stdio.h>
#include<stdlib.h>

struct node {
  int data;
  struct node * prev;
  struct node * next;
};

void addValue(struct node * ptr,int i) {
    
  printf("Enter the data for the node-%d\n",i);
  scanf("%d",&ptr->data);
  ptr->next = NULL;
  ptr->prev = NULL;
}

struct node * createLL(){
  struct node * start = NULL;
  struct node * head = start;
  struct node * temp = NULL;
  int size;
  printf("Please enter the size of the list \n");
  scanf("%d",&size);
  
  for(int i=0;i<size;i++) {
    if (i==0) {
      head = start = (struct node *) malloc(sizeof(struct node ));
      addValue(start,i);
    }
    else {
      start->next = (struct node *) malloc(sizeof(struct node));
      addValue(start->next,i);
      start->next->prev = start;
      start = start->next;
    }

  }
  return head;

}
void printLL(struct node * head) {
  printf("Original order is \n");
  while (head->next) {
    //printf("Original oreder is \n");
    printf("Node Data is %d\n",head->data);
    head = head->next;
  }
  printf();
  printf("Reverse order is \n");
  while(head) {
    //printf("Reverse order is\n");
    printf("Node Data is %d\n",head->data);
    head = head->prev;
  }
}

//struct node * insertAtBegin(data) {

  

//}

int main(){
  struct node * head = createLL();
  printLL(head);
  
}
