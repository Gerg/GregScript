#!/usr/bin/env python3
import re
class Compiler(object):
  CHAR_MAPPING = {
    ')': '(',
    '(': ')',
    '{': '}',
    '}': '{'
  }

  def compile(self, inputString):
    outputString = ''
    for char in inputString:
      outputString += self._transformChar(char)
    return outputString

  def _transformChar(self, char):
    return self.CHAR_MAPPING.get(char, char)
