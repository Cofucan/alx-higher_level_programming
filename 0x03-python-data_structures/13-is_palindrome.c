#include "lists.h"

int get_list_len(listint_t **head);

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
	long long int left_sum = 0, right_sum = 0;
	listint_t *curr = *head;

	/* If list is empty or has only one node */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	list_len = get_list_len(head);

	/* Allocate an array to store the integers from the lists' nodes */
	numbers = malloc(sizeof(int) * list_len);
	if (!numbers)
		return (0);

	if ((list_len & 1) == 0)
	{ /* If there's an even number of nodes int the list */
		right_idx = list_len / 2;
		left_idx = right_idx - 1;
	}
	else if ((list_len & 1) == 1)
	{ /* If there's an odd number of nodes in the list */
		right_idx = (list_len / 2) + 1;
		left_idx = (list_len / 2) - 1;
	}

	/* Copy over the integers from each node into the new array */
	curr = *head;
	for (x = 0; x < list_len; x++, curr = curr->next)
	{
		numbers[x] = curr->n;
		if (x <= left_idx)
			left_sum += numbers[x];
		else if (x >= right_idx)
			right_sum += numbers[x];
	}

	if (left_sum != right_sum)
		return (0);

	for ( ; left_idx >= 0; left_idx--, right_idx++)
		if (numbers[left_idx] != numbers[right_idx])
		{
			free(numbers);
			return (0);
		}

	free(numbers);
	return (1);
}

/**
 * get_list_len - returns the length of a linked list
 * @head: pointer to head of list
 *
 * Return: Integer, the length of the list.
 */

int get_list_len(listint_t **head)
{
	listint_t *curr = *head;
	int list_len = 1;

	while (curr->next)
	{ /* Get the length of the list */
		list_len++;
		curr = curr->next;
	}

	return (list_len);
}
