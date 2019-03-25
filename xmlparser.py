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
                                row_tag = sys.argv[i + 1]
                                i += 1
                        elif (sys.argv[i] == '-c') and (i + 1 < arg_len):
                                cat_tag = sys.argv[i + 1]
                                i += 1
                        elif (sys.argv[i] == '-o') and (i + 1 < arg_len):
                                out_filename = sys.argv[i + 1]

                                if not out_filename.endswith('.csv'):
                                        out_filename += '.csv'

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

        check_assignment(line_list, row_tag, cat_tag)

        #debug
        parse(line_list, row_tag, cat_tag)

        #TODO: fwrite(parse(line_list, row_tag, cat_tag))
        sys.exit()

# Parse
def parse(line_list, row_tag, cat_tag):
        row_list = []
        line_list_index = None

        if cat_tag != None:
                line_list_index = search(line_list, cat_tag)

                if line_list_index == -1:
                        sys.exit('category tag not found')
                
                row_list.append(get_row(line_list, line_list_index))
                

# Search
def search(line_list, tag):
        for i in range(len(line_list)):
                if line_list[i].startswith('<' + tag):
                        return i + 1

        return -1

# Get row


# File Write
def fwrite(row_list, out_filename):
        outf = open(out_filename, 'a')

        for i in range(len(row_list)):
                outf.write(','.join(row_list[i]) + '\n')

        outf.close()


# Check assignment
def check_assignment(line_list, row_tag, cat_tag):
        if len(line_list) == 0 or row_tag == None or row_tag == cat_tag:
                usage()
                sys.exit('Missing argument(s)')

# Usage failure
def usage():
        print('''Usage:         python xmlparser.py -r <row_tag> <FILE>
                                      [-c <category_tag>]
                                      [-o <output_file>]''')

main()
