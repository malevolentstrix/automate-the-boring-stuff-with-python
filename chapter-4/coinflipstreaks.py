import random
numberOfStreaks = 0
samplespace = []
fstreak = 1
falsestreak = 0
truestreak = 0
tstreak = 1
for experimentNumber in range(10000):
    for hundredtimes in range(100):
        randval = random.randint(0, 1)
        if randval == 1:
          randval = 'T'
        else:
           randval = 'F'
        samplespace.append(randval)
   # print(samplespace[0:100])
    for i in range(99):
        if (samplespace[i] == 'F') & (samplespace[i+1] == 'F'):
            fstreak = fstreak + 1;
            if fstreak == 6:
                falsestreak = falsestreak + 1;
        if (samplespace[i] == 'T') & (samplespace[i+1] == 'T'):
            tstreak = tstreak + 1;
            if tstreak == 6:
                truestreak = truestreak + 1; 
   # print(truestreak)
   # print(falsestreak)
    numberOfStreaks = truestreak + falsestreak
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))