"""
Program: videoStoreGUI.py
Author: Joey Esencan 7/19/2023

GUI based version of the video store project from chapter 2

NOTE: The file breezypythongui.py MUST be in the same directory
as this file for the app to run correctly.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header
class VideoStore(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self, title = "Five Star Video", width = 340, height = 280, resizable = False, background = "darkred")
		self.normalFont = Font(family = "Tahoma", size = 10)
		self.addLabel(text = "Five Star Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "darkred", foreground = "lightyellow", font = Font(family = "Arial", size = 26))
		self.addLabel(text = "New rentals: $3.00, Old Rentals: $2.00", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "darkred", foreground = "lightyellow")
		self.addLabel(text = "Number of new videos being rented: ", row = 2, column = 0, background = "darkred", foreground = "lightyellow", sticky = "NE", font = self.normalFont)
		self.newVideos = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NW", width = 4)
		self.addLabel(text = "Number of old videos being rented:", row = 3, column = 0, background = "darkred", foreground = "lightyellow", sticky = "NE", font = self.normalFont)
		self.oldVideos = self.addIntegerField(value = 0, column = 1, row = 3, sticky = "NW", width = 4)
		self.button = self.addButton(text = "Calculate Total", row = 4, column = 0, columnspan = 2, command = self.calculate)

		self.addLabel(text = "The total for the order is: ", row = 5, column = 0, sticky = "NE", background = "darkred", foreground = "white", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 6)
	def calculate(self):
		new = self.newVideos.getNumber()
		old = self.oldVideos.getNumber()
		
		result = (new * 3.00) + (old * 2.00)
		
		# Output phase
		self.total.setNumber(result)



# Global definition of the main() method
def main():
	VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()