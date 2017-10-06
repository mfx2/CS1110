# a3test.py
# Michael Xiao (mfx2) and Debo Adebola (aaa292)
# October 5, 2016
""" Unit Test for Assignment A3"""

import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71),
                              a3.complement_rgb(colormodel.RGB(250, 0, 71)))
    cornelltest.assert_equals(colormodel.RGB(255-255, 255-255, 255-255),
                              a3.complement_rgb(colormodel.RGB(255, 255, 255)))
    cornelltest.assert_equals(colormodel.RGB(255-0, 255-0, 255-0),
                              a3.complement_rgb(colormodel.RGB(0, 0, 0)))

def test_round():
    """Test function round (a3 version)"""
    cornelltest.assert_equals(130.6,   a3.round(130.59,1))
    cornelltest.assert_equals(130.5,   a3.round(130.54,1))
    cornelltest.assert_equals(100.0,   a3.round(100,1))
    cornelltest.assert_equals(100.6,   a3.round(100.55,1))
    cornelltest.assert_equals(99.57,   a3.round(99.566,2))
    cornelltest.assert_equals(99.99,   a3.round(99.99,2))
    cornelltest.assert_equals(100.0,   a3.round(99.995,2))
    cornelltest.assert_equals(22.00,   a3.round(21.99575,2))
    cornelltest.assert_equals(21.99,   a3.round(21.994,2))
    cornelltest.assert_equals(10.01,   a3.round(10.013567,2))
    cornelltest.assert_equals(10.0,    a3.round(10.000000005,2))
    cornelltest.assert_equals(10.0,    a3.round(9.9999,3))
    cornelltest.assert_equals(9.999,   a3.round(9.9993,3))
    cornelltest.assert_equals(1.355,   a3.round(1.3546,3))
    cornelltest.assert_equals(1.354,   a3.round(1.3544,3))
    cornelltest.assert_equals(0.046,   a3.round(.0456,3))
    cornelltest.assert_equals(0.045,   a3.round(.0453,3))
    cornelltest.assert_equals(0.006,   a3.round(.0056,3))
    cornelltest.assert_equals(0.001,   a3.round(.0013,3))
    cornelltest.assert_equals(0.0,     a3.round(.0004,3))
    cornelltest.assert_equals(0.001,   a3.round(.0009999,3))


def test_str5():
    """Test function str5"""
    cornelltest.assert_equals('130.6',  a3.str5(130.59))
    cornelltest.assert_equals('130.5',  a3.str5(130.54))
    cornelltest.assert_equals('100.0',  a3.str5(100))
    cornelltest.assert_equals('100.6',  a3.str5(100.55))
    cornelltest.assert_equals('99.57',  a3.str5(99.566))
    cornelltest.assert_equals('99.99',  a3.str5(99.99))
    cornelltest.assert_equals('100.0',  a3.str5(99.995))
    cornelltest.assert_equals('22.00',  a3.str5(21.99575))
    cornelltest.assert_equals('21.99',  a3.str5(21.994))
    cornelltest.assert_equals('10.01',  a3.str5(10.013567))
    cornelltest.assert_equals('10.00',  a3.str5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.str5(9.9999))
    cornelltest.assert_equals('9.999',  a3.str5(9.9993))
    cornelltest.assert_equals('1.355',  a3.str5(1.3546))
    cornelltest.assert_equals('1.354',  a3.str5(1.3544))
    cornelltest.assert_equals('0.046',  a3.str5(.0456))
    cornelltest.assert_equals('0.045',  a3.str5(.0453))
    cornelltest.assert_equals('0.006',  a3.str5(.0056))
    cornelltest.assert_equals('0.001',  a3.str5(.0013))
    cornelltest.assert_equals('0.000',  a3.str5(.0004))
    cornelltest.assert_equals('0.001',  a3.str5(.0009999))


def test_str5_color():
    """Test the str5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                              a3.str5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 1.0)));
    cornelltest.assert_equals('(1.000, 100.0, 23.12, 54.44)',
                              a3.str5_cmyk(colormodel.CMYK(1, 100, 23.12345, 54.435)));
    cornelltest.assert_equals('(98.45, 0.000, 0.123)',
                              a3.str5_hsv(colormodel.HSV(98.448, 0, .123456)));
    cornelltest.assert_equals('(312.0, 0.500, 0.568)',
                              a3.str5_hsv(colormodel.HSV(312, 0.5, 0.56789)));
    
def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.str5(cmyk.black))

    rgb = colormodel.RGB(50, 123, 43);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('59.35', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('65.04', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('51.76', a3.str5(cmyk.black))

def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    cmyk = colormodel.CMYK(100.0, 100.0, 100.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    cmyk = colormodel.CMYK(34.0, 12.5432, 66.666666, 1.0)
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(167, rgb.red)
    cornelltest.assert_equals(221, rgb.green)
    cornelltest.assert_equals(84, rgb.blue)
    
    cmyk = colormodel.CMYK(72.4444, 65.0, 90.1, 56.23)
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(31, rgb.red)
    cornelltest.assert_equals(39, rgb.green)
    cornelltest.assert_equals(11, rgb.blue)
    
    cmyk = colormodel.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
     
def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    #MAX = MIN
    rgb = colormodel.RGB(255, 255, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(0, 0, 0);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(100, 100, 100);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.392', a3.str5(hsv.value))
    
    #MAX = R and G >= B
    rgb = colormodel.RGB(200, 150, 100);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('30.00', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.500', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.784', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(242, 67, 67);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.723', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.949', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 0, 0);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('1.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    #MAX = R and G < B
    rgb = colormodel.RGB(123, 87, 99);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('340.0', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.293', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.482', a3.str5(hsv.value))
    
    #MAX = G
    rgb = colormodel.RGB(1, 6, 2);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('132.0', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.833', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.024', a3.str5(hsv.value))
    
    #MAX = B
    rgb = colormodel.RGB(12, 64, 242);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('226.4', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.950', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.949', a3.str5(hsv.value))

def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    #hi = 0
    hsv = colormodel.HSV(0.0, 0.0, 0.0);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    hsv = colormodel.HSV(45.5, 0.34, 0.34);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(87, rgb.red)
    cornelltest.assert_equals(80, rgb.green)
    cornelltest.assert_equals(57, rgb.blue)
    
    #hi = 1
    hsv = colormodel.HSV(80.0, 0.5, 0.123);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(26, rgb.red)
    cornelltest.assert_equals(31, rgb.green)
    cornelltest.assert_equals(16, rgb.blue)
    
    #hi = 2
    hsv = colormodel.HSV(153.3, 0.9, 0.4);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(10, rgb.red)
    cornelltest.assert_equals(102, rgb.green)
    cornelltest.assert_equals(61, rgb.blue)
    
    #hi = 3
    hsv = colormodel.HSV(181.1, 0.234, 0.432);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(84, rgb.red)
    cornelltest.assert_equals(110, rgb.green)
    cornelltest.assert_equals(110, rgb.blue)
    
    #hi = 4
    hsv = colormodel.HSV(275.0, 0.175, 0.275);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(65, rgb.red)
    cornelltest.assert_equals(58, rgb.green)
    cornelltest.assert_equals(70, rgb.blue)
    
    #hi = 5
    hsv = colormodel.HSV(359.9, 0.76, 0.765);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(195, rgb.red)
    cornelltest.assert_equals(47, rgb.green)
    cornelltest.assert_equals(47, rgb.blue)

# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == "__main__":
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
