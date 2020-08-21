import random

n = input("How long do you want your password to be?\n")

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!?.@#$%^&<>`~;:'_[]{}()-+*/="

password = "".join(random.sample(
	lower_case + upper_case + numbers + symbols, n
	))

print(password)
