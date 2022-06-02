""" https://www.interviewbit.com/problems/balance-array/ """

from typing import *


class Solution:
    def balance_array(self, A: List[int]) -> int:
        count = 0
        peven = {}
        seven = {}
        podd = {}
        sodd = {}
        for i in range(len(A)):
            if i % 2 == 0:
                peven[i] = peven.get(i - 2, 0) + A[i]
            else:
                podd[i] = podd.get(i - 2, 0) + A[i]
        for i in range(len(A) - 1, -1, -1):
            if i % 2 == 0:
                seven[i] = seven.get(i + 2, 0) + A[i]
            else:
                sodd[i] = sodd.get(i + 2, 0) + A[i]

        for i in range(len(A)):
            even_sum = odd_sum = 0
            if i % 2 == 0:
                even_sum = sodd.get(i + 1, 0) + peven[i] - A[i]
                odd_sum = seven.get(i, 0) + podd.get(i - 1, 0) - A[i]
            else:
                even_sum = sodd.get(i, 0) + peven[i - 1] - A[i]
                odd_sum = seven.get(i + 1, 0) + podd[i] - A[i]
            count += int(even_sum == odd_sum)

        return count
