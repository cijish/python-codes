#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import xlrd
import xlwt
import unicodedata
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from Tkinter import *
 
class TkFileDialogExample(Tkinter.Frame):
 
   def __init__(self, root):

     # define out put exls file and row count
     self.book = xlwt.Workbook(encoding="utf-8")
     self.sheet_out = self.book.add_sheet("compared file") 
     self.count  = 0

     Tkinter.Frame.__init__(self, root)
     self.frame = Frame(bg = "#C7C1FF")
     self.frame.pack()

     self.frame1 = Frame(self.frame, bg = "#C7C1FF")
     self.frame1.pack()

     self.frame2 = Frame(self.frame, bg = "#C7C1FF")     
     self.frame2.pack()

     #self.frame2 = Frame(width=800, bg = "#C7C1FF" bd = '0')
     #self.frame2.pack()

     #Label(self.frame1, text="Select  An Excel file For compare!", bg = "#C7C1FF").pack()
     
   

     # options for buttons
     button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
 
     # define buttons
     Tkinter.Button(self.frame1, text='Select  An Excel file For compare!', command=self.askopencompairingfile, width=60, bg = "#CDB7F0").pack(**button_opt)
     Tkinter.Button(self.frame2, text='Select  An Excel file As Source!', command=self.askopensourcefile, width=60, bg = "#CDB7F0").pack(**button_opt)
     Tkinter.Button(self, text='Compare Files', command=self.compairfiles, width=60, bg = "#CDB7F0").pack(**button_opt)

     # define options for opening or saving a file
     self.file_opt = options = {}
     options['defaultextension'] = '' # couldn't figure out how this works
     options['filetypes'] = [('excel files', '.*')]
     options['initialdir'] = 'C:\\'
     #options['initialfile'] = 'myfile.txt'
     options['parent'] = root
     options['title'] = 'This is a title'
 

     self.dir_opt = options = {}
     options['initialdir'] = 'C:\\'
     options['mustexist'] = False
     options['parent'] = root
     options['title'] = 'This is a title'
 
   def encode(self,data):
      try:
         return unicodedata.normalize('NFKD', data).encode('ascii','ignore') 
      except:
         return data

#______________________________________________________________________________________________________________________________


   def askopencompairingfile(self):
 
     """Returns an opened file in read mode.
     This time the dialog just returns a filename and the file is opened by your own code. bg = "#C7C1FF", expand = 1, padx = 10, pady = 10
     """
 
     # get filename
     filename = tkFileDialog.askopenfilename(**self.file_opt)
 
     # open file on your own
     if filename:
       self.file_1 = xlrd.open_workbook(filename)
       self.v = StringVar()
       #self.v.set(self.file_1.sheet_names()[0])

       try:

          self.frame_worksheet1.destroy()
          self.frame_worksheet1 = Frame(self.frame1, width=800, bg = "#C7C1FF")
          self.frame_worksheet1.pack()
          Label(self.frame_worksheet1, text="Select work sheet of " + filename, bg = "#C7C1FF").pack()
          try:self.frame_col1.destroy()
          except: pass

       except:
          self.frame_worksheet1 = Frame(self.frame1, width=800, bg = "#C7C1FF")
          self.frame_worksheet1.pack()
          Label(self.frame_worksheet1, text="Select work sheet of " + filename, bg = "#C7C1FF").pack()

       for sheet_name in self.file_1.sheet_names():
          self.rb_comp =  Radiobutton(self.frame_worksheet1, text=sheet_name, variable=self.v, value=sheet_name, command=self.sel_comp_sheet, bg = "#C9A0DC")
    self.rb_comp.pack(anchor=W)
       #self.rb_comp_col = Label(self.frame1, text="Select work col For compare!", bg = "#C7C1FF")
       #self.rb_comp_col.pack()


       return ""

   def sel_comp_sheet(self):

      self.v2 = IntVar()
      #self.v2.set(0)
      try:
          self.frame_col1.destroy()
          self.frame_col1 =  Frame(self.frame1, width=800, bg = "#C7C1FF")
          self.frame_col1.pack()
          Label(self.frame_col1, text ="Select Column for compare!", bg = "#C7C1FF").pack()

      except:

          self.frame_col1 =  Frame(self.frame1, width=800, bg = "#C7C1FF")
          self.frame_col1.pack()
          Label(self.frame_col1, text ="Select Column for compare!", bg = "#C7C1FF").pack()
      sheet = self.file_1.sheet_by_name(str(self.v.get()))
      xx =  list(self.encode(title) for title in   sheet.row_values(0))

      #for x in range(6):
      for x in xx :
           #self.rb_comp_col = Radiobutton(self.frame_col1, text="col "+str(x), variable=self.v2, value=x, bg = "#F4BBFF")
           self.rb_comp_col = Radiobutton(self.frame_col1, text=str(x), variable=self.v2, value=xx.index(x), bg = "#F4BBFF")
	   self.rb_comp_col.pack(anchor=W, side = 'left', expand = 1, padx = 10, pady = 10)

