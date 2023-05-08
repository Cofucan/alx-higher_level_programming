#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list has a cycle.
 * @list: linked list to be checked.
 *
 * Return: 0 if no cycle or 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* Check if list is null or contains only 1 node */
	if (!list || !list->next)
		return (0);

	while (slow->next && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
