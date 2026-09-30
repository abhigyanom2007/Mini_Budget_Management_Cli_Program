import sys, math, time

def calc_bal(lst):
    print("\n Financial Summary ")
    ti = 0.0
    te = 0.0

    flag = True
    while flag == True:
        # for i in range(len(lst)):
        #     if lst[i] == "Income":
        
        for r in lst:
            if r["type"] == "Income":
                ti = ti + r["amount"]
            if r["type"] == "Expense":
                te = te + r["amount"]

        nb = ti - te

        # print("Net Balance: " + nb) 
        print(f"Total Income:  {ti}")
        print(f"Total Expense:  {te}")
        print(" ")
        print(f"Net Balance:  {nb}")
        
        flag = False
