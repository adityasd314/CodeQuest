The City of Cinetopia
---------------------

locked

-   [Problem](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/the-city-of-cinetopia)
-   [Submissions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/the-city-of-cinetopia/submissions)
-   [Leaderboard](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/the-city-of-cinetopia/leaderboard)
-   [Discussions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/the-city-of-cinetopia/forum)

In the bustling City of Cinetopia, a group of movie enthusiasts has caught wind of a new cinema about to make its grand debut. This cinema promises to premiere a fresh movie every day for **n days**. Our moviegoer, Alex, is eagerly anticipating this cinematic experience.\
Alex has meticulously gathered the movie schedule, complete with an assigned entertainment value **ai** for each movie. However, there's an intriguing twist to this movie marathon. The longer Alex waits between cinema visits, the more the entertainment value of the next movie decreases. This decline is determined by a preset value **d** and by the number of days since Alex's last visit **cnt**.\
**For example**, let's say **d is equal to 2**, and Alex is presented with the array of movie entertainment values **a=[3, 2, 5, 4, 6]**. If Alex decides to attend the premieres of movies with indices 1 and 3, his 'cnt' value for day 1 would be 1 - 0 = 1, and for day 3, it would be 3 - 1 = 2. Consequently, the total entertainment value of the selected movies would be calculated as **a1 - d*1 + a3 - d*2 = 3 - 2*1 + 5 - 2*2 = 2.**\
However, Alex's schedule is quite tight, and he can visit a **maximum of 'm' movies**. His mission is to devise a strategy that allows him to **select which movies to attend in a way that maximizes the total entertainment value**.

**Input Format**

The first line contains a single integer **t** --- the number of test cases. The description of the test cases follows.\
The first line of each test case contains three integers **n, m, and d**.\
The second line of each set of input data contains **n integers a1,a2,...,an** --- the entertainment values of the movies.

**Constraints**

**1 ≤ t ≤ 104\
1 ≤ n ≤ 2⋅105\
1 ≤ m ≤ n\
1 ≤ d ≤ 109\
-109 ≤ ai ≤ 109\
It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.**

**Output Format**

For each test case, output a single integer --- the maximum total entertainment value that Alex can get.

**Sample Input 0**

6
5 2 2
3 2 5 4 6
4 3 2
1 1 1 1
6 6 6
-82 45 1 -77 39 11
5 2 2
3 2 5 4 8
2 1 1
-1 2
6 3 2
-8 8 -2 -1 9 0

**Sample Output 0**

2
0
60
3
0
7

**Explanation 0**

NA