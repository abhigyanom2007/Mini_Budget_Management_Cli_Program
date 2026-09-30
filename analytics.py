def cb(d):
    print("\n Financial Summary ")

    # ti = 0
    inc = []
    exp = []

    i = 0
    k = True
    while k:
        if i == len(d):
            k = False
        else:
            r = d[i]
            if r["type"] == "Income":
                inc.append(r["amount"])
            if r["type"] == "Expense":
                exp.append(r["amount"])
            i = i + 1

    # sum incomes
    ti = 0.0
    x = 0
    f1 = True
    while f1:
        if x == len(inc):
            f1 = False
        else:
            ti = ti + inc[x]
            x = x + 1

    # sum expenses
    te = 0.0
    y = 0
    f2 = True
    while f2:
        if y == len(exp):
            f2 = False
        else:
            te = te + exp[y]
            y = y + 1

    nb = ti - te

    # print(ti)
    print("Total Income:  " + str(ti))
    print("Total Expense:  " + str(te))
    print(" ")
    print("Net Balance:  " + str(nb))
