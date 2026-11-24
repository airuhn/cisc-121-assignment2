def solution(A):
    A.sort() # sort ascending
    return max([A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1]]) # 3 largest or 2 smallest x largest