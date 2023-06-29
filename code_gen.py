import scanner

ss = []
pb = []
i = 0
top = -1
class Code_gen:


    @staticmethod
    def code_generator(str, token):
        if str == '#break':
            Code_gen.break_function()
        elif str == '#pushid':
            Code_gen.pushid(token)
        elif str == '#assign':
            Code_gen.assign()
        elif str == '#addop':
            Code_gen.addop()
        elif str == '#plus':
            Code_gen.plus()

    @staticmethod
    def break_function():
        if len(ss) != 0:
            pb[ss[top]] = '(JP,' + str(i) + ',,)'
    @staticmethod
    def pushid(token):
        address =

    @staticmethod
    def assign():
        pass

    @staticmethod
    def addop():
        pass

    @staticmethod
    def plus():
        pass