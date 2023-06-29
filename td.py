
transition_diagrams = {
    'Program': {
        0: {
            'Declaration-list': 160
        },
        160: {
            '$': 1
        },
        1: {}
    },
    'Declaration-list': {
        2: {
            'Declaration': 3,
            'epsilon': 4
        },
        3: {
            'Declaration-list': 4
        },
        4: {}
    },
    'Declaration': {
        5: {
            'Declaration-initial': 6
        },
        6: {
            'Declaration-prime': 7
        },
        7: {}
    },
    'Declaration-initial': {
        8: {
            'Type-specifier': 9
        },
        9: {
            'ID': 10
        },
        10: {}
    },
    'Declaration-prime': {
        11: {
            'Fun-declaration-prime': 12,
            'Var-declaration-prime': 12
        },
        12: {}
    },
    'Var-declaration-prime': {
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
    'Fun-declaration-prime': {
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
            'Compound-stmt': 22
        },
        22: {}
    },
    'Type-specifier': {
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
            'Param-prime': 28
        },
        28: {
            'Param-list': 29
        },
        29: {}
    },
    'Param-list': {
        30: {
            ',': 31,
            'epsilon': 33
        },
        31: {
            'Param': 32
        },
        32: {
            'Param-list': 33
        },
        33: {}
    },
    'Param': {
        34: {
            'Declaration-initial': 35
        },
        35: {
            'Param-prime': 36
        },
        36: {}
    },
    'Param-prime': {
        37: {
            '[': 38,
            'epsilon': 39
        },
        38: {
            ']': 39
        },
        39: {}
    },
    'Compound-stmt': {
        40: {
            '{': 41
        },
        41: {
            'Declaration-list': 42
        },
        42: {
            'Statement-list': 43
        },
        43: {
            '}': ('-',44,'#assign')
        },
        44: {}
    },
    'Statement-list': {
        45: {
            'Statement': 46,
            'epsilon': 47
        },
        46: {
            'Statement-list': 47
        },
        47: {}
    },
    'Statement': {
        48: {
            'Expression-stmt': 49,
            'Compound-stmt': 49,
            'Selection-stmt': 49,
            'Iteration-stmt': 49,
            'Return-stmt': 49
        },
        49: {}
    },
    'Expression-stmt': {
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
    'Selection-stmt': {
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
    'Iteration-stmt': {
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
    'Return-stmt': {
        69: {
            'return': 70
        },
        70: {
            'Return-stmt-prime': 71
        },
        71: {}
    },
    'Return-stmt-prime': {
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
            'Simple-expression-zegond': 77,
            'ID': ('#pid',76,'-')
        },
        76: {
            'B': 77
        },
        77: {}
    },
    'B': {
        78: {
            '=':157,
            '[': 79,
            'Simple-expression-prime': 82
        },
        79: {
            'Expression': ('-',80,'#assign')
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
    'Simple-expression-zegond': {
        87: {
            'Additive-expression-zegond': 88
        },
        88: {
            'C': 89
        },
        89: {}
    },
    'Simple-expression-prime': {
        90: {
            'Additive-expression-prime': 91
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
            'Additive-expression': 95
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
    'Additive-expression': {
        99: {
            'Term': 100
        },
        100: {
            'D': 101
        },
        101: {}
    },
    'Additive-expression-prime': {
        102: {
            'Term-prime': 103
        },
        103: {
            'D': 104
        },
        104: {}
    },
    'Additive-expression-zegond': {
        105: {
            'Term-zegond': 106
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
            'D': ('-',111,'#addop')
        },
        111: {}
    },
    'Addop': {
        112: {
            '+': ('#plus',113,'-'),
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
    'Term-prime': {
        117: {
            'Factor-prime': 118
        },
        118: {
            'G': 119
        },
        119: {}
    },
    'Term-zegond': {
        120: {
            'Factor-zegond': 121
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
            'ID': ('#pid',130,'-'),
            'NUM': 131
        },
        128: {
            'Expression': 129
        },
        129: {
            ')': 131
        },
        130: {
            'Var-call-prime': 131
        },
        131: {}
    },
    'Var-call-prime': {
        132: {
            '(': 133,
            'Var-prime': 135
        },
        133: {
            'Args': 134
        },
        134: {
            ')': 135
        },
        135: {}
    },
    'Var-prime': {
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
    'Factor-prime': {
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
    'Factor-zegond': {
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
            'Arg-list': 149,
            'epsilon': 149
        },
        149: {}
    },
    'Arg-list': {
        150: {
            'Expression': 151
        },
        151: {
            'Arg-list-prime': 152
        },
        152: {}
    },
    'Arg-list-prime': {
        153: {
            ',': 154,
            'epsilon': 156
        },
        154: {
            'Expression': 155
        },
        155: {
            'Arg-list-prime': 156
        },
        156: {}
    }
}


# add epsilon to the first and terminal first


def first(input):
    if input in non_terminals:
        return first_[input]
    else:
        return input


first_ = {'Program': ['int', 'void', 'epsilon'],
          'Declaration-list': ['int', 'void', 'epsilon'],
          'Declaration': ['int', 'void'],
          'Declaration-initial': ['int', 'void'],
          'Declaration-prime': [';', '[', '('],
          'Var-declaration-prime': [';', '['],
          'Fun-declaration-prime': ['('],
          'Type-specifier': ['int', 'void'],
          'Params': ['int', 'void'],
          'Param-list': [',', 'epsilon'],
          'Param': ['int', 'void'],
          'Param-prime': ['[', 'epsilon'],
          'Compound-stmt': ['{'],
          'Statement-list': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return', 'epsilon'],
          'Statement': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return'],
          'Expression-stmt': ['ID', ';', 'NUM', '(', 'break'],
          'Selection-stmt': ['if'],
          'Iteration-stmt': ['repeat'],
          'Return-stmt': ['return'],
          'Return-stmt-prime': ['ID', ';', 'NUM', '('],
          'Expression': ['ID', 'NUM', '('],
          'B': ['[', '(', '=', '<', '==', '+', '-', '*', 'epsilon'],
          'H': ['=', '<', '==', '+', '-', '*', 'epsilon'],
          'Simple-expression-zegond': ['NUM', '('],
          'Simple-expression-prime': ['(', '<', '==', '+', '-', '*', 'epsilon'],
          'C': ['<', '==', 'epsilon'],
          'Relop': ['<', '=='],
          'Additive-expression': ['ID', 'NUM', '('],
          'Additive-expression-prime': ['(', '+', '-', '*', 'epsilon'],
          'Additive-expression-zegond': ['NUM', '('],
          'D': ['+', '-', 'epsilon'],
          'Addop': ['+', '-'],
          'Term': ['ID', 'NUM', '('],
          'Term-prime': ['(', '*', 'epsilon'],
          'Term-zegond': ['NUM', '('],
          'G': ['*', 'epsilon'],
          'Factor': ['ID', 'NUM', '('],
          'Var-call-prime': ['[', '(', 'epsilon'],
          'Var-prime': ['[', 'epsilon'],
          'Factor-prime': ['(', 'epsilon'],
          'Factor-zegond': ['NUM', '('],
          'Args': ['ID', 'NUM', '(', 'epsilon'],
          'Arg-list': ['ID', 'NUM', '('],
          'Arg-list-prime': [',', 'epsilon']}

follow = {'Program': ["$"],
          'Declaration-list': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Declaration': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Declaration-initial': [';', '[', '(', ')', ','],
          'Declaration-prime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Var-declaration-prime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return',
                                    '$'],
          'Fun-declaration-prime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return',
                                    '$'],
          'Type-specifier': ['ID'],
          'Params': [')'],
          'Param-list': [')'],
          'Param': [')', ','],
          'Param-prime': [')', ','],
          'Compound-stmt': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'else', 'repeat', 'until',
                            'return', '$'],
          'Statement-list': ['}'],
          'Statement': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Expression-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Selection-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Iteration-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Return-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Return-stmt-prime': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
          'Expression': [';', ']', ')', ','],
          'B': [';', ']', ')', ','],
          'H': [';', ']', ')', ','],
          'Simple-expression-zegond': [';', ']', ')', ','],
          'Simple-expression-prime': [';', ']', ')', ','],
          'C': [';', ']', ')', ','],
          'Relop': ['ID', 'NUM', '('],
          'Additive-expression': [';', ']', ')', ',', '<', '=='],
          'Additive-expression-prime': [';', ']', ')', ',', '<', '=='],
          'Additive-expression-zegond': [';', ']', ')', ',', '<', '=='],
          'D': [';', ']', ')', ',', '<', '=='],
          'Addop': ['ID', 'NUM', '('],
          'Term': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Term-prime': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Term-zegond': [';', ']', ')', ',', '<', '==', '+', '-'],
          'G': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Factor': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Var-call-prime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Var-prime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Factor-prime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Factor-zegond': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Args': [')'],
          'Arg-list': [')'],
          'Arg-list-prime': [')']}

non_terminals = ['Program', 'Declaration-list', 'Declaration', 'Declaration-initial', 'Declaration-prime',
                 'Var-declaration-prime', 'Fun-declaration-prime', 'Type-specifier', 'Params', 'Param-list', 'Param',
                 'Param-prime', 'Compound-stmt', 'Statement-list', 'Statement', 'Expression-stmt', 'Selection-stmt',
                 'Iteration-stmt', 'Return-stmt', 'Return-stmt-prime', 'Expression', 'B', 'H', 'Simple-expression-zegond',
                 'Simple-expression-prime', 'C', 'Relop', 'Additive-expression', 'Additive-expression-prime',
                 'Additive-expression-zegond', 'D', 'Addop', 'Term', 'Term-prime', 'Term-zegond', 'G', 'Factor',
                 'Var-call-prime', 'Var-prime', 'Factor-prime', 'Factor-zegond', 'Args', 'Arg-list', 'Arg-list-prime']

terminals = []

starter_of_non_terminals = {'Program': 0, 'Declaration-list': 2, 'Declaration': 5, 'Declaration-initial': 8,
                            'Declaration-prime': 11, 'Var-declaration-prime': 13, 'Fun-declaration-prime': 18,
                            'Type-specifier': 23, 'Params': 25, 'Param-list': 30, 'Param': 34, 'Param-prime': 37,
                            'Compound-stmt': 40, 'Statement-list': 45, 'Statement': 48, 'Expression-stmt': 50,
                            'Selection-stmt': 54, 'Iteration-stmt': 62, 'Return-stmt': 69, 'Return-stmt-prime': 72,
                            'Expression': 75, 'B': 78, 'H': 83, 'Simple-expression-zegond': 87,
                            'Simple-expression-prime': 90, 'C': 93, 'Relop': 96, 'Additive-expression': 99,
                            'Additive-expression-prime': 102, 'Additive-expression-zegond': 105, 'D': 108, 'Addop': 112,
                            'Term': 114, 'Term-prime': 117, 'Term-zegond': 120, 'G': 123, 'Factor': 127,
                            'Var-call-prime': 132, 'Var-prime': 136, 'Factor-prime': 140, 'Factor-zegond': 144,
                            'Args': 148, 'Arg-list': 150, 'Arg-list-prime': 153}
