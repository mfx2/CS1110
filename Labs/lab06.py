# lab06.py
# Michael Xiao (mfx2)
# Initial skeleton by Walker White (wmw2)
# THE DATE COMPLETED HERE
"""Module to demonstrate debugging and error handling.

This module contains several functions with bugs in it.  You are to
find and remove the bugs using the techniques that we talked about in
class.  

In addition, you will also add assert statements to this functions to
assert the (somewhat complex) precondition.  These assert statements
will be aided by the latter two functions in this module."""


# PART 1: DEBUGGING
def time_to_military(s):
    """ Returns: the time in 24-hour (military) format.
    
    24-hour format has the form '<hours>:<minutes>'. The hours are between 0 and 23, 
    and are always two digits (so there must be a leading zero).  The minutes are 
    between 0 and 59, and are always 2 digits.
    
    Examples:
        '2:45 PM' becomes '14:45'
        '9:05 AM' becomes '09:05'
        '12:00 AM' becomes '00:00'
    
    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM"""
    # PART 2: Add assert statements here to enforce preconditions
    assert type(s) == str
    assert is_time_format(s)
    # Split up the string
    pos1 = s.index(':')
    pos2 = s.index(' ')
    
    # Extract hours and minutes
    hour = int(s[:pos1])
    mins = s[pos1+1:pos2]
    suff = s[pos2+1:]
    
    # Adjust hour to be correct.
    if (suff == 'PM'):
        hour += 12
    else:
        hour = hour
    
    # Add a leading zero if necessary
    if (hour < 10):
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    
    # Glue it back together
    return str(hour)+':'+mins


def time_to_minutes(s):
    """Returns: number of minutes since midnight
    
    Examples:
       '2:45 PM' => 14*60+45 = 885
       '9:05 AM' => 9*60+5 = 545
      '12:00 AM' => 0
    
    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM"""
    # PART 2: Add assert statements here to enforce preconditions
    assert type(s) == str
    assert is_time_format(s)
    
    # Find the separators
    pos1 = s.index(':') + 1
    pos2 = s.index(' ')
    
    # Get hour and convert to int
    hour = s[:pos1-1]
    hour = int(hour)
    print 'hour is ' + str(hour)
    # Adjust hour to be correct.
    suff = s[pos2+1:]
    print 'suff is ' + suff
    if (suff == 'PM'):
        hour = hour+12
        print 'suff is PM'
        print 'hour is ' + str(hour)
    elif (suff == 'AM' and hour == 12):
        hour = 0
        print 'suff is AM and hour is 12'
    
    # Get min and convert to int
    mins = s[pos1:pos2]
    mins = int(mins)
    print 'mins is ' + str(mins)
    
    return hour*60+mins


# PART 2: ASSERT HELPER
def is_time_format(s):
    """Returns: True if s is a string in 12-format <hours>:<min> AM/PM
    
    Example: 
        is_time_format('2:45 PM') returns True
        is_time_format('2:45PM') returns False
        is_time_format('14:45') returns False
        is_time_format('14:45 AM') returns False
        is_time_format(245) returns False
    
    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)"""
    if ':' in s:
        pos1 = s.index(':')      
    else:
        return False
    
    if ' ' in s:
        if s.count(' ') != 1:
            return False
        pos2 = s.index(' ')      
    else:
        return False
    
    hour = s[:pos1]
    if hour.isdigit():
        pass
    else:
        return False
    
    hour = int(hour)
    minutes = s[pos1+1:pos2]
    if minutes.isdigit():
        pass
    else:
        return False
    minutes = int(minutes)
    
    if hour > 12:
        return False
    if hour < 1:
        return False
    if minutes > 59:
        return False
    if minutes <0 :
        return False
    
    suff = s[pos2+1:]
    
    if suff == 'PM':
        pass
    elif suff == 'AM':
        pass
    else:
        return False
    
    if type(s) != str:
        return False
    
    return True
    
    # HINT: Your function must be prepared to do something if s is a string.
    # Even if s is a string, the first number before the colon may be one
    # or two digits.  You must be prepared for either.
    # You might find the method s.isdigit() to be useful.


# PART 3: TRY-EXCEPT
def something_to_military(s):
    """Returns: the time in 24-hour (military) format if appropriate.
    
    The function is the same as time_to_military if s satisfies the
    precondition for that function.  If s does not satisfy the precondition
    then this function returns 'Invalid time format'
    
    Examples: 
        something_to_military('2:45 PM') returns '14:45'
        something_to_military('9:05 AM') returns '09:05'
        something_to_military('12:00 AM') returns '00:00'
        something_to_military(905) returns 'Invalid time format'
        something_to_military('abc') returns 'Invalid time format'
        something_to_military('9:05') returns 'Invalid time format'
    
    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)"""
    try:
        return time_to_military(s)
    except:
        return 'Invalid time format'
    # You are not allowed to use 'if' in this definition. Use try-except instead.
    # Hint: You have to complete PART 2 before you complete this part.
