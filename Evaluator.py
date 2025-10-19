# evaluator.py

from lark import Tree, Token

class Environment:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent

    def get(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise Exception(f"Variable '{name}' not defined")

    def set(self, name, value):
        self.variables[name] = value


class Evaluator:
    def evaluate(self, node, env):
        # Handle Token (literal)
        if isinstance(node, Token):
            if node.type == "INT":
                return {"type": "int", "value": int(node.value)}
            if node.type == "FLOAT":
                return {"type": "float", "value": float(node.value)}
            if node.type == "CHAR":
                return {"type": "char", "value": node.value}
            if node.type == "STRING":
                return {"type": "string", "value": node.value[1:-1]}  # strip quotes
            if node.type == "BOOL":
                return {"type": "bool", "value": node.value == "true"}
            raise Exception(f"Unknown token type: {node.type}")

        # Handle Tree (non-literal)
        if isinstance(node, Tree):
            node_type = node.data

            # Program / block
            if node_type == "program":
                result = None
                for stmt in node.children:
                    result = self.evaluate(stmt, env)
                return result

            if node_type == "block":
                block_env = Environment(parent=env)
                result = None
                for stmt in node.children:
                    result = self.evaluate(stmt, block_env)
                return result

            # Variable declaration: var_type name = value
            if node_type == "var_decl":
                var_type = node.children[0].value  # Token
                var_name = node.children[1].value  # Token
                value = self.evaluate(node.children[2], env)
                if value["type"] != var_type:
                    raise Exception(f"Type mismatch: variable '{var_name}' declared as {var_type}, got {value['type']}")
                env.set(var_name, value)
                return value

            # Assignment: name = value
            if node_type == "assignment":
                var_name = node.children[0].value  # Token
                value = self.evaluate(node.children[1], env)
                old_value = env.get(var_name)
                if old_value["type"] != value["type"]:
                    raise Exception(f"Type mismatch in assignment to '{var_name}'")
                env.set(var_name, value)
                return value

            # Identifier
            if node_type == "identifier":
                return env.get(node.children[0].value)

            # Binary expression: left operator right
            if node_type == "bin_expr":
                left = self.evaluate(node.children[0], env)
                operator = node.children[1].value  # Token
                right = self.evaluate(node.children[2], env)
                return self.apply_operator(operator, left, right)

        raise Exception(f"Unknown node: {node}")


    def apply_operator(self, operator, left, right):
        if left["type"] != right["type"]:
            raise Exception(f"Cannot operate on different types: {left['type']} and {right['type']}")

        t = left["type"]

        if t == "int" or t == "float":
            if operator == "+": return {"type": t, "value": left["value"] + right["value"]}
            if operator == "-": return {"type": t, "value": left["value"] - right["value"]}
            if operator == "*": return {"type": t, "value": left["value"] * right["value"]}
            if operator == "/": return {"type": t, "value": left["value"] / right["value"]}
            if operator == "==": return {"type": "bool", "value": left["value"] == right["value"]}
            if operator == "!=": return {"type": "bool", "value": left["value"] != right["value"]}
            if operator == ">": return {"type": "bool", "value": left["value"] > right["value"]}
            if operator == "<": return {"type": "bool", "value": left["value"] < right["value"]}

        if t == "string":
            if operator == "+": return {"type": "string", "value": left["value"] + right["value"]}
            if operator == "==": return {"type": "bool", "value": left["value"] == right["value"]}
            if operator == "!=": return {"type": "bool", "value": left["value"] != right["value"]}

        if t == "bool":
            if operator == "&&": return {"type": "bool", "value": left["value"] and right["value"]}
            if operator == "||": return {"type": "bool", "value": left["value"] or right["value"]}
            if operator == "==": return {"type": "bool", "value": left["value"] == right["value"]}
            if operator == "!=": return {"type": "bool", "value": left["value"] != right["value"]}

        if t == "char":
            if operator == "==": return {"type": "bool", "value": left["value"] == right["value"]}
            if operator == "!=": return {"type": "bool", "value": left["value"] != right["value"]}

        raise Exception(f"Operator {operator} not supported for type {t}")


# Example usage with Lark parse tree
if __name__ == "__main__":
    from lark import Lark

    grammar = """
    ?start: program
    ?program: stmt*
    ?stmt: var_decl ";" | bin_expr ";" | assignment ";" | identifier ";"
    var_decl: TYPE IDENT "=" expr
    assignment: IDENT "=" expr
    bin_expr: expr OP expr
    ?expr: bin_expr | NUMBER
    identifier: IDENT

    TYPE: "int" | "float" | "char" | "bool" | "string"
    IDENT: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /\d+(\.\d+)?/
    OP: "+" | "-" | "*" | "/" | "==" | "!=" | ">" | "<"

    %ignore " "
    """

    parser = Lark(grammar, parser="lalr")
    tree = parser.parse("int x = 5 + 3; x;")
    env = Environment()
    evaluator = Evaluator()
    result = evaluator.evaluate(tree, env)
    print(result)  # {'type': 'int', 'value': 8}
