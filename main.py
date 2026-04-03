from stack import ArrayStack
from bst import BinarySearchTree


def evaluate_postfix(expression, variables):
    stack = ArrayStack()
    tokens = expression.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/', '%']:
            if stack.size() < 2:
                print("Error: Not enough operands for operation")
                return None
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
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
            
            stack.push(result)
        
        elif token.lstrip('-').isdigit():
            stack.push(int(token))
        
        else:
            value = variables.search(token)
            if value is None:
                print(f"Error: Variable '{token}' not found")
                return None
            stack.push(value)
    
    if stack.size() != 1:
        print("Error: Invalid postfix expression")
        return None
    
    return stack.pop()


def main():
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
    
    while True:
        user_input = input("> ").strip()
        
        if user_input == "":
            continue
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        if user_input.lower() == "display":
            print("Variables in the tree:")
            variables.display_tree()
            continue
        
        if user_input.lower().startswith("delete all"):
            variables.delete_all()
            print("All variables deleted")
            continue
        
        if user_input.lower().startswith("delete "):
            var_name = user_input.split()[1]
            variables.delete(var_name)
            print(f"Variable '{var_name}' deleted")
            continue
        
        if '=' in user_input:
            parts = user_input.split('=')
            var_name = parts[0].strip()
            expression = parts[1].strip()
            
            result = evaluate_postfix(expression, variables)
            if result is not None:
                variables.insert(var_name, result)
                print(f"{var_name} = {result}")
        
        else:
            result = evaluate_postfix(user_input, variables)
            if result is not None:
                print(f"Result: {result}")


if __name__ == "__main__":
    main()
