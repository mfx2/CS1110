# models.py
# Michael Xiao - mfx2 and Debo Adebola - aaa292
# 4th December 2016
"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random 
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.


class Paddle(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A NEW PADDLE
    def __init__(self):
        GRectangle.__init__(self, x=GAME_WIDTH/2, y=PADDLE_OFFSET+(PADDLE_HEIGHT/2),
                            width=PADDLE_WIDTH,height=PADDLE_HEIGHT,
                            linecolor=colormodel.BLACK, fillcolor=colormodel.BLACK)       

    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS
    def move(self,position):
        """Moves the paddle to a new position"""
        assert type(position) == int
        #print id(self) #trace that move is being called
        
        self.x = self.x + position

        if self.x < PADDLE_WIDTH / 2:
            self.x = PADDLE_WIDTH / 2
        if self.x > GAME_WIDTH-PADDLE_WIDTH / 2:
            self.x = GAME_WIDTH-PADDLE_WIDTH / 2
            
    def collide(self,ball):
        """Returns: True if the ball collides with the paddle
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball"""
        assert isinstance(ball, Ball)
        
        top = (ball.y)+(BALL_DIAMETER/2)
        bottom = (ball.y)-(BALL_DIAMETER/2)
        left = (ball.x)-(BALL_DIAMETER/2)
        right = (ball.x)+(BALL_DIAMETER/2)
        
        #if self.contains(right,top):
        #    return True
        if self.contains(right,bottom):
            return True
        #elif self.contains(left,top):
        #    return True
        elif self.contains(left,bottom):
            return True        
        else:
            return False
        
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Brick(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A BRICK
    def __init__(self,myx=2+(BRICK_WIDTH/2),myy=TOP_Y,myfillcolor=colormodel.RED):
        """Initializer to create brick"""
        GRectangle.__init__(self,x = myx, y=myy, width=BRICK_WIDTH,
                            height=BRICK_HEIGHT, fillcolor = myfillcolor)
                
    # METHOD TO CHECK FOR COLLISION
    def collidesTopBottom(self,ball):
        """Returns: True if the ball collides with this brick
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball"""
        assert isinstance(ball, Ball)
        
        top = (ball.y)+(BALL_DIAMETER/2)
        bottom = (ball.y)-(BALL_DIAMETER/2)
        left = (ball.x)-(BALL_DIAMETER/2)
        right = (ball.x)+(BALL_DIAMETER/2)
        
        if self.contains(right,top):
            return True
        elif self.contains(right,bottom):
            return True
        elif self.contains(left,top):
            return True
        elif self.contains(left,bottom):
            return True        
        else:
            return False
    
    def collidesSide(self,ball):
        """Returns: True if the ball collides with this brick
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball"""
        assert isinstance(ball, Ball)
        
        top = (ball.y)+(BALL_DIAMETER/2)
        bottom = (ball.y)-(BALL_DIAMETER/2)
        left = (ball.x)-(BALL_DIAMETER/2)
        right = (ball.x)+(BALL_DIAMETER/2)
        
        if (self.left==right) or (self.right==left):
            if ((top >= self.bottom) and (bottom <= self.top)):
                return True
        else:
            return False
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Ball(GEllipse):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO SET RANDOM VELOCITY
    def __init__(self):
        """Initializer for the ball"""
        
        self._vx = random.uniform(1.0,5.0) 
        self._vx = self._vx * random.choice([-1, 1])
        self._vy = -4.0
        GEllipse.__init__(self, x=GAME_WIDTH/2, y=GAME_HEIGHT/2,
                          width=BALL_DIAMETER,height=BALL_DIAMETER,
                          linecolor=colormodel.BLACK,fillcolor=colormodel.BLACK)

    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    
    def moveBall(self):
        """Moves the ball and bounces it off edges of screen"""
        self.y = self.y + self._vy
        self.x = self.x + self._vx
        
        if self.top > GAME_HEIGHT:
            self._vy = - self._vy
                        
        if self.right > GAME_WIDTH:
            self._vx = -self._vx
        if self.left < 0:
            self._vx = -self._vx
                    
    def collideBallBrick(self, brick):
        """Bounces the ball in the opposite direction if it collides with a
        brick
        
        Parameter brick: brick that ball collides with
        Precondition: brick is a Brick object
        """
        assert isinstance(brick, Brick)
        
        if brick.collidesSide(self) == True:
            self._vx = - self._vx
        if brick.collidesTopBottom(self) == True:
            self._vy = - self._vy
        
    def collideBallPaddle(self, paddle):
        """Bounces the ball in the opposite direction if it collides with the
        paddle
        
        Parameter: paddle is player's paddle
        Precondition: paddle is Paddle object
        """
        assert isinstance(paddle, Paddle)
        
        if paddle.collide(self) == True:
            self._vy = - self._vy
            
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def ballBottom(self):
        """Returns True if the ball hits the bottom edge of screen"""
        if self.bottom <= 0:
            return True
        else:
            return False

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE
