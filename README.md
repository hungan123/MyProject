# MyProject
After the course ended with 100% of students completing. As a farewell to the past school year as well as welcoming the bustling summer coming, the school organized a camping trip in a beautiful place for the classes. The camping night performance program is becoming hot with 150 students registering. Because the performance time is limited, the school has proposed a plan to organize a lucky draw with conditions for screening participants. This plan is implemented as follows:

- With 150 students registered to participate, the Organizing Committee will divide them into 6 groups (A, B, C, D, E, F) with 25 people each. There are 6 sets of cards, each set of cards consists of 100 cards marked from 1 to 100.

- Each group (A, B, C, D, E, F) will be given a set of cards, and 25 members in each small group will take turns picking up and holding any card in the set. This card will be considered as each student's registration number.

- After the registration number drawing is completed, the following screening conditions will be carried out in turn as below:

Screening 1:

Students in each group (A, B, C, D, E, F) will line up in a random row (6 groups of 6 rows) with the corresponding drawn registration number.

For the combined group (A, B, C), consider 3 students at a time in order from the beginning of the row to the end of the row, and eliminate students with the smallest registration number (can eliminate 1, 2 or all 3 if 3 students have the same number in the round of consideration).

Similar to the grouping (D, E, F)

Screening 2:

For each individual group (A, B, C, D, E, F), multiply all the registration numbers of the group members, then divide by (largest registration number - smallest registration number), if the division has a REMUNERATION, then the members with the largest and smallest registration numbers will be eliminated, otherwise no one will be eliminated.

Screening 3:

In each group (A, B, C) or (D, E, F), if any registration exists 3 times, the students with that registration number will be eliminated.

Final:

After passing the 3 stages of screening 1, 2 and 3, the remaining candidates will be able to participate in the performance. And the organizers want to know how many different registration numbers there are in all groups (A + B + C + D + E + F) after screening.



Detailed example:

150 students are divided into 6 groups and arranged in 6 rows with corresponding lottery registration numbers as below:

A: 55 59 73 65 56 52 71 70 72 57 64 74 66 61 53 50 60 62 51 69 63 68 58 67 54

B: 60 51 69 53 74 73 61 66 70 55 72 71 54 56 65 58 63 68 64 59 50 52 67 62 57

C: 51 55 70 50 53 52 67 64 65 61 60 57 62 69 63 74 56 54 71 58 68 73 59 72 66



D: 70 74 63 58 55 54 61 68 52 56 59 66 65 62 53 60 51 72 64 50 57 73 71 67 69

E: 51 72 50 70 63 60 68 71 61 67 55 69 66 59 52 74 54 53 64 56 62 57 73 65 58

F: 67 71 51 62 56 55 64 57 70 52 66 74 69 50 59 65 58 73 72 53 63 54 68 61 60



Screening 1:

Find the smallest registration number of each group (A, B, C) and (D, E, F) with 3 students at a time from the first row to the last row

A: 55 59 73 65 56 52 71 70 72 57 64 74 66 61 53 50 60 62 51 69 63 68 58 67 54

B: 60 51 69 53 74 73 61 66 70 55 72 71 54 56 65 58 63 68 64 59 50 52 67 62 57

C: 51 55 70 50 53 52 67 64 65 61 60 57 62 69 63 74 56 54 71 58 68 73 59 72 66



D: 70 74 63 58 55 54 61 68 52 56 59 66 65 62 53 60 51 72 64 50 57 73 71 67 69

E: 51 72 50 70 63 60 68 71 61 67 55 69 66 59 52 74 54 53 64 56 62 57 73 65 58

F: 67 71 51 62 56 55 64 57 70 52 66 74 69 50 59 65 58 73 72 53 63 54 68 61 60



The smallest registration number in A, B, C in each order

  51 51 69 50 52 61 64 65 55 60 57 54 56 53 50 56 54 51 58 50 52 58 62 54

The smallest registration number in D, E, F in each turn order

  51 71 50 58 55 54 61 57 52 52 55 66 65 50 52 60 51 53 64 50 57 54 68 61 58



With screening rule 1 , the excluded students (RM) of the groups will be as follows:

A: 55 59 73 65 56 RM 71 70 72 57 64 74 66 61 RM RM 60 62 RM 69 63 68 RM 67 RM

B: 60 RM RM 53 74 73 RM 66 70 RM 72 71 RM RM 65 58 63 68 64 59 RM RM 67 RM 57

C: RM 55 70 RM RM RM 67 RM RM 61 RM RM 62 69 63 74 RM RM 71 RM 68 73 59 72 66



