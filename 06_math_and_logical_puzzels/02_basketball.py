import time

def probability(wanted: int, chances: int) -> float:
    outcomes: int = int('0b'+'1'*chances, 2)
    start: int = int('0b'+'1'*wanted, 2)
    count: int = 0
    
    for i in range(start, outcomes):
        if bin(i).count('1') >= wanted:
            count+=1

    return count/(chances**2)


if __name__ == '__main__':
    startTime = time.time()
    '''
        input:
        [1] 2  --> test cases
        [2] 1 2 (format: 'required chances')  --> case-1
        [3] 2 3                               --> case-2
    '''
    cases = int(input())
    ans = 0

    for i in range(cases):
        temp = input().split()
        chance = probability(int(temp[0]), int(temp[1]))

        if i == 0:
            ans = i+1

        if ans < chance:
            ans = i+1

    print(ans)
    print("program executed is %s second(s)" % (time.time() - startTime))
    exit(0)
