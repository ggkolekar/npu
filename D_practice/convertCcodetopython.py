#include <stdio.h>
int main(void) {
float sum; # Sum of 12 rainfall amounts */
char response; # User response ('y' or 'n') */
float amount; # Rainfall amount for each month */
int count; # Loop control variable */
do {
#Input 12 monthly rainfall amounts. Verifying that each is nonnegative, and calculates the sum.*/
sum = 0;
for (count = 1; count <= 12; count++) :
print("Enter rainfall amount %d:", count);
# Inputs one month's rainfall amount. */
do {
scanf("%f", &amount);
if (amount < 0.0f)
printf("Amount cannot be negative. Enter again: ");
} while (amount < 0.0f);
sum = sum + amount;
}
printf("\n");
printf("Average rainfall is %7.2f inches\n", sum / 12);
printf("Do you have another recording site? (y or n): ");
# Inputs a character from the user and, if necessary, repeatedly prints an error message and inputs another
#character if the character isn't 'y' or 'n'.
#
do
{
scanf(" %c", &response);
if (response != 'y' && response != 'n')
print("Please try y or n: ");
} while (response != 'y' && response != 'n');
} while (response == 'y');
return 0;
}