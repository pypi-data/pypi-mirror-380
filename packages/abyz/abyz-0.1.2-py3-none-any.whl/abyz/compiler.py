import argparse
from .replacements import replace_singles
from .correct import correct
from .syntax_check import syntax_check

def compile(source: str, output: str | None = None) -> str:
    """Main compiler function, which takes abyz code and transpiles it to python code"""

    if output is None:
        output = source.replace(".abyz",".py")

    # Read abyz code to compile
    with open(source, encoding='utf-8') as file:
        content = file.read()

    # Check for non-ascii characters
    syntax_check(content)

    content = content.split("\n")

    # Replace reserved words with their respective python code
    content = replace_singles(content,"numbers")
    content = replace_singles(content,"symbols")

    # Remove spaces, commented for now due to some issues
    #for i, row in enumerate(content):
    #    content[i] = row.replace(" ", "")

    # Add extra corrections for some spaces
    content = correct(content)

    # Write compiled code to executable file
    with open(output, "w") as f:
        f.write("\n".join(content) + "\n")

    # Return output file path for being executed if needed
    return output

if __name__=="__main__":

    # Parse in and out arguments
    parser = argparse.ArgumentParser(description ='abyz script compiler')
    parser.add_argument('-s', '--source', type = str, help ='abyz code to be compiled', required=True)
    parser.add_argument('-o', '--output', type = str, help ='output file name')

    args = parser.parse_args()
    source = args.source
    output = args.output

    compile(source, output)
