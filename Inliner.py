#!/usr/bin/env python3
from docopt import docopt
from sys import exit as sys_exit
from sys import stderr as sys_stderr
import json
import re

# from colorama import Fore, Back, Style

class Inliner(object):

    # REGEX for label definition and its uses
    LABEL = "[A-Za-z0-9_]+"
    label_def = re.compile("^"+LABEL+":$")
    label_use = re.compile("\{\{(@|"+LABEL+")\}\}")
    const_def = re.compile("^\' define "+LABEL+" ")

    # REGEX for search numbered lines
    line_numbered = re.compile("^[0-9]{1,} ?")

    def __init__(self, input_program, line_number, step_line, remark="\'"):

        self.basic = {}
        self.labels = {}

        self.line_number = int(line_number)
        self.step_line = int(step_line)

        self.remark = remark

        # this REGEX searchs for both strings and comments
        self.quotes = re.compile("(\"[^\"]+\"|"+remark+".*$)")

        self.__parse(input_program)


    def __json(self):
        """
        Lists code's dictionary in JSON format (used by me for debug).

        There is no input arguments and the output is the dictionary
        formated as a JSON file.
        """
        return json.dumps(self.basic, indent=2)


    def __labels(self, line, code):
        """
        Rplaces labels by line number or values.

        'line' is the BASIC's line number and 'code' are the joined BASIC
        statements. Both are the key/value pai from the 'self.basic' dictionary.
        Returns a single string begining with line number and labels translated.
        """
        for i in range(len(code)):

            while True:

                label_check = self.label_use.search(code[i])

                if label_check:
                    # retrive the label's name
                    label = label_check.group(1)

                    if label is "@":
                        # is this the 'self' label?
                        code[i] = self.__replace(
                            code[i],"{{@}}",str(line))

                    elif label in self.labels.keys():
                        # is this a common label?
                        code[i] = self.__replace(
                            code[i], "{{"+label+"}}",self.labels[label])
                        repeat = 0

                    else:
                        # warning if an undefined label was found
                        self.__message("Undefined label {} in line {}."\
                            .format(label, line))
                        sys_exit(2)
                else:
                    break

        return code


    def __message(self, text):
        """
        Prints text in POSIX's standard error.

        'text' is the text to print.
        """
        print("*** {} ***".format(text), file=sys_stderr)


    def __new_line(self, line):
        """
        Adds a new line inside 'self.basic' dictionary and increments the
        line counter.

        'line' is a string containing the BASIC statements.
        Returns a empty list to initialize 'single' list on '__parse'
        method.
        """
        self.basic[str(self.line_number)] = line
        self.line_number += self.step_line

        return []


    def __parse(self, input_file):
        """
        Parses BASIC program and populates 'self.basic' dictionary.

        'input_file' is the file to be converted.
        """
        single = []
        counter = 1

        for line in input_file:

            # removes all leading and trailing spaces
            line = line.strip()

            if line is "":
                # that's a empty line!
                if len(single)>0:
                    single = self.__new_line(single)

            elif self.line_numbered.search(line):
                # BAD: a line that begins with a number!
                self.__message('Numbered line found: {}'.format(line))

            elif line[0] is "\'":
                # looks like a comment...

                if re.search("\'\'",line):
                    # double '' are comments that will be preserved

                    if len(single)>0:
                        single = self.__new_line(single)

                    # inserts the comment
                    single = self.__new_line([
                        "{}{}".format(
                            self.remark,
                            line[2:])
                        ])

                elif self.const_def.search(line):
                    # there is a constant (aka 'define')
                    const = self.const_def.search(line)
                    value_pos = int(const.span()[1])
                    const_name = const.group()[9:value_pos-1]
                    const_value = line[value_pos:]
                    self.labels[const_name] = const_value

            elif line[-1] is ":" :
                # that's a line ending with ":"

                if self.label_def.search(line):
                    # syntax is ok, creates a new label
                    self.labels[line[0:-1]] = str(self.line_number)
                else:
                    # syntax didn't match, show it
                    self.__message(
                        "Wrong syntax on label '{}' at line {}.".\
                        format(line, counter)
                        )

            elif line[0] is "\\":
                # joins this to the previous line
                single[len(single)-1] += line[1:]

            else:
                single.append(line)

            counter += 1


    def __replace(self, string, text, value):
        """
        Replaces 'text' by 'value' on 'string'.

        Returns the same string with text replaced.
        """
        return string.replace(text, value)


    def __uppercase(self, text):
        """
        Put BASIC statements in upper case, except if between quotes

        'text' is the BASIC line with labels already translated.
        Returns the same line with BASIC statements in uppercase.
        """

        # everything in UPPERCASE
        upper_text = text.upper()

        for quote in self.quotes.findall(text):
            # strings to the original format
            upper_text  = upper_text.replace(quote.upper(), quote)

        return upper_text


    def list(self, uppercase, linefeed):
        """
        Lists the converted BASIC program.

        'uppercase' is the parameter from command line argument.
        Returns the BASIC program on standard output.
        """
        output=""

        for line in sorted(self.basic.keys(), key=lambda lin: int(lin)):
            current = format(
                "{} {}".format(
                    line, ":".join(
                        self.__labels(line, self.basic[line]))
                        ) + linefeed
                    )

            if uppercase is True:
                current = self.__uppercase(current)

            if len(current)>255:
                self.__message(
                    "More than 255 characters in line {}.".format(line)
                    )

            output += current

        return output


    def load(input_program):
        """
        Retrieves a BASIC program from a file.

        'input_program' is a string containing the path and filename from
        command line parameters.
        Returns the file content plus extra new lines.
        """
        try:
            # load a file
            f = open(input_program, 'r')

            for input_line in f:
                yield input_line

            f.close()

            # forces new lines at end of file
            yield "\n\n"


        except IOError as err:
            # someting went wrong
            self.__message(err.strerror)
            exit(2)


# vim: set fileencoding=utf-8
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4
