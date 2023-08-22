# thanks to Luna5ama for the conversion math
class ColorHSB:
    def __init__(self, h: float, s: float, b: float) -> None:
        self.h, self.s, self.b = h, s, b

    def ToRGB(self):
        hue = (self.h % 1.0) * 6.0
        intHue = int(hue)
        f = hue - intHue
        p = self.b * (1.0 - self.s)
        q = self.b * (1.0 - f * self.s)
        t = self.b * (1.0 - (1.0 - f) * self.s)
        
        if intHue == 0:
            return ColorRGB(self.b, t, p, 255)
        elif intHue == 1:
            return ColorRGB(q, self.b, p, 255)
        elif intHue == 2:
            return ColorRGB(p, self.b, t, 255)
        elif intHue == 3:
            return ColorRGB(p, q, self.b, 255)
        elif intHue == 4:
            return ColorRGB(t, p, self.b, 255)
        elif intHue == 5:
            return ColorRGB(self.b, p, q, 255)
        else:
            return ColorRGB(255, 255, 255)        
    
    def ToHex(self):
        rgb = self.ToRGB()
        return "#{0:02x}{1:02x}{2:02x}".format(max(0, min(rgb.red, 255)), max(0, min(rgb.green, 255)), max(0, min(rgb.blue, 255)))
    
class ColorHex: # no conversions for these as they are very complicated
    def __init__(self, hex: str) -> None:
        self.hex = hex
        
    def __str__(self) -> str:
        return f"#{self.hex}"
    
    def get_formatted(self) -> str:
        return f"#{self.hex}"

class ColorRGB:
    def __init__(self, red: int, green: int, blue: int, alpha: int = 255):
        self.red, self.green, self.blue, self.alpha = red, green, blue, alpha
        
    def ToHSB(self) -> ColorHSB:
        cMax = max(self.red, self.green, self.blue)
        if (cMax == 0): 
            return ColorHSB(0.0, 0.0, 0.0, self.alpha / 255.0)

        cMin = min(self.red, self.green, self.blue)
        diff = cMax - cMin

        diff6 = diff * 6.0
        
        if cMax == cMin:
            hue = 0.0
        elif cMax == self.red:
            hue = (self.green - self.blue) / diff6 + 1.0
        elif cMax == self.green:
            hue = (self.blue - self.red) / diff6 + (1.0 / 3.0)
        else:
            hue = (self.red - self.green) / diff6 + (2.0 / 3.0)

        hue %= 1.0

        saturation = diff / float(cMax)
        brightness = cMax / 255.0

        return ColorHSB(hue, saturation, brightness, self.alpha / 255.0)
    
    def ToHex(self):
        return "#{0:02x}{1:02x}{2:02x}".format(max(0, min(self.red, 255)), max(0, min(self.green, 255)), max(0, min(self.blue, 255)))
    
    def ToCMYK(self):
        rp, bp, gp = self.red / 255, self.green / 255, self.blue / 255
        k = 1 - max(rp, bp, gp)
        c = (1 - rp - k) / (1 - k)
        m = (1 - gp - k) / (1 - k)
        y = (1 - bp - k) / (1 - k)
        return CMYK(c, m, y, k)
    
    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def get_alpha(self):
        return self.alpha
    
    def __str__(self):
        return f"RGB({self.red}, {self.blue}, {self.green}, {self.alpha})"
    
    def get_formatted(self):
        return f"RGB({self.red}, {self.blue}, {self.green}, {self.alpha})"
    
class CMYK():
    def __init__(self, cyan: int, magenta: int, yellow: int, key: int) -> None:
        self.cyan, self.magenta, self.yellow, self.key = cyan, magenta, yellow, key
        
    def ToRGB(self):
        r = 255 * (1 - self.cyan) * (1 - self.key)
        g = 255 * (1 - self.magenta) * (1 - self.key)
        b = 255 * (1 - self.yellow) * (1 - self.key)
        return ColorRGB(r, g, b)
    
    def ToHex(self):
        rgb = self.ToRGB()
        return "#{0:02x}{1:02x}{2:02x}".format(max(0, min(rgb.red, 255)), max(0, min(rgb.green, 255)), max(0, min(rgb.blue, 255)))
    
    def ToHSB(self) -> ColorRGB:
        rgb = self.ToRGB()
        return ColorRGB.ToHSB(rgb)
    
    def get_cyan(self):
        return self.cyan
    
    def get_magenta(self):
        return self.magenta
    
    def get_yellow(self):
        return self.yellow
    
    def get_key(self):
        return self.key
    
    def get_black(self):
        return self.key
        
    def __str__(self):
        return f"CMYK({self.cyan}, {self.magenta}, {self.yellow}, {self.key})"
    
    def get_formatted(self):
        return f"CMYK({self.cyan}, {self.magenta}, {self.yellow}, {self.key})"