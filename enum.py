# enum.py
'''
enum.py module contains the cenum class, which is a class for defining and manipulating enumerated values.
'''




class cenum(int):
	'''
	Enumeration value is a named integer.
	'''
	#pylint: disable=R0904

	def __new__(cls, rank, name):
		obj = int.__new__(cls, rank)
		obj.name = name
		obj.rank = rank
		return obj

	def __repr__(self):
		return 'CEnum(' + repr(int(self)) + ', ' + repr(self.name) + ')'


if __name__ == '__main__':

  small   = cenum(1, 'SMALL')
  medium  = cenum(5, 'MEDIUM')
  large   = cenum(10, 'LARGE')

  print small
  print small.name

  print large
  print large.name


  if large > small:
    print large - small
  else:
    print medium




  print 'Done'