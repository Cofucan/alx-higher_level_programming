#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: Pointer to the first node.
 * @number: Number to be inserted.
 *
 * Return: Pointer to new node, or NULL if it fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	/* If list is empty or num to be inserted is less than the first number */
	if (*head == NULL || curr->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* If number to be inserted is within the range of the list */
	while (curr->next)
	{
		if (curr->n <= number && curr->next->n >= number)
		{
			new_node->next = curr->next;
			curr->next = new_node;
			return (new_node);
		}
		curr = curr->next;
	}

	/* If number to be inserted is greater than the last number */
	if (!curr->next)
	{
		new_node->next = curr->next;
		curr->next = new_node;
	}

	return (new_node);
}
