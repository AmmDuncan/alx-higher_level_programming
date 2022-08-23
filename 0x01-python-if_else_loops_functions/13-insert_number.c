#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert number into sorted linked list
 * @head: pointer to pointer to head of linked list
 * @number: number to insert into linked list
 * Return: pointer to newly added node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *cur;

	new = malloc(sizeof(listint_t));
	(*new).n = number;
	(*new).next = NULL;
	cur = *head;

	if (*head == NULL || head == NULL)
	{
		head = &new;
		return (new);
	}

	while (cur)
	{
		if (cur->next == NULL)
			if (cur->n < number)
			{
				(*cur).next = new;
				return (new);
			}
			else
			{
				(*new).next = cur;
				head = &new;
				return (new);
			}
		else if (cur->n >= number)
		{
			if (prev)
			{
				prev->next = new;
				new->next = cur;
				return (new);
			}
			else
			{
				(*new).next = *head;
				head = &new;
				return (new);
			}
		}
		prev = cur;
		cur = cur->next;
	}

	return (NULL);
}
