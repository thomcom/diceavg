import random

random.seed()

class DiceAvg:
    def RollDice(self,dicenum):
        rolledDice = []
        for i in range(dicenum):
            rolledDice.append(random.randint(1,6))
        return(rolledDice)
    def AverageRolls(self,rollcount,dicenum):
        rollSum = 0.0
        for i in range(rollcount):
            roll = self.RollDice(dicenum)
            roll.sort()
            rollSum = rollSum + sum(roll[-3:])
        return(rollSum / rollcount)
