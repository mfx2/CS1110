#dice.py
#Michael Xiao (mfx2)
#8/30/16

def make_email(s):
    company = s[s.index('@'):]
    if company == '@ubisoft.com':
        period = s.index('.')
        last = s[:period]
        first = s[period+1:s.index('@')]
    else:
        period1 = s.index('.')
        period2 = s.index('.',period1+1)
        first = s[:period1]
        last = s[period2+1:s.index('@')]
    return first+'.'+last+'@ubiware.com'


def add_color(color1, color2):
    red = color1.red + color2.red
    if red > 255:
        red = 255
        
    blue = color1.blue + color2.blue
    if blue > 255:
        blue = 255
        
    green = color1.green + color2.green
    if green > 255:
        green = 255

    alpha = color1.alpha + color2.alpha
    if alpha > 255:
        alpha = 255

    return colormodel.RGB(red,green,blue,alpha)

def alpha_blend(color1,color2):
    r1 = color1.red/255
    r2 = color2.red/255
    g1 = color1.green/255
    g2 = color2.green/255
    b1 = color1.blue/255
    b2 = color2.blue/255
    a1 = color1.alpha/255
    a2 = color2.alpha/255
    
    r = (a1*r1+(1-a1)*r2)*255
    g = (a1*g1+(1-a1)*g2)*255
    b = (a1*b1+(1-a1)*b2)*255
    a = (a1+(1-a1)*a2)*255
    
    return colormodel.RGB(r,g,b,a)

def isnetid(s):
    if len(s) < 3:
        return False
    if s[2].isdigit():
        pos=2
    else:
        pos=3
        
    prefix = s[:pos].isalpha()
    suffix = s[pos:].isdigit()
    
    return prefix and suffix

def unify_first_word(s):
    
    # seperate out first word
    if ' ' in s:
        first = s[:s.index(' ')]
        last = s[s.index(' '):]
    else:
        first = s
        last = ''
    #find case of first letter
    if first.islower():
        result = first.lower()
    else:
        result = first.upper()
        
    return result + last
