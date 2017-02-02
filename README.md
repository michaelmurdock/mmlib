#mmlib
Python utility classes and functions. 
These functions will probably not be very useful without some understanding of the context in which they were developed.


### Sample code for files_and_folders:

```python
import files_and_folders  as ff

dir1 = r'.\dir1'
x_matching_files1 = ff.get_list_of_matching_files(dir1, ['*.jpg', '*.jpeg', '*.j2k', '*.png'], return_full_path=False)
for fn in x_matching_files1:
  print(fn)
    
slist = ff.create_string_from_list([1, 2, 3, 4, 5, 6], num_items=-1, separator = '--')
```


### Sample code for fname_info class:

```python
import fname_info as fni
```

####This should work:

```python
  name = fni.cfname_info(fullname = r'C:\test_suffix.ext')
  print(name.filename)
  print(name.basename)
  print(name.suffix)
  print(name.fullname)
  print(name.dirname)
  print(name.parentname)
```

####This should fail: if filename is supplied, must also supply directory

```python
  try:
    name1 = fni.cfname_info(filename='fake_filename.txt')
  except Exception as e:
    print('Correctly failed: %s' % (str(e)))
```

####This should fail: If directory is supplied, must also supply filename

```python
  try:
    name2 = fni.cfname_info(dirname = r'c:\test')
  except Exception as e:
    print('Correctly failed: %s' % (str(e)))
'''