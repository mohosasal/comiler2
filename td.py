transition_diagrams = {
    'Program': {
        0: {
            'Declarationlist': 160
        },
        160: {
            '$': 1
        },
        1: {}
    },
    'Declarationlist': {
        2: {
            'Declaration': 3,
            'epsilon': 4
        },
        3: {
            'Declarationlist': 4
        },
        4: {}
    },
    'Declaration': {
        5: {
            'Declarationinitial': 6
        },
        6: {
            'Declarationprime': 7
        },
        7: {}
    },
    'Declarationinitial': {
        8: {
            'Typespecifier': 9
        },
        9: {
            'ID': 10
        },
        10: {}
    },
    'Declarationprime': {
        11: {
            'Fundeclarationprime': 12,
            'Vardeclarationprime': 12
        },
        12: {}
    },
    'Vardeclarationprime': {
        13: {
            ';': 17,
            '[': 14
        },
        14: {
            'NUM': 15
        },
        15: {
            ']': 16
        },
        16: {
            ';': 17
        },
        17: {}
    },
    'Fundeclarationprime': {
        18: {
            '(': 19
        },
        19: {
            'Params': 20
        },
        20: {
            ')': 21
        },
        21: {
            'Compoundstmt': 22
        },
        22: {}
    },
    'Typespecifier': {
        23: {
            'int': 24,
            'void': 24
        },
        24: {}
    },
    'Params': {
        25: {
            'int': 26,
            'void': 29
        },
        26: {
            'ID': 27
        },
        27: {
            'Paramprime': 28
        },
        28: {
            'Paramlist': 29
        },
        29: {}
    },
    'Paramlist': {
        30: {
            ',': 31,
            'epsilon': 33
        },
        31: {
            'Param': 32
        },
        32: {
            'Paramlist': 33
        },
        33: {}
    },
    'Param': {
        34: {
            'Declarationinitial': 35
        },
        35: {
            'Paramprime': 36
        },
        36: {}
    },
    'Paramprime': {
        37: {
            '[': 38,
            'epsilon': 39
        },
        38: {
            ']': 39
        },
        39: {}
    },
    'Compoundstmt': {
        40: {
            '{': 41
        },
        41: {
            'Declarationlist': 42
        },
        42: {
            'Statementlist': 43
        },
        43: {
            '}': 44
        },
        44: {}
    },
    'Statementlist': {
        45: {
            'Statement': 46,
            'epsilon': 47
        },
        46: {
            'Statementlist': 47
        },
        47: {}
    },
    'Statement': {
        48: {
            'Expressionstmt': 49,
            'Compoundstmt': 49,
            'Selectionstmt': 49,
            'Iterationstmt': 49,
            'Returnstmt': 49
        },
        49: {}
    },
    'Expressionstmt': {
        50: {
            'Expression': 51,
            'break': 52,
            ';': 53
        },
        51: {
            ';': 53
        },
        52: {
            ';': 53
        },
        53: {}
    },
    'Selectionstmt': {
        54: {
            'if': 55
        },
        55: {
            '(': 56
        },
        56: {
            'Expression': 57
        },
        57: {
            ')': 58
        },
        58: {
            'Statement': 59
        },
        59: {
            'else': 60
        },
        60: {
            'Statement': 61
        },
        61: {}
    },
    'Iterationstmt': {
        62: {
            'repeat': 63
        },
        63: {
            'Statement': 64
        },
        64: {
            'until': 65
        },
        65: {
            '(': 66
        },
        66: {
            'Expression': 67
        },
        67: {
            ')': 68
        },
        68: {}
    },
    'Returnstmt': {
        69: {
            'return': 70
        },
        70: {
            'Returnstmtprime': 71
        },
        71: {}
    },
    'Returnstmtprime': {
        72: {
            ';': 74,
            'Expression': 73
        },
        73: {
            ';': 74
        },
        74: {}
    },
    'Expression': {
        75: {
            'Simpleexpressionzegond': 77,
            'ID': 76
        },
        76: {
            'B': 77
        },
        77: {}
    },
    'B': {
        78: {
            '=': 157,
            '[': 79,
            'Simpleexpressionprime': 82
        },
        79: {
            'Expression': 80
        },
        80: {
            ']': 81
        },
        81: {
            'H': 82
        },
        82: {},
        157: {
            'Expression': 82
        }
    },
    'H': {
        83: {
            '=': 158,
            'G': 84
        },
        84: {
            'D': 85
        },
        85: {
            'C': 86
        },
        86: {},
        158: {
            'Expression': 86
        }
    },
    'Simpleexpressionzegond': {
        87: {
            'Additiveexpressionzegond': 88
        },
        88: {
            'C': 89
        },
        89: {}
    },
    'Simpleexpressionprime': {
        90: {
            'Additiveexpressionprime': 91
        },
        91: {
            'C': 92
        },
        92: {}
    },
    'C': {
        93: {
            'Relop': 94,
            'epsilon': 95
        },
        94: {
            'Additiveexpression': 95
        },
        95: {}
    },
    'Relop': {
        96: {
            '<': 98,
            '==': 98
        },
        98: {}
    },
    'Additiveexpression': {
        99: {
            'Term': 100
        },
        100: {
            'D': 101
        },
        101: {}
    },
    'Additiveexpressionprime': {
        102: {
            'Termprime': 103
        },
        103: {
            'D': 104
        },
        104: {}
    },
    'Additiveexpressionzegond': {
        105: {
            'Termzegond': 106
        },
        106: {
            'D': 107
        },
        107: {}
    },
    'D': {
        108: {
            'Addop': 109,
            'epsilon': 111
        },
        109: {
            'Term': 110
        },
        110: {
            'D': 111
        },
        111: {}
    },
    'Addop': {
        112: {
            '+': 113,
            '-': 113
        },
        113: {}
    },
    'Term': {
        114: {
            'Factor': 115
        },
        115: {
            'G': 116
        },
        116: {}
    },
    'Termprime': {
        117: {
            'Factorprime': 118
        },
        118: {
            'G': 119
        },
        119: {}
    },
    'Termzegond': {
        120: {
            'Factorzegond': 121
        },
        121: {
            'G': 122
        },
        122: {}
    },
    'G': {
        123: {
            '*': 124,
            'epsilon': 126
        },
        124: {
            'Factor': 125
        },
        125: {
            'G': 126
        },
        126: {}
    },
    'Factor': {
        127: {
            '(': 128,
            'ID': 130,
            'NUM': 131
        },
        128: {
            'Expression': 129
        },
        129: {
            ')': 131
        },
        130: {
            'Varcallprime': 131
        },
        131: {}
    },
    'Varcallprime': {
        132: {
            '(': 133,
            'Varprime': 135
        },
        133: {
            'Args': 134
        },
        134: {
            ')': 135
        },
        135: {}
    },
    'Varprime': {
        136: {
            '[': 137,
            'epsilon': 139
        },
        137: {
            'Expression': 138
        },
        138: {
            ']': 139
        },
        139: {}
    },
    'Factorprime': {
        140: {
            '(': 141,
            'epsilon': 143
        },
        141: {
            'Args': 142
        },
        142: {
            ')': 143
        },
        143: {}
    },
    'Factorzegond': {
        144: {
            '(': 145,
            'NUM': 147
        },
        145: {
            'Expression': 146
        },
        146: {
            ')': 147
        },
        147: {}
    },
    'Args': {
        148: {
            'Arglist': 149,
            'epsilon': 149
        },
        149: {}
    },
    'Arglist': {
        150: {
            'Expression': 151
        },
        151: {
            'Arglistprime': 152
        },
        152: {}
    },
    'Arglistprime': {
        153: {
            ',': 154,
            'epsilon': 156
        },
        154: {
            'Expression': 155
        },
        155: {
            'Arglistprime': 156
        },
        156: {}
    }
}


