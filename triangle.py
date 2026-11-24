def solution(A):
    A.sort() # sort ascending
    for i in range(len(A) - 2): # look at each triplet
        if A[i] + A[i + 1] > A[i + 2]: # if the sum of the first two is greater than the third, it is a triangle
            return 1 
    return 0

