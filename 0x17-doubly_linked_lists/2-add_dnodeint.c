#include "lists.h"
/**
 * add_dnodeint - adds a new node at the beginning of a dlistint_t list
 * @head: head pointer
 * @n: data
 * Return: new node pointer
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t * new = malloc(sizeof(dlistint_t));
	if (**head == NULL)
	{
		**head = new;
		return new
	}
	(*head)->prev = new;
	new->next = **head;
	**head = new;
	return 
}
