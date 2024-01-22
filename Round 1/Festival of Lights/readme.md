Festival of Lights
------------------

locked

-   [Problem](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/festival-of-lights)
-   [Submissions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/festival-of-lights/submissions)
-   [Leaderboard](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/festival-of-lights/leaderboard)
-   [Discussions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/festival-of-lights/forum)

Goju Satoru visits India on the festival of Diwali. Goju is very fond of lights, so he steals an infinite number of red and blue light bulbs. He also loves patterns and is very eccentric, so he arranges the lights by infinitely repeating a given finite pattern S.\
For example, **if S is BBRB**, the infinite sequence Goju builds would be **BBRBBBRBBBRB**...\
Blue is Goju's favorite color, so he wants to know the number of blue bulbs between the **Ith bulb** and **Jth bulb**, inclusive, in the infinite sequence he built (lights are numbered with consecutive integers starting from 1). In the sequence above, the indices would be numbered as follows:\
**\
B B R B B B R B B B R B ...\
1 2 3 4 5 6 7 8 9 10 11 12 ...

**So, for example, there are 4 blue lights between the 4th and 8th positions, but only 2 between the 10th and 12th.\
Since the sequence can be very long, he has asked you as one of his students at the academy to use your cursed technique of programming to write a program for him

**Input Format**

First line of each test case consists of a string **S**, denoting the initial finite pattern.\
Second line of each test case consists of **two space separated integers I and J**, defined above.

**Constraints**

**1 ≤ length of S ≤ 100.\
Each character of S is either uppercase B or uppercase R.**

**Output Format**

For each test case, output one line containing **y**, where y is the number of blue bulbs between the **Ith bulb** and **Jth bulb** of the infinite sequence, inclusive.

**Sample Input 0**

BBRB
4 8

**Sample Output 0**

4

**Explanation 0**

NA