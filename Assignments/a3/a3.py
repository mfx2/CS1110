# a3.py
# Michael Xiao (mfx2) and Debo Adebola (aaa292)
# October 5, 2016
""" Functions for Assignment A3"""

import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object"""
    color = colormodel.RGB(0,0,0)
    color.red=255-rgb.red
    color.green=255-rgb.green
    color.blue=255-rgb.blue
    return color

def round(number, places):
    """Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float, number is >= 0
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3"""
    a = number * (10.0**places)
    b = a + 0.5
    c = int(b)
    d = c/10.0**places
    return float(d)

def str5(value):
    """Returns: value as a string, but expand or round to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360."""

    f = float(value)
    s = str(f)
    if len(s) > 5:
        places = 4 - s.index('.')
        f = round(f,places)
        s = str(f)
        s = s[:5]
        
        if len(s) < 5:
            s = s + (5-len(s))*'0'
    elif len(s) < 5:
        s = s + (5-len(s))*'0'
    else:
        s = s
    return s

def str5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces
    after the commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object."""
    
    c = str5(cmyk.cyan)
    m = str5(cmyk.magenta)
    y = str5(cmyk.yellow)
    k = str5(cmyk.black)
    
    return '('+str(c)+', '+str(m)+', '+str(y)+', '+str(k)+')'

def str5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object."""
    h = str5(hsv.hue)
    s = str5(hsv.saturation)
    v = str5(hsv.value)
    
    return '('+str(h)+', '+str(s)+', '+str(v)+')'


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object"""
    cmyk = colormodel.CMYK(0.0,0.0,0.0,0.0)
    
    c = 1 - (rgb.red / 255.0)
    m = 1 - (rgb.green / 255.0)
    y = 1 - (rgb.blue / 255.0)
    
    if c == 1 and m == 1 and y == 1:
        cmyk = colormodel.CMYK(0.0,0.0,0.0,100.0)
    else:
        k = min(c, m, y)
        
        cmyk.cyan = (c-k)/(1-k)*100
        cmyk.magenta = (m-k)/(1-k)*100
        cmyk.yellow = (y-k)/(1-k)*100
        cmyk.black = k*100
        
    return cmyk

def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object."""
    rgb = colormodel.RGB(0,0,0)
    
    c = cmyk.cyan / 100.0
    m = cmyk.magenta / 100.0
    y = cmyk.yellow / 100.0
    k = cmyk.black / 100.0

    rgb.red = int(round((1-c)*(1-k)*255,0))
    rgb.green = int(round((1-m)*(1-k)*255,0))
    rgb.blue = int(round((1-y)*(1-k)*255,0))

    return rgb

def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object"""
    hsv = colormodel.HSV(0.0,0.0,0.0)
    
    r = rgb.red/255.0
    g = rgb.green/255.0
    b = rgb.blue/255.0
    
    big = max(r,g,b)
    small = min(r,g,b)
    
    if big == small:
        hsv.hue = 0.0
    elif big == r and g >= b:
        hsv.hue = 60.0 * (g-b)/(big-small)
    elif big == r and g < b:
        hsv.hue = 60.0 * (g-b)/(big-small) + 360.0
    elif big == g:
        hsv.hue = 60.0 * (b-r)/(big-small) + 120.0
    elif big == b:
        hsv.hue = 60.0 * (r-g)/(big-small) + 240.0
        
    if big == 0:
        hsv.saturation = 0
    else:
        hsv.saturation = 1 - small/big
    
    hsv.value = big
    
    return hsv

def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object."""
    rgb = colormodel.RGB(0,0,0)
    
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    
    hi = math.floor(h/60)
    f = (h / 60) - hi
    p = v * (1 - s)
    q = v * (1 - (f * s))
    t = v * (1 - ((1 - f) * s))
    
    if hi == 0:
        r = v
        g = t
        b = p
    elif hi == 1:
        r = q
        g = v
        b = p
    elif hi == 2:
        r = p
        g = v
        b = t
    elif hi == 3:
        r = p
        g = q
        b = v
    elif hi == 4:
        r = t
        g = p
        b = v
    elif hi == 5:
        r = v
        g = p
        b = q
    
    rgb.red = int(round(r*255,0))
    rgb.green = int(round(g*255,0))
    rgb.blue = int(round(b*255,0))

    return rgb
