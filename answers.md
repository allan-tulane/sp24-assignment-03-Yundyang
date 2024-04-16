# CMPS 2200 Assignment 3
## Answers

**Name:**_ Yundan Yang


Place all written answers from `assignment-03.md` here for easier grading.



1a) 

To make N dollars with the fewest num of coins in power of 2(2^0...2^k),we start with the larget denomination coin that does not exceed N. And then subtract the value of that coin from N to get a new N. Repeat this process until N is zero.


1b)

For any given N, choosing 2^k where k is the largest int such that 2^k <= N, is obviously the best local choice because it reduces N by the Largest possible anount in a single step. After the first coin is choosen, we are left with a smaller instance of the same problem: making change for N - 2^k. This subproblem does not depend on the previous choices and can be solved using the same greedy strategy. The solution for N is simply the chosen 2^k plus the solution for n-2^k. Additionally, because of the binary nature of the denominat9ons, there cannot be a better solutoin that uses smaller coins to make up the amount of 2^k since it would require more coins by def.


1c)

Work = O(log N)
Span = O(log N)


2a)

A simple counterexample is a currency with denominations of 1,3,4. If we change for 6 dollars, the greedy algo would choose 2 coins for denomination 3, for a total of two coins. But the optimal solution is to use three 2- dollar coins, resulting in fewer coins (only one coin).


2b)

The optimal solution to making change for n can be built from the optimal solutions to making change for smallar amounts. If the optimal num of coins needed for all amounts less than N, then the optimal num of coins for N is one more than the minnimum of teh optimal solutions for N -Di for each denomination Di available.


2c)

top down:
Algorithm CoinChangeRecursive(N, denominations):
    Input: An integer N to make change for and an array of k denominations denominations[1...k]
    Output: The minimum number of coins needed to make change for N

    Let memo[0...N] be a new array
    Set all entries of memo to -1 (indicating uncomputed)
    Set memo[0] = 0

    Function FindMinCoins(amount):
        If memo[amount] >= 0:
            return memo[amount]

        minCoins = ∞
        For each coin in denominations:
            If coin <= amount:
                candidate = FindMinCoins(amount - coin) + 1
                minCoins = min(minCoins, candidate)

        memo[amount] = minCoins
        return minCoins

    result = FindMinCoins(N)
    If result == ∞:
        return "Change cannot be made with the given denominations"
    Else:
        return result


W = O(Nk)
S = O(NK)