#********************************************************************************************************************************

   def askopensourcefile(self):
 
     """Returns an opened file in read mode.
     This time the dialog just returns a filename and the file is opened by your own code.
     """
 
     # get filename
     filename = tkFileDialog.askopenfilename(**self.file_opt)
     # open file on your own
     if filename:
       self.out_filename =  filename
       self.file_2 = xlrd.open_workbook(filename)
       self.v3 = StringVar()
       #self.v3.set(self.file_2.sheet_names()[0])
      
       try:

          self.frame_worksheet2.destroy()
          self.frame_worksheet2 = Frame(self.frame2, width=800, bg = "#C7C1FF")
          self.frame_worksheet2.pack()
          Label(self.frame_worksheet2, text="Select work sheet of " + filename, bg = "#C7C1FF").pack()
          try:self.frame_col2.destroy()
          except: pass

       except:
          self.frame_worksheet2 = Frame(self.frame2, width=800, bg = "#C7C1FF")
          self.frame_worksheet2.pack()
          Label(self.frame_worksheet2, text="Select work sheet of " + filename, bg = "#C7C1FF").pack()

       for sheet_name in self.file_2.sheet_names():
           self.rb_source = Radiobutton(self.frame_worksheet2, text=sheet_name, variable=self.v3, value=sheet_name, command=self.sel_source_sheet, bg = "#C9A0DC")
           self.rb_source.pack(anchor=W)
       # elf.rb_source_col = Label(self.frame2, text="Select work col For compare!", bg = "#C9A0DC")
       #self.rb_source_col.pack()


       return ""
#_________________________________________________________________________________________________________________________________
   def sel_source_sheet(self):

      self.v4 = IntVar()
      #self.v4.set(0)

      try:
          self.frame_col2.destroy()
          self.frame_col2 =  Frame(self.frame2, width=800, bg = "#C7C1FF")
          self.frame_col2.pack()
          Label(self.frame_col2, text ="Select Column for compare!", bg = "#C7C1FF").pack()

      except:

          self.frame_col2 =  Frame(self.frame2, width=800, bg = "#C7C1FF")
          self.frame_col2.pack()
          Label(self.frame_col2, text ="Select Column for compare!", bg = "#C7C1FF").pack()
      sheet = self.file_2.sheet_by_name(str(self.v3.get()))
      xx =  list(self.encode(title) for title in   sheet.row_values(2))
      for x in xx:
           self.rb_source_col = Radiobutton(self.frame_col2, text=str(x), variable=self.v4, value=xx.index(x), bg = "#F4BBFF")
           self.rb_source_col.pack(anchor=W, side = 'left', expand = 1, padx = 10, pady = 10) 


#______________________________________________________________________________________________________________________________

   def compairfiles(self):
 

	sheet = self.file_1.sheet_by_name(str(self.v.get()))
	#sheet = wb.sheet_by_index(0)
	titles =  list(self.encode(title) for title in   sheet.row_values(0))
	#print titles
	code_list = list(set(sheet.col_values(int(self.v2.get()))))
	if "" in code_list: code_list.remove("")
	code_list = list(self.encode(item)  for item in  code_list)
	#print code_list


	sheet = self.file_2.sheet_by_name(str(self.v3.get()))
	for rownum in range(sheet.nrows):
	  data =  sheet.row_values(rownum)
	  colno = 0
	  if data[int(self.v4.get())]: 
	   data = list(self.encode(item) for item in  data)
	   if not data[int(self.v4.get())] in code_list:
		 for val in data:
 		   self.sheet_out.write(self.count, colno, val) 
		   colno  += 1
		 self.count +=1


	self.book.save(self.out_filename + "_processed_spreadsheet.xls")
        messg = StringVar()
        tkMessageBox.showinfo("Message", "File Successfully Created!")

        #self.last_label = Label(self, text="File Successfully Created!", bg = "#C7C1FF")
        #self.last_label.pack()
 

 
if __name__=='__main__':
   root = Tkinter.Tk()

   TkFileDialogExample(root).pack()
   root.mainloop()
