import os
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day7_Input.txt')
file = open(full_path,'r')
data = file.read()
data = data.split('\n')
### Part 1
labels = ['A','K','Q','J','T','9','8','7','6','5','4','3','2','1']
label_dict = {}
i = 0
for label in labels[::-1]:
    label_dict[label] = i
    i += 1

hands = [s.split(' ')[0] for s in data]
bids =  [s.split(' ')[1] for s in data]
hands_dict = {}
for i in range(0,len(hands)):
    hands_dict[hands[i]] = bids[i]
### card rank High Card = 0, One pair = 1, Two Pair = 2, Three of a kind = 3, full house = 4, 4 of a kind = 5, 5 of a kind = 6
def get_rank(hand):
    count_cards = [hand.count(s) for s in hand]
    if 5 in count_cards:
        return 6
    elif 4 in count_cards:
        return 5
    elif 3 in count_cards:
        if 2 in count_cards:
            return 4
        else:
            return 3
    elif 2 in count_cards:
        if len([s for s in count_cards if s==2]) == 4:
            return 2
        else:
            return 1
    else:
        return 0

def get_strength(hand):
    return [label_dict[s] for s in hand]

def hand_strength(hand):
    return (get_rank(hand),get_strength(hand))


hands.sort(key=lambda hand: hand_strength(hand))

i = 1
sum = 0
for hand in hands:
    sum += (i * int(hands_dict[hand]))
    i +=1
print(sum)


### Part 2
file = open(full_path,'r')
data = file.read()
data = data.split('\n')
labels = ['A','K','Q','J','T','9','8','7','6','5','4','3','2','1']
label_dict = {}
i = 1
for label in labels[::-1]:
    label_dict[label] = i
    i += 1

label_dict['J'] = 0

hands = [s.split(' ')[0] for s in data]
bids =  [s.split(' ')[1] for s in data]
hands_dict = {}
for i in range(0,len(hands)):
    hands_dict[hands[i]] = bids[i]
### card rank High Card = 0, One pair = 1, Two Pair = 2, Three of a kind = 3, full house = 4, 4 of a kind = 5, 5 of a kind = 6
def get_rank(hand):
    count_cards = [hand.count(s)for s in hand if not s=='J']
    nr_jokers = hand.count('J')
    if 5 in count_cards:
        return 6
    elif 4 in count_cards:
        if nr_jokers == 0:
            return 5
        else:
            return 6
    elif 3 in count_cards:
        if nr_jokers == 2:
            return 6
        elif nr_jokers == 0:
            if 2 in count_cards:
                return 4
            else:
                return 3
        else:
            return 5
    elif 2 in count_cards:
        if nr_jokers == 3:
            return 6
        elif nr_jokers == 2:
            return 5
        elif nr_jokers == 1:
            if len([s for s in count_cards if s==2]) == 4:
                return 4
            else:
                return 3
        elif nr_jokers == 0:
            if len([s for s in count_cards if s==2]) == 4:
                return 2
            else:
                return 1
    elif 1 in count_cards:
        if nr_jokers == 4:
            return 6
        if nr_jokers == 3:
            return 5
        if nr_jokers == 2:
            return 3
        if nr_jokers == 1:
            return 1
        else:
            return 0
    elif nr_jokers == 5:
        return 6
def get_strength(hand):
    return [label_dict[s] for s in hand]

def hand_strength(hand):
    return (get_rank(hand),get_strength(hand))


hands.sort(key=lambda hand: hand_strength(hand))

for hand in hands:
    if hand_strength(hand)[0] is None:
        print(hand)
        print(hand_strength(hand))

i = 1
sum = 0
for hand in hands:
    sum += (i * int(hands_dict[hand]))
    i +=1
print(sum)
