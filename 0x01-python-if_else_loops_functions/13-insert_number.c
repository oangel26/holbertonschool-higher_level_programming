#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node: function that inserts a number into a sorted singly linked list.
 * @head: pointer to pointer to listint_t
 * @number: number to incert
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	/* Guard condition */
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	/* EDGE case no node */
	if (*head == NULL)
	{
		*head = new;
	}
	/* EDGE case only one node*/
	else if ((*head)->next == NULL)
	{
		if ((*head)->n > number)
		{
			new->next = *head;
			*head = new;
		}
	}
	else
	{
		/* EDGE case more than one node */
		while (current->next != NULL)
		{
			if (current->next->n > number)
				break;
			current = current->next;
		}
		/* EDGE case if insertion is in last node */
		if (current->next == NULL)
		{
			 current->next = new;
		}
		else
		{
		new->next = current->next;
		current->next = new;
		}
	}
	return (*head);
}
