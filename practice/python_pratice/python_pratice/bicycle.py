"""
需求文档：
写一个Bicycle(自行车)类,有run(骑行)方法,
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，
参数传入, 同时有两个方法：
1）fill_charge(vol) 用来充电, vol 为电量
2）run(km) 方法用于骑行,每骑行10km消耗电量1度
,当电量消耗尽时调用Bicycle的run方法骑行，
通过传入的骑行里程数，显示骑行结果
"""

class Bicycle:
    def run(self,km):
        print(f'用脚骑行了{km}公里，好累呀')

class Ebicycle(Bicycle):

    def __init__(self,valume):
        self.valume=valume

    def file_charge(self,add_valume):
        current_valume=self.valume+add_valume
    def run(self,km):
        ebicycle_km=self.valume*10
        if ebicycle_km >= km:
            free_valume=self.valume-km/10
            print(f'使用电动车骑行了{km},剩余{free_valume}度电量')
        else:
            bicycle_km=km-ebicycle_km
            super().run(bicycle_km)



ebike=Ebicycle(250)
ebike.run(2000)

