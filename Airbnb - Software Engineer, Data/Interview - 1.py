"""
Date: 2021 03 30
Problem: Online Assignment
Result: Pass 12 Test Cases
"""


class Problem1:
    """
    XML Validator

    Input a string, check whether it is a valid XML.
    XML contains text and tag, where text contains ASCII codes except for "<" and ">" and tag comes in two flavors <>.
    Tags can not be empty like <> or </>.
    Start Tag - <a>
    End Tag - </a>
    """

    def validate_xml(self, xml):
        # Write your code here

        stack = []

        i = 0
        while i <= len(xml) - 1:
            if xml[i] == "<":  # find tag start
                j = xml.find(">", i + 1)  # find tag end
                if j == -1:  # end not found, xxx<xxx
                    return "parse error"
                if j == i + 1:  # empty tag, <>
                    return "parse error"
                if "<" in xml[i + 1:j + 1]:  # another start is set between this pair, xxx<xxx<xxx>xxx
                    return "parse error"

                tag = xml[i + 1:j]
                if tag[0] != "/":  # left tag, <a>
                    stack.append(tag)
                else:  # right tag, </a>
                    if not stack:  # isolated right tag
                        return "parse error"
                    elif stack.pop() != tag[1:]:  # left/right do not match, <a> and </b>
                        return "encountered closing tag without matching open tag for <{0}>".format(tag)
                i = j + 1  # iterate after the tag end
            else:
                i += 1  # iterate at the next character

        if not bool(stack):  # all match
            return "valid"
        else:  # isolated left tag
            return "missing closing tag for <{0}>".format(stack[-1])


if __name__ == '__main__':
    xml = "2sddaq<qwe><ww></qwe>"

    sol = Problem1()
    print(sol.validate_xml(xml))
