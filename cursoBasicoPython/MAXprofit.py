

data = [-30, 9, 1, 8, -5, 6, -24]
rango = []

def maxprofit(data):
    profit = 0
    maxSuma = 0
    for x in range(len(data)):
        profitn = profit
        profit += data[x]
        
        print(profit)

        if profit > maxSuma:
            maxSuma = profit
            rango.append(x)
        elif profit < 0 and profit>profitn:
            maxSuma = profit
            rango.append(x)
            
    print(rango)
    # return [(rango[0]), (rango[len(rango)-1])]
    



print(maxprofit(data))


            

        

