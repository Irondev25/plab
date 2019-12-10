def bonAppetit(bill, k, b):
    count = 0
    for i in range(len(bill)):
        if(i != k):
            count += int(bill[i])
    pay = count//2
    if(pay != b):
        print(b-pay)
    else:
        print("Bon Appetit")


n = input("Enter number of Items")
k = input("Enter item of allergy")
bill = list()
for i in range(n):
    bill.append(input())
b = int(input("Enter bill"))
bonAppetit(bill, int(k), b)
