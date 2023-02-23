#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int =8234
#Print the number of even digits in the variable "var_int".
a1 = var_int%10 #4
var_int = var_int//10 #123
a2 = var_int%10 #3
var_int = var_int//10 #12
a3 = var_int%10 #2
a4 = var_int//10 #1
a1 = (a1+3)%2
a2 = (a2+3)%2
a3 = (a3+3)%2
a4 = (a4+3)%2
print(a1+a2+a3+a4)