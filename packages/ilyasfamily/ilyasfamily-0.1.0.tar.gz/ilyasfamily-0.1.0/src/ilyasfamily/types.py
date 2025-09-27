import datetime
import uuid
import base64

class Date:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = datetime.date.fromisoformat(value)
        elif isinstance(value, datetime.date):
            self.value = value
        else:
            raise TypeError("Date must be str or datetime.date")
    def __repr__(self):
        return f'@date("{self.value.isoformat()}")'

class DateTime:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = datetime.datetime.fromisoformat(value)
        elif isinstance(value, datetime.datetime):
            self.value = value
        else:
            raise TypeError("DateTime must be str or datetime.datetime")
    def __repr__(self):
        return f'@datetime("{self.value.isoformat()}")'

class Binary:
    def __init__(self, data: bytes):
        self.data = data
    def __repr__(self):
        b64 = base64.b64encode(self.data).decode("utf-8")
        return f'@binary("{b64}")'

class UUID:
    def __init__(self, value=None):
        self.value = uuid.uuid4() if value is None else uuid.UUID(str(value))
    def __repr__(self):
        return f'@uuid("{self.value}")'

class Set:
    def __init__(self, values):
        self.values = set(values)
    def __repr__(self):
        return f"@set({list(self.values)})"

class Map:
    def __init__(self, mapping):
        self.mapping = dict(mapping)
    def __repr__(self):
        return f"@map({self.mapping})"

class Tuple:
    def __init__(self, *values):
        self.values = tuple(values)
    def __repr__(self):
        return f"@tuple({self.values})"

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.nodes = []
        self.edges = []
    def add_node(self, node_id, label=None):
        self.nodes.append({"id": node_id, "label": label})
    def add_edge(self, source, target, weight=None):
        edge = {"from": source, "to": target}
        if weight is not None:
            edge["weight"] = weight
        self.edges.append(edge)
    def __repr__(self):
        return f"@graph(directed={self.directed}, nodes={self.nodes}, edges={self.edges})"
