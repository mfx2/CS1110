# lab12.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Loop invariant functions"""


def num_space_runs(s):
    """Returns: The number of runs of spaces in the string s.
    
    A run is a collection of adjacent spaces.  We need a non-space character
    in-between to break up runs.
    
    Example: num_space_runs('  a  f   g    ') returns 4
             num_space_runs('a  f   g') returns 2
             num_space_runs('  a  bc   d') returns 3
    
    Parameter s: The string to parse
    Precondition: s is a nonempty string with letters and spaces"""
    # PUT THE INITIALIZATION CODE HERE
    spaces = 0
    k = 0
    # invariant: s[0..i] contains n runs of spaces
    # PUT THE WHILE LOOP HERE
    while k < len(s):
        if k !=0:
            if s[k]==' ':
                if s[k] == s[k-1]:
                    k = k+1
                else:
                    spaces = spaces + 1
                    k = k + 1
            else:
                k = k + 1
        if k == 0:
            if s[k]==' ':
                spaces = spaces + 1
                k = k + 1
            else:
                k = k + 1
 
    # post: s[0..len(s)-1] contains n runs of spaces
    # PUT THE RETURN STATEMENT HERE
    return spaces


def split(s):
    """Returns: Returns a list of works (separated by spaces) in s
    
    Words are indicated by spaces; there is always a space after each word.
    
    Example: split('a b c d ') returns ['a','b','c','d']
             split('a ') returns ['a']
    
    Parameter s: The string to parse
    Precondition: s is a nonempty string with no adjacent spaces.  There is 
    no space at the beginning, but there is a single space at the end"""
    # PUT THE INITIALIZATION CODE HERE
    result = []
    k = 0
    # invariant: result contains the words in s[0..pos-1], and s[pos-1] is a space
    # PUT THE WHILE LOOP HERE
    while k < len(s):
        if k == 0:
            if s[k] != ' ':
                result.append(s[k])
        
        else:
            if s[k] != ' ':
                if s[k-1] != ' ':
                    a = result.index(s[k-1])
                    result[a] = s[k-1] + s[k]
                    
                else:    
                    result.append(s[k])
        k  = k + 1
    
    pos = s.find(' ')
    result = s[:pos-1]
    while pos != len(s):
        pos2 = s.find(' ',pos)
        result.append(s[pos:pos2-1])
        pos = pos2
        
    # post: result contains the words in s[0..len(s)-1], and s[len(s)-1] is a space
    # PUT THE RETURN STATEMENT HERE
    return result
