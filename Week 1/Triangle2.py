numofrows = int(input("Enter number of rows"))

def TriangleTwo(n):
    for i in range(1, n+1):
        print((" " * (n-i)) + ((2*i-1)*"*") + (" " * (n-i)))

TriangleTwo(numofrows)

# TimeComplexity = O(n)