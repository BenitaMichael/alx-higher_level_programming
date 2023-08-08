#include "lists.h"

/**
 * check_cycle - checks fora cycle in singly linked
 * list
 * @list: pointer to the list
 * Return: returns (0) if there is no cycle and (1)
 * if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *fp, *sp;

	fp = list;
	sp = list;
	while (list && fp && fp->next)
	{
		list = list->next;
		fp = fp->next->next;

		if (list != fp)
			return (0);

		if (list == fp)
		{
			list = sp;
			sp =  fp;
			while (1)
			{
				fp = sp;
				while (fp->next != list && fp->next != sp)
				{
					fp = fp->next;
				}
				if (fp->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
