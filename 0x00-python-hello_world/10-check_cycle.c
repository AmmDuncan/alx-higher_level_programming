#include "lists.h"

/**
 * check_cycle - check if linked list is a cycle
 * @list: pointer to head of list
 * Return: 1 if is cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return (1);

		fast = fast->next;
		if (fast != NULL)
			fast = fast->next;
		slow = slow->next;
	}

	return (0);
}
