# files_and_folders.py


import os
import os.path

import fnmatch
#import cefpython as cefp



IMAGE_EXTENSIONS = ('*.jpg', '*.jpeg', '*.j2k', '*.png')


def get_list_of_matching_files(dir, file_ext_list, return_full_path=False):
    '''
    Returns a list of filenames by walking down all of the subdirectories beneath 
    the specified directory to match files with an extension from the specified list.
    Example list:   ['*.jpg', '*.jpeg', '*.j2k', '*.png']
    '''
    x_matching_files = []      
    for root, dirs, files in os.walk(dir):
        r = root
        d = dirs
        for extension in file_ext_list:
            for filename in fnmatch.filter(files, extension):
              if return_full_path:
                full_filename = os.path.join(root, filename)
                x_matching_files.append(full_filename)
              else:
                x_matching_files.append(filename)

    return x_matching_files



def create_string_from_list(long_list, num_items=-1, separator = ','):
	'''
	Private method for creating a string representation of some number of elements of the 
	passed-in list. If the intent is to use every item in the list, num_items must be set
	to -1. If the intent is to only use the first N items from the list when creating the
	string, then the client must set num_items to N.
	Example for num_items := 2:
	[ 1.0, 2.0, 3.0, 4.0 ] --> '1.0, 2.0'
	'''
	if num_items == -1:
		num_items = len(long_list)


	shortened_list = long_list[0:num_items]
	#sep = ", "

	string_version_of_list = separator.join([str(x) for x in shortened_list])
	return string_version_of_list
	

def create_filename_with_new_ext(input_filename, new_file_ext):
		'''
		This function takes a path-qualified filename and returns a string corresponding to that
		filename, but with the new specified extension. Example:
		foo\image1.jpg --> foo\image1.feat_ext
		'''
		try:
			# split off the extension
			(root, ext) = os.path.splitext(input_filename)
		except Exception as e:
			msg = 'Exception thrown splitting the extension on file: %s. Details: %s' % (input_filename, str(e))
			return Result(False, msg, None)

		new_name = root + '.' + new_file_ext
		return Result(True, '', new_name)


#def get_application_path(file=None):
#    '''
#    On Windows after downloading file and calling Browser.GoForward(), current working directory 
#    is set to %UserProfile%. Calling os.path.dirname(os.path.realpath(__file__)) returns for eg. 
#    "C:\Users\user\Downloads". A solution is to cache path on first call.

#    This function is based on the method of the same name in the cefpython package.
#    '''
#    import re, os, platform
#    if not hasattr(cefp.GetApplicationPath, "dir"):
#        if hasattr(sys, "frozen"):
#            dir = os.path.dirname(sys.executable)
#        elif "__file__" in globals():
#            dir = os.path.dirname(os.path.realpath(__file__))
#        else:
#            dir = os.getcwd()
#        cefp.GetApplicationPath.dir = dir

#    # If file is None return current directory without trailing slash.
#    if file is None:
#        file = ""

#    # Only when relative path.
#    if not file.startswith("/") and not file.startswith("\\") and (
#            not re.search(r"^[\w-]+:", file)):
#        path = GetApplicationPath.dir + os.sep + file
#        if platform.system() == "Windows":
#            path = re.sub(r"[/\\]+", re.escape(os.sep), path)
#        path = re.sub(r"[/\\]+$", "", path)
#        return path
#    return str(file)