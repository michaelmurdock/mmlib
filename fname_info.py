# fname_info.py
'''
fname.py module wraps the cfname class, which is used to simplify the task
of dealing with filenames.
'''
from  __future__ import print_function

import os.path



class cfname_info(object):
    '''
    An instance of cfname_info class is used to represent a single filename.
    After an instance is constructed, the client can access the properties to get
    whatever name is required.
    '''
    def __init__(self, fullname='', dirname='', filename='', basename='', suffix='', ext=''):
        '''
        Client code must supply either the (path-qualified) fullname OR the dir and filename.
        The 
        Definition of terms:
          full      : full means the item (directory name or filename) is fully path-qualified
          suffix : The part of the filename before the extension.
          fullname = dirname + filename
          filename = basename + suffix + ext

        Note: If the fullname is supplied, we split it, which means we override dirname 
        (if it was supplied) and the filename (if it was supplied). This means a constructor 
        with a fullname will still work with a bogus dirname or filename.
        '''
        validation_rule = 'filename supplied without dirname is invalid.'
        if filename and not dirname:
            raise ValueError(validation_rule)
        
        validation_rule = 'dirname supplied without a filename is invalid.'
        if dirname and not (filename or (basename and suffix and ext)):
            raise ValueError(validation_rule)
        
        validation_rule = 'If fullname is not supplied, dirname and either filename or base, suffix and ext must be supplied'
        #if (not filename or not dirname) and not fullname:
        if not fullname and (not dirname and not (filename or (basename and suffix and ext))):
            raise ValueError(validation_rule)

        validation_rule = 'If basename, suffix or ext is supplied, then all must be supplied'
        if basename and not (suffix or ext):
          raise ValueError(validation_rule)
        #if suffix and not (basename or ext):
        #  raise ValueError(validation_rule)
        if ext and not (basename or suffix):
          raise ValueError(validation_rule)

                
        self._fullname = fullname
        self._dirname = dirname
        self._filename = filename
        self._suffix = suffix

        (result, errmsg) = self._process_names()

        # More validation checks
        validation_rule = 'basename + suffix + ext must equal filename'
        if self._basename + self._suffix + self._ext != self._filename:
            raise ValueError(validation_rule)

        validation_rule = 'dirname + filename must equal fullname'
        if os.path.join(self._dirname, self._filename) != self._fullname:
            raise ValueError(validation_rule)


    def _update_on_this_change(self, item_that_was_changed):
      '''
      item_that_was_changed can be one of the following:
        'fullname'
        'filename'
        ' ... '

      '''





    def _process_names(self):
        '''
        Private method that updates all the missing information based on items
        are currently defined (non-NULL).
        '''

        # If we have a fullname, split it up to create dirname and filename
        # This rule implies that fullname supercedes dirname and filename
        if self._fullname:
            (self._dirname, self._filename) = os.path.split(self._fullname)


            # We started with a fullname, used it to get dirname and filename, and now
            # might want to derive basename, suffix, and ext

            # If suffix is defined, but not basename, use filename and suffix to create basename and ext
            if self._suffix  and not self._basename:
              (base_and_suffix, self._ext) = os.path.splitext(self._filename)
              self._basename = base_and_suffix.split(self._suffix)[0]

              raise ValueError('THIS IS AS FAR AS I GOT!!!'

        # If we don't have a fullname, create it from dirname and filename
        else:
            
            # If we have a filename, use it with dirname to create fullname
            if self._filename:

              if not self._dirname:
                raise ValueError('If fullname is not defined, but filename is defined, then dirname also needs to be defined!')

              self._fullname = os.path.join(self._dirname, self._filename)

            # If we don't have a filename, that must mean we need to build it from 
            # base, suffix and ext.
            else:
              # Note: Suffix is NOT required: it can be NULL and we can stil build our filename
              if not (self._basename and self._ext):
                raise ValueError('If fullname and filename are not defined, then basename, suffix and ext all need to be defined')

              self._filename = self._basename + self._suffix + self._ext

              # Now that we have the filename, we use it and dirname to create the fullname
              self._fullname = os.path.join(self._dirname, self._filename)
        
              
        # At this point we have either:
        #   fullname, dirname and filename, or
        #        
                
        # If we don't have the basename, create it from the filename
        if not self._basename:   
        (base_and_suffix, self._ext) = os.path.splitext(self._filename)
        self._parentname = os.path.split(self._dirname)[1]
        if self._suffix:
            self._basename = base_and_suffix.split(self._suffix)[0]
        else:
            self._basename = base_and_suffix

        return (True, '')

    @property
    def filename(self):
        return self._filename

    @property
    def fullname(self):
        return self._fullname

    @property
    def basename(self):
        '''
        basename is the part of the filename preceeding the suffix
        '''
        return self._basename

    @property
    def dirname(self):
        return self._dirname

    @property
    def parentname(self):
        return self._parentname

    @property
    def suffix(self):
        '''
        Suffix is the part of the filename after the basename, but before the ext.
        '''
        return self._suffix

    @property
    def ext(self):
        return self._ext

    @property
    def tag(self):
        return self._tag



def test_instance_properties(inst):
    try:
        a=inst.basename
        b=inst.filename
        c=inst.dirname
        d=inst.fullname
        e=inst.parentname
        f=inst.suffix
        g=inst.ext

    except Exception as e:
        return (False, 'Unexpected exception in test_instance_properties. Details: %s' % (str(e)))

    return (True, '')

def unit_test_pos(id, d, f, fn, s):
    '''
    Positive unit test harness: Expectation is to run without failure.
    '''
    try:
        inst = cfname(dirname=d, filename=f, fullname=fn, suffix=s)
       
    except ValueError as e:
        return (False, 'Unexpected exception with test %d: %s' % (id, str(e)))

    return (True, '')

def unit_test_neg(id, d, f, fn, s):
    '''
    Negative unit test harness: Expectation is to fail.
    '''
    try:
        inst = cfname(dirname=d, filename=f, fullname=fn, suffix=s)
       
    except ValueError as e:
        return (True, 'Expected exception with test %d: %s' % (id, str(e)))

    return (False, 'Error: unit_test_neg expected an exception on %d' % (id))



def run_unit_tests():
    '''
    '''

    # Positive unit tests - I expect positive results
    id = 1
    (result, errmsg) = unit_test_pos(id, r'c:\process_root\crop_tests', '31129_193939-00550.jpg', '', '')
    if not result:
        return (False, id, errmsg)
     
    id = 2
    (result, errmsg) = unit_test_pos(id, r'c:\process_root\crop_tests', '31129_193939-00550_processed.jpg', '', '_processed')
    if not result:
        return (False, id, errmsg)

    id = 3
    good_inst1 = cfname(dirname=r'c:\process_root\crop_tests', filename='31129_193939-00550_processed.jpg', fullname='', suffix='_processed')
    (result, errmsg) = test_instance_properties(good_inst1)
    if not result:
        return (False, id, errmsg)

    id = 4
    good_inst2 = cfname(dirname='', filename='', fullname=r'c:\process_root\crop_tests\31129_193939-00550_processed.jpg', suffix='_processed')
    (result, errmsg) = test_instance_properties(good_inst2)
    if not result:
        return (False, id, errmsg)

    # Negative unit tests - I expect failures
    id = 10
    (result, errmsg) = unit_test_neg(id, '', '31129_193939-00550_processed.jpg', '', '_processed')
    print('%s . Details: %s' % (str(result), errmsg))
    if not result:
        return (False, id, errmsg)

    id = 11
    (result, errmsg) = unit_test_neg(id, r'c:\process_root\crop_tests', '', '', '_processed')
    print('%s . Details: %s' % (str(result), errmsg))
    if not result:
        return (False, id, errmsg)

    id = 12
    (result, errmsg) = unit_test_neg(id, r'c:\process_root\crop_tests', '', r'c:\process_root\crop_tests\31129_193939-00550_processed.jpg', '_processed')
    print('%s . Details: %s' % (str(result), errmsg))
    if not result:
        return (False, id, errmsg)

    id = 13
    (result, errmsg) = unit_test_neg(id, '', '', r'c:\process_root\crop_tests\31129_193939-00550_processed.jpg', '_badsuffix')
    print('%s . Details: %s' % (str(result), errmsg))
    if not result:
        return (False, id, errmsg)

    id = 14 
    (result, errmsg) = unit_test_neg(id, r'c:\process_root\bogus_folder', '31129_193939-00550_processed.jpg', r'c:\process_root\crop_tests\31129_193939-00550_processed.jpg', '_processed')
    print('%s . Details: %s' % (str(result), errmsg))
    if not result:
        return (False, id, errmsg)

    return (True, 0, '')
  

if __name__ == "__main__":

    #(result, test_id, errmsg) = run_unit_tests()
    #if not result:
    #    print('Unit test failure %d: %s' % (test_id, errmsg))
    #    exit(0)


    

    inst2 = cfname_info(fullname=r'C:\process_root\crop_tests\31129_193939-00550_processed.jpg', suffix='_processed')

    print('Test1:')
    print('filename: '   + inst2.filename)
    print('fullname: '   + inst2.fullname)
    print('basename: '   + inst2.basename)
    print('dirname: '    + inst2.dirname)
    print('parentname: ' + inst2.parentname)
    print('suffix: '     + inst2.suffix)
    print('ext: '        + inst2.ext)



    print('Test2:')
    fni = cfname_info(dirname=r'c:\test', basename='base', suffix='suffix', ext='.jpg')
    print('filename: '   + fni.filename)
    print('fullname: '   + fni.fullname)
    print('basename: '   + fni.basename)
    print('dirname: '    + fni.dirname)
    print('parentname: ' + fni.parentname)
    print('suffix: '     + fni.suffix)
    print('ext: '        + fni.ext)

    print('Done ...')


