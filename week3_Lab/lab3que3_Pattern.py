def printTriangle(height):
    # control the number of rows
        for i in range(height):
            # print the number of spaces
            for j in range(5-i):
                print(' ', end='')

            # print the number of starts
            for j in range(i+1):
                print('*', end='')
            print('\n')
        print()
    # bottom half of the triangle
        for i in range(height):
            # print the number of spaces
            for j in range(i+1):
                print(' ', end='')

            # print the number of starts
            for j in range(5-i):
                print('*', end='')
            print('\n')
        print()


def main():
    height = int(input('Enter the height of the triangle: '))
    printTriangle(height)

main()

