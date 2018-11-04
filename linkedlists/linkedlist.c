#include<stdio.h>
#include<stdlib.h>


struct node {
  int data;
  struct node * next;
};

  void addValue(struct node * ptr,int i) {
    
    printf("Enter the data for the node-%d\n",i);
    scanf("%d",&ptr->data);
    ptr->next = NULL;
  }


  struct node * createLL() {
    int i,size;
    struct node * start = NULL;
    struct node * head = start;
    printf("Enter the size of the linked list\n");
    scanf("%d",&size);
    for(i=0;i<size;i++){
      if (i == 0) {
	head = start = (struct node *) malloc(sizeof(struct node)); 
	addValue(start,i);
      }
      else{
	start->next = (struct node *)malloc(sizeof(struct node));
	addValue(start->next,i);
	start = start->next;
      }
    }
    return head;
    
  }

void printLL(struct node * head) {
  while (head) {
    printf("Node Data is %d\n",head->data);
    head = head->next;
  }
}
struct node * insertNode_start(struct node* head, int data) {
  struct node * new =(struct node *) malloc(sizeof(struct node *));
  new->data = data;
  new->next = head;
  head = new;
  return head;
}

void insertMiddle(struct node * head,int afterVal,int newVal) {
  struct node * new = (struct node *) malloc(sizeof(struct node *));
  new->data = newVal;
  //struct node * temp = (struct node *) malloc(sizeof(struct node *));
  while (head->data != afterVal) {
    head = head->next;
  }
  //temp = head;
  new->next = head->next;
  head->next = new;
}

void insertend(struct node * head,int data) {
  struct node * new = (struct node *) malloc(sizeof(struct node *));
  //memset(new,'\0',sizeof(new));
  new->data = data;
  while (head->next != NULL) {
    head = head->next;
  }
  head->next = new;
  
}

void print_recur(struct node* head)  {
  if (head) {
    printf("%d\n",head->data);
    head = head->next;
    return print_recur(head);
  }
  return;
}

int main() {
  struct node * head = createLL();
  printLL(head);
  if (head) {
    printf("Checking if the head is still at it's original location\n");
    printf("%d\n",head->data);
  }
  int value = 0;
  printf("Insert a node at the beginning\n");
  scanf("%d",&value);
  head = insertNode_start(head,value);
  printLL(head);
  printf("Insert node at the end\n");
  scanf("%d",&value);
  insertend(head,value);
  print_recur(head);
  //printf("######");
  int after = 0;
  printf("Insert a node after some node\n");
  scanf("%d",&after);
  printf("The value to insert after this node\n");
  scanf("%d",&value);
  insertMiddle(head,after,value);
  print_recur(head);
}
