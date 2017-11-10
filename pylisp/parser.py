import re
import syntax

LIST_START = '('
LIST_END = ')'
QUOTE_LIST_START = '\'('


def get_all_list_tokens(tokens: list):
    stack = 1
    list_tokens = []
    tokens.pop(0)

    while stack != 0:
        token = tokens.pop(0)
        list_tokens.append(token)
        if token == LIST_START or token == QUOTE_LIST_START:
            stack += 1
        elif token == LIST_END:
            stack -= 1

    list_tokens.pop(-1)
    return list_tokens


def split_tokens(code):
    return re.split(r'\s+', code)


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def parse(tokens):
    nodes = []
    while len(tokens) > 0:
        first = tokens[0]
        if first == LIST_START:                         # op
            sub_tokens = get_all_list_tokens(tokens)
            sub_nodes = parse(sub_tokens[1:])
            nodes.append(syntax.OpNode(sub_tokens[0], sub_nodes))
        elif first == QUOTE_LIST_START:                 # list
            sub_tokens = get_all_list_tokens(tokens)
            sub_nodes = parse(sub_tokens)
            nodes.append(syntax.ListNode(sub_nodes))
        elif first[0] == '\'' and first[-1] == '\'':    # string
            nodes.append(syntax.StringNode(tokens.pop(0)))
        elif is_int(first):                             # int
            nodes.append(syntax.IntNode(tokens.pop(0)))
        elif is_float(first):                           # float
            nodes.append(syntax.FloatNode(tokens.pop(0)))
        else:
            raise SyntaxError()

    return nodes
