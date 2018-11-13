# Anders Engebretsen
# CS 21: Fall 18
# Project: Number Tree

"""
    Module Description:
    This is a program that includes several functions about a number tree.
    One recursive function will be called upon in the other functions to
    get the right number from the number tree. 
    Here is a short description of the funtctions:
    1. A recursive function called get_number that takes two parameters,
    n and k, and returns the corresponding value a(n, k) from the above
    number tree.
    2. A function called get_row_sum that takes one parameter called
    i and returns the sum of all entries in row i.
    3. A function called get_alternating_sum that takes one parameter
    called i and returns the alternating sum of all entries in row i.
    4. A function called get_sum_of_squares that takes one parameter
    called i and returns the sum of the squares of the entries in row i.
    5. A function called print_tree that takes one parameter called
    num_rows,and returns no value. The function should print out the
    first num_rows rows of the tree in a left-justified manner.
    6. A function called get_diagonal_sum that takes one parameter
    called i and returns the sum of the entries in the diagonal row that
    extends to the upper right from the first entry in row i when the number
    tree is left-justified.
    7. A function called print_pretty_tree that takes one parameter called
    num_rows and returns no value. The function should print out the first
    num_rows rows of the number tree, but with the following substitutions:
    • If an entry is odd, then substitute a single asterisk for the number.
    • If an entry is even, then print a single space for the number.

    Functions 2-7 calls  function 1 to get the right values from the
    number tree. 

"""

# Define the get_number function. This will be the base of the whole program
# as all the other functions use it. "n" is the number of rows, and "k" is
# the location in this row. 
def get_number(n,k):
    # All the outer numbers in the tree are 1. Therefore, if n == 0, k == 0 or
    # n == k, the function should return 1. There are as many horizontal numbers
    # in the tree, as the line it is. Therefore, n == k should be the last
    # location and return 1. 
    if n == 0:
        return 1
    elif k == n:
        return 1
    elif k == 0:
        return 1
    # As mentioned, when n == k, it should be the last number in that row.
    # Therefore, when k exceeds n, the function should return None.
    elif k > n:
       return None
    # Each number is defined to be the sum of its two parents,
    # the element just above and to the left of it and the element
    # just above and to the right of it. Therefore, we use recursive function
    # that will go back in the number tree to find elements that occur earlier
    # in the number tree.
    else:
        return get_number(n-1, k-1) + get_number(n-1,k)
    
# Define the get_row_sum that adds up all the elements in a row and returns
# the total sum of the row. 
def get_row_sum(i):
    # Define the start value of the sum of the rows as 0.
    total = 0
    # Define the base condition; if there is only one row, it will return 1.
    # If it is less or equal to 0, it will not return None since it is not
    # defined in the number tree.
    if i == 1:
        return 1
    elif i <= 0:
        return None
    # A for loop will iterate through the row number i. Row 1 has index 0
    # , so in the call for get_number function it has to be i-1, which is
    # constant for the loop. "n" will start at 0 and increase by one for
    # every iteration until it has reached the range. For every iteration,
    # the element in that row will be added to total cumulation of the row.
    else:
        for n in range(i):
            total += get_number(i-1, n)
    # Return the total value for the whole row.
    return total

# Define the get_alternating_sum that is a similar to the get_row_sum, except
# that this time we have to determine to add or subtract the element in the
# row. It should alternate between positive and negative.
def get_alternating_sum(i):
    # Define the start values of n and the alternate_total as 0.
    n = 0
    alternate_total = 0
    # Make an if-else statement that returns None if the input is undefined
    # in the number tree. That means that if the input is less or equal to 0.
    if i <= 0:
        return None
    else:
        # A while loop that will iterate until the condition is met. n will
        # increase by 1 for every iteration because of "n += 1". If n is a
        # even number, it will add the element in the row it represents to
        # the alternate_total. If n is an odd number, it will subtract the
        # element. 
        while n < i:
            if n % 2 == 0:
                alternate_total += get_number(i-1, n)
                n += 1
            else:
                alternate_total -= get_number(i-1, n)
                n += 1
    # The function will return the alternate_total
    return alternate_total

