__author__ = 'deveshbajpai'


class PRIME1:
    m = 0
    n = 0

    def solve(self):
        for i in range(self.m, self.n+1):
            if(self.isPrime2(i)):
                print i
        print ''

    @staticmethod
    def eratosthenes2(n):
        multiples = set()
        for i in range(2, n+1):
            if i not in multiples:
                yield i
                multiples.update(range(i*i, n+1, i))




    def isPrime2(self,n):
        if n==2 or n==3:
            return True
        if n%2==0 or n<2:
            return False
        for i in range(3,int(n**0.5)+1,2):   # only odd numbers
            if n%i==0:
                return False

        return True

    def is_prime(self,n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n%3 == 0:
            return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f +=6
        return True

if __name__ == "__main__":
    print PRIME1.eratosthenes2(100)
    '''
    cases = int(input())
    result = []

    for case in range(cases):
        obj = PRIME1()
        obj.m,obj.n = map(int,raw_input().split(" "))
        result.append(obj.solve())
    '''
