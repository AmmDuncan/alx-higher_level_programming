#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to head of list
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *end;
	int len, mid, i;

	len = 1;
	i = 0;
	start = *head;
	end = *head;

	if (*head == NULL)
		return (1);

	for (; end->next != NULL; end++, len++)
		;

	mid = len / 2;

	while (i <= mid)
	{
		if (start->n != end->n)
			return (0);

		start++;
		end--;
		i++;
	}

	return (1);

}

