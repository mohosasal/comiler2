#################################### imports

import scanner
from anytree import Node, RenderTree
import td


#################################### main class


class MyParser:

    def __init__(self, scanner):
        self.main_node = Node("Program")
        self.scanner = scanner
        self.all_token = self.scanner.get_next_token()
        self.token = self.get_what_we_need_from_token()
        self.messages = []

    def get_what_we_need_from_token(self):
        if self.all_token[1][0] == 'NUM' or self.all_token[1][0] == 'ID':
            return self.all_token[1][0]
        else:
            return self.all_token[1][1]

    def diagram_transition(self, this_node, state, line):
        rented1 = False
        rented2 = False

        ##########the state of finals

        if len(td.transition_diagrams[line][state]) == 0:
            return

        ##########other states

        for transition in td.transition_diagrams[line][state].keys():

            # checking for transtitions first without epsilon
            if self.token in td.first(transition):
                rented1 = True
                rented2 = True

                if transition in td.non_terminals:
                    that_node = Node(transition, parent=this_node)
                    self.diagram_transition(that_node, td.starter_of_non_terminals[transition], transition)
                    self.diagram_transition(this_node, td.transition_diagrams[line][state][transition], line)

                else:
                    if self.token == '$':
                        Node('$', parent=this_node)
                    else:
                        Node(self.all_token[1], parent=this_node)
                    self.all_token = self.scanner.get_next_token()
                    self.token = self.get_what_we_need_from_token()
                    self.diagram_transition(this_node, td.transition_diagrams[line][state][transition], line)
                break

        if rented1 == False:  # epsilon handling
            
            for transition in td.transition_diagrams[line][state].keys():

                if "epsilon" in td.first(transition):
                    rented2 = True
                    that_node = Node(transition, parent=this_node)

                    if transition in td.non_terminals:

                        self.diagram_transition(that_node, td.starter_of_non_terminals[transition], transition)
                        self.diagram_transition(this_node, td.transition_diagrams[line][state][transition], line)

                    else:
                        self.diagram_transition(this_node, td.transition_diagrams[line][state][transition], line)
                    break


        if rented2 == False:  # error handling
            transition = list(td.transition_diagrams[line][state].keys())[0]
            non_terminal_exist = False
            for trans in td.transition_diagrams[line][state].keys():
                if trans in td.non_terminals:
                    non_terminal_exist = True
            if not non_terminal_exist:
                error_message = 'missing ' + transition
                self.messages.append(error_message)
                self.diagram_transition(this_node, td.transition_diagrams[line][state][transition], line)
                return
            if self.token not in td.follow[line]:

                # illegal token message

                error_message = "illegal" + " " + self.token
                self.messages.append(error_message)

                # start over from this line

                self.all_token = self.scanner.get_next_token()
                self.token = self.get_what_we_need_from_token()
                self.diagram_transition(this_node, state, line)

            else:

                # missing line

                error_message = "missing" + " " + line
                self.messages.append(error_message)
                return

                # exit this line

            ################################## !!!!!!!!!!!!!!!!!   third error should be handled!
