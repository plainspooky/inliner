#!/usr/bin/env python3
import json
import logging
import re
from sys import exit as sys_exit
from sys import stderr as sys_stderr

logger = logging.getLogger(__name__)


class Inliner(object):

    # REGEX for label definition and its uses
    LABEL = "[A-Za-z0-9_]+"
    label_def = re.compile("^" + LABEL + ":$")
    label_use = re.compile("\{\{(@|" + LABEL + ")\}\}")
    const_def = re.compile("^\' define " + LABEL + " ")

    # REGEX for search numbered lines
    line_numbered = re.compile("^[0-9]{1,} ?")

    def __init__(self, program, start_line, step_line, remark="\'"):
        """class constructor\n
        """
        self.basic = {}
        self.labels = {}
        self.line_number = int(start_line)
        self.step_line = int(step_line)
        self.remark = remark
        self.quotes = re.compile("(\"[^\"]+\"|" + remark + ".*$)")

        self.__parse(program=program)

    def __json(self):
        """Lists code's dictionary in JSON format. It's used only for debug.\n
        """
        return json.dumps(self.basic, indent=2)

    def __labels(self, line, code):
        """Rplaces a label by a line number or a value.\n
        'line' is line number and 'code' the BASIC statements the\n
        Key/Value of 'self.basic' dictionary.\n
        Returns a string with all labels translated.\n
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
                            string=code[i],
                            text="{{@}}",
                            value=str(line))

                    elif label in self.labels.keys():
                        # is this a common label?
                        code[i] = self.__replace(
                            string=code[i],
                            text="{{" + label + "}}",
                            value=self.labels[label])
                        repeat = 0

                    else:
                        # exist if found a undefined label
                        logger.error(
                            "Undefined label '{}' in '{}'".format(
                                label, code[i]))
                        sys_exit(2)
                else:
                    break

        return code

    def __new_line(self, line):
        """Adds a new line into 'self.basic' dictionary and increments
        the ine counter.\n
        'line' is a array containing the BASIC statements.\n
        Returns a empty list to initialize 'single' list on '__parse'
        method.
        """
        self.basic[str(self.line_number)] = line
        self.line_number += self.step_line

        return []

    def __parse(self, program):
        """Parses the BASIC program and populates 'self.basic' dictionary.\n
        'program' is the file to be converted.
        """
        single = []
        counter = 1

        for line in program:

            # removes all leading and trailing spaces
            line = line.strip()

            if line is "":
                # that's a empty line!
                if len(single) > 0:
                    single = self.__new_line(line=single)

            elif self.line_numbered.search(line):
                # BAD: a line that begins with a number!
                logger.warning(
                    'Numbered line: {}'.format(line[0:64]))

            elif line[0] is "\'":
                # looks like a comment...

                if re.search("\'\'", line):
                    # double '' are comments that will be preserved

                    if len(single) > 0:
                        single = self.__new_line(single)

                    # inserts a comment
                    single = self.__new_line(
                        line=["{}{}".format(self.remark, line[2:])])

                elif self.const_def.search(line):

                    # there is a constant (aka 'define')
                    const = self.const_def.search(line)
                    value_pos = int(const.span()[1])
                    const_name = const.group()[9:value_pos - 1]
                    const_value = line[value_pos:]
                    self.labels[const_name] = const_value

            elif line[-1] is ":":

                # that's a line ending with ":"
                if self.label_def.search(line):

                    # syntax is ok, creates a new label
                    self.labels[line[0:-1]] = str(self.line_number)

                else:
                    # syntax didn't match, show it
                    logger.error(
                        "Invalid label syntax '{}' in line {}.".format(
                            line, counter)
                    )

            elif line[0] is "\\":

                # joins to the previous line
                single[len(single) - 1] += line[1:]

            else:
                single.append(line)

            counter += 1

    def __replace(self, string, text, value):
        """Replaces 'text' by 'value' on a 'string'.\n
        Returns the same string with text replaced.
        """
        return string.replace(text, value)

    def __uppercase(self, text):
        """Put all BASIC statements in upper case.\n
        'text' is a BASIC line with labels already translated.\n
        Returns the same line with BASIC statements in uppercase.
        """
        upper_text = text.upper()

        for quote in self.quotes.findall(text):
            upper_text = upper_text.replace(quote.upper(), quote)

        return upper_text

    def list(self, uppercase, linefeed='\n'):
        """Lists the converted BASIC program.\n
        'uppercase' is the parameter from command line argument and
        'linefeed' is the characters for break the lines.\n
        Returns the BASIC program on standard output.
        """
        output = ""

        for line in sorted(self.basic.keys(), key=lambda lin: int(lin)):
            current = format(
                "{} {}".format(
                    line, ":".join(
                        self.__labels(line=line, code=self.basic[line]))
                ) + linefeed
            )

            if uppercase is True:
                current = self.__uppercase(text=current)

            if len(current) > 255:
                logger.warning(
                    "More than 255 characters in line {}.".format(line))

            output += current

        return output

    def load(filename):
        """Retrieves the content of a 'filename' file.\n
        'filename' is a string containing the path + name of file.\n
        Returns the file's content plus extra new lines.
        """
        try:
            with open(filename, 'r') as f:
                for line in f:
                    yield line
            f.close()
            # return open(filename,'r').read() + "\n\n"
            yield "\n\n"

        except IOError:
            logger.error("Can't read '{}' file!".format(filename))
            sys_exit(2)


# vim: set fileencoding=utf-8
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4
