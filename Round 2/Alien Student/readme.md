Alien Student
-------------

locked

-   [Problem](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/alien-student)
-   [Submissions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/alien-student/submissions)
-   [Leaderboard](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/alien-student/leaderboard)
-   [Discussions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/alien-student/forum)

You are trying to teach an alien to spell words. You initially tried evaluating its spellings like you normally would (checked if it matches the correct spelling or not) but then saw that the alien had very poor accuracy in his attempts.\
To boost his confidence in the hopes of eventually getting him on the correct path you decide that the alien's answer word A is acceptable if it is the same length as the target word W, and the **ith letter of A is either the ith, (i-1)th, or (i+1)th letter of W, for all i in the range of the length of A.**\
(The first letter of A must match either the first or second letter of W, since the 0th letter of W doesn't exist. Similarly, the last letter of A must match either the last or next-to-last letter of W.)\
Note that the target word itself is always an acceptable answer word. You want to determine, **for each target word, how many distinct acceptable answer words there are.**\
Since this number may be very large, please output it modulo 1000000007 (10^9 + 7).

**Input Format**

Each test case consists of one line with a string consisting only of **lowercase English letters (a through z).**

**Constraints**

**1 ≤ length of each string ≤ 1000.**

**Output Format**

For each test case,\
**output one line containing the number of distinct acceptable answer words, modulo 109 + 7.**

**Sample Input 0**

ag

**Sample Output 0**

4

**Explanation 0**

The acceptable answer words are **aa, ag, ga, and gg.**