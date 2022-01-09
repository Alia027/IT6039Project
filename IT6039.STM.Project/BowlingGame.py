class BowlingGame:
    #constructor that creates a rolls array
    def __init__(self):
        self.rolls=[]


    #sets the code for the pins hit by the ball during roll
    def roll(self, pins):
        self.rolls.append(pins)


    #records the score
    def score(self):
        result = 0  
        rollIndex = 0
        #there are 10 frames per game, the player gets two rolls per frame
        for frameIndex in range(10):
            #checking if the rolls are within the 10 frames 
            if frameIndex in range(10):
                #strike score
                result += self.strikeScore(rollIndex)   #chnaged syntax to camel case
                #increments the roll index by 1
                rollIndex += 1
            #score for a spare
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                #checks the amount of frames has been played
                result += self.frameScore(rollIndex)
            rollIndex +=2
            #returns score
            return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex]==10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]==10
    
    def strikeScore(self, rollIndex):
        return 10+ self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    def spareScore(self, rollIndex):
        return 10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]

