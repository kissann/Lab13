import t1
import math
class Person:
    def __init__(self,healf,attack,protection,name="Dragon"):
        self.healf=healf
        self.attack=attack
        self.protection=protection
        self.name=name
class Battle:
    def __init__(self,her_a,drag_a,her_pr,drag_pr):
        self.her_a=her_a
        self.drag_a=drag_a
        self.her_pr=her_pr
        self.drag_pr=drag_pr
def main():
    name = input("Введите имя героя")
    heroes=Person(int(t1.healf()),t1.attack(10),t1.protection(10),name)
    drugon=Person(int(t1.healf()),t1.attack(10),t1.protection(10))
    round = min(drugon.healf, heroes.healf)

    round = 1
    print("Жизнь героя " + str(heroes.healf))
    flag = True
    while flag:
        if (drugon.healf > 0) or (heroes.healf > 0):
            print("Раунд" + str(round) + "\n")
            battle=Battle(t1.attack(heroes.attack),t1.attack(drugon.attack),t1.attack(heroes.protection),t1.attack(drugon.protection))

            act_h = input("Ваши действия герой? (Attac, Prot)")
            act_d = t1.drag_act()
            if (act_h == 'Attac' and act_d == 'Attac'):
                print("Дракон тоже атакует")
                drugon.healf = drugon.healf - battle.her_a / 2
                heroes.healf = heroes.healf - battle.her_a / 2
            if (act_h == 'Prot' and act_d == 'Prot'):
                print("Дракон тоже выбрал стратегию защиты")
            if (act_h == 'Attac' and act_d == 'Prot'):
                print("Дракон решил защитится")
                if battle.her_a > battle.drag_pr:
                    yron = battle.her_a - battle.drag_pr
                if battle.her_a < battle.drag_pr:
                    yron = 0
                drugon.healf= drugon.healf - yron
            if (act_h == 'Prot' and act_d == 'Attac'):
                print("Дракон атакует")
                if battle.drag_a > battle.her_pr:
                    yron = battle.her_a - battle.drag_pr
                if battle.drag_a < battle.her_pr:
                    yron = 0
                heroes.healf = heroes.healf- yron
            if (drugon.healf <= 0):
                print("Игра закончена Дракон сдох")
                flag = False
            if (heroes.healf <= 0):
                print("Игра закончена Герой сдох")
                flag = False
            round = round + 1
        print(heroes.healf)
        print(drugon.healf)
main()
