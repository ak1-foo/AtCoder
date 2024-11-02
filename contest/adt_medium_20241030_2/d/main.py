S1 = input()
S2 = input()
S3 = input()

S = [S1, S2, S3]
contests = ['ABC', 'ARC', 'AGC', 'AHC']

for contest in contests:
    if contest not in S:
        print(contest)
        break
