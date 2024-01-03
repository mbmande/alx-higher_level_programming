#include "lists.h"

/**
 * check_cycle - it checks for cicle
 * @list: the lists
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *ft, *sw;

	if (!list || !list->next)
		return (0);

	ft = list;
	sw = list;

	while (sw != NULL && ft != NULL && ft->next != NULL)
	{
		sw = sw->next;
		ft = ft->next->next;

		if (sw == ft)
			return (1);
	}
	return (0);

}
