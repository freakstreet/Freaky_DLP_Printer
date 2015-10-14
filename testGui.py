from tkinter import *
import time


class DispImg(Tk):
    def __init__(self,*args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.label = Label(self, text="", width=20, anchor="w")
        self.label.pack(side="top",fill="both",expand=True)
        #~ self.print_label_slowly("Hello, world!")

    def print_label_slowly(self, message):
        '''Print a label one character at a time using the event loop'''
        t = self.label.cget("text")
        t += message[0]
        self.label.config(text=t)
        if len(message) > 1:
            self.after(250, self.print_label_slowly, message[1:])	


###############################################
##
##						DEBUG CODE
##
###############################################
def exit(event):
	print("Escape touch pushed : exiting")
	winPanel.quit()
	winImg.quit()
	winExit.quit()
    
if __name__ == "__main__":
	#~ path = '/home/lsa/Documents/DLP_Printer_soft_Freaky/gear.slice/gear0013.png'
	
	#~ winExit = Tk()
	#~ w, h = winExit.winfo_screenwidth(), winExit.winfo_screenheight()
	#~ winExit.geometry("%dx%d+10+10" % (100, 100))
	#~ winExit.bind("<Escape>", exit)
	
	#~ winPanel = Tk()
	#~ winPanel.overrideredirect(1)
	#~ winPanel.geometry("%dx%d+500+500" % (480, 320))
	
	#~ winImg = Tk()
	#~ #winImg.overrideredirect(1)
	#~ #winImg.geometry("%dx%d+0+0" % (w-200, h-200))
	
	#~ photo = PhotoImage(file=path)
	#~ photo_label = Label(image=photo)
	#~ photo_label.grid()             
	#~ photo_label.image = photo      

	#~ text = Label(text='Image loaded: '+ repr(path)) # included to show background color
	#~ text.grid()    
	
	dispImg = DispImg()
	dispImg.mainloop()
	for i in range(0, 5):
		dispImg.print_label_slowly("Inc" + repr(i))	
		time.sleep(3)
	