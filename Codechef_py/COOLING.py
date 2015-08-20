__author__ = 'deveshbajpai'
'''
The chef has just finished baking several pies, and it's time to place them on cooling racks.
The chef has exactly as many cooling racks as pies. Each cooling rack can only hold one pie, and each pie may only be
held by one cooling rack,
but the chef isn't confident that the cooling racks can support the weight of the pies.
The chef knows the weight of each pie,
and has assigned each cooling rack a maximum weight limit.
What is the maximum number of pies the chef can cool on the racks?

Input:

Input begins with an integer T≤30, the number of test cases.
Each test case consists of 3 lines.
The first line of each test case contains a positive integer N≤30,
the number of pies (and also the number of racks).
The second and third lines each contain exactly positive N integers not exceeding 100.
The integers on the second line are the weights of the pies, and the integers on the third line
are the weight limits of the cooling racks.
Output:

For each test case, output on a line the maximum number of pies the chef can place on the racks.
Sample input:

2
3
10 30 20
30 10 20
5
9 7 16 4 8
8 3 14 10 10

Sample output:

3
4

Algorithm:
Sort the list of racks and pies in ascending order. Iterate over them and check, if the current pie's weight is less or
equal to current rack's weight. If so, increment the count and pie counter. Else, discard the current rack, which means
increment the rack counter. Return the count as a final answer.

Problem Url:
https://www.codechef.com/problems/COOLING

'''
class COOLING:
    num = 0
    pie = []
    rack = []

    def solve(self):
        self.pie.sort()
        self.rack.sort()
        count = 0
        rack_var = 0
        pie_var = 0
        while(pie_var < len(self.pie) and rack_var < len(self.rack)):
            p = self.pie[pie_var]
            r = self.rack[rack_var]
            if(p<=r):
                count=count+1
                pie_var=pie_var+1
            rack_var=rack_var+1


        return count


if __name__ == "__main__":
    cases = int(input())
    result = []
    for x in range(cases):
        c = COOLING()
        c.num = map(int,raw_input().split())
        c.pie = map(int,raw_input().split(" "))
        c.rack = map(int,raw_input().split(" "))
        result.append(c.solve())


    for i in result:
        print int(i)