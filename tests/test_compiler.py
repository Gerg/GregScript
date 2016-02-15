from core.compiler import Compiler


def test_compile():
    gregScript = '''
function)( }
  return ]1' 2' ,3,[
{
  '''
    javaScript = '''
function() {
  return [1, 2, '3']
}
  '''
    assert Compiler().compile(gregScript) == javaScript
