
#################################### imports

import Scanner
from anytree import Node, RenderTree


#################################### setting dfa s

transition_diagram=dict()
terminals=[]
non_terminals=[]
starter_of_non_terminals=dict()

#################################### first follow

first= {'Program': ['int', 'void', '0'],
         'Declarationlist': ['int', 'void', '0'],
         'Declaration': ['int', 'void'],
         'Declarationinitial': ['int', 'void'],
         'Declarationprime': [';', '[', '('],
         'Vardeclarationprime': [';', '['],
         'Fundeclarationprime': ['('],
         'Typespecifier': ['int', 'void'],
         'Params': ['int', 'void'],
         'Paramlist': [',', '0'],
         'Param': ['int', 'void'],
         'Paramprime': ['[', '0'],
         'Compoundstmt': ['{'],
         'Statementlist': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return', '0'],
         'Statement': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return'],
         'Expressionstmt': ['ID', ';', 'NUM', '(', 'break'],
         'Selectionstmt': ['if'],
         'Iterationstmt': ['repeat'],
         'Returnstmt': ['return'],
         'Returnstmtprime': ['ID', ';', 'NUM', '('],
         'Expression': ['ID', 'NUM', '('],
         'B': ['[', '(', '=', '<', '==', '+', '-', '*', '0'],
         'H': ['=', '<', '==', '+', '-', '*', '0'],
         'Simpleexpressionzegond': ['NUM', '('],
         'Simpleexpressionprime': ['(', '<', '==', '+', '-', '*', '0'],
         'C': ['<', '==', '0'],
         'Relop': ['<', '=='],
         'Additiveexpression': ['ID', 'NUM', '('],
         'Additiveexpressionprime': ['(', '+', '-', '*', '0'],
         'Additiveexpressionzegond': ['NUM', '('],
         'D': ['+', '-', '0'],
         'Addop': ['+', '-'],
         'Term': ['ID', 'NUM', '('],
         'Termprime': ['(', '*', '0'],
         'Termzegond': ['NUM', '('],
         'G': ['*', '0'],
         'Factor': ['ID', 'NUM', '('],
         'Varcallprime': ['[', '(', '0'],
         'Varprime': ['[', '0'],
         'Factorprime': ['(', '0'],
         'Factorzegond': ['NUM', '('],
         'Args': ['ID', 'NUM', '(', '0'],
         'Arglist': ['ID', 'NUM', '('],
         'Arglistprime': [',', '0'],
         'EPSILON': ['0']}

follow = {'Program': ["$"],
          'Declarationlist': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Declaration': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Declarationinitial': [';', '[', '(', ')', ','],
          'Declarationprime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Vardeclarationprime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Fundeclarationprime': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
          'Typespecifier': ['ID'],
          'Params': [')'],
          'Paramlist': [')'],
          'Param': [')', ','],
          'Paramprime': [')', ','],
          'Compoundstmt': ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return', '$'],
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
          'Arglistprime': [')'],
          'EPSILON': ['ID', ';', 'NUM', ']', '(', ')', ',', '{', '}', 'break', 'if', 'repeat', 'return', '<', '==', '+', '-', '*', '$']}

#################################### main class



class Parser:

    def __init__(self ,node_0,parser):
        self.main_node =Node("Program")
        self.parser=parser
        self.token=""





    def diagram_transition(self,this_node,state,line):





        ############################################### final state handling
        # if we are in the final state of the program


        if state is final_state:
            return




        ###########################################first follow   (change the functionality of first follow set up)

        rented=False
        for trans in transition_diagram[state]:

            if self.token in first[trans]:
                rented=True
                # add node to the tree in the left most child of the parrent
                that_node=Node(trans,parent=this_node)
                if trans is not terminals:
                    self.diagram_transition(that_node,first_state_of_node,token,trans)
                    #getting next token?
                    self.diagram_transition(this_node,next_state_of_this_state,next_token,line)

                else:
                    #token= get next token
                    return



        if rented==False:  # error handling

            if token not in follow[line]:
                pass
                #illegal token message
                #start over from this line
            else:
                #missing line
                #exit this line








