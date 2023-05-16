
#################################### imports

import Scanner
from anytree import Node, RenderTree
import td




#################################### main class



class Parser:

    def __init__(self ,scanner):
        self.main_node =Node("Program")
        self.scanner =scanner
        self.token=""
        self.messages=[]





    def diagram_transition(self,this_node,state,line):

        rented1 = False
        rented2= False



        ##########the state of finals

        if len(td.transition_diagrams[line][state])==0:
            return

        ##########other states


        for transition in td.transition_diagrams[line][state].keys():

            #checking for transtitions first without epsilon
            if self.token in td.first[transition] :
                rented1=True
                that_node = Node(transition, parent=this_node)

                if transition in td.non_terminals:

                    self.diagram_transition(that_node,td.starter_of_non_terminals[transition],transition)
                    self.diagram_transition(this_node,td.transition_diagrams[line][state][self.token],line)

                else:
                    self.token = self.scanner.get_next_token()

                    return


        if rented1==False:           # epsilon handling

            for transition in td.transition_diagrams[line][state].keys():

                if "epsilon" in td.first[transition] and self.token in td.follow[transition]:

                    rented2=True

                    that_node = Node(transition, parent=this_node)

                    if transition in td.non_terminals:

                        self.diagram_transition(that_node, td.starter_of_non_terminals[transition], transition)

                    else:
                        self.diagram_transition(this_node, td.transition_diagrams[line][state][self.token], line)


        elif rented2==False:               #error handling


            if self.token not in td.follow[line]:

                #illegal token message

                error_message="illegal"+" "+self.token
                self.messages.append(error_message)

                #start over from this line

                self.token = self.scanner.get_next_token()
                self.diagram_transition(this_node, td.starter_of_non_terminals[line],line)

            else:

                #missing line

                error_message="missing"+" "+line
                self.messages.append(error_message)
                return

                #exit this line






