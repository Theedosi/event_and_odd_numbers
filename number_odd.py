#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 2468
#Print the number of odd digits in the variable "var_int".
a1 = var_int%10
var_int = var_int//10
a2 = var_int%10
var_int = var_int//10
a3 = var_int%10
a4 = var_int//10
a1 = (a1+2)%2
a2 = (a2+2)%2
a3 = (a3+2)%2
a4 = (a4+2)%2
print(a1+a2+a3+a4)