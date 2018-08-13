import random

play = input('Press T to toss a coin')

heads = 0
tails = 0

def toss_coin():
    toss = random.randint(1,2)
    if(toss == 1):
        global heads
        heads += 1
        print('It was Heads')
    else:
        global tails
        tails += 1
        print("It was tails")


while play == 't':
    toss_coin()
    print('-------------------------------')
    print('|  Heads:  |  '+str(heads)+'  |')
    print('-------------------------------')
    print('|  Tails:  |  '+str(tails)+'  |')
    print('-------------------------------')
    play = input('Press T to toss a coin')