D: 70 74 63 RM RM RM RM 68 RM 56 59 RM RM 62 53 RM RM 72 RM RM RM 73 71 67 69

E: RM 72 RM 70 63 60 68 71 61 67 RM 69 66 59 RM 74 54 RM RM 56 62 57 73 65 RM

F: 67 RM 51 62 56 55 64 RM 70 RM 66 74 69 RM 59 65 58 73 72 53 63 RM RM RM 60



Screening 2:

For group A: The smallest registration number in group A is 55 , the largest in group A is 74 , the result of multiplying all registration numbers in group A is 24706114253832042444183504814080000 , and the remainder of the division is: 0

Since the remainder of the division is 0 , keep the students of group A the same.

Same for group B

For group C: The smallest registration number in group C is 55 , the largest in group C is 74 , the result of multiplying all registration numbers in group C is 31009658378006367135014400 , and the remainder of the division is: 7

Because there is a remainder , we will exclude students with registration numbers 55 and 74 in group C.

Same for the remaining groups.



After screening 2 , the student status of the groups is:

A: 55 59 73 65 56 RM 71 70 72 57 64 74 66 61 RM RM 60 62 RM 69 63 68 RM 67 RM

B: 60 RM RM 53 74 73 RM 66 70 RM 72 71 RM RM 65 58 63 68 64 59 RM RM 67 RM 57

C: RM RM 70 RM RM RM 67 RM RM 61 RM RM 62 69 63 RM RM RM 71 RM 68 73 59 72 66



D: 70 74 63 RM RM RM RM 68 RM 56 59 RM RM 62 53 RM RM 72 RM RM RM 73 71 67 69

E: RM 72 RM 70 63 60 68 71 61 67 RM 69 66 59 RM 74 54 RM RM 56 62 57 73 65 RM

F: 67 RM 51 62 56 55 64 RM 70 RM 66 74 69 RM 59 65 58 73 72 53 63 RM RM RM 60



Screening 3:

Group (A + B + C) will include students with the following registration numbers:

55, 59, 73, 65, 56, 71, 70, 72, 57, 64, 74, 66, 61, 60, 62, 69, 63, 68, 67, 60, 53, 74, 73, 66, 70, 72, 71, 65, 58, 63, 68, 64, 59, 67, 57, 70, 67, 61, 62, 69, 63, 71, 68, 73, 59, 72, 66

Group (D + E + F) will include those with the following registration numbers:

70, 74, 63, 68, 56, 59, 62, 53, 72, 73, 71, 67, 69, 72, 70, 63, 60, 68, 71, 61, 67, 69, 66, 59, 74, 54, 56, 62, 57, 73, 65, 67, 51, 62, 56, 55, 64, 70, 66, 74, 69, 59, 65, 58, 73, 72, 53, 63, 60



We see that in the combined group (A + B + C) there are registration numbers that appear 3 times.

59, 73, 71, 70, 72, 66, 63, 68, 67

We see that in the combined group (D + E + F) there are registration numbers that appear 3 times.

70, 74, 63, 56, 59, 62, 72, 73, 67, 69



So after excluding students whose registration number appears 3 times, the remaining students have the following registration numbers:

Group (A + B + C):

55, 65, 56, 57, 64, 74, 61, 60, 62, 69, 60, 53, 74, 65, 58, 64, 57, 61, 62, 69

Group (D + E + F)

68, 53, 71, 60, 68, 71, 61, 66, 54, 57, 65, 51, 55, 64, 66, 65, 58, 53, 60

As a result, we can count that there are 17 different registration numbers in all groups A + B + C + D + E + F



You need to do the following:

Proceed to program to input 6 character strings (group A, group B, group C, group D, group E, group F), then write a program to return the result value.



Example program call:

ChallengeClass().FindTalent("55,59,73,65,56,52,71,70,72,57,64,74,66,61,53,50,60,62,51,69,63,68 ,58,67,54","60,51,69,53,74,73,61,66,70,55,72,71,54,56,65,58,63,68,64,59,50 ,52,67,62,57","51,55,70,50,53,52,67,64,65,61,60,57,62,69,63,74,56,54,71,58 ,68 ,73,59,72,66","70,74,63,58,55,54,61,68,52,56,59,66,65,62,53,60,51,72,64,50 ,57,73,71,67,69","51,72,50,70,63,60,68,71,61,67,55,69,66,59,52,74,54,53,64 ,56,62,57,73,65,58","67,71,51,62,56,55,64,57,70,52,66,74,69,50,59,65,58,73 ,72,53,63,54,68,61,60")



Constraints:

Each number series in the participation will have 25 students with the corresponding value being the registration number.
Registration numbers will be in the range [1..100]


