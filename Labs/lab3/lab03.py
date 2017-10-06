#lab03.py
#Michael Xiao (mfx2)
#9/6/2016

def first_inside_quotes(s):
    """returns: the first substring of s between two double quote caracters
    a quote character is one that is inside a string, not one that delimits it.  We typically use single quotes (') to delimit a string if want to use a double quote character (") inside of it.
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' because it only picks the first such substring
    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters.
    pass"""
    
    First=s.index('"')
    Start=First+1
    End=s.index('"',First+1)
    return s[Start:End]
