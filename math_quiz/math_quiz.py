import random


def generate_random_integer(min_value: int, max_value: int) -> int:
    """
    Generates a random integer within the specified inclusive range [min_value, max_value].

    Args:
        min_value (int): The minimum possible value.
        max_value (int): The maximum possible value.

    Returns:
        int: A random integer between min_value and max_value, inclusive.

    Raises:
        ValueError: If min_value is greater than max_value.

    Example:
    >>> generate_random_integer(2, 10)
    7
    >>> generate_random_integer(4, 5)
    4
    >>> generate_random_integer(6, 1)
    ValueError
    """
    return random.randint(int(min_value), int(max_value))


def get_random_operator() -> str:
    """
    Returns a random arithmetic operator from the set: '+', '-', or '*'.

    Returns:
        str: A randomly chosen arithmetic operator from '+', '-', or '*'.

    Example:
    >>> get_random_operator()
    '-'
    """
    return random.choice(["+", "-", "*"])


def execute_arithmetic_operation(
    left_operand: int, right_operand: int, operator: str
) -> tuple[str, int]:
    """
    Executes an arithmetic operation based on the provided operands and operator.

    Args:
        left_operand (int): The first (left) operand.
        right_operand (int): The second (right) operand.
        operator (str): The arithmetic operator, which can be one of '+', '-', or '*'.

    Returns:
        tuple[str, int]: A tuple containing the expression as a string and the result of the expression as an integer.

    Raises:
        ValueError: If the operator is not one of '+', '-', or '*'.

    Example:
    >>> execute_arithmetic_operation(6, 1, '-')
    ('6 + 1', 5)
    >>> execute_arithmetic_operation(9, 3, 'q')
    ValueError: Invalid operator! Only '+', '-', and '*' are allowed.
    """
    if operator not in {"+", "-", "*"}:
        raise ValueError("Invalid operator! Only '+', '-', and '*' are allowed.")

    expression = f"{left_operand} {operator} {right_operand}"

    match operator:
        case "+":
            result = left_operand + right_operand
        case "-":
            result = left_operand - right_operand
        case "*":
            result = left_operand * right_operand

    return expression, result


def play_math_quiz():
    """Start a math quiz game where users solve randomly generated
    arithmetic problems.

    The total score will be displayed at the end.

    Returns:
        None

    Example:
    >>> play_math_quiz()
    Welcome to the Math Quiz Game!
    You will be presented with math problems, and you need to provide the correct answers.

    Question: 2 + 1
    Your answer: 3
    Correct! You earned a point.

    Question: 1 * 9
    Your answer: 8
    Wrong answer. The correct answer is 9.

    Question: 5 - 1
    Your answer: 4
    Correct! You earned a point.

    Game over! Your score is: 2/3
    """
    earned_score = 0
    TOTAL_QUESTIONS = 3

    print("Welcome to the Math Quiz Game!")
    print(
        "You will be presented with math problems, "
        "and you need to provide the correct answers."
    )

    for _ in range(TOTAL_QUESTIONS):
        # Generate random operands and operator
        left_operand = generate_random_integer(1, 10)
        right_operand = generate_random_integer(1, 5)
        operator = get_random_operator()

        # Formulate problem and compute the correct answer
        PROBLEM, ANSWER = execute_arithmetic_operation(
            left_operand,
            right_operand,
            operator,
        )
        print(f"\nQuestion: {PROBLEM}")

        # Capture and validate user input
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input! Please enter a numerical answer.")

        # Check the user's answer and update score
        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            earned_score +=1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Display the final score
    print(f"\nGame over! Your score is: {earned_score}/{TOTAL_QUESTIONS}")


if __name__ == "__main__":
    play_math_quiz()
