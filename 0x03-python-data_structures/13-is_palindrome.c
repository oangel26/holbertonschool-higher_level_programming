#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *runner;
	int list_l = 0;
	int i, j;

	runner = *head;
	current = *head;

	if (*head == NULL)
		return (1);

	while (runner->next != NULL)
	{
		list_l++;
		runner = runner->next;
	}
	list_l++;
	printf("list_l = %d\n", list_l);
	if (list_l % 2 == 0)
	{
		for (i = 0; i < list_l / 2; i++)
		{
			runner = current;
			for (j = i; j < list_l - i -1; j++)
			{
				runner = runner->next;
			}
			if (current->n != runner->n)
			{
				return (0);
			}
			current = current->next;
		}
	}
	else if (list_l % 3 == 0)
	{
		for (i = 0; i < (list_l - 1) / 2; i++)
		{
			runner = current;
			for (j = i; j < list_l - i - 1; j++)
			{
				runner = runner->next;
			}
			if (current->n != runner->n)
			{
				return (0);
			}
			current = current->next;
		}
	}
	return (1);
}
