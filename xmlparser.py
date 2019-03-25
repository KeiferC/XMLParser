#
#       filename:       xmlparser.py
#       author:         @KeiferC
#       date:           25 Mar. 2019
#       version:        0.0.1
#       
#       description:    converts a given XML file to a CSV file
#
#       usage:          python xmlparser.py -r <row_tag> <FILE>
#                                           [-c <category_tag>]
#                                           [-o <output_file>]
#
#       TODO:         Modularize main (variable assignment by reference)
#                     Check for input file type (assert xml)
#                     Add output file type varieties
#               
#

import sys, re

# 
# main
#
# Handles command line argument parsing and runs 
# the program
#
# @param        n/a
# @return       n/a
#
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

                        else:
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
        fwrite(parse(line_list, row_tag, cat_tag), out_filename)
        sys.exit()

# 
# parse
#
# Given a list of lines from an XML file, a row tag, and
# an optional category tag, returns a list of row elements
#
# @param        list - list of lines from XML file
# @param        string - row tag
# @param        string - category tag
# @return       list - list of rows
#
def parse(line_list, row_tag, cat_tag):
        row_list = []
        index = None

        # Parse category tag if exists
        if cat_tag != None:
                index = search(line_list, cat_tag)

                if index == -1:
                        sys.exit('category tag not found')

                row_list.append(get_row(line_list, index))

        # Parse through rows
        index = search(line_list, row_tag)

        if index == -1:
                sys.exit('row tag not found')

        while line_list[index].startswith('<' + row_tag):
                row_list.append(get_row(line_list, index))
                index += 1

        return row_list

# 
# search
#
# Given a list and a tag, returns the index in which the
# tag appears within the list. Returns -1 if not found
#
# @param        list - list of lines from XML file
# @param        string - tag to be searched
# @return       int - index in which tag is found
#
def search(line_list, tag):
        for i in range(len(line_list)):
                if line_list[i].startswith('<' + tag):
                        return i
        return -1

# 
# get_row
#
# Given a list and an index, parses through the line in
# the list and returns the isolated row elements in the
# form of a list
#
# @param        list - list of lines from XML file
# @param        int - index to parse
# @return       list - row (list of elements)
#
def get_row(line_list, index):
        row = []
        line = str(line_list[index])
        row_close = None
        tag_closer = None

        line = line.split('>')
        row_close = line[0].replace('<', '</')
        
        for i in range(1, len(line)):
                if line[i] == row_close:
                        break
                if line[i].startswith('<'):
                        continue
                tag_closer = re.compile(re.escape('</') + '.*')
                row.append(tag_closer.sub('', line[i]))

        return row

# 
# fwrite
#
# Given a list of rows and an output filename,
# writes the list to a file in CSV form
#
# @param        list - list of CSV rows
# @param        string - output filename
# @return       n/a
#
def fwrite(row_list, out_filename):
        outf = open(out_filename, 'a')

        for i in range(len(row_list)):
                outf.write(','.join(row_list[i]) + '\n')

        outf.close()

# 
# check_assignment
#
# Exits program if required command line arguments
# are not provided
#
# @param        list - list of lines from XML file
# @param        string - row tag
# @param        string - category tag
# @return       n/a
#
def check_assignment(line_list, row_tag, cat_tag):
        if len(line_list) == 0 or row_tag == None or row_tag == cat_tag:
                usage()
                sys.exit('Missing argument(s)')

# 
# usage
#
# Prints program usage instructions
#
# @param        n/a
# @return       n/a
#
def usage():
        print('''Usage:         python xmlparser.py -r <row_tag> <FILE>
                                   [-c <category_tag>]
                                   [-o <output_file>]''')


main()
