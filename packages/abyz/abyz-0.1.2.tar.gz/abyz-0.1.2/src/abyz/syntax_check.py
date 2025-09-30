from string import ascii_letters

def syntax_condition(char: str) -> bool:
    """Condition to check for non-ascii characters"""
    
    return char not in ascii_letters and char!=" " and char not in "\n\t\r"

def syntax_check(content: str) -> None:
    """Function to check for non-ascii characters in the content"""

    chars = list(content)

    for char in chars:
        if syntax_condition(char):
            raise SyntaxError(f"Non-ascii character found: '{char}' (ord: {ord(char)})")

    