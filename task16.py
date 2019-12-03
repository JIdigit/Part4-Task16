from random import randint
from random import random
# def create_a_hero(hero):
#     # hero = input()
#     return hero

class Hero():
    level = 1

    def __init__(self, name, number, team):
        self.name = name
        self.number = number
        self.team = team
        
        
    def level_increase(self):
        self.level +=1




class Soldier(Hero):
    

    def __init__(self,name, number, team):
        self.number_of_soldiers = []
        Hero.__init__(self, name, number, team)

    def level_up(self):
        self.level_increase()

    def following_hero(self):
        try:
            return f'Soldier number { self.number_of_soldiers[randint(0, len(self.number_of_soldiers))]} follows Hero {self.name}'
        except IndexError:
        
            print('No soldiers in the team')
            return 'Sorry'
        
        




def main():

    team1 = Soldier('ShadowFiend', 123, 'team1')
    team2 = Soldier('Lina', 228, 'team2')

    while True:
        for i in range(randint(1,19)):
            rand_int = randint(0,2)
            if rand_int == 0:
                team1.number_of_soldiers.append(randint(0, 1000))
                # print(len(soldiers_team2.number_of_soldiers))
            elif rand_int == 1:
                team2.number_of_soldiers.append(randint(1000,2000))
            else:
                pass
        
        
        if len(team1.number_of_soldiers) > len(team2.number_of_soldiers):
            team1.level_up()
        elif len(team1.number_of_soldiers) < len(team2.number_of_soldiers):
            team2.level_up()
        
            
        print(f'Hero1 lvl: {team1.level} and hero2: {team2.level}')
        quit = input('Press  -Y- to finish the game or -F- to make soldier follow a Hero -any other key to continue-: ')
        if quit.lower() == 'y':
            break
        elif quit.lower() == 'f':
            print(team1.following_hero())
        else:
            print('One more ROUND')
            continue
    # input('Do you want to continue?') 

    # ####### ПРОБЛЕМА В ТОМ ЧТО СОЛДАТЫ НЕ УНИКАЛЬНЫ #########

    
        
        
        

    
    
        
    
        


    













if __name__ == '__main__':
    main()


