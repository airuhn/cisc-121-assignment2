def solution(A):
    A.sort() # sort ascending
    n = len(A)
    count = 0

    for x in range(n - 2): # x = smallest side
        z = x + 2. # z = largest side 
        for y in range(x + 1, n - 1): # y = middle side
            while z < n and A[x] + A[y] > A[z]: # move z forward while it still makes a triangle
                z += 1
            count += z - y - 1 # every z between y and the current z makes a triangle with x and y
    return count

