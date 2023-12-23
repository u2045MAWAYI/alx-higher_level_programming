#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is no cycle, 0 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
