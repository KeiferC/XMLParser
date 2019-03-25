#
# xmlparser.py - converts given XML file to CSV file
#
# Usage:  python xmlparser.py [-c <category_tag>] -r <row_tag>
#                <input_file> [-o <output_file>]

import sys

# Main - Command Line
# TODO: A way to assign variables via another function (e.g. by reference)?
def main():
        line_list = []
        row_tag = None
        cat_tag = None
        out_filename = None
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
                                out_filename = str(sys.argv[i + 1])
                                i += 1
                        else: # TODO: check for file type
                                line_list = [line.rstrip('\n') for 
                                             line in open(sys.argv[i])]
                                if out_filename == None:
                                        out_filename = \
                                        sys.argv[i].rstrip('.xml') + '.csv'
                        
                        i += 1
        else:
                usage()
                sys.exit('Usage error')

        check_assignment(line_list, row_tag)
        #debug
        row_list = [['asdf'], 
                    ['lkjhlkjh', 'lkj'], 
                    ['1234123', '0987', '789']]
        fwrite(row_list, out_filename)
        #TODO: fwrite(parse())
        sys.exit()

# Parse


# Search


# Get row


# File Write
def fwrite(row_list, out_filename):
        outf = open(out_filename, 'a')

        for i in range(len(row_list)):
                outf.write(','.join(row_list[i]) + '\n')

        outf.close()


# Check assignment
def check_assignment(line_list, row_tag):
        if len(line_list) == 0 or row_tag == None:
                usage()
                sys.exit('Missing argument(s)')

# Usage failure
def usage():
        print('''Usage:         python xmlparser.py -r <row_tag> <FILE>
                                      [-c <category_tag>]
                                      [-o <output_file>]''')

main()
