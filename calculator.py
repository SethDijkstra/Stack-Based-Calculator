from stack import ArrayStack
from bst import BinarySearchTree


class PostfixCalculator:

    def __init__(self):
        # BST to store variables
        self.variableTree = BinarySearchTree()
        # stack for evaluation
        self.stack = ArrayStack()

    def evaluatePostfixExpression(self, expression):
        # clear stack before each evaluation
        self.stack.clear()

        tokens = expression.split()

        for token in tokens:

            # operator case
            if token in ['+', '-', '*', '/']:
                if self.stack.size() < 2:
                    print("Error: Not enough operands")
                    return None

                operand2 = self.stack.pop()
                operand1 = self.stack.pop()

                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    if operand2 == 0:
                        print("Error: Division by zero")
                        return None
                    result = operand1 // operand2

                self.stack.push(result)

            # number case
            elif token.lstrip('-').isdigit():
                self.stack.push(int(token))

            # variable case
            else:
                value = self.variableTree.search(token)
                if value is None:
                    print(f"Error: Variable '{token}' not found")
                    return None
                self.stack.push(value)

        # final result check
        if self.stack.size() != 1:
            print("Error: Invalid postfix expression")
            return None

        return self.stack.pop()

    def setVariable(self, key, value):
        self.variableTree.insert(key, value)

    def deleteAllVariables(self):
        self.variableTree.delete_all()

    def displayVariables(self):
        self.variableTree.display_tree()