#add epsilon to the first and terminal first


def first(input):

    if input in non_terminals:
        return first_[input]
    else:
        return input

first_ = {'Program': ['int', 'void', 'epsilon'],
         'Declarationlist': ['int', 'void', 'epsilon'],
         'Declaration': ['int', 'void'],
         'Declarationinitial': ['int', 'void'],
         'Declarationprime': [';', '[', '('],
         'Vardeclarationprime': [';', '['],
         'Fundeclarationprime': ['('],
         'Typespecifier': ['int', 'void'],
         'Params': ['int', 'void'],
         'Paramlist': [',', 'epsilon'],
         'Param': ['int', 'void'],
         'Paramprime': ['[', 'epsilon'],
         'Compoundstmt': ['{'],
         'Statementlist': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return', 'epsilon'],
         'Statement': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return'],
         'Expressionstmt': ['ID', ';', 'NUM', '(', 'break'],
         'Selectionstmt': ['if'],
         'Iterationstmt': ['repeat'],
         'Returnstmt': ['return'],
         'Returnstmtprime': ['ID', ';', 'NUM', '('],
         'Expression': ['ID', 'NUM', '('],
         'B': ['[', '(', '=', '<', '==', '+', '-', '*', 'epsilon'],
         'H': ['=', '<', '==', '+', '-', '*', 'epsilon'],
         'Simpleexpressionzegond': ['NUM', '('],
         'Simpleexpressionprime': ['(', '<', '==', '+', '-', '*', 'epsilon'],
         'C': ['<', '==', 'epsilon'],
         'Relop': ['<', '=='],
         'Additiveexpression': ['ID', 'NUM', '('],
         'Additiveexpressionprime': ['(', '+', '-', '*', 'epsilon'],
         'Additiveexpressionzegond': ['NUM', '('],
         'D': ['+', '-', 'epsilon'],
         'Addop': ['+', '-'],
         'Term': ['ID', 'NUM', '('],
         'Termprime': ['(', '*', 'epsilon'],
         'Termzegond': ['NUM', '('],
         'G': ['*', 'epsilon'],
         'Factor': ['ID', 'NUM', '('],
         'Varcallprime': ['[', '(', 'epsilon'],
         'Varprime': ['[', 'epsilon'],
         'Factorprime': ['(', 'epsilon'],
         'Factorzegond': ['NUM', '('],
         'Args': ['ID', 'NUM', '(', 'epsilon'],
         'Arglist': ['ID', 'NUM', '('],
         'Arglistprime': [',', 'epsilon']}

