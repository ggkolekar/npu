def min_(lst):
    # smallest number at index 0 in list
    smallest: int = lst[0]
    #if lst: else None
    # loop to find smallest number in lst
    for i in range(len(lst)):
        if i<smallest:
            smallest=i
    return smallest


def max_(lst):
    # root element variable
    largest: int = lst[0]
    # loop to find largest number in lst
    for i in range(len(lst)):
        if (lst[i] > int(largest)):
            largest = lst[i]
    return largest


def sum_(lst):
    sum = 0

    for i in lst:
        sum += i
    return sum


def avg_(lst):
    total: int = 0
    for i in range(len(lst)):
        total += i
        res = total/len(lst)
    return res


#def mode_(lst):


def bring_menu(lst):

    print('You entered : ', lst)
    print('What do you want to find ?')
    print(' Enter 1 for smallest \n',
    ' Enter 2 for largest \n',
    ' Enter 3 for sum \n',
    ' Enter 4 for average \n',
    ' Enter 5 for mode \n',)
    menu = input("Enter your choice : ")
    if menu == '1':
        print('Smallest is :', min_(lst))
    elif menu == '2':
        print('Largest is :', max_(lst))
    elif menu == '3':
        print('Sum is :', sum_(lst))
    elif menu == '4':
        print('Average is :', avg_(lst))
    #elif menu == '5':
      #  print('Mode is :', mode_(lst))
    else:
        print('Invalid Option')

def main():
    lst = input("Enter your list by using comma between numbers: ").split(',')
    for i in range(len(lst)):
        lst[i] = int(lst[i])

        bring_menu(lst)

main()
