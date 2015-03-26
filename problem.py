class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def log(self, data):
    	print data


x = Complex(3.0, -4.5)

x.log('test')