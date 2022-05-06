#include "lists.h"

/**
 * check_cycle - check if a list is cycle
 * @list: pointer to head of list
 * Return: 1 if is cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	fast = list->next;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
