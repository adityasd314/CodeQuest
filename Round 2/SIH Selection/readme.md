SIH Selection
-------------

locked

-   [Problem](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/sih-selection)
-   [Submissions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/sih-selection/submissions)
-   [Leaderboard](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/sih-selection/leaderboard)
-   [Discussions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/sih-selection/forum)

As a Competitive programmer, for you, DSA has become boring and too easy. So you decide to get a little more into the development side of coding and embark on the journey of participating in next year's Smart India Hackathon (SIH).\
For this, you have to pick a team of **exactly P students** to accompany you. There are **N** students for you to pick from. The **ith student has a skill rating Si**, which is a positive integer indicating how skilled they are at coding.\
You have decided that a team is fair if it has exactly P students on it and they all have the same skill rating. That way, everyone plays a fair role in the team. Initially, it might not be possible to pick a fair team, so you will give some of the students one-on-one training. **It takes one hour of training to increase the skill rating of any student by 1**.\
You'd like to find the **minimum number of hours of training** you need to give before you are able to pick a fair team.

**Input Format**

Each test case starts with a line containing the two integers **N** and **P**, the number of students and the number of students you need to pick, respectively. Then, another line follows containing **N** integers **Si**; the **ith** of these is the skill of the **ith student**.

**Constraints**

**1 ≤ Si ≤ 10000, for all i.\
2 ≤ N ≤ 105.\
2 ≤ P ≤ N.\
**

**Output Format**

For each test case, **output one line containing the minimum number of hours of coaching needed, before you can pick a fair team of P students.**

**Sample Input 0**

4 3
3 1 9 100

**Sample Output 0**

14

**Explanation 0**

You can spend a total of 6 hours training the first student and 8 hours training the second one. This gives the first, second and third students a skill level of 9. This is the minimum time you can spend, so the answer is 14.