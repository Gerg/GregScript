from core.compiler import Compiler

def test_compile():
  assert Compiler.compile(')') == '('

