from calculator import PostfixCalculator

def main():
    """
    Main function that runs the calculator interface.
    """
    calculator = PostfixCalculator()
    
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
        
        # display BST
        if user_input.lower() == "display":
            print("Variables in the tree:")
            calculator.displayVariables()
            continue
        
        # delete all variables
        if user_input.lower().startswith("delete all"):
            calculator.deleteAllVariables()
            print("All variables deleted")
            continue
        
        # delete single variable
        if user_input.lower().startswith("delete "):
            var_name = user_input.split()[1]
            calculator.variableTree.delete(var_name)
            print(f"Variable '{var_name}' deleted")
            continue
        
        # assignment case
        if '=' in user_input:
            parts = user_input.split('=')
            var_name = parts[0].strip()
            expression = parts[1].strip()
            
            result = calculator.evaluatePostfixExpression(expression)
            if result is not None:
                calculator.setVariable(var_name, result)
                print(f"{var_name} = {result}")
        
        # normal evaluation
        else:
            result = calculator.evaluatePostfixExpression(user_input)
            if result is not None:
                print(f"Result: {result}")


if __name__ == "__main__":
    main()
