import unittest
#from unittest.result import TestResult
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    #sets up the game to play
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    #changed the test names to test_ so the program can identify what needs to be tested 

    #Gutterball is when 1 roll strikes 0 pins. Gutter game is when all 20 rolls strike 0 pins
    #def testGutterGame(self):
    #    for i in range(0, 20):
    #        self.game.rolls(0)
    #    assert self.game.score()==0

    #refactored code
    def test_GutterGame(self):
        self.rollMany(0, 20)
        assert self.game.score()==0


    #code represents all 20 rolls strikes 1 pin each time
    def test_AllOnes(self):
        self.rollMany(1,20)
        assert self.game.score()==20


    #Open frame is when the player fails to knock down all 10 pins during a frame
    def test_OpenFrame(self):  #renamed from OneSpare to OpenFrame 
        #self.game.rolls(5)    #removed and refactored
        #self.game.rolls(5)    #removed and refactored
        self.rollMany(5, 2)    #refactored to minimise code repitition
        self.game.rolls(3)
        self.rollMany(0, 17)
        assert self.game.score()==13


    #the following code is testing for multiple values 
    def test_OneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0, 16)
        assert self.game.score()==24


    #the code is when all rolls gets a srikes (10) which gives you 2 extra rolls
    def test_PerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score()==300


    #the following code is testing for when all rolls, strike 5 pins
    def test_AllSpare(self):     #changed name appropriately
        self.rollMany(5,21)
        assert self.game.score()==150


    #created code with error for testing
    def test_GutterGame(self):
        self.rollMany(6, 20)
        assert self.game.score()==0


    #created code with error for testing
    def test_PerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score()==3


    #created code with error for testing
    def test_OneStrike(self):
        self.game.rolls(3)
        self.rollMany(10, 2)
        self.rollMany(0, 15)
        assert self.game.score()==24


    #the method for striking the same amount of pins multiple times
    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rolls(pins)


    #runs the unit tests
    #not working during to directory issues that I cannot work out
    if __name__ == '__main__':
        unittest.main()


