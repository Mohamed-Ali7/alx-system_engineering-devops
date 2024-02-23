#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
/**
 * infinite_while - loops infinitely
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * Return: 0 on success and 0 on failure
*/

int main(void)
{
	pid_t  pid = 0;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0);
	}

	infinite_while();
	return (0);
}
