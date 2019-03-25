#
# xmlparser.py - converts given XML file to CSV file
#
# Usage:  python xmlparser.py [-c <category_tag>] -r <row_tag>
#                <input_file> [-o <output_file>]

import sys

# Main - Command Line
def main():
        line_list = []
        row_tag = None
        cat_tag = None
        out_file = None
        arg_len = len(sys.argv)
        i = 1

        # Command Line Parsing
        if (arg_len < 9) and (arg_len > 3) and (arg_len % 2 == 0):
                while i < arg_len:
                        if (sys.argv[i] == '-r') and (i + 1 < arg_len):
                                row_tag = str(sys.argv[i + 1])
                                i += 1
                        elif (sys.argv[i] == '-c') and (i + 1 < arg_len):
                                cat_tag = str(sys.argv[i + 1])
                                i += 1
                        elif (sys.argv[i] == '-o') and (i + 1 < arg_len):
                                out_file = str(sys.argv[i + 1])
                                i += 1
                        else: # TODO: check for file type
                                line_list = [line.rstrip('\n') for 
                                             line in open(sys.argv[i])]
                        
                        i += 1
        else:
                usage()

        # debug:
        print('\n'.join(line_list))

# Parse


# Search


# Get row


# File Write


# Usage failure
def usage():
        print('''Usage:         python xmlparser.py -r <row_tag> <FILE>
                                      [-c <category_tag>]
                                      [-o <output_file>]''')

main()
