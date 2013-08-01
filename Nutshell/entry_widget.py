import Tkinter 
root = Tkinter.Tk() 
var = Tkinter.StringVar() 
entry = Tkinter.Entry(root, textvariable = var) 
entry.focus_set() 
entry.pack() 
var.set(root.title()) 
def changeTitle(): root.title(var.get()) 
Tkinter.Button(root, text =" Change Title", command = changeTitle). pack() 
Tkinter.Button( root, text =" Iconify", command = root.iconify). pack() 
Tkinter.Button( root, text =" Close", command = root.destroy). pack() 
Tkinter.mainloop( )

"""
Martelli, Alex (2009-06-30). Python in a Nutshell (Kindle Locations 16926-16929). O'Reilly Media. Kindle Edition. 
"""
