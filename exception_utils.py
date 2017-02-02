# exception_utils.py
'''
This module contains helper functions for dealing with exceptions.

'''
from __future__ import print_function

import sys
import traceback


def get_exception_details(name_or_context):
  '''
  Helper function to make it easy to print the message in context name for exception e.
  '''
  primary_details = 'Exception in %s. ' % (name_or_context)
  return primary_details + ''.join(traceback.format_exception(*sys.exc_info())[-2:]).strip().replace('\n',': ')


#def getExceptionDetails():
#  '''
#  Returns a string derived from the Exception information in the exc_info object
#  '''
#  sDetail1 = ''
#  exception_info = sys.exc_info()
#  if sys.exc_info()[0]:
#    sDetail1 = str(sys.exc_info()[0])

#  sDetail2 = ''
#  if sys.exc_info()[1]:
#    sDetail2 = str(sys.exc_info()[1])
#  return ' Exception Details: ' + sDetail1 + sDetail2


if __name__ == '__main__':


  try:
    assert False

  except Exception as e:
    details = get_exception_details('Asertion failure')
    print(details)

  try:
    # Test1 - List indexing error
    x_items = [1, 2, 3]
    missing_item = x_items[4]

  except Exception as e:
    details = get_exception_details('Test1')
    print(details)
    



  print('Done')