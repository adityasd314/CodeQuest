Mystical Realm of Eldoria
-------------------------

locked

-   [Problem](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/mystical-realm-of-eldoria)
-   [Submissions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/mystical-realm-of-eldoria/submissions)
-   [Leaderboard](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/mystical-realm-of-eldoria/leaderboard)
-   [Discussions](https://www.hackerrank.com/contests/codequest-4-0-jr/challenges/mystical-realm-of-eldoria/forum)

In the mystical realm of Eldoria, the fearless warrior, Sir Alaric, faces a daunting task:\
to vanquish a legendary fire-breathing beast known as the Inferno Drake. The epic battle with this formidable dragon spans 100,500 heart-pounding seconds. Armed with a magical toxin-infused blade, Sir Alaric embarks on his quest.\
With each strike of his blade, the dragon becomes poisoned, causing it to suffer 1 damage per every **k** consecutive seconds, starting from the very moment of the dagger's thrust.\
However, if Sir Alaric strikes again before the poison's effect expires, the new poison cancels out the old one.\
For example, let's assume k = 4. If Sir Alaric strikes the Inferno Drake at seconds 2, 4, and 10, the poison's effect unfolds as follows:\
It damages the dragon on the 2nd and 3rd seconds, then on the 4th, 5th, 6th, and 7th seconds, and finally on the 10th, 11th, 12th, and 13th seconds. This cumulative effect results in a total of 10 damage to the dragon. Sir Alaric is aware of the Inferno Drake's formidable health, denoted as **'h'** hit points.\
His quest is to uncover the smallest possible value of **'k' (the duration of the poison effect)** that will allow him to inflict at least **'h'** damage to the dragon, ultimately achieving victory in this mythical battle.

**Input Format**

To fine-tune his battle strategy, Sir Alaric undertakes a series of quests. The initial line of input specifies the number of quests Sir Alaric will embark upon:

-   The first line of each quest provides a single integer, **'t'**, representing the number of quests Sir Alaric will undertake.
-   Subsequently, each quest is defined by the following details:
-   The first line of the quest features two integers, **'n'** and **'h'**, denoting the number of attacks Sir Alaric will execute and the total damage required to defeat the Inferno Drake.
-   The second line presents **'n' integers, 'a1, a2, ..., an'**, which represent the precise moments when Sir Alaric launches his attacks.

**Constraints**

**1 ≤ t ≤ 1000\
1 ≤ n ≤ 100\
1 ≤ h ≤ 1018\
1 ≤ ai ≤ 109 ; ai < ai+1**

**Output Format**

For each quest, Sir Alaric must determine the optimal value of the parameter 'k' to ensure his success in vanquishing the Inferno Drake by inflicting at least 'h' damage. The output for each quest consists of a single integer, representing the **minimum value of 'k' required for Sir Alaric's victory.**

**Sample Input 0**

4
2 5
1 5
3 10
2 4 10
5 3
1 2 4 5 7
4 1000
3 25 64 1337

**Sample Output 0**

3
4
1
470