from typing import TYPE_CHECKING, Generator
import astroid
import sys
from astroid.nodes import Assign, Call, Expr
from astroid.builder import AstroidBuilder
import os

if TYPE_CHECKING:
    import ast

class Flake8Deprecation:
    name: str = "flake8-deprecation"
    version: str ="1.0.1"

    def __init__(self, tree: "ast.Module", filename: str)-> None:
        #print(f"Current working directory: {os.getcwd()}")
        #print(f"filename: {filename}")
        self.filename=filename
        with open(filename, 'r', encoding='utf-8') as f:
            python_code = f.read()
        self.astroid_module: astroid.Module = astroid.parse(python_code)


    def run(self):
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(self.filename)))
            sys.path.insert(0, os.getcwd())
            #print(f"{sys.path=}")

            for call in self.recursive_parse_source(self.astroid_module):
                #print(call)
                if self.contains_warnings(call):
                    yield (
                        call.lineno,
                        call.col_offset,
                        f"WNG311: \"{call.func.repr_name()}\" unconditionally calls warnings.warn",
                        type(self)

                    )
        finally:
            sys.path.pop(0)
            sys.path.pop(0)


    def recursive_parse_source(self, top_level: astroid.NodeNG)-> Generator[Call, None, None]:
        for child in top_level.get_children():
            if isinstance(child, astroid.Assign):
                yield from self.recursive_parse_source(child.value)
            elif isinstance(child, astroid.Expr):
                yield child.value


    def contains_warnings(self, call_node: Call)-> bool:
        """Checks whetehr the function underlying the provided call itself calls warnings.warn

        TODO should cache this
        """
        possible_definitions: list = list(call_node.func.infer())

        #print(f"{possible_definitions=}")

        top_level_exprs = [node for node in possible_definitions[0].get_children() if isinstance(node, Expr)]

        for expr in top_level_exprs:
            call = next(expr.get_children())
            if call.func.expr.name == "warnings" and call.func.attrname == "warn":
                return True
        return False

if __name__=="__main__":

    plugin = Flake8Deprecation(None, "tests/should_warn.py")

    results =list(plugin.run())
    print(results)
