balance = 50000
withdraw = int(input("Enter amount: "))

if withdraw < 100:
    print("Minimum withdrawal is ₹100")

elif withdraw % 100 != 0:
    print("Amount should be multiple of 100")

elif withdraw > balance:
    print("Insufficient Balance")

else:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
