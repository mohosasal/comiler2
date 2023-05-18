# Mohammad Mahdi Heydari Nasab, 99105389
# Mohammad Hossein Salimi, 99101738


action_to_action_number = {
    "alphabet": 0,
    "digit": 1,
    "whitespace": 2,
    "slash": 3,
    "star": 4,
    "equal": 5,
    "symbol": 6,
    "invalid": 7
}

state_number_to_state = {0: ("start", "non_terminal"),
                         1: ("number", "non_terminal"),
                         2: ("NUM", "terminal"),
                         3: ("Invalid number", "error"),
                         4: ("variable", "non_terminal"),
                         5: ("Invalid input", "error"),
                         6: ("before_end_of_comment", "non_terminal"),
                         7: ("valid_comment", "terminal"),
                         8: ("SYMBOL", "terminal"),
                         9: ("equal", "non_terminal"),
                         10: ("whitespace", "terminal"),
                         11: ("slash", "non_terminal"),
                         12: ("comment", "non_terminal"),
                         13: ("star", "non_terminal"),
                         14: ("Unmatched comment", "error"),
                         15: ("valid_variable", "terminal"),
                         16: ("invalid comment", "error"),
                         17: ("symbol_with_lookahead", "terminal")}

dfa_matrix = [[4, 1, 10, 11, 13, 9, 8, 5],
              [3, 1, 2, 2, 2, 2, 2, 5],
              [2, 2, 2, 2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3, 3, 3, 3],
              [4, 4, 15, 15, 15, 15, 15, 5],
              [5, 5, 5, 5, 5, 5, 5, 5],
              [12, 12, 12, 7, 12, 12, 12, 12],
              [7, 7, 7, 7, 7, 7, 7, 7],
              [8, 8, 8, 8, 8, 8, 8, 8],
              [17, 17, 17, 17, 17, 8, 17, 5],
              [10, 10, 10, 10, 10, 10, 10, 10],
              [16, 16, 16, 16, 12, 16, 16, 5],
              [12, 12, 12, 12, 6, 12, 12, 12],
              [17, 17, 17, 14, 17, 17, 17, 5],
              [14, 14, 14, 14, 14, 14, 14, 14],
              [15, 15, 15, 15, 15, 15, 15, 15],
              [16, 16, 16, 16, 16, 16, 16, 16],
              [17, 17, 17, 17, 17, 17, 17, 17]]

keywords = ["break", "else", "if", "int", "repeat", "return", "until", "void"]
symbol_table = keywords.copy()


class MyFuckingScanner:
    # def __int__(self, file_to_read):
    #     self.index = 0
    #     self.str_line = 1
    #     self.state = 0
    #     f = open(file_to_read, "r")
    #     self.file = f.read().split("\n")
    #     self.tokens = dict()

    def __init__(self, file_to_read):
        self.index = 0
        self.str_line = 0
        self.state = 0
        f = open(file_to_read, "r")
        self.file = f.read().split("\n")
        self.tokens = dict()
        self.str = self.file[self.str_line]
        for i in range(len(self.file)):
            self.file[i] += ' '
    def dfa_transition(state_number, transition):
        transition_index = action_to_action_number[transition]
        new_state = dfa_matrix[state_number][transition_index]
        return new_state

    def get_str_line(self):
        return self.str_line + 1
    def get_next_token(self):
        if self.str_line >= len(self.file):
            return 0, ('END', '$')
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u",
                    "v", "w", "x", "y", "z", "A", "B", "C", "D", 'E', 'F', 'G', 'H', 'I', "J", 'K', 'L', 'M', 'N', 'O',
                    "P",
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        symbols = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-", "<"]
        whitespace_ascii_codes = [32, 10, 13, 9, 11, 12]
        next_index = self.index
        if next_index >= len(self.str):
            self.index = 0
            self.str_line += 1
            if self.str_line < len(self.file):
                self.str = self.file[self.str_line]
            return self.get_next_token()
        while True:
            if state_number_to_state[self.state][1] != "non_terminal":
                break
            if next_index == len(self.str):
                break
            character = self.str[next_index]
            if character in digits:
                action = "digit"
            elif character in alphabet:
                action = "alphabet"
            elif ord(character) in whitespace_ascii_codes:
                action = "whitespace"
            elif character == "/":
                action = "slash"
            elif character == "*":
                action = "star"
            elif character == "=":
                action = "equal"
            elif character in symbols:
                action = "symbol"
            else:
                action = "invalid"
            self.state = MyFuckingScanner.dfa_transition(self.state, action)
            next_index += 1
        state_string = state_number_to_state[self.state][0]
        state_type = state_number_to_state[self.state][1]

        if state_type == "error":
            if state_string == "invalid comment":
                next_index -= 1
                token_string = 'Invalid input'
            else:
                token_string = state_string
            print(token_string, self.str[self.index:next_index])
        elif state_type == "non_terminal":
            print(self.state)
            token_string = 'Unclosed comment'
        elif state_type == "terminal":
            if state_string == "NUM":
                next_index -= 1
                token_string = state_string
            elif state_string == "valid_comment" or state_string == "whitespace":
                self.index = next_index
                self.state = 0
                return self.get_next_token()
            elif state_string == "SYMBOL":
                token_string = state_string
            elif state_string == "symbol_with_lookahead":
                next_index -= 1
                token_string = "SYMBOL"
            elif state_string == "valid_variable":
                next_index -= 1
                if self.str[self.index:next_index] in keywords:
                    token_string = "KEYWORD"
                else:
                    token_string = "ID"
                if self.str[self.index:next_index] not in symbol_table:
                    symbol_table.append(self.str[self.index:next_index])
            else:
                token_string = ""
        if state_type == "non_terminal":
            self.state = 12
        else:
            self.state = 0
        saved_str = self.str[self.index:next_index]
        if next_index >= len(self.str):
            self.index = 0
            self.str_line += 1
            if self.str_line < len(self.file):
                self.str = self.file[self.str_line]
        else:
            self.index = next_index
        # print((token_string, saved_str))
        return next_index, (token_string, saved_str)
