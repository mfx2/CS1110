# breakout.py
# Michael Xiao - mfx2 and Debo Adebola - aaa292
# Nov. 17, 2016
"""Primary module for Breakout application

This module contains the main controller class for the Breakout application. There is no
need for any any need for additional classes in this module.  If you need more classes, 
99% of the time they belong in either the play module or the models module. If you 
are ensure about where a new class should go, 
post a question on Piazza."""
from constants import *
from game2d import *
from play import *


# PRIMARY RULE: Breakout can only access attributes in play.py via getters/setters
# Breakout is NOT allowed to access anything in models.py

class Breakout(GameApp):
    """Instance is the primary controller for the Breakout App
    
    This class extends GameApp and implements the various methods necessary for processing 
    the player inputs and starting/running a game.
    
        Method start begins the application.
        
        Method update either changes the state or updates the Play object
        
        Method draw displays the Play object and any other elements on screen
    
    Because of some of the weird ways that Kivy works, you SHOULD NOT create an
    initializer __init__ for this class.  Any initialization should be done in
    the start method instead.  This is only for this class.  All other classes
    behave normally.
    
    Most of the work handling the game is actually provided in the class Play.
    Play should have a minimum of two methods: updatePaddle(input) which moves
    the paddle, and updateBall() which moves the ball and processes all of the
    game physics. This class should simply call that method in update().
    
    The primary purpose of this class is managing the game state: when is the 
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state.
    
    INSTANCE ATTRIBUTES:
        view    [Immutable instance of GView; it is inherited from GameApp]:
                the game view, used in drawing (see examples from class)
        input   [Immutable instance of GInput; it is inherited from GameApp]:
                the user input, used to control the paddle and change state
        _state  [one of STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE,
                STATE_LOSE]:
                the current state of the game represented a value from constants.py
        _game   [Play, or None if there is no game currently active]: 
                the controller for a single game, which manages the paddle, ball, and bricks
        _mssg   [GLabel, or None if there is no message to display]
                the currently active message
    
    STATE SPECIFIC INVARIANTS: 
        Attribute _game is only None if _state is STATE_INACTIVE.
        Attribute _mssg is only None if  _state is STATE_ACTIVE or STATE_COUNTDOWN.
    
    For a complete description of how the states work, see the specification for the
    method update().
    
    You may have more attributes if you wish (you might need an attribute to store
    any text messages you display on the screen). If you add new attributes, they
    need to be documented here.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        last_keys   [input.key_count, or 0 if there are no keys pressed]
        step        [int, counts the steps (60 per second)]
        _mssgscore  [GLabel or None] displays current score
    """
    
    # DO NOT MAKE A NEW INITIALIZER!
    
    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """Initializes the application.
        
        This method is distinct from the built-in initializer __init__ (which you 
        should not override or change). This method is called once the game is running. 
        You should use it to initialize any game specific attributes.
        
        This method should make sure that all of the attributes satisfy the given 
        invariants. When done, it sets the _state to STATE_INACTIVE and create a message 
        (in attribute _mssg) saying that the user should press to play a game."""
        
        self._state = STATE_INACTIVE
        self._game = None
        self._mssg = GLabel(x=240,y=310,
                            text='Welcome to Brick Breaker! Press any key to play',
                            font_size=20)
        self.last_keys = 0
        self.step = 0
        self._mssgscore = None
    
    def update(self,dt):
        """Animates a single frame in the game.
        
        It is the method that does most of the work. It is NOT in charge of playing the
        game.  That is the purpose of the class Play.  The primary purpose of this
        game is to determine the current state, and -- if the game is active -- pass
        the input to the Play object _game to play the game.
        
        As part of the assignment, you are allowed to add your own states.  However, at
        a minimum you must support the following states: STATE_INACTIVE, STATE_NEWGAME,
        STATE_COUNTDOWN, STATE_PAUSED, and STATE_ACTIVE.  Each one of these does its own
        thing, and so should have its own helper.  We describe these below.
        
        STATE_INACTIVE: This is the state when the application first opens.  It is a 
        paused state, waiting for the player to start the game.  It displays a simple
        message on the screen.
        
        STATE_NEWGAME: This is the state creates a new game and shows it on the screen.  
        This state only lasts one animation frame before switching to STATE_COUNTDOWN.
        
        STATE_COUNTDOWN: This is a 3 second countdown that lasts until the ball is 
        served.  The player can move the paddle during the countdown, but there is no
        ball on the screen.  Paddle movement is handled by the Play object.  Hence the
        Play class should have a method called updatePaddle()
        
        STATE_ACTIVE: This is a session of normal gameplay.  The player can move the
        paddle and the ball moves on its own about the board.  Both of these
        should be handled by methods inside of class Play (NOT in this class).  Hence
        the Play class should have methods named updatePaddle() and updateBall().
        
        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However, the game is
        still visible on the screen.
        
        STATE_LOSE: Like STATE_INACTIVE and STATE_PAUSED, this is a paused state when the
        game has ended. The brick(s) are still visible on the screen.
        
        STATE_WIN:  Like STATE_INACTIVE and STATE_PAUSED, this is a paused state when the
        player has won and the game has ended. The brick(s) are still visible on the screen.
        
        The rules for determining the current state are as follows.
        
        STATE_INACTIVE: This is the state at the beginning, and is the state so long
        as the player never presses a key.  In addition, the application switches to 
        this state if the previous state was STATE_ACTIVE and the game is over 
        (e.g. all balls are lost or no more bricks are on the screen).
        
        STATE_NEWGAME: The application switches to this state if the state was 
        STATE_INACTIVE in the previous frame, and the player pressed a key.
        
        STATE_COUNTDOWN: The application switches to this state if the state was
        STATE_NEWGAME in the previous frame (so that state only lasts one frame).
        
        STATE_ACTIVE: The application switches to this state after it has spent 3
        seconds in the state STATE_COUNTDOWN.
        
        STATE_PAUSED: The application switches to this state if the state was 
        STATE_ACTIVE in the previous frame, the ball was lost, and there are still
        some tries remaining.
        
        You are allowed to add more states if you wish. Should you do so, you should 
        describe them here.
        
        STATE_LOSE: The application switches to this state if the state was 
        STATE_ACTIVE in the previous frame, the ball was lost, and there are no tries
        some of the bricks still remain.
        
        STATE_WIN: The application switches to this state if the state was 
        STATE_ACTIVE in the previous frame and all of the bricks are eliminated.
        
        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        if self._state == STATE_INACTIVE:
            self.ifInactive()
               
        if self._state == STATE_NEWGAME:
            self.ifNew()
            
        if self._state == STATE_COUNTDOWN:
            self.ifCountdown()
        
        if self._state == STATE_ACTIVE:
            self.ifActive()
                
        if self._state == STATE_PAUSED:
            self.ifPaused()
        
        if self._state == STATE_LOSE:
            self.ifLose()
            
        if self._state == STATE_WIN:
            self.ifWin()
    
    def draw(self):
        """Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject.  To draw a GObject 
        g, simply use the method g.draw(self.view).  It is that easy!
        
        Many of the GObjects (such as the paddle, ball, and bricks) are attributes in Play. 
        In order to draw them, you either need to add getters for these attributes or you 
        need to add a draw method to class Play.  We suggest the latter.  See the example 
        subcontroller.py from class."""
        if self._state == STATE_INACTIVE:
             self._mssg.draw(self.view)
        if self._state == STATE_COUNTDOWN:
            self._mssg.draw(self.view)
            self._game.drawBricks(self.view)
            self._game.drawPaddle(self.view)
        if self._state == STATE_NEWGAME:
            self._game.drawBricks(self.view)
            self._game.drawPaddle(self.view)
        if self._state == STATE_ACTIVE:   
            self._game.drawBricks(self.view)
            self._game.drawPaddle(self.view)
            self._game.drawBall(self.view)
            self._mssg.draw(self.view)
            self._mssgscore.draw(self.view)
        if self._state == STATE_PAUSED:
            self._mssg.draw(self.view)
            self._game.drawBricks(self.view)
            self._game.drawPaddle(self.view)
            self._mssgscore.draw(self.view)
        if self._state == STATE_LOSE:
            self._game.drawBricks(self.view)
            self._mssg.draw(self.view)
        if self._state == STATE_WIN:
            self._game.drawBricks(self.view)
            self._mssg.draw(self.view)
            self._mssgscore.draw(self.view)


    # HELPER METHODS FOR THE STATES GO HERE
    def ifInactive(self):
        """Helper method for STATE_INACTIVE"""
        #Walker M. White (wmw2) used a similar system to do this in state.py
        curr_keys = self.input.key_count
        change = curr_keys > 0 and self.last_keys == 0
        
        if change:
            self._state = STATE_NEWGAME
        self.last_keys= curr_keys
        #End Walker White's help   
            
        self._game = None
        self._mssg = GLabel(x=240, y=310, linecolor=colormodel.BLACK,
                            text='WELCOME TO BRICK BREAKER! PRESS ANY KEY TO PLAY',
                            font_Size = 20)
    
    def ifNew(self):
        """Helper method for STATE_NEW"""
        self._mssg = None
        self._game = Play()
        self._state = STATE_COUNTDOWN
            
    def ifCountdown(self):
        """Helper method for STATE_COUNTDOWN"""
        self.step = self.step + 1
        self._mssg = GLabel(x=240, y=310, text='3', font_size=40)
            
        #Walker M. White (wmw2) used a similar system to do this in etch-a-sketch demo
        if 120 > self.step >= 60:
            self._mssg = GLabel(x=240, y=310, text='2', font_size=40)
        if 180 > self.step >= 120:
            self._mssg = GLabel(x=240, y=310, text='1', font_size=40)
        if self.step >= 180:
        #End Walker White's help
            self._game.serveBall()
            self._state = STATE_ACTIVE
            self.step = 0
            
        self._game.updatePaddle(self.input)
    
    def ifActive(self):
        """Helper method for STATE_ACTIVE"""
        self._game.updatePaddle(self.input)
        self._game.updateBall()
        self._game.updateBricks()
        
        self._mssgscore = GLabel(x=60, y=600, text='Score: '+str(self._game._score),
                                    font_size=25, linecolor = colormodel.BLACK)    
            
        if self._game.updateLives() == True:
            self._state = STATE_PAUSED
                        
        a = str(self._game.returnLives())
        if self._game.returnLives() == 3:
            self._mssg = GLabel(x=430, y=600, text=a+' lives left',
                                font_size=20, linecolor = colormodel.GREEN)
        elif self._game.returnLives() == 2:
            self._mssg = GLabel(x=430, y=600, text=a+' lives left',
                                font_size=20, linecolor = colormodel.ORANGE)
        elif self._game.returnLives() == 1:
            self._mssg = GLabel(x=420, y=600, text=a+' life left!!',
                                font_size=25, linecolor = colormodel.RED)
        else:
            self._state = STATE_LOSE
        
        if self._game.returnBricks() == 0:
            self._state = STATE_WIN
    
    def ifPaused(self):
        """Helper method for STATE_PAUSED"""
        if self._game.returnLives() == 2:
            a = '1 LIFE'
        elif self._game.returnLives() == 1:
            a = '2 LIVES'
            
        self._mssg = GLabel(x=240, y=310,
                            text=a+' LOST. PRESS ANY KEY TO RESUME',
                            font_size=24)
            
        curr_keys = self.input.key_count
        change = curr_keys > 0 and self.last_keys == 0
        
        if change:
            self._state = STATE_COUNTDOWN
        self.last_keys= curr_keys
    
    def ifLose(self):
        """Helper method for STATE_LOSE"""
        self._game.updateBricks()
        a = str(self._game.returnBricks())
            
        if self._game.returnBricks() > 1:
            b = 'You lost the game with '+a+' bricks remaining!'
        else:
            b = 'You lost the game with '+a+' brick remaining!'
            
        self._mssg = GLabel(x=240, y=310, text=b
                            + ' Press any key to play again!',
                            font_size=14, linecolor = colormodel.RED)
            
        curr_keys = self.input.key_count
        change = curr_keys > 0 and self.last_keys == 0
        
        if change:
            self._state = STATE_INACTIVE
        self.last_keys= curr_keys
        
    def ifWin(self):
        """Helper method for STATE_WIN"""
        self._game.updateBricks()
        b = 'Congratulations! You won the game!!'
        self._mssg = GLabel(x=240, y=310, text=b
                            +' Press any key to play again!', font_size=14,
                            linecolor = colormodel.GREEN)
            
        curr_keys = self.input.key_count
        change = curr_keys > 0 and self.last_keys == 0
        
        if change:
            self._state = STATE_INACTIVE
        self.last_keys= curr_keys
        
