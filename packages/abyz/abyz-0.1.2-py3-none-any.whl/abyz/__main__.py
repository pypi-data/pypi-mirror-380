import os
import argparse
from abyz.compiler import compile

def main():

    # Parse in and out arguments
    parser = argparse.ArgumentParser(description ='abyz script compiler')
    parser.add_argument('-s', '--source', type = str, help ='abyz source code to be compiled', required=True)
    parser.add_argument('-o', '--output', type = str, help ='output file name')
    parser.add_argument('-x', '--exec', action='store_true', help ='execute the program')

    args = parser.parse_args()
    source = args.source
    output = args.output
    exec_code = args.exec

    out = compile(source, output)

    if exec_code:
        os.system("python "+out)

if __name__ == "__main__":
    
    main()