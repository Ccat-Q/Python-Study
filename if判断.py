#输入猫猫饥饿值来判断吃不吃猫粮
Hungry_Index  = int(input("猫猫饥饿值："))
#if判断
if Hungry_Index >= 60:
    print("不用加猫粮")
else: #Hungry_Index < 60
    print("快去加猫粮")
