__author__ = 'deveshbajpai'
'''
Johnny needs to make a rectangular box for his physics class project. He has bought P cm of wire and S cm2 of special paper. He would like to use all the wire (for the 12 edges) and paper (for the 6 sides) to make the box.
What is the largest volume of the box that Johnny can make?
Input

The first line contains t, the number of test cases (about 10). Then t test cases follow.
Each test case contains two integers P and S in a line (1 ≤ P ≤ 40000, 1 ≤ S ≤ 20000). You may assume that there always exists an optimal solution for the given input cases.
Output

For each test case, print a real number that is the largest volume of the box that Johnny can make, rounded to two decimal places.
Example

Input:
2
20 14
20 16

Output:
3.00
4.15

Output details
First case: the dimensions of the largest box may be 3, 1 and 1.
Second case: the dimensions of the largest box may be 7/3, 4/3 and 4/3.

Algorithm: The volume is maximized when the base area of the rectangle consists of equal sides. Keeping that, it
reduces to 2 variables and 2 equations. Keeping that, it reduces to a quadratic equation in a variable. We will get
 2 values for it. Calculate the volume for both cases and report the bigger value as the answer.
'''
from math import sqrt


def solve(p,s):

    det = sqrt((p*p)-(24*s))

    b1 = (-p + det)/(-12)
    b2 = (-p - det)/(-12)

    c1 = p/4 - (2*b1)
    c2 = p/4 - (2*b2)

    return round(max(b1*b1*c1,b2*b2*c2),2)

if __name__ == "__main__":

    cases = int(input())
    results = []
    for case in range(cases):
        p,s = map(int,raw_input().split(" "))
        results.append(solve(p,s))

    for result in results:
        print result