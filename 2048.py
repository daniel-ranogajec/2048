import random
import os

poz = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

score = 0
while True:
    os.system('cls')
    i=0
    t=0
    while (i<16):
        if poz[i]==0:
            t=t+1
        i=i+1
    if t==0:
        print ('GAME OVER')
        print ('SCORE: ',score)
        print ('Name: ')
        ime = input()
        if (int(score)<10):
            score_ = f'0000{score}'
        elif (int(score)<100):
            score_ = f'000{score}'
        elif (int(score)<1000):
            score_ = f'00{score}'
        elif (int(score)<10000):
            score_ = f'0{score}'
        else:
            score_ = score
        lista = []
        with open ('highscore.txt', 'r') as rf:
            for line in rf:
                lista.append(line)
        ime_ = f'{score_} {ime}\n'
        lista.append(ime_)
        s = sorted(lista, reverse=True)
        with open ('highscore.txt', 'w') as wf:
            for line in s:
                wf.write(line)
        print('\n')
        print ('Scoreboard:')
        print('\n')
        with open ('highscore.txt', 'r') as f:
            for line in f:
                print (line)
      
    brojevi = [2,2,2,2,4]
    r_broj = random.choice(brojevi)

    n=0
    while (n!=1):
        rand = random.randrange(0,16,1)
        if poz[rand]==0:
            poz[rand]=r_broj
            n=1

    a = '*************************'
    print (a)
    print ('* ',poz[0],' * ',poz[1],' * ',poz[2],' * ',poz[3],' *')
    print (a)
    print ('* ',poz[4],' * ',poz[5],' * ',poz[6],' * ',poz[7],' *')
    print (a)
    print ('* ',poz[8],' * ',poz[9],' * ',poz[10],' * ',poz[11],' *')
    print (a)
    print ('* ',poz[12],' * ',poz[13],' * ',poz[14],' * ',poz[15],' *')
    print (a)

    print (score)

    x = input()

    if (x=='w'):
        for i in range(0,4):
            if (poz[i+12]==poz[i] and poz[i+4]==0 and poz[i+8]==0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+12]==poz[i+4] and poz[i]==0 and poz[i+8]==0 and poz[i+4]!=0):
                poz[i]=poz[i+12]*2
                poz[i+4]=0
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+12]!=poz[i+4] and poz[i+8]==0 and poz[i]==0 and poz[i+12]!=0 and poz[i+4]!=0):
                poz[i]=poz[i+4]
                poz[i+4]=poz[i+12]
                poz[i+12]=0
            elif (poz[i+12]==poz[i+8] and poz[i]==0 and poz[i+4]==0 and poz[i+8]!=0):
                poz[i]=poz[i+12]*2
                poz[i+8]=0
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+12]==poz[i+4] and poz[i]!=0 and poz[i]!=poz[i+12] and poz[i+8]==0):
                poz[i+4]=poz[i+4]*2
                poz[i+12]=0
                score = score + poz[i+4]
            elif (poz[i]!=poz[i+4] and poz[i+4]==poz[i+8] and poz[i]!=0 and poz[i+4]!=0):
                poz[i+4]=poz[i+4]*2
                poz[i+8]=poz[i+12]
                poz[i+12]=0
                score = score + poz[i+4]
            elif (poz[i+12]==poz[i+8] and poz[i]==poz[i+4] and poz[i]!=0 and poz[i+8]!=0):
                poz[i]=poz[i]*2
                poz[i+4]=poz[i+8]*2
                poz[i+8]=0
                poz[i+12]=0
                score = score + poz[i] + poz[i+4]
            elif (poz[i+12]==poz[i+8] and poz[i]!=0 and poz[i+4]!=0 and poz[i]!=poz[i+4]):
                poz[i+8]=poz[i+8]*2
                poz[i+12]=0
                score = score + poz[i+8]
            elif (poz[i+12]==poz[i+8] and poz[i]==0 and poz[i+4]!=0):
                poz[i]=poz[i+4]
                poz[i+4]=poz[i+8]*2
                poz[i+8]=0
                poz[i+12]=0
                score = score + poz[i+4]
            elif (poz[i]==poz[i+4] and poz[i+8]!=0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+4]=poz[i+8]
                poz[i+8]=poz[i+12]
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+8]==poz[i] and poz[i+4]==0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+8]=0
                poz[i+4]=poz[i+12]
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+8]==poz[i+4] and poz[i]==0 and poz[i+4]!=0):
                poz[i]=poz[i+4]*2
                poz[i+4]=poz[i+12]
                poz[i+8]=0
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+8]==poz[i+4] and poz[i]!=0 and poz[i+4]!=0):
                poz[i+4]=poz[i+4]*2
                poz[i+8]=poz[i+12]
                poz[i+12]=0
                score = score + poz[i+4]
            elif (poz[i+4]==poz[i] and poz[i+8]==0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+4]=poz[i+12]
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+4]==poz[i] and poz[i+8]!=0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+4]=poz[i+8]
                poz[i+8]=poz[i+12]
                poz[i+12]=0
                score = score + poz[i]
            elif (poz[i+12]!=0 and poz[i]==0 and poz[i+4]==0 and poz[i+8]==0):
                poz[i]=poz[i+12]
                poz[i+12]=0
            elif (poz[i]!=poz[i+12] and poz[i+4]==0 and poz[i+8]==0):
                poz[i+4]=poz[i+12]
                poz[i+8]=0
                poz[i+12]=0
            elif (poz[i]!=poz[i+12] and poz[i+4]!=0 and poz[i+8]==0):
                poz[i+8]=poz[i+12]
                poz[i+12]=0
            elif (poz[i+12]!=poz[i+4] and poz[i+4]!=0 and poz[i+12]!=0 and poz[i+8]==0 and poz[i]==0):
                poz[i]==poz[i+4]
                poz[i+4]=poz[i+12]
                poz[i+12]=0
            elif (poz[i+12]!=poz[i+4] and poz[i+4]!=0 and poz[i+12]!=0  and poz[i+4]!=poz[i] and poz[i+8]==0 and poz[i]!=0):
                poz[i+8]=poz[i+12]
                poz[i+12]=0
            elif (poz[i]==0 and poz[i+4]==0 and poz[i+8]!=poz[i+12]):
                poz[i]=poz[i+8]
                poz[i+4]=poz[i+12]
                poz[i+8]=0
                poz[i+12]=0
            elif (poz[i]!=poz[i+8] and poz[i+4]==0):
                poz[i+4]=poz[i+8]
                poz[i+8]=poz[i+12]
                poz[i+12]=0
            elif (poz[i]!=poz[i+4] and poz[i]!=0 and poz[i+8]==0 and poz[i+12]!=poz[i+4]):
                poz[i+8]=poz[i+12]
                poz[i+12]=0
            elif (poz[i]==0 and poz [i+4]==0 and poz[i+8]!=0 and poz[i+8]!=poz[i+12]):
                poz[i]=poz[i+8]
                poz[i+4]=poz[i+12]
                poz[i+8]=0
                poz[i+12]=0
            elif (poz[i]!=poz[i+8] and poz[i]!=0 and poz[i+8]!=0 and poz[i+4]==0):
                poz[i+4]=poz[i+8]
                poz[i+8]=poz[i+12]
                poz[i+12]=0
            elif (poz[i]==0 and poz[i+4]!=poz[i+8] and poz[i+8]!=poz[i+12]):
                  poz[i]=poz[i+4]
                  poz[i+4]=poz[i+8]
                  poz[i+8]=poz[i+12]
                  poz[i+12]=0

    elif (x=='s'):
        for i in range(0,4):
            if (poz[i]==poz[i+12] and poz[i+8]==0 and poz[i+4]==0 and poz[i+12]!=0):
                poz[i+12]=poz[i+12]*2
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i]==poz[i+8] and poz[i+12]==0 and poz[i+4]==0 and poz[i+8]!=0):
                poz[i+12]=poz[i]*2
                poz[i+8]=0
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i]!=poz[i+8] and poz[i+12]==0 and poz[i+4]==0 and poz[i+8]!=0 and poz[i]!=0):
                poz[i+12]=poz[i+8]
                poz[i+8]=poz[i]
                poz[i]=0
            elif (poz[i]==poz[i+4] and poz[i+12]==0 and poz[i+8]==0 and poz[i+4]!=0):
                poz[i+12]=poz[i]*2
                poz[i+4]=0
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i]==poz[i+8] and poz[i+12]!=0 and poz[i+12]!=poz[i] and poz[i+4]==0):
                poz[i+8]=poz[i+8]*2
                poz[i]=0
                score = score + poz[i+8]
            elif (poz[i+12]!=poz[i+8] and poz[i+8]==poz[i+4] and poz[i+12]!=0 and poz[i+8]!=0):
                poz[i+8]=poz[i+8]*2
                poz[i+4]=poz[i]
                poz[i]=0
                score = score + poz[i+8]
            elif (poz[i]==poz[i+4] and poz[i+12]==poz[i+8] and poz[i+12]!=0 and poz[i+4]!=0):
                poz[i+12]=poz[i+12]*2
                poz[i+8]=poz[i+4]*2
                poz[i+4]=0
                poz[i]=0
                score = score + poz[i+12] + poz[i+8]
            elif (poz[i]==poz[i+4] and poz[i+12]!=0 and poz[i+8]!=0 and poz[i+12]!=poz[i+8]):
                poz[i+4]=poz[i+4]*2
                poz[i]=0
                score = score + poz[i+4]
            elif (poz[i]==poz[i+4] and poz[i+12]==0 and poz[i+8]!=0):
                poz[i+12]=poz[i+8]
                poz[i+8]=poz[i+4]*2
                poz[i+4]=0
                poz[i]=0
                score = score + poz[i+8]
            elif (poz[i+12]==poz[i+8] and poz[i+4]!=0 and poz[i+12]!=0):
                poz[i+12]=poz[i+12]*2
                poz[i+8]=poz[i+4]
                poz[i+4]=poz[i]
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i+4]==poz[i+12] and poz[i+8]==0 and poz[i+12]!=0):
                poz[i+12]=poz[i+12]*2
                poz[i+4]=0
                poz[i+8]=poz[i]
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i+4]==poz[i+8] and poz[i+12]==0 and poz[i+8]!=0):
                poz[i+12]=poz[i+8]*2
                poz[i+8]=poz[i]
                poz[i+4]=0
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i+4]==poz[i+8] and poz[i+12]!=0 and poz[i+8]!=0):
                poz[i+8]=poz[i+8]*2
                poz[i+4]=poz[i]
                poz[i]=0
                score = score + poz[i+8]
            elif (poz[i+8]==poz[i+12] and poz[i+4]==0 and poz[i+12]!=0):
                poz[i+12]=poz[i+12]*2
                poz[i+8]=poz[i]
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i+8]==poz[i+12] and poz[i+4]!=0 and poz[i+12]!=0):
                poz[i+12]=poz[i+12]*2
                poz[i+8]=poz[i+4]
                poz[i+4]=poz[i]
                poz[i]=0
                score = score + poz[i+12]
            elif (poz[i]!=0 and poz[i+12]==0 and poz[i+8]==0 and poz[i+4]==0):
                poz[i+12]=poz[i]
                poz[i]=0
            elif (poz[i+12]!=poz[i] and poz[i+8]==0 and poz[i+4]==0):
                poz[i+8]=poz[i]
                poz[i+4]=0
                poz[i]=0
            elif (poz[i]!=poz[i+8] and poz[i+8]!=0 and poz[i]!=0 and poz[i+4]==0 and poz[i+12]==0):
                poz[i+12]==poz[i+8]
                poz[i+8]=poz[i]
                poz[i]=0
            elif (poz[i]!=poz[i+8] and poz[i+8]!=0 and poz[i]!=0  and poz[i+8]!=poz[i+12] and poz[i+4]==0 and poz[i+12]!=0):
                poz[i+4]=poz[i]
                poz[i]=0
            elif (poz[i+12]!=poz[i] and poz[i+8]==0 and poz[i+4]==0):
                poz[i+8]=poz[i]
                poz[i+4]=0
                poz[i]=0
            elif (poz[i+12]==0 and poz[i+8]==0 and poz[i+4]!=poz[i]):
                poz[i+12]=poz[i+4]
                poz[i+8]=poz[i]
                poz[i+4]=0
                poz[i]=0
            elif (poz[i+12]!=poz[i+4] and poz[i+8]==0):
                poz[i+8]=poz[i+4]
                poz[i+4]=poz[i]
                poz[i]=0
            elif (poz[i+12]!=poz[i+8] and poz[i+12]!=0 and poz[i+4]==0 and poz[i]!=poz[i+8]):
                poz[i+4]=poz[i]
                poz[i]=0
            elif (poz[i+12]==0 and poz [i+8]==0 and poz[i+4]!=0 and poz[i+4]!=poz[i]):
                poz[i+12]=poz[i+4]
                poz[i+8]=poz[i]
                poz[i+4]=0
                poz[i]=0
            elif (poz[i+12]!=poz[i+4] and poz[i+12]!=0 and poz[i+4]!=0 and poz[i+8]==0):
                poz[i+8]=poz[i+4]
                poz[i+4]=poz[i]
                poz[i]=0
            elif (poz[i+12]==0 and poz[i+4]!=poz[i+8] and poz[i+4]!=poz[i]):
                  poz[i+12]=poz[i+8]
                  poz[i+8]=poz[i+4]
                  poz[i+4]=poz[i]
                  poz[i]=0

    elif(x=='d'):
        for i in range(0,13,4):
            if (poz[i]==poz[i+3] and poz[i+2]==0 and poz[i+1]==0 and poz[i+3]!=0):
                poz[i+3]=poz[i+3]*2
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i]==poz[i+2] and poz[i+3]==0 and poz[i+1]==0 and poz[i+2]!=0):
                poz[i+3]=poz[i]*2
                poz[i+2]=0
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i+2]!=poz[i] and poz[i+1]==0 and poz[i+3]==0 and poz[i+2]!=0 and poz[i]!=0):
                poz[i+3]=poz[i+2]
                poz[i+2]=poz[i]
                poz[i]=0
            elif (poz[i]==poz[i+1] and poz[i+3]==0 and poz[i+2]==0 and poz[i+1]!=0):
                poz[i+3]=poz[i]*2
                poz[i+1]=0
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i]==poz[i+2] and poz[i+3]!=0 and poz[i+3]!=poz[i] and poz[i+1]==0):
                poz[i+2]=poz[i+2]*2
                poz[i]=0
                score = score + poz[i+2]
            elif (poz[i+3]!=poz[i+2] and poz[i+2]==poz[i+1] and poz[i+3]!=0 and poz[i+2]!=0):
                poz[i+2]=poz[i+2]*2
                poz[i+1]=poz[i]
                poz[i]=0
                score = score + poz[i+2]
            elif (poz[i]==poz[i+1] and poz[i+3]==poz[i+2] and poz[i+3]!=0 and poz[i+1]!=0):
                poz[i+3]=poz[i+3]*2
                poz[i+2]=poz[i+1]*2
                poz[i+1]=0
                poz[i]=0
                score = score + poz[i+3] + poz[i+2]
            elif (poz[i]==poz[i+1] and poz[i+3]!=0 and poz[i+2]!=0 and poz[i+3]!=poz[i+2]):
                poz[i+1]=poz[i+1]*2
                poz[i]=0
                score = score + poz[i+1]
            elif (poz[i]==poz[i+1] and poz[i+3]==0 and poz[i+2]!=0):
                poz[i+3]=poz[i+2]
                poz[i+2]=poz[i+1]*2
                poz[i+1]=0
                poz[i]=0
                score = score + poz[i+2]
            elif (poz[i+3]==poz[i+2] and poz[i+1]!=0 and poz[i+3]!=0):
                poz[i+3]=poz[i+3]*2
                poz[i+2]=poz[i+1]
                poz[i+1]=poz[i]
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i+1]==poz[i+3] and poz[i+2]==0 and poz[i+3]!=0):
                poz[i+3]=poz[i+3]*2
                poz[i+1]=0
                poz[i+2]=poz[i]
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i+1]==poz[i+2] and poz[i+3]==0 and poz[i+2]!=0):
                poz[i+3]=poz[i+2]*2
                poz[i+2]=poz[i]
                poz[i+1]=0
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i+1]==poz[i+2] and poz[i+3]!=0 and poz[i+2]!=0):
                poz[i+2]=poz[i+2]*2
                poz[i+1]=poz[i]
                poz[i]=0
                score = score + poz[i+2]
            elif (poz[i+2]==poz[i+3] and poz[i+1]==0 and poz[i+3]!=0):
                poz[i+3]=poz[i+3]*2
                poz[i+2]=poz[i]
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i+2]==poz[i+3] and poz[i+1]!=0 and poz[i+3]!=0):
                poz[i+3]=poz[i+3]*2
                poz[i+2]=poz[i+1]
                poz[i+1]=poz[i]
                poz[i]=0
                score = score + poz[i+3]
            elif (poz[i]!=0 and poz[i+3]==0 and poz[i+2]==0 and poz[i+1]==0):
                poz[i+3]=poz[i]
                poz[i]=0
            elif (poz[i+3]!=poz[i] and poz[i+2]==0 and poz[i+1]==0):
                poz[i+2]=poz[i]
                poz[i+1]=0
                poz[i]=0
            elif (poz[i+3]!=poz[i] and poz[i+2]!=0 and poz[i+1]==0):
                poz[i+1]=poz[i]
                poz[i]=0
            elif (poz[i]!=poz[i+2] and poz[i+2]!=0 and poz[i]!=0 and poz[i+1]==0 and poz[i+3]==0):
                poz[i+3]==poz[i+2]
                poz[i+2]=poz[i]
                poz[i]=0
            elif (poz[i]!=poz[i+2] and poz[i+2]!=0 and poz[i]!=0  and poz[i+2]!=poz[i+3] and poz[i+1]==0 and poz[i+3]!=0):
                poz[i+1]=poz[i]
                poz[i]=0        
            elif (poz[i+3]==0 and poz[i+2]==0 and poz[i+1]!=poz[i]):
                poz[i+3]=poz[i+1]
                poz[i+2]=poz[i]
                poz[i+1]=0
                poz[i]=0
            elif (poz[i+3]!=poz[i+1] and poz[i+2]==0):
                poz[i+2]=poz[i+1]
                poz[i+1]=poz[i]
                poz[i]=0
            elif (poz[i+3]!=poz[i+2] and poz[i+3]!=0 and poz[i+1]==0 and poz[i]!=poz[i+2]):
                poz[i+1]=poz[i]
                poz[i]=0
            elif (poz[i+3]==0 and poz [i+2]==0 and poz[i+1]!=0 and poz[i+1]!=poz[i]):
                poz[i+3]=poz[i+1]
                poz[i+2]=poz[i]
                poz[i+1]=0
                poz[i]=0
            elif (poz[i+3]!=poz[i+1] and poz[i+3]!=0 and poz[i+1]!=0 and poz[i+2]==0):
                poz[i+2]=poz[i+1]
                poz[i+1]=poz[i]
                poz[i]=0
            elif (poz[i+3]==0 and poz[i+2]!=poz[i+1] and poz[i+1]!=poz[i]):
                  poz[i+3]=poz[i+2]
                  poz[i+2]=poz[i+1]
                  poz[i+1]=poz[i]
                  poz[i]=0

    elif(x=='a'):
        for i in range(0,13,4):
            if (poz[i+3]==poz[i] and poz[i+1]==0 and poz[i+2]==0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+3]==poz[i+1] and poz[i]==0 and poz[i+2]==0 and poz[i+1]!=0):
                poz[i]=poz[i+3]*2
                poz[i+1]=0
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+1]!=poz[i+3] and poz[i]==0 and poz[i+2]==0 and poz[i+1]!=0 and poz[i+3]!=0):
                poz[i]=poz[i+1]
                poz[i+1]=poz[i+3]
                poz[i+3]=0
            elif (poz[i+3]==poz[i+2] and poz[i]==0 and poz[i+1]==0 and poz[i+2]!=0):
                poz[i]=poz[i+3]*2
                poz[i+2]=0
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+3]==poz[i+1] and poz[i]!=0 and poz[i]!=poz[i+3] and poz[i+2]==0):
                poz[i+1]=poz[i+1]*2
                poz[i+3]=0
                score = score + poz[i+1]
            elif (poz[i]!=poz[i+1] and poz[i+1]==poz[i+2] and poz[i]!=0 and poz[i+1]!=0):
                poz[i+1]=poz[i+1]*2
                poz[i+2]=poz[i+3]
                poz[i+3]=0
                score = score + poz[i+1]
            elif (poz[i+3]==poz[i+2] and poz[i]==poz[i+1] and poz[i]!=0 and poz[i+2]!=0):
                poz[i]=poz[i]*2
                poz[i+1]=poz[i+2]*2
                poz[i+2]=0
                poz[i+3]=0
                score = score + poz[i] + poz[i+1]
            elif (poz[i+3]==poz[i+2] and poz[i]!=0 and poz[i+1]!=0 and poz[i]!=poz[i+1]):
                poz[i+2]=poz[i+2]*2
                poz[i+3]=0
                score = score + poz[i+2]
            elif (poz[i+3]==poz[i+2] and poz[i]==0 and poz[i+1]!=0):
                poz[i]=poz[i+1]
                poz[i+1]=poz[i+2]*2
                poz[i+2]=0
                poz[i+3]=0
                score = score + poz[i+1]
            elif (poz[i]==poz[i+1] and poz[i+2]!=0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+1]=poz[i+2]
                poz[i+2]=poz[i+3]
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+2]==poz[i] and poz[i+1]==0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+2]=0
                poz[i+1]=poz[i+3]
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+2]==poz[i+1] and poz[i]==0 and poz[i+1]!=0):
                poz[i]=poz[i+1]*2
                poz[i+1]=poz[i+3]
                poz[i+2]=0
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+2]==poz[i+1] and poz[i]!=0 and poz[i+1]!=0):
                poz[i+1]=poz[i+1]*2
                poz[i+2]=poz[i+3]
                poz[i+3]=0
                score = score + poz[i+1]
            elif (poz[i+1]==poz[i] and poz[i+2]==0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+1]=poz[i+3]
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+1]==poz[i] and poz[i+2]!=0 and poz[i]!=0):
                poz[i]=poz[i]*2
                poz[i+1]=poz[i+2]
                poz[i+2]=poz[i+3]
                poz[i+3]=0
                score = score + poz[i]
            elif (poz[i+3]!=0 and poz[i]==0 and poz[i+1]==0 and poz[i+2]==0):
                poz[i]=poz[i+3]
                poz[i+3]=0
            elif (poz[i]!=poz[i+3] and poz[i+1]==0 and poz[i+2]==0):
                poz[i+1]=poz[i+3]
                poz[i+2]=0
                poz[i+3]=0
            elif (poz[i]!=poz[i+3] and poz[i+1]!=0 and poz[i+2]==0):
                poz[i+2]=poz[i+3]
                poz[i+3]=0
            elif (poz[i+3]!=poz[i+1] and poz[i+1]!=0 and poz[i+3]!=0 and poz[i+2]==0 and poz[i]==0):
                poz[i]==poz[i+1]
                poz[i+1]=poz[i+3]
                poz[i+3]=0
            elif (poz[i+3]!=poz[i+1] and poz[i+1]!=0 and poz[i+3]!=0  and poz[i+1]!=poz[i] and poz[i+2]==0 and poz[i]!=0):
                poz[i+2]=poz[i+3]
                poz[i+3]=0        
            elif (poz[i]==0 and poz[i+1]==0 and poz[i+2]!=poz[i+3]):
                poz[i]=poz[i+2]
                poz[i+1]=poz[i+3]
                poz[i+2]=0
                poz[i+3]=0
            elif (poz[i]!=poz[i+2] and poz[i+1]==0):
                poz[i+1]=poz[i+2]
                poz[i+2]=poz[i+3]
                poz[i+3]=0
            elif (poz[i]!=poz[i+1] and poz[i]!=0 and poz[i+2]==0 and poz[i+3]!=poz[i+1]):
                poz[i+2]=poz[i+3]
                poz[i+3]=0
            elif (poz[i]==0 and poz [i+1]==0 and poz[i+2]!=0 and poz[i+2]!=poz[i+3]):
                poz[i]=poz[i+2]
                poz[i+1]=poz[i+3]
                poz[i+2]=0
                poz[i+3]=0
            elif (poz[i]!=poz[i+2] and poz[i]!=0 and poz[i+2]!=0 and poz[i+1]==0):
                poz[i+1]=poz[i+2]
                poz[i+2]=poz[i+3]
                poz[i+3]=0
            elif (poz[i]==0 and poz[i+1]!=poz[i+2] and poz[i+2]!=poz[i+3]):
                  poz[i]=poz[i+1]
                  poz[i+1]=poz[i+2]
                  poz[i+2]=poz[i+3]
                  poz[i+3]=0
