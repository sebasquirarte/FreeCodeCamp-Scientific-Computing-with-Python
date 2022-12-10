# Arithmetic Arranger | Part of FreeCodeCamp's 'Scientific Computing with Python Certification'
# Sebastian Quirarte | 10 Dec 22 | sebastianquirajus@gmail.com

def arithmetic_arranger(problems, solution = False):
    """
    Receives a list of strings that are arithmetic problems (addition or subtraction) 
    and returns the problems arranged vertically and side-by-side.
    If result is set to True, the answers are displayed as well.
    Possible errors:
        'Error: Too many problems.' More than 5 problems supplied to the function.
        'Error: Too many operands.' More than 2 operands per problem supplied to the function.
        'Error: Operator must be '+' or '-'.'
        'Error: Numbers must only contain digits.'
        'Error: Numbers cannot be more than four digits.'
    """
  # Verify that there aren't more than 5 problems
  if len(problems) > 5:
    return("Error: Too many problems.")
  else:
    # Create empty rows
    first_row = ""
    second_row = ""
    separator_row = ""
    result_row = ""

    counter = 0
    # Go through each problem
    for problem in problems:
      p_split = problem.split()

      # Verify that only two operands and one operator
      if len(p_split) > 3:
        return("Error: Too many operands.")

      # Get operands and operator
      num1 = (p_split[0])
      operator = p_split[1]
      num2 = (p_split[2])

      # Verify operands are numbers and less than 4 digits
      if not num1.isnumeric() or not num2.isnumeric():
        return("Error: Numbers must only contain digits.")
      if len(num1) > 4 or len(num2) > 4:
        return("Error: Numbers cannot be more than four digits.")

      # Determines length of longest operand
      if len(num1) > len(num2) or len(num1) == len(num2):
        length = len(num1)
      else:
        length = len(num2)

      # Sum operator
      if operator == "+":
        result = int(num1) + int(num2)
      # Subtraction operator
      elif operator == "-":
        result = int(num1) - int(num2)
      # Invalid operator
      else:
        return("Error: Operator must be '+' or '-'.")

      # Format problem
      num1_format = num1.rjust(length + 2)
      num2_format = operator + num2.rjust(length + 1)
      separator_format = "-" * (len(num2_format))
      answer_format = str(result).rjust(length + 2)

      # Add values to corresponding row
      # No spacing if first problem
      if counter == 0:
        first_row = first_row + num1_format
        second_row = second_row + num2_format
        separator_row = separator_row + separator_format
        result_row = result_row + answer_format
      # Add spacing if not first problem
      else:
        first_row = first_row + (" " * 4) + num1_format
        second_row = second_row + (" " * 4) + num2_format
        separator_row = separator_row + (" " * 4) + separator_format
        result_row = result_row + (" " * 4) + answer_format

      counter += 1

    # Create arranged problems with answer
    if solution:
      arranged_problems = "%s\n%s\n%s\n%s" % (first_row, second_row, separator_row, result_row)
    # Create arranged problems without answer
    else:
      arranged_problems = "%s\n%s\n%s" % (first_row, second_row, separator_row)

    return arranged_problems
