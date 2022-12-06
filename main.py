import string
import re
from pprint import pprint


def day1_1():
    """
    Trouver le maximum de calories.
    Résultat : 69795
    """
    maxcal = 0
    tmp = 0
    with open('day1.txt') as f:
        for line in f:
            line = line.strip()
            if line == "":
                if tmp > maxcal:
                    maxcal = tmp
                tmp = 0
            else:
                tmp += int(line)
    return maxcal


def day1_2():
    """
    Trouver les 3 maximums de calories.
    Résultat : 208437
    """
    cal_list = []
    tmp = 0
    with open('day1.txt') as f:
        for line in f:
            line = line.strip()
            if line == "":
                cal_list.append(tmp)
                tmp = 0
            else:
                tmp += int(line)
    return sum(sorted(cal_list, reverse=True)[0:3])


def day2_1():
    """
    Calculer le score obtenu à pierre-feuille-ciseaux avec des règles particulières.
    Résultat : 11063
    """
    total = 0
    with open('day2.txt') as f:
        for line in f:
            line = line.strip().split()
            opp, me = line[0], line[1]
            if me == "X":  # rock
                total += 1
                if opp == "A":  # rock
                    total += 3
                elif opp == "C":  # scissors
                    total += 6
            elif me == "Y":  # paper
                total += 2
                if opp == "B":  # paper
                    total += 3
                elif opp == "A":  # rock
                    total += 6
            elif me == "Z":  # scissors
                total += 3
                if opp == "C":  # scissors
                    total += 3
                elif opp == "B":  # paper
                    total += 6
    return total


def day2_2():
    """
    Calculer le score obtenu à pierre-feuille-ciseaux avec des nouvelles règles.
    Résultat : 10349
    """
    total = 0
    dico = {"A": 1, "B": 2, "C": 3}  # rock paper scissors
    with open('day2.txt') as f:
        for line in f:
            line = line.strip().split()
            opp, me = line[0], line[1]
            if me == "X":  # lose
                total += 1 + (dico[opp] + 1) % 3
            elif me == "Y":  # draw
                total += dico[opp] + 3
            elif me == "Z":  # win
                total += 1 + dico[opp] % 3 + 6
    return total


def day3_1():
    """
    Renvoie la somme des priorités associées à chaque lettre présente dans les deux moitiés d'une liste de chaînes de
    caractères.
    Résultat : 8139
    """
    # init priorities
    priorities = {}
    for idx, letter in enumerate(string.ascii_letters):
        priorities[letter] = idx + 1
    duplicates = []
    total = 0
    with open('day3.txt') as f:
        for rucksack in f:
            rucksack = rucksack.strip()
            tmp1 = set(rucksack[:len(rucksack) // 2])
            tmp2 = set(rucksack[len(rucksack) // 2:])
            duplicates.append(tmp1.intersection(tmp2).pop())
    for letter in duplicates:
        total += priorities[letter]
    return total


def day3_2():
    """
    Renvoie la somme des priorités associées à chaque lettre présente dans les deux moitiés d'une liste de trois
    chaînes de caractères.
    Résultat : 2668
    """
    # init priorities
    priorities = {}
    for idx, letter in enumerate(string.ascii_letters):
        priorities[letter] = idx + 1
    duplicates_list = []
    total = 0

    with open('day3.txt') as f:
        lines = f.readlines()

    for idx in range(0, len(lines), 3):
        r1, r2, r3 = [set(s.strip()) for s in lines[idx: idx + 3]]
        duplicates_list.append(r1.intersection(r2).intersection(r3).pop())

    for letter in duplicates_list:
        total += priorities[letter]
    return total


def day4_1():
    """
    Résultat : 599
    """
    total = 0
    with open('day4.txt') as f:
        for line in f:
            e1, e2 = line.split(",")
            min1, max1 = [int(x) for x in e1.split("-")]
            min2, max2 = [int(x) for x in e2.split("-")]
            if min1 <= min2 and max2 <= max1:
                total += 1
            elif min2 <= min1 and max1 <= max2:
                total += 1
    return total


def day4_2():
    """
    Résultat : 928
    """
    total = 0
    with open('day4.txt') as f:
        for line in f:
            e1, e2 = line.split(",")
            min1, max1 = [int(x) for x in e1.split("-")]
            min2, max2 = [int(x) for x in e2.split("-")]
            if min1 <= min2 <= max1:
                total += 1
            elif min2 <= min1 <= max2:
                total += 1
    return total


def day5_1():
    """
    Résultat : 'LBLVVTVLP'
    """
    # TODO : Coder un parser plutôt que l'input hardcodée
    out = [
        ["W", "B", "D", "N", "C", "F", "J"],
        ["P", "Z", "V", "Q", "L", "S", "T"],
        ["P", "Z", "B", "G", "J", "T"],
        ["D", "T", "L", "J", "Z", "B", "H", "C"],
        ["G", "V", "B", "J", "S"],
        ["P", "S", "Q"],
        ["B", "V", "D", "F", "L", "M", "P", "N"],
        ["P", "S", "M", "F", "B", "D", "L", "R"],
        ["V", "D", "T", "R"]
    ]
    ret = ""
    with open('day5.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines[10:]]
    for line in lines:
        nb_to_move, source, target = [int(x) for x in re.findall("[0-9]+", line)]
        for i in range(int(nb_to_move)):
            out[target - 1].append(out[source - 1].pop())
    # pprint(out)
    for k in range(len(out)):
        ret += out[k][-1]
    return ret


def day5_2():
    """
    Résultat : 'TPFFBDRJD'
    """
    out = [
        ["W", "B", "D", "N", "C", "F", "J"],
        ["P", "Z", "V", "Q", "L", "S", "T"],
        ["P", "Z", "B", "G", "J", "T"],
        ["D", "T", "L", "J", "Z", "B", "H", "C"],
        ["G", "V", "B", "J", "S"],
        ["P", "S", "Q"],
        ["B", "V", "D", "F", "L", "M", "P", "N"],
        ["P", "S", "M", "F", "B", "D", "L", "R"],
        ["V", "D", "T", "R"]
    ]
    ret = ""
    with open('day5.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines[10:]]
    for line in lines:
        nb_to_move, source, target = [int(x) for x in re.findall("[0-9]+", line)]
        list_to_move = []
        for i in range(int(nb_to_move)):
            list_to_move.append(out[source - 1].pop())
        list_to_move.reverse()
        out[target - 1] += list_to_move
    # pprint(out)
    for k in range(len(out)):
        ret += out[k][-1]
    return ret


def day6(nb_char):
    """
    Résultat 1 : 1109
    Résultat 2 : 3695
    """
    with open('day6.txt') as f:
        string = f.read().strip()
    f = lambda msg, n: next(i + n for i in range(len(msg)) if len(set(msg[i:i + n])) == n)
    return f(string, nb_char)


if __name__ == "__main__":
    ret = day6(nb_char=4)
    pprint(ret)
