#!/usr/bin/env python3
import re
class Compiler(object):
  
  @classmethod
  def compile(cls, inputString):
    return re.sub('\)', '(', inputString)
