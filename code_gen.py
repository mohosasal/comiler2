import scanner

ss = []
pb = []
temporary_table = dict()

class Code_gen:

    def __init__(self, scanner):
        self.scanner = scanner
        self.i = 0
        self.last_temp_address = 500
        self.temps_index = 0


    def code_generator(self, str, token):
        if str == '#break':
            Code_gen.break_function(self)
        elif str == '#pushid':
            Code_gen.pushid(self, token)
        elif str == '#assign':
            Code_gen.assign(self)
        elif str == '#addop':
            Code_gen.addop(self)
        elif str == '#plus':
            Code_gen.plus(self)

    def break_function(self):
        if len(ss) != 0:
            pb[ss[len(ss) - 1]] = '(JP,' + str(self.i) + ',,)'

    def pushid(self, token, symbol_table):
        address = scanner.symbol_table[token]
        ss.append(address)


    def assign(self):
        top = ss[len(ss) - 1]
        second_top = ss[len(ss) - 2]
        ss.pop(2)
        pb[self.i] = '(ASSIGN, ' + str(top) + ', ' + str(second_top) + ',)'
        self.i += 1


    def addop(self):
        top = ss[len(ss) - 1]
        second_top = ss[len(ss) - 2]
        third_top = ss[len(ss) - 3]
        to_push=0
        ss.pop(3)
        temp = self.gettemp()
        pb[self.i] = '(' + second_top + ', ' + str(third_top) + ', ' + str(top) + ', ' + str(temp) + ')'
        self.i += 1
        ss.append(temp)




    def plus(self):
        ss.append('ADD')

    def minus(self):
        ss.append('SUB')

    def array(self):
        pass


    def memory_allocation(self):
        pass


    def gettemp(self):
        name = 't' + str(self.temps_index)
        temporary_table[name] = self.last_temp_address
        self.last_temp_address += 4
        return temporary_table[name]
