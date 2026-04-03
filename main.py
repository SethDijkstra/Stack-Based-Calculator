from stack import ArrayStack
from bst import BinarySearchTree


def evaluate_postfix(expression, variables):
    """
    Evaluates a postfix expression and returns the result.
    
    Args:
        expression: A string containing the postfix expression
        variables: A BinarySearchTree containing variable names and values
    
    Returns:
        The integer result of the expression, or None if there was an error
    """
    stack = ArrayStack()
    tokens = expression.split()
    
    for token in tokens:
        # check if the token is an operator
        if token in ['+', '-', '*', '/', '%']:
            # make sure we have at least two operands on the stack
            if stack.size() < 2:
                print("Error: Not enough operands for operation")
                return None
            
            # pop two operands (order matters for subtraction and division)
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # perform the operation based on which operator we have
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
            elif token == '%':
                if operand2 == 0:
                    print("Error: Modulo by zero")
                    return None
                result = operand1 % operand2
            
            # push the result back onto the stack
            stack.push(result)
        
        # check if the token is a number (including negative numbers)
        elif token.lstrip('-').isdigit():
            stack.push(int(token))
        
        # if it is not an operator or number it must be a variable
        else:
            # look up the variable in the binary search tree
            value = variables.search(token)
            if value is None:
                print(f"Error: Variable '{token}' not found")
                return None
            stack.push(value)
    
    # after processing all tokens there should be exactly one value left
    if stack.size() != 1:
        print("Error: Invalid postfix expression")
        return None
    
    return stack.pop()


def main():
    """
    Main function that runs the calculator interface.
    Handles user input and manages the variable storage.
    """
    variables = BinarySearchTree()
    
    print("Stack-Based Calculator for Postfix Notation")
    print("Commands:")
    print("  Enter a postfix expression to evaluate")
    print("  var_name = postfix_expression (to store result in variable)")
    print("  display (to show all variables)")
    print("  delete var_name (to delete a variable)")
    print("  delete all (to delete all variables)")
    print("  quit (to exit)")
    print()
    
    # main loop to keep asking for input until user quits
    while True:
        user_input = input("> ").strip()
        
        # skip empty input
        if user_input == "":
            continue
        
        # check if user wants to quit
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        # check if user wants to display all variables
        if user_input.lower() == "display":
            print("Variables in the tree:")
            variables.display_tree()
            continue
        
        # check if user wants to delete all variables
        if user_input.lower().startswith("delete all"):
            variables.delete_all()
            print("All variables deleted")
            continue
        
        # check if user wants to delete a specific variable
        if user_input.lower().startswith("delete "):
            var_name = user_input.split()[1]
            variables.delete(var_name)
            print(f"Variable '{var_name}' deleted")
            continue
        
        # check if user wants to assign a result to a variable
        if '=' in user_input:
            parts = user_input.split('=')
            var_name = parts[0].strip()
            expression = parts[1].strip()
            
            result = evaluate_postfix(expression, variables)
            if result is not None:
                variables.insert(var_name, result)
                print(f"{var_name} = {result}")
        
        # otherwise just evaluate the expression and display the result
        else:
            result = evaluate_postfix(user_input, variables)
            if result is not None:
                print(f"Result: {result}")


if __name__ == "__main__":
    main()
