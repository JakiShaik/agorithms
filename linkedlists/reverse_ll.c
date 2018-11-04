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
  
  struct node * reverse(struct node * curr){
    struct node * prev = NULL;
    struct node * next  = NULL;

    while(curr) {
      next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }
    return prev; 
    
  }

int main() {
  struct node * head = createLL();
  printLL(head);
  head = reverse(head);
  printf("################\n");
  printf("Reversing the linkedlist\n");
  printLL(head);

}