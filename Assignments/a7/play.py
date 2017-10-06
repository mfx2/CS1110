# play.py
# Michael Xiao - mfx2 and Debo Adebola - aaa292
# 4th December 2016
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *


# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
        _tries  [int >= 0]: the number of tries left 
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        _score  [int >=0]: shows number of blocks hit
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def setBrick(self,x,y,color):
        """Returns a Brick object with center (x,y) of colour color
        Parameter x: x position of brick
        Precondition: x is a number
        
        Parameter y: y position of brick
        Precondition: y is a number
        
        Parameter color: color of brick
        Precondition: color is a colormodel color
        """
        assert type(x)==int or type(x)==float
        assert type(y)==int or type(y)==float
        assert color in [colormodel.WHITE,colormodel.LIGHT_GRAY,colormodel.GRAY,
                         colormodel.DARK_GRAY,colormodel.BLACK,colormodel.RED,
                         colormodel.PINK,colormodel.YELLOW,colormodel.ORANGE,
                         colormodel.GREEN,colormodel.BLUE,colormodel.MAGENTA,
                         colormodel.CYAN]
        
        return Brick(x,y,color)
        
    def getPaddle(self):
        """Gets the single Paddle object"""
        return Paddle()
    
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    def __init__(self):
        """Initializer for the brick"""
        brick = []
        colour = [colormodel.RED, colormodel.RED, colormodel.ORANGE,
                  colormodel.ORANGE,colormodel.YELLOW, colormodel.YELLOW,
                  colormodel.GREEN,colormodel.GREEN, colormodel.CYAN,
                  colormodel.CYAN]
      
        for vert in range(BRICK_ROWS):
            color = colour[vert]
      
            for hor in range(BRICKS_IN_ROW):
                x= 2 + (BRICK_WIDTH/2) + ((GAME_WIDTH / BRICKS_IN_ROW)*hor)         
                y= TOP_Y - ((BRICK_HEIGHT+BRICK_SEP_V)*vert)
                brick.append(self.setBrick(x,y,color))
        
        print 'There are '+str(len(brick))+' brick(s) in this game.' 
        
        self._bricks = brick
        self._paddle = self.getPaddle()
        self._ball = None
        self._tries = NUMBER_TURNS
        self._score = 0
    
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    def updatePaddle(self, selfinput):
        """Moves the paddle with left and right keys
        Parameter selfinput: input from user
        Precondition: input is instance of GInput
        """
        assert isinstance(selfinput,GInput)
        position = 0
        
        if selfinput.is_key_down('right'):
            position = 5
        if selfinput.is_key_down('left'):
            position = -5
        
        self._paddle.move(position) 
    
    def serveBall(self):
        """Serves the ball"""
        self._ball = Ball()
        
    def updateBall(self):
        """Moves the ball and controls bouncing physics"""
        
        self._ball.moveBall()
        self._ball.collideBallPaddle(self._paddle)
        for a in self._bricks:
            self._ball.collideBallBrick(a)
        
    def updateBricks(self):
        """Removes bricks when they have been hit by the ball"""
        for a in self._bricks:
            if (a.collidesTopBottom(self._ball) == True) or \
            (a.collidesSide(self._ball) == True):
                self._score = self._score + 1
                self._bricks.remove(a)

      
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    def drawBricks(self, view):
        """Draws the bricks on screen"""
        for a in self._bricks:
            a.draw(view)
        
    def drawPaddle(self, view):
        """Draws the paddle on screen"""
        self._paddle.draw(view)

    def drawBall(self, view):
        """Draws the ball on screen"""
        self._ball.draw(view)
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION - see method updateBall
    
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
    def updateLives(self):
        """Updates the number of attempts the player has left"""
        if self._ball.ballBottom() == True:
            self._tries = self._tries - 1
            return True 
            
    def returnLives(self):
        """Returns: the number or lives left"""
        return self._tries
    
    def returnBricks(self):
        """Returns: the number of bricks left"""
        return len(self._bricks)
