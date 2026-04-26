def fixed_deposit(principal, rate, time):
    principal_series = []
    amount_series = []
    inflation_adj = []
    tax_adj = []
    for i in range(0, time):
        if (i == 0):
            principal_series.append(principal)
        else:
            principal_series.append(amount_series[i-1])
        
        interest = principal_series[i] * rate
        amount = principal_series[i] + interest
        amount_series.append(amount)
        
        inflation_amount = amount_series[i] / (1 + inflation)
        inflation_adj.append(inflation_amount)
        
        tax_amount = inflation_adj[i] * tax
        amount = inflation_adj[i] - tax_amount
        tax_adj.append(amount)

    print(principal_series)
    print(amount_series)
    print(inflation_adj)
    print(tax_adj)

    return tax_adj[time - 1]

inflation = 0.05
tax = 0.1

amount1 = fixed_deposit(10000, 0.06, 5)
amount2 = fixed_deposit(20000, 0.07, 10)
amount3 = fixed_deposit(20000, 0.07, 3)

print(amount1, amount2, amount3)