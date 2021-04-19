#coding:utf-8

class Hero:
    hp=0
    power=0
    name=''
    speed_line=''
    def figtht(self,enemy_hp,enemy_power):
        my_final_hp=self.hp-enemy_power
        enemy_final_hp=enemy_hp-self.power
        if my_final_hp > enemy_final_hp:
            print(f'{self.name}赢了')
        elif my_final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("打平了")
        print(f'{self.name}的血量还剩{my_final_hp}，敌人的血量还剩{enemy_final_hp}')

    def speedLine(self):
        print(f'{self.name}说：{self.speed_line}')