# Define the get_sum_of_squares function that takes one parameter, i, which
# will square each element in the row and return the total sum of the sqaures.
def get_sum_of_squares(i):
    # Set the start value for the squares_total equal to zero and the n that
    # represents the index of the element in the row.
    n = 0
    squares_total = 0
    #  Make an if-else statement that returns None if the input is undefined
    # in the number tree. That means that if the input is less or equal to 0.
    if i <= 0:
        return None
    # A while loop that will iterate until the condition is met. n will
    # increase by 1 for every iteration because of "n += 1". Every element
    # in the row will be sqaured and then added to the total sum.
    else:
        while True:
            if n < i:
                squares_total += (get_number(i-1, n))**2
                n += 1
            # When the condition is not met, it will break out of the loop.
            else:
                break
    # The function will return the sum of the squares in the row
    return squares_total

# Define the print_tree function with a num_rows as a parameter.
# It will print out the number tree on the screen, with the amount of rows
# entered as a paramenter.
def print_tree(num_rows):
    # A nested for loop that where the first loop is the iterations of the
    # num_rows, while the second loop´s iterations are the elements in each
    # row.
   for i in range(num_rows+1):
        for n in range(i+1):
            # An if statement that stops the iteration when the
            # preferred number of rows are reached. 
            if i == num_rows:
                break
            else:
                # It will call on the get_number statement and print the number
                # to the screen on the same line (end = " ").
                print(get_number(i, n), end = " ")
        # After each iteration it will jump down a line, before it goes back
        # up to the first iteration again.
        print("")

# Define the get_diagonal_sum that takes one paramenter, i. It adds up the
# numbers in an up - and rightward diagonal. 
def get_diagonal_sum(i):
    # Set the start values equal to zero.
    total_diagonal = 0
    k = 0
    # An if-else statement that depends on the amount of elements to include
    # in the diagonal. So even numbers will include half of the amount that
    # is in the parameter, i, while odd numbers will be the integer division
    # of the parameter, plus one. For instance, i = 4 will give k = 2. And
    # 3 will be k = 3//2 +1, which equals 2 as well.
    if i % 2 == 0:
        k = i//2
        # When the k is decided, it is used as the range for the for loop
        # and then the element in the number tree is called upon with the
        # get_number function. i-1 represents the row, which decreases by
        # one for every iteration, (therefore, the i -= 1). Item starts
        # at 0 and will increase by one for every itereation. It represents
        # the position of the element in that particular row. The element
        # is added to the total_diagonal sum.
        for item in range(k):
            total_diagonal += get_number(i-1, item)
            i -= 1
    else:
        k = i//2 + 1
        # Same process as above. but for when i is odd.
        for item in range(k):
            total_diagonal += get_number(i-1, item)
            i -= 1
    # The function returns the total_diagonal sum.
    return total_diagonal

# Define the print_pretty_tree function that takes one parameter, num_rows.
# This function will print out a tree of asterixs.
def print_pretty_tree(num_rows):
    # Set the start value of k equal to number of rows. This will be used to
    # determine the number of spaces that will be printed before the first
    # asterix in each line. 
    k = num_rows
    # A for loop that will iterate down the number of rows.
    for i in range(num_rows):
        # A nested for loop that will determine how many spaces that will
        # be printed before the first asterix in every row. The range will
        # decrease with one for each iteration, which means the asterix
        # will be printed one spot to the left of the previous row.
        for w in range(k):
            print(end = " ")
        k = k - 1
        # Another nested for loop that determines whether to print a blank
        # space or an asterix. The range will be the number of iterations in
        # the first for loop plus one, because that is how many it elements
        # that is in that row in the number tree.
        for n in range(i+1):
            # If it is an even number, a blank space will be printed.
            # end = " ", means that they will be printed on the same line.
            if get_number(i, n) % 2 == 0:
                print(" ", end = " ")
            # If it is an odd number, an asterix will be printed to the screen.
            else:
                print("*", end = " ")
        # After each iteration it will jump down a line, before it goes back
        # up to the first iteration again.
        print("")
   
                
        
           
            
    
