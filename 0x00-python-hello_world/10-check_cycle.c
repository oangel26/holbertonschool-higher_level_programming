#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if linked list is a cycle
 * @list: pointer to list
 * Return: Always 0.
 */
int check_cycle(listint_t *list);
{
	listint_t *head = list;
	listint_t *tmp = list;

	while (tmp->next != NULL)
	{
		if (list->next != NULL)
		{
			
		list = list->next;
