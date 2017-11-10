
class Context(object):

    def __init__(self):
        self.functions = {}
        self.stack = []


class OpNode(object):

    def __init__(self, op, children):
        self.op = op
        self.children = children

    def evaluate(self, context):
        return context.functions[self.op](*self.children)


class IntNode(object):

    def __init__(self, value):
        self.value = int(value)

    def evaluate(self, context):
        return self.value


class FloatNode(object):

    def __init__(self, value):
        self.value = float(value)

    def evaluate(self, context):
        return self.value


class StringNode(object):

    def __init__(self, value):
        self.value = value[1:-1]

    def evaluate(self, context):
        return self.value


class ListNode(object):

    def __init__(self, value):
        self.value = value
        
    def evaluate(self, context):
        return self.value