#include "lists.h"

/**
 * @brief 
 * 
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *tmp;

	if (*head == NULL || head == NULL)
		return (NULL);

	ptr = *head;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);

	while (ptr->next != NULL)
	{
		if (ptr->n > number)
			break;
		tmp = ptr;
		ptr = ptr->next;
	}

	tmp->n = number;
	tmp->next= ptr 


}