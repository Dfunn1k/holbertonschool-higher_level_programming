#include "lists.h"
#include <stdlib.h>

/**
 * @brief 
 * 
 * @param head 
 * @return int 
 */
size_t listint_len(const listint_t *h)
{
	if (h == NULL)
		return (0);

	return (1 + listint_len(h->next))

}

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int count = 1;

	if (*head == NULL)
		return (1);

	ptr = *head;
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	return (count);
}