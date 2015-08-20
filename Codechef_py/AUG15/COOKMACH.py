__author__ = 'deveshbajpai'

import math
'''
Chef is on a vacation these days, so his friend Chefza is trying to solve Chef's everyday tasks.
Today's task is to make a sweet roll. Rolls are made by a newly invented cooking machine. The machine is pretty universal - it can make lots of dishes and Chefza is thrilled about this.
To make a roll, Chefza has to set all the settings to specified integer values. There are lots of settings, each of them set to some initial value. The machine is pretty complex and there is a lot of cooking to be done today, so Chefza has decided to use only two quick ways to change the settings. In a unit of time, he can pick one setting (let's say its current value is v) and change it in one of the following ways.
If v is even, change this setting to v/2. If v is odd, change it to (v − 1)/2.
Change setting to 2 × v
The receipt is given as a list of integer values the settings should be set to. It is guaranteed that each destination setting can be represented as an integer power of 2.
Since Chefza has just changed his profession, he has a lot of other things to do. Please help him find the minimum number of operations needed to set up a particular setting of the machine. You can prove that it can be done in finite time.
Input

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The only line of each test case contains two integers A and B denoting the initial and desired values of the setting, respectively.
Output

For each test case, output a single line containing minimum number of operations Chefza has to perform in order to set up the machine.
Constraints

1 ≤ T ≤ 200
1 ≤ A ≤ 107
1 ≤ B ≤ 107, and B is an integer power of 2
Subtasks

Subtask #1 [40 points]: A ≤ 100 and B ≤ 100
Subtask #2 [60 points]: No additional constraints
Example

Input:
6
1 1
2 4
3 8
4 16
4 1
1 4

Output:
0
1
4
2
2
2
Explanation

In the first test case, you don't need to do anything.
In the second test case, you need to multiply 2 by 2 and get 4. This is done in 1 operation.
In the third test case, you need to obtain 1 from 3 and then multiply it by 2 three times to obtain 8. A total of 4 operations.
In the fourth test case, multiply 4 by 2 twice.
In the fifth test case, divide 4 by 2 twice.
In the sixth test case, multiply 1 by 2 twice.




Algorithm: Consider 3 broad cases:
Case 1: a is equal to b - No operation needed
Case 2: a is less than b - If a is even or equal to 1, divide b by a and find the logarithm base 2 to find result
                         - If a is odd, perform v-1/2 operation and then use logarithm as in above case
Case 3: a is more than b - If a is even, divide a by b and find the logarithm base 2 to find result
                         - If a is odd, perform v-1/2 operation and then use logarithm as in above case

Problem Url:
https://www.codechef.com/AUG15/problems/COOKMACH

'''

class COOKMACH:
    a = b = 0

    def solve(self):

        if(self.a == self.b):
            return 0
        elif(self.a < self.b):
            if(self.a%2==0 or self.a==1):
                return math.log((self.b/self.a),2)
            else:
                denom = max((self.a-1)/2,1)
                return math.log((self.b/denom),2)+1
        elif(self.a > self.b):
            if(self.a%2==0):
                return math.log((self.a/self.b),2)
            else:
                num = max((self.a-1)/2,1)
                return math.log(num/self.b,2)+1


if __name__ == "__main__":
    t = map(int,raw_input().split())
    t_ = 0
    result = []
    while(t_ < t):
        c = COOKMACH()
        c.a,c.b = map(int,raw_input().split(" "))
        result.append(c.solve())
        t_ += 1

    for i in result:
        print int(i)