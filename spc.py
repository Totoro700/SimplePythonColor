_B='#{0:02x}{1:02x}{2:02x}'
_A=1.
class ColorHSB:
	def __init__(A,h,s,b):A.h,A.s,A.b=h,s,b
	def ToRGB(A):
		F=A.h%_A*6.;B=int(F);G=F-B;C=A.b*(_A-A.s);D=A.b*(_A-G*A.s);E=A.b*(_A-(_A-G)*A.s)
		if B==0:return ColorRGB(A.b,E,C,255)
		elif B==1:return ColorRGB(D,A.b,C,255)
		elif B==2:return ColorRGB(C,A.b,E,255)
		elif B==3:return ColorRGB(C,D,A.b,255)
		elif B==4:return ColorRGB(E,C,A.b,255)
		elif B==5:return ColorRGB(A.b,C,D,255)
		else:return ColorRGB(255,255,255)
	def ToHex(B):A=B.ToRGB();return _B.format(max(0,min(A.red,255)),max(0,min(A.green,255)),max(0,min(A.blue,255)))
class ColorHex:
	def __init__(A,hex):A.hex=hex
	def __str__(A):return f"#{A.hex}"
	def get_formatted(A):return f"#{A.hex}"
class ColorRGB:
	def __init__(A,red,green,blue,alpha=255):A.red,A.green,A.blue,A.alpha=red,green,blue,alpha
	def ToHSB(A):
		D=.0;B=max(A.red,A.green,A.blue)
		if B==0:return ColorHSB(D,D,D,A.alpha/255.)
		F=min(A.red,A.green,A.blue);G=B-F;E=G*6.
		if B==F:C=D
		elif B==A.red:C=(A.green-A.blue)/E+_A
		elif B==A.green:C=(A.blue-A.red)/E+_A/3.
		else:C=(A.red-A.green)/E+2./3.
		C%=_A;H=G/float(B);I=B/255.;return ColorHSB(C,H,I,A.alpha/255.)
	def ToHex(A):return _B.format(max(0,min(A.red,255)),max(0,min(A.green,255)),max(0,min(A.blue,255)))
	def ToCMYK(B):C,D,E=B.red/255,B.green/255,B.blue/255;A=1-max(C,D,E);F=(1-C-A)/(1-A);G=(1-E-A)/(1-A);H=(1-D-A)/(1-A);return CMYK(F,G,H,A)
	def get_red(A):return A.red
	def get_green(A):return A.green
	def get_blue(A):return A.blue
	def get_alpha(A):return A.alpha
	def __str__(A):return f"RGB({A.red}, {A.blue}, {A.green}, {A.alpha})"
	def get_formatted(A):return f"RGB({A.red}, {A.blue}, {A.green}, {A.alpha})"
class CMYK:
	def __init__(A,cyan,magenta,yellow,key):A.cyan,A.magenta,A.yellow,A.key=cyan,magenta,yellow,key
	def ToRGB(A):B=255*(1-A.cyan)*(1-A.key);C=255*(1-A.magenta)*(1-A.key);D=255*(1-A.yellow)*(1-A.key);return ColorRGB(B,C,D)
	def ToHex(B):A=B.ToRGB();return _B.format(max(0,min(A.red,255)),max(0,min(A.green,255)),max(0,min(A.blue,255)))
	def ToHSB(A):B=A.ToRGB();return ColorRGB.ToHSB(B)
	def get_cyan(A):return A.cyan
	def get_magenta(A):return A.magenta
	def get_yellow(A):return A.yellow
	def get_key(A):return A.key
	def get_black(A):return A.key
	def __str__(A):return f"CMYK({A.cyan}, {A.magenta}, {A.yellow}, {A.key})"
	def get_formatted(A):return f"CMYK({A.cyan}, {A.magenta}, {A.yellow}, {A.key})"