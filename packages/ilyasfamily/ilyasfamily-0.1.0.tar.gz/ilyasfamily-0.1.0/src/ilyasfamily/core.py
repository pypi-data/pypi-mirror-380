from .types import Date, DateTime, Binary, UUID, Set, Map, Tuple, Graph

# ==============================
# Mathematical formats
# ==============================
def s_expr(obj):
    if isinstance(obj, dict):
        return "(" + " ".join(f"({k} {s_expr(v)})" for k,v in obj.items()) + ")"
    elif isinstance(obj, list):
        return "(" + " ".join(s_expr(v) for v in obj) + ")"
    else:
        return str(obj)

class Node:
    def __init__(self, label, props=None):
        self.label = label
        self.props = props or {}
    def __repr__(self):
        return f"@node(\"{self.label}\", {self.props})"

# ==============================
# Serializer / Parser
# ==============================
def dumps(obj, fmt="ilyas"):
    if fmt == "ilyas":
        return repr(obj)
    elif fmt == "s_expr":
        return s_expr(obj)
    elif fmt == "node":
        if isinstance(obj, Node):
            return repr(obj)
        raise TypeError("Only Node supported for node format")
    else:
        raise ValueError("Unknown format")

def loads(text):
    # very naive parser for demo purposes
    if text.startswith("@date"):
        return Date(text[text.find("\"")+1:text.rfind("\"")])
    elif text.startswith("@datetime"):
        return DateTime(text[text.find("\"")+1:text.rfind("\"")])
    elif text.startswith("@uuid"):
        return UUID(text[text.find("\"")+1:text.rfind("\"")])
    elif text.startswith("@binary"):
        data = base64.b64decode(text[text.find("\"")+1:text.rfind("\"")])
        return Binary(data)
    else:
        return text

# ==============================
# File helpers for .ifamily
# ==============================
def dump_file(obj, path, fmt="ilyas"):
    if not path.endswith(".ifamily"):
        raise ValueError("File must have .ifamily extension")
    with open(path, "w", encoding="utf-8") as f:
        f.write(dumps(obj, fmt))

def load_file(path):
    if not path.endswith(".ifamily"):
        raise ValueError("File must have .ifamily extension")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    return loads(text)

# ==============================
# Example usage
# ==============================
if __name__ == "__main__":
    person = Node("Person", {
        "Name": "Budi",
        "Age": 21,
        "Address": Node("Address", {"City": "Bandung", "Code": 40123})
    })

    dump_file(person, "person.ifamily")
    loaded = load_file("person.ifamily")
    print("Loaded:", loaded)
