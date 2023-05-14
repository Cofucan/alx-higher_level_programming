#include "lists.h"

/**
 * is_palindrome - checks if a singly-linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if its not a palindrome or 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	int x, left_idx, right_idx, list_len = 0;
	int *numbers;
	listint_t *curr = *head;

	/* If list is empty or has only one node */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (curr->next)
	{ /* Get the length of the list */
		list_len++;
		curr = curr->next;
	}

	/* Allocate an array to store the integers from the lists' nodes */
	numbers = malloc(sizeof(int) * list_len);
	if (!numbers)
		return (0);

	/* Copy over the integers from each node into the new array */
	curr = *head;
	for (x = 0; x < list_len; x++, curr = curr->next)
		numbers[x] = curr->n;

	if (list_len > 1 && (list_len & 1) == 0)
	{ /* If there are more than 1 (even number) nodes in the list */
		right_idx = list_len / 2;
		left_idx = right_idx - 1;
	}
	else if (list_len > 1 && (list_len & 1) == 1)
	{ /* If there are more than 1 (odd number) nodes in the list */
		right_idx = (list_len / 2) + 1;
		left_idx = (list_len / 2) - 1;
	}
	for ( ; left_idx >= 0; left_idx--, right_idx++)
		if (numbers[left_idx] != numbers[right_idx])
			return (0);

	free(numbers);
	return (1);
}
