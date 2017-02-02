# mcmLib_driver.py
from __future__ import print_function


import utilsLib
import db_utils
import msg as m
import exception_utils as eu
import files_and_folders as ff
import fname_info as fni



if __name__ == '__main__':

  # files_and_folders
  dir1 = r'.\dir1'
  x_matching_files1 = ff.get_list_of_matching_files(dir1, ['*.jpg', '*.jpeg', '*.j2k', '*.png'], return_full_path=False)
  for fn in x_matching_files1:
    print(fn)
    
  slist = ff.create_string_from_list([1, 2, 3, 4, 5, 6], num_items=-1, separator = '--')

  # ---------------------------------------------------------------------------------
  # cfname_info class
  # --------------------------------------------------------------------------------

  # This should work
  name = fni.cfname_info(fullname = r'C:\pyDev\__My Scripts\mcm_lib2\test_suffix.ext')
  print(name.filename)
  print(name.basename)
  print(name.suffix)
  print(name.fullname)
  print(name.dirname)
  print(name.parentname)

  # This should fail: if filename is supplied, must also supply directory
  try:
    name1 = fni.cfname_info(filename='fake_filename.txt')
  except Exception as e:
    print('Correctly failed: %s' % (str(e)))

  # This should fail: If directory is supplied, must also supply filename
  try:
    name2 = fni.cfname_info(dirname = r'c:\test')
  except Exception as e:
    print('Correctly failed: %s' % (str(e)))



  #spath1 = ff.get_application_path()
  #print(spath1)

  #spath2 = ff.get_application_path(file=r'C:\Python27\python.exe')
  #print(spath2)
      



  # exception_utils
  try:
    x_items = [1, 2, 3]
    missing_item = x_items[4]

  except Exception as e:
    details = eu.get_exception_details('List indexing error')
    print(details)
    

  # msg
  response = m.MsgAlert("My New Message", "My New Title", flags=m.Button.OK_CANCEL + m.Icon.BANG)
  if response == m.Response.OK:
    print('Ok')
  else:
    print(response)

  print('Done')


