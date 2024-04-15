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
