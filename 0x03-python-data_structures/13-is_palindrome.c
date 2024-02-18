#include <stdio.h>
#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_t {
    int data;
    struct listint_t* next;
} listint_t;

/* Function to reverse a linked list */
listint_t* reverseLinkedList(listint_t* head) {
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) // Empty list or single element list
        return 1;

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = NULL;
    listint_t *mid_node = NULL;
    int is_palindrome = 1; // Assume palindrome initially

    // Move fast pointer to the end and slow pointer to the middle
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // If the length of the list is odd, move slow pointer one step forward
    if (fast != NULL) {
        mid_node = slow;
        slow = slow->next;
    }

    prev_slow->next = NULL; // Break the list into two halves

    listint_t *second_half_reversed = reverseLinkedList(slow);

    listint_t *temp1 = *head;
    listint_t *temp2 = second_half_reversed;

    // Compare both halves
    while (temp1 != NULL && temp2 != NULL) {
        if (temp1->data != temp2->data) {
            is_palindrome = 0;
            break;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    // Reconstruct the original list
    prev_slow->next = reverseLinkedList(second_half_reversed);

    // If the length of the list is odd, link the mid node back to the list
    if (mid_node != NULL) {
        prev_slow->next = mid_node;
        mid_node->next = slow;
    }

    return is_palindrome;
}

/* Utility function to create a new node */
listint_t* newNode(int data) {
    listint_t* node = (listint_t*)malloc(sizeof(listint_t));
    node->data = data;
    node->next = NULL;
    return node;
}

/* Utility function to print the linked list */
void printList(listint_t* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    listint_t* head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(2);
    head->next->next->next->next = newNode(1);

    printf("Original linked list: ");
    printList(head);

    if (is_palindrome(&head))
        printf("The linked list is a palindrome.\n");
    else
        printf("The linked list is not a palindrome.\n");

    return 0;
}
