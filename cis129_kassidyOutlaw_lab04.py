# module 4 lab 4
# Kassidy Outlaw
# 02/25/2025
# Modifies a company's store bonuses to have a tier-system of bonus values while including an individual employee bonus

# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percentage of sales increase

# this code gets the monthly sales amount
monthlySales = int(input('What were your monthly sales?'))
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0
# this code gets the percentage of increase in sales
salesIncrease = float(input('What was your percentage increase in monthly sales?'))
salesIncrease = salesIncrease / 100
# this code determines the employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0
# this code prints the bonus information
print('The store bonus amount is:', storeAmount)
print('The employee bonus amount is:', empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congratulations! You have reached the highest bonus amounts possible!')

