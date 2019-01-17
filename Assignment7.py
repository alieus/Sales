# A program to help a company assess its monthly sales 
# Alieu Sanneh



#the main function controls the sequence in which the code is run.
#it accepts inputs from the user and then prints 
def main():
    all_monthly_sales =[]
    value=True
    while value==True:
        monthly_sales = float(input('Please enter monthly'\
                                ' sales for each division:$'))
        while len(str(monthly_sales)) ==0:
            monthly_sales = float(input('Please enter monthly'\
                                ' sales for each division:$'))
            
 
        if monthly_sales>=0:
           print('Enter a negative number after the'
             ' last amount has been entered')
           all_monthly_sales.append(monthly_sales)
        elif monthly_sales <0:
            value = False
    threshold = float(input('Please enter a threshold:'))
    
    print('\nThe monthly sales amounts entered are: \n'\
           + format_it(all_monthly_sales))

    print ('\nThe highest monthly sales amount is $'\
           + format(get_highest(all_monthly_sales), ',.2f'))
    print('\nThe highest monthly sales amount is $'\
          +format(max(all_monthly_sales), ',.2f'))
    print('\nThe lowest monthly sales amount is $'\
          +format(min(all_monthly_sales), ',.2f'))
    print('\nThe lowest monthly sales amount is $'\
          +format(get_low(all_monthly_sales), ',.2f'))
    print('\nThe sum of all the monthly sales is $'\
          +format(sum(all_monthly_sales), ',.2f'))
    print('\nThe sum of all the monthly sales is $'\
          +format(sum_it(all_monthly_sales), ',.2f'))
    print('\nThe average monthly sales is $'\
          +format(average_it(all_monthly_sales), ',.2f'))
    print('\nThe monthly sales amounts greater than or equal to $' \
          + str(threshold) + ' are: \n'\
          + format_it(greater_equal_thres( all_monthly_sales, threshold)))


#returns the highest monthly sales amount 
def get_highest(all_monthly_sales):
    highest = all_monthly_sales[0]
    for i in range(1, len(all_monthly_sales)):
        if all_monthly_sales[i] > highest:
            highest = all_monthly_sales[i]
    return highest

#returns the lowest monthly sales amount
def get_low(all_monthly_sales):
    lowest = all_monthly_sales[0]
    for i in range (1, len(all_monthly_sales)):
        if all_monthly_sales[i]<lowest:
            lowest = all_monthly_sales[i]
    return lowest

#returns the sum of all the sales amounts entered by the user
def sum_it(all_monthly_sales):
    total = 0
    for value in all_monthly_sales:
        total += value
    return total

#returns the average sales amounts
def average_it(all_monthly_sales):
    total = 0
    count = 0
    for num in all_monthly_sales:
        total+=num
        count+=1
    average = total/count
    return average

#returns all the monthly sales amounts greater or equal to the threshold
#specified by the user. These values are put into a new list.
def greater_equal_thres( all_monthly_sales, threshold):
    new_list = []
    for value in all_monthly_sales:
        if value >= threshold:
            new_list.append(value)
    return new_list

# this function accepts a list as an argument and then returns the values
#in the list as a formatted string. It creates a new string and then adds
#each formatted value into the string.
def format_it (arg):
  new_list='{$' + format(arg[0], ',.2f')
  for i in range(1,len(arg)):
      new_list += ', $' + format(arg[i], ',.2f')
  new_list+= '}'
  return new_list
 

# runs the program
main()

##documentation

##Test Case 1
##when the program was tested with the values below, it produced
##results that match a calculator.

#Please enter monthly sales for each division:$100.75
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$200.95
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$300.85
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$400.50
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$-1
#Please enter a threshold:200.94

#The monthly sales amounts entered are: 
#{$100.75, $200.95, $300.85, $400.50}

#The highest monthly sales amount is $400.50

#The highest monthly sales amount is $400.50

#The lowest monthly sales amount is $100.75

#The lowest monthly sales amount is $100.75

#The sum of all the monthly sales is $1,003.05

#The sum of all the monthly sales is $1,003.05

#The average monthly sales is $250.76

#The monthly sales amounts greater than or equal to $200.94 are: 
#{$200.95, $300.85, $400.50}


##Test Case 2
##when the program was retested with the values below, it produced
##results that match a calculator.


#Please enter monthly sales for each division:$0
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$1000
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$3000
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$6000.8765
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$9000.76
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$50000
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$45000
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$3500.76
#Enter a negative number after the last amount has been entered
#Please enter monthly sales for each division:$-1
#Please enter a threshold:3501

#The monthly sales amounts entered are: 
#{$0.00, $1,000.00, $3,000.00, $6,000.88, $9,000.76, $50,000.00, $45,000.00, $3,500.76}

#The highest monthly sales amount is $50,000.00

#The highest monthly sales amount is $50,000.00

#The lowest monthly sales amount is $0.00

#The lowest monthly sales amount is $0.00

#The sum of all the monthly sales is $117,502.40

#The sum of all the monthly sales is $117,502.40

#The average monthly sales is $14,687.80

#The monthly sales amounts greater than or equal to $3501.0 are: 
#{$6,000.88, $9,000.76, $50,000.00, $45,000.00}