follow = {'Program': ["$"],
          'Declarationlist': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Declaration': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Declarationinitial': [';', '[', '(', ')', ','],
          'Declarationprime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Vardeclarationprime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return',
                                  '$'],
          'Fundeclarationprime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return',
                                  '$'],
          'Typespecifier': ['ID'],
          'Params': [')'],
          'Paramlist': [')'],
          'Param': [')', ','],
          'Paramprime': [')', ','],
          'Compoundstmt': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'else', 'repeat', 'until',
                           'return', '$'],
          'Statementlist': ['}'],
          'Statement': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Expressionstmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Selectionstmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Iterationstmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Returnstmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Returnstmtprime': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Expression': [';', ']', ')', ','],
          'B': [';', ']', ')', ','],
          'H': [';', ']', ')', ','],
          'Simpleexpressionzegond': [';', ']', ')', ','],
          'Simpleexpressionprime': [';', ']', ')', ','],
          'C': [';', ']', ')', ','],
          'Relop': ['ID', 'NUM', '('],
          'Additiveexpression': [';', ']', ')', ',', '<', '=='],
          'Additiveexpressionprime': [';', ']', ')', ',', '<', '=='],
          'Additiveexpressionzegond': [';', ']', ')', ',', '<', '=='],
          'D': [';', ']', ')', ','],
          'Addop': ['ID', 'NUM', '('],
          'Term': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Termprime': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Termzegond': [';', ']', ')', ',', '<', '==', '+', '-'],
          'G': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Factor': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Varcallprime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Varprime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Factorprime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Factorzegond': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Args': [')'],
          'Arglist': [')'],
          'Arglistprime': [')']}

non_terminals = ['Program', 'Declarationlist', 'Declaration', 'Declarationinitial', 'Declarationprime',
                 'Vardeclarationprime', 'Fundeclarationprime', 'Typespecifier', 'Params', 'Paramlist', 'Param',
                 'Paramprime', 'Compoundstmt', 'Statementlist', 'Statement', 'Expressionstmt', 'Selectionstmt',
                 'Iterationstmt', 'Returnstmt', 'Returnstmtprime', 'Expression', 'B', 'H', 'Simpleexpressionzegond',
                 'Simpleexpressionprime', 'C', 'Relop', 'Additiveexpression', 'Additiveexpressionprime',
                 'Additiveexpressionzegond', 'D', 'Addop', 'Term', 'Termprime', 'Termzegond', 'G', 'Factor',
                 'Varcallprime', 'Varprime', 'Factorprime', 'Factorzegond', 'Args', 'Arglist', 'Arglistprime']

terminals = []

starter_of_non_terminals = {'Program': 0, 'Declarationlist': 2, 'Declaration': 5, 'Declarationinitial': 8,
                            'Declarationprime': 11, 'Vardeclarationprime': 13, 'Fundeclarationprime': 18,
                            'Typespecifier': 23, 'Params': 25, 'Paramlist': 30, 'Param': 34, 'Paramprime': 37,
                            'Compoundstmt': 40, 'Statementlist': 45, 'Statement': 48, 'Expressionstmt': 50,
                            'Selectionstmt': 54, 'Iterationstmt': 62, 'Returnstmt': 69, 'Returnstmtprime': 72,
                            'Expression': 75, 'B': 78, 'H': 83, 'Simpleexpressionzegond': 87,
                            'Simpleexpressionprime': 90, 'C': 93, 'Relop': 96, 'Additiveexpression': 99,
                            'Additiveexpressionprime': 102, 'Additiveexpressionzegond': 105, 'D': 108, 'Addop': 112,
                            'Term': 114, 'Termprime': 117, 'Termzegond': 120, 'G': 123, 'Factor': 127,
                            'Varcallprime': 132, 'Varprime': 136, 'Factorprime': 140, 'Factorzegond': 144,
                            'Args': 148, 'Arglist': 150, 'Arglistprime': 153}
