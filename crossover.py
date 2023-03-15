import random

from individual import Individual

cities = [(0, [2.8772042630674854, 0.6755146794164368]), (1, [0.7631050888945423, 7.977539609320381]), (2, [6.12592833160131, 8.015152032135182]), (3, [8.224559943685591, 4.810170116581878]), (4, [3.167443707548707, 9.73465466560635]), (5, [4.976426000285059, 5.161592573052834]), (6, [4.043780744116312, 5.507745524984201]), (7, [9.17387079706267, 1.7895321632702943]), (8, [1.3088811144982282, 5.532109252200708]), (9, [4.842043477648861, 2.2851486712281077])]

mother = Individual(cities)
father = Individual(cities)

def isvalid(child):
    return len(set(child))==10
def crossover(mother, father):
    l = len(mother)

    # cutoff = random.sample(range(0,l),2)
    # cutoff = sorted(cutoff)
    cutoff = [3,6]

    head_mother = mother[:cutoff[0]]
    middle_mother = mother[cutoff[0]:cutoff[1]]
    tail_mother = mother[cutoff[1]:]
    print(head_mother, middle_mother, tail_mother)

    head_father = father[:cutoff[0]]
    middle_father = father[cutoff[0]:cutoff[1]]
    tail_father = father[cutoff[1]:]
    print(head_father, middle_father, tail_father)
    middle_child1 = middle_mother
    middle_child2 = middle_father
    head_child1 = [None] * len(head_mother)
    head_child2 = [None] * len(head_mother)
    tail_child1 = [None] * len(tail_mother)
    tail_child2 = [None] * len(tail_mother)
    for i in range(len(head_mother)):
        if head_father[i] not in middle_child1 and head_father[i] not in head_child1:
            head_child1[i] = head_father[i]
        elif head_mother[i] not in middle_child1 and head_mother[i] not in head_child1:
            head_child1[i] = head_mother[i]
        else:
            head_child1[i] = middle_child2[middle_child1.index(head_mother[i])]
        
        
        if head_mother[i] not in middle_child2 and head_mother[i] not in head_child2:
            head_child2[i] = head_mother[i]
        elif head_father[i] not in middle_child2 and head_father[i] not in head_child2:
            head_child2[i] = head_father[i]
        else:
            head_child2[i] = middle_child1[middle_child2.index(head_father[i])]

    for i in range(len(tail_mother)):
        if tail_father[i] not in middle_child1+head_child1+tail_child1:
            tail_child1[i] = tail_father[i]
        elif tail_mother[i] not in middle_child1+head_child1+tail_child1:
            tail_child1[i] = tail_mother[i]
        elif tail_mother[i] in middle_child1:
            tail_child1[i] = middle_child2[middle_child1.index(tail_mother[i])]
        elif tail_mother[i] in head_child1:
            tail_child1[i] = head_mother[head_child1.index(tail_mother[i])]

        if tail_mother[i] not in middle_child2+head_child2+tail_child2:
            tail_child2[i] = tail_mother[i]
        elif tail_father[i] not in middle_child2+head_child2+tail_child2:
            tail_child2[i] = tail_father[i]
        elif tail_father[i] in middle_child2:
            tail_child2[i] = middle_child1[middle_child2.index(tail_father[i])]
        elif tail_father[i] in head_child2:
            tail_child2[i] = head_father[head_child2.index(tail_father[i])]
    print(head_child1, middle_child1, tail_child1)
    print(head_child2, middle_child2, tail_child2)
    child1 = head_child1+middle_child1+tail_child1
    child2 = head_child2+middle_child2+tail_child2
    assert isvalid(child1)
    assert isvalid(child2)
crossover(mother.solution, father.solution)
crossover([7,3,2,1,4,5,6,0,8,9], [4,0,2,1,5,6,7,8,9,3])