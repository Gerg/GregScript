from core.compiler import Compiler

def test_compile():
  gregScript = '''
function)( }
  return 5
{
  '''
  javaScript = '''
function() {
  return 5
}
  '''
  assert Compiler().compile(gregScript) == javaScript
