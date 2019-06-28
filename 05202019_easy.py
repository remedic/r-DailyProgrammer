#!/usr/bin/env python

#https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/?st=jxg8432m&sh=71d260ab


#Optional Warmup 1:
#Given a sequence of answers, return the same set of answers with all the 0's removed

def warmup1(seq):
    out=[]
    for value in seq:
        if value!=0:
            out.append(value)
    return(out)


q1=[5,3,0,2,6,2,0,7,2,5]
q2=[4,0,0,1,3]
q3=[1,2,3]
q4=[0,0,0]
q5=[]

print("WARMUP 1:")
for q in [q1,q2,q3,q4,q5]:
    print(str(q) + " => " + str(warmup1(q)))

#Optional Warmup 2:
#Given a sequence of answers, return the sequence sorted in descending order, so that the first number is the largest and the last number is the smallest 

def warmup2(seq):

    def check_sort(seq):
        flag=True
        for i,val in enumerate(seq):
            if i>0:
                if seq[i]>seq[i-1]:
                    flag=False
        return(flag)

    def bubble_sort(seq):
        for i,val in enumerate(seq):
            if i>0:
                if seq[i]>seq[i-1]:
                    a=seq[i]
                    b=seq[i-1]
                    seq[i]=b
                    seq[i-1]=a
        return(seq)

    if check_sort(seq)==True:
        return(seq)
    else:
        seq=bubble_sort(seq)
        return(warmup2(seq))

q1=[5,1,3,4,2]
q2=[0,0,0,4,0]
q3=[1]
q4=[]

print("WARMUP 2:")
for q in [q1,q2,q3,q4]:
    print(str(q) + " => " + str(warmup2(q)))

#Optional Warmup 3:
#Given a number N and a sequence of answers, return true if N is greater than the number of answers (i.e the length of the sequence), and false if N is less than or equal to the number of answers.

def warmup3(N, seq):
    if N>len(seq):
        return(True)
    else:
        return(False)

q1=[7, [6, 5, 5, 3, 2, 2, 2]]
q2=[5, [5, 5, 5, 5, 5]]
q3=[5, [5, 5, 5, 5]]
q4=[3, [1, 1]]
q5=[1, []]
q6=[0, []]

print("WARMUP 3:")
for q in [q1,q2,q3,q4,q5,q6]:
    print(str(q) + " => " + str(warmup3(q[0], q[1])))

#Optional Warmup 4:
#Given a number N and a sequence in descending order, subtract 1 from each of the first N answers in the sequence, and return the results

def warmup4(N, seq):
    for value in range(0,N):
        seq[value]=seq[value]-1
    return(seq)

q1=[4, [5, 4, 3, 2, 1]]
q2=[11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]]
q3=[1, [10, 10, 10]]
q4=[3, [10, 10, 10]]
q5=[1, [1]]

print("WARMUP 4:")
for q in [q1,q2,q3,q4,q5]:
    print(str(q) + " => " + str(warmup4(q[0], q[1])))

#Challenge
'''
Perform the Havel-Hakimi algorithm on a given sequence of answers. This algorithm will return true if the answers are consistent (i.e. it's possible that everyone is telling the truth) and false if the answers are inconsistent (i.e. someone must be lying):

        Remove all 0's from the sequence (i.e. warmup1).
        If the sequence is now empty (no elements left), stop and return true.
        Sort the sequence in descending order (i.e. warmup2).
        Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call it N. The sequence is now 1 shorter than it was after the previous step.
        If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
        Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
        Continue from step 1 using the sequence from the previous step.
        Eventually you'll either return true in step 2, or false in step 5.

        You don't have to follow these steps exactly: as long as you return the right answer, that's fine. Also, if you answered the warmup questions, you may use your warmup solutions to build your challenge solution, but you don't have to.
'''

def hh(seq):
    seq = warmup1(seq)
    if len(seq)==0:
        return(True)
    else:
        seq = warmup2(seq)
        N = seq[0]
        seq = seq[1:]
        if warmup3(N, seq)==True:
            return(False)
        else:
            seq = warmup4(N, seq)
            return(hh(seq))

q1=[5, 3, 0, 2, 6, 2, 0, 7, 2, 5]
q2=[4, 2, 0, 1, 5, 0]
q3=[3, 1, 2, 3, 1, 0]
q4=[16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]
q5=[14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]
q6=[15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]
q7=[6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]
q8=[2, 2, 0]
q9=[3, 2, 1]
q10=[1, 1]
q11=[1]
q12=[]

print("Challenge:")
for q in [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]:
    print(str(q) + " => " + str(hh(q)))


