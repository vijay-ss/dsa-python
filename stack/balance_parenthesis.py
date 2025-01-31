from stack import Stack


def is_balanced_parenthesis(paren_string: str) -> bool:
    """
    Use a stack to check whether or not a string
    has balanced usage of parenthesis.

    Example:
        (), ()(), (({[]}))  <- Balanced.
        ((), {{{)}], [][]]] <- Not Balanced.


    Balanced Example: {[]}


    Non-Balanced Example: (()

    Non-Balanced Example: ))
    """
    stack = Stack()
    left_paren = ["(", "{", "["]
    right_paren = [")", "}", "]"]

    for char in paren_string:
        if char in left_paren:
            stack.push(char)
        if char in right_paren:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if not is_match(char, top):
                    return False

    return stack.size == 0


def is_match(char1: str, char2: str) -> bool:
    match_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    return match_dict[char1] == char2     


if __name__ == '__main__':
    print(is_balanced_parenthesis(r"({a+b})"))
    print(is_balanced_parenthesis(r"(h"))
    print(is_balanced_parenthesis(r"(({[]}))"))