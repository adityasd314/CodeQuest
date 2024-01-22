Research in COEP Tech
---------------------

locked

-   [Problem](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/research-in-coep-tech)
-   [Submissions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/research-in-coep-tech/submissions)
-   [Leaderboard](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/research-in-coep-tech/leaderboard)
-   [Discussions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/research-in-coep-tech/forum)

In COEP Tech, many of the professors are very active in the field of research. The overall quality of the professor's research papers are assessed by an external RnD body.\
The score of a researcher is the **largest integer 'h' such that the researcher has h papers with at least h citations each**. Suppose a professor has written **N** papers in his lifetime and has assigned you to determine his score **after each paper he wrote.**\
The **ith paper has Ai citations** and the number of citations that each paper has, will never change after it is written. Design an algorithm for this professor so that he gives you good research opportunities in the future!

**Input Format**

Each test case begins with a line containing **N**, the number of papers. The second line contains **N** integers. **The ith integer is Ai, the number of citations the ith paper has.**

**Constraints**

**1 ≤ N ≤ 105\
1 ≤ Ai ≤ 105**

**Output Format**

For each test case, output **one line containing the score after the Professor wrote his ith paper.**

**Sample Input 0**

3
5 1 2

**Sample Output 0**

1 1 2

**Explanation 0**

The professor wrote N = 3 papers.\
After the 1st paper, the professor's score is 1, since he has 1 paper with at least 1 citation.\
After the 2nd paper, the score is still 1.\
After the 3rd paper, the score is 2, since he has 2 papers with at least 2 citations (the 1st and 3rd papers).

**Sample Input 1**

6
1 3 3 2 2 15

**Sample Output 1**

1 1 2 2 2 3

**Explanation 1**

The professor wrote N = 6 papers.\
After the 1st paper, score is 1, since he has 1 paper with at least 1 citation.\
After the 2nd paper, score is still 1.\
After the 3rd paper, score is 2, since he has 2 papers with at least 2 citations (the 2nd and 3rd papers).\
After the 4th paper, score is still 2.\
After the 5th paper, score is still 2.\
After the 6th paper, score is 3, since he has 3 papers with at least 3 citations (the 2nd, 3rd and 6th papers).