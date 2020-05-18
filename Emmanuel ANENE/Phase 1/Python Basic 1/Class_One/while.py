# Continues to ask for user input until the user types 'bananas'
print("Heres a list of significant numbers...")
msg = input("but first whats the secret password? ")
while msg != "P.A.S.S.W.O.R.D":
	print("WRONG!")
	msg = input("whats the secret password? ")
print("CORRECT!")


# for num in range(1,11):
# 	print(num)

# equivalent of above for loop
num = 1
while num < 11:
	print(num)
	num += 1
