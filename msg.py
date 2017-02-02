# 
# msg.py
#

'''
mcmLib module for UI messaging stuff, which currently is only the MsgAlert function and the CProgressBar class.
The behavior of the MsgAlert function with regards to the Button and Icon arguments is very unpredictable.
'''

__author__ = "MichaelMurdock"
__date__ = "$Aug 2, 2010 8:34:58 PM$"

import win32gui
import utilsLib
import enum as e


class Button(object):
	'''
	Button attributes:
	'''
	OK					        = e.cenum(0, 'OK')
	OK_CANCEL			      = e.cenum(1, 'OK_CANCEL')
	ABORT_RETRY_IGNORE	= e.cenum(2, 'ABORT_RETRY_IGNORE')
	YES_NO_CANCEL		    = e.cenum(3, 'YES_NO_CANCEL') 
	YES_NO				      = e.cenum(4, 'YES_NO') 
	RETRY_CANCEL		    = e.cenum(5, 'RETRY_CANCEL')



class Icon(object):
	'''
	Icon attributes:
  '''
	BLANK	    = e.cenum(0, 'BLANK')
	X		      = e.cenum(16, 'X')
	QMARK	    = e.cenum(32, 'QMARK')
	BANG	    = e.cenum(48, 'BANG')
	INFO	    = e.cenum(64, 'INFO')
	BLANK2	  = e.cenum(80, 'BLANK2')
	
class Response(object):
  '''
  Response attributes:
  '''
  OK			    = e.cenum(1, 'OK')
  CANCEL		  = e.cenum(2, 'CANCEL')
  ABORT		    = e.cenum(3, 'ABORT')
  RETRY		    = e.cenum(4, 'RETRY') 
  IGNORE		  = e.cenum(5, 'IGNORE')
  TRY_AGAIN	  = e.cenum(10, 'TRY_AGAIN')
  CONTINUE	  = e.cenum(11, 'CONTINUE')


BeepNoMessageBox			= 0x8
DontKnow					= 0x9

	
def MsgAlert(sMessage, sTitle, flags=Icon.BLANK + Button.OK, beep=False):
	'''
	flags are combinations of the following hex numbers, aliased as indicated:

	Buttons Style:
		ButtonOk					:	0	:	OK
		ButtonOkCancel				:	1	:	OK, Cancel
		ButtonAbortRetryIgnore		:	2	:	Abort, Retry, Ignore
		ButtonYesNoCancel			:	3	:	Yes, No, Cancel
		ButtonYesNo					:	4	:	Yes, No
		ButtonRetryCancel			:	5	:	Retry, Cancel
		ButtonCancelAgainContinue	:	6	:	Cancel, Try Again, Continue
		ButtonCancelAgainContinueTB	:	7	:	Cancel, Try Again, Continue In Taskbar
		BeepNoMessageBox			:	8	:	Beeps, but no MessageBox
		DontKnow					:	9	:	Beeps, but no MessageBox
	
	Icon Style:
		IconNone	:	0	:	(blank)
		IconX		:	16	:	X
		IconQMark	:	32	:	?
		IconBang	:	48	:	!
		IconI		:	64	:	i
		IconBlank	:	80	:	(blank)

	
	'''
	response = win32gui.MessageBox(0, sMessage, sTitle, flags)
	if beep:
		win32gui.MessageBeep(0)


	return response



import Tkinter
class CProgressBar(object):
	'''
	An instance of this class allows an application to create Tkinter-based widget that displays a progress bar.
	Based on ActiveState recipe 577926
	'''
	
	def settitle(self, title):
		self.__root.title(title)
		
		
	def __init__(self, width, height,title='Wait please...'):
		'''
		Create CProgressBar instance with the widget of the specified size and with the optional
		title string in the widget's titlebar.
		'''
		#self.__root = Tkinter.Toplevel()
		self.__root = Tkinter.Tk() #updated by Petr
		self.__root.resizable(False, False)
		self._title = title
		self.__root.title(title)
		self.__canvas = Tkinter.Canvas(self.__root, width=width, height=height)
		self.__canvas.grid()
		self.__width = width
		self.__height = height

	def open(self):
		'''
		Open (render) the CProgressBar widget
		'''
		self.__root.deiconify()
		self.__root.focus_set()
		#self.__root.update()

	def close(self):
		'''
		Close the CProgressBar widget
		'''
		self.__root.withdraw()

	def update(self, ratio, message=None):
		'''
		Update CProgressBar instance with a bar size proportional to passed in ratio.
		If message string is supplied, it is displayed in the titlebar of the widget.
		Since this method returns False if an exception occurs, or if the user destroys
		the control (by red-x closing it) during an update, the client code should monitor
		this method's return value and stop processing when it returns False.
		'''
		try:
			self.__canvas.delete(Tkinter.ALL)
			self.__canvas.create_rectangle(0, 0, self.__width * ratio, self.__height, fill='blue')
		except:
			return False

		if message:
			try:
				self.__root.title(self._title + '   ' + message)
			except:
				return False
		try:
			self.__root.update()
			self.__root.focus_set()
		except:
			return False

		return True





if __name__ == '__main__':

	# --------------------------- MsgAlert ---------------------------------

	# X - Cancel, Try Again, Continue
	#iFlag = Icon.X | Button.YesNo

	# Bang - Y, N, Cancel
	#iFlag = Icon.QMark | Button.OkCancel  
	
	# Bang - Abort, Retry, Ignore
	#iFlag = Icon.QMark | Button.Ok

	# Bang - Abort, Retry, Ignore
	#iFlag = Icon.QMark
	
	
	r1 = MsgAlert("My Message", "My Title", flags=Icon.QMARK + Button.YES_NO_CANCEL, beep=True)
	if r1 == Response.CANCEL:
		print 'Cancel selected.'
	else:
		print r1

	r2 = MsgAlert("My New Message", "My New Title", flags=Button.OK_CANCEL + Icon.BANG)
	if r2 == Response.OK:
		print 'Ok'
	else:
		print r2

	r3 = MsgAlert("My Newest Message", "My Newest Title", flags=Button.ABORT_RETRY_IGNORE + Icon.X)
	if r3 == Response.ABORT:
		print 'Aborted!'
	else:
		print r3


	# ----------------------- ProgressBar ----------------------------------
	import time
	bSuccess = True
	pb = CProgressBar(500, 20,title='Processing...')
	pb.open()
	for i in xrange(0, 100000):
		if i % 50 == 0:
			time.sleep(0.1)
			ratio = i/10000.0
			if i % 1000 == 0:
				if not pb.update(ratio, str(ratio)):
					bSuccess = False
					break
			else:
				if not pb.update(ratio):
					bSuccess = False
					break
	
	if bSuccess:			
		print 'Processing completed successfully!'
	else:
		print 'Processing aborted due to an error.'

	
