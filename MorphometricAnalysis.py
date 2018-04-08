"""
Created on Sat Dec 16 22:04:40 2017
@author: Katie Binley
"""

""" ************************** Import relavant libraries *********************************** """

import pandas as pd

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np

import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

from PIL import ImageTk, Image


""" **************************************************************************************** """



class Window(tk.Frame):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Analysis tools")
        window['bg']="white"
        
        # make buttons
        b1 = ttk.Button(window, text = "Polygon area", width=10, command=self.polygon_command)     
        b1.grid(row=3, column=4)
        
        b2 = ttk.Button(window, text = "Sholl analysis", width=10, command=self.sholl_command)
        b2.grid(row=6, column=4)
        
        b3 = ttk.Button(window, text = "Quit", width=5, command=window.destroy)
        b3.grid(row=8, column=4)
        
        b4 = ttk.Button(window, text = "Get image", width=10, command=self.find_filepath)
        b4.grid(row=1, column=4)
        
        # make labels
        l1 = Label(window, text = "Filepath:")
        l1.config(font=("Verdana", 20))
        l1.grid(sticky="e", row=1, column=1)
        
        l2 = Label(window)
        l2.grid(row=2, column=1)
        
        l3 = Label(window, text = "pixels per um")
        l3.config(font=("Verdana", 12))
        l3.grid(sticky="w", row=3, column=2)
        
        l4 = Label(window)
        l4.grid(row=4, column=1)
        
        l5 = Label(window, text = "Max Sholl radius (um):")
        l5.config(font=("Verdana", 12))
        l5.grid(sticky="e", row=5, column=1)
        
        l6 = Label(window, text = "Sholl radius interval (um):")
        l6.config(font=("Verdana", 12))
        l6.grid(sticky="e", row=6, column=1)
        
        l7 = Label(window)
        l7.grid(row=7, column=1)
        
        
        # make entry boxes
        self.filepath = StringVar()
        self.e1 = Entry(window, textvariable = self.filepath)
        self.e1.grid(row=1, column=2)
        
        self.scale = StringVar()
        e2 = Entry(window, textvariable = self.scale)
        e2.grid(row=3, column=1)
        
        self.usershollmax = StringVar()
        e3 = Entry(window, textvariable = self.usershollmax)
        e3.grid(row=5, column=2)
        
        self.usershollinterval = StringVar()
        e4 = Entry(window, textvariable = self.usershollinterval)
        e4.grid(row=6, column=2)
        
     
        
    def polygon_command(self):
        print("Drawing polygon...")
        
        global path
        path = self.filepath.get()
        # Bring up warning window if user hasn't entered file name
        if self.filepath.get() == "":
            #print("No file selected")
            self.getfilepath = tk.Toplevel(self.window)
            self.app = WarningWindow(self.getfilepath)
        else:
            self.getfilepath = tk.Toplevel(self.window)
            self.app = PolygonWindow(self.getfilepath)
        
        # Get scale from entry box
        Window.enteredimgscale = self.scale.get()
        if self.scale.get() == "":
            Window.imgscale = 1
        else:
            Window.imgscale = float(self.scale.get())
    
    
    def sholl_command(self):
        print("Carrying out Sholl analysis...")
        
        # Get scale from entry box
        if self.scale.get() == "":
            Window.imgscale = 1
        else:
            Window.imgscale = float(self.scale.get())
            
        
        
        # Get max and increment for Sholl analysis
        if self.usershollmax.get() == "":
            Window.shollmax = 300
        else:
            Window.shollmax = float(self.usershollmax.get())
            
        
        if self.usershollinterval.get() == "":
            Window.shollinterval = 10
        else:
            Window.shollinterval = float(self.usershollinterval.get())
        
        
        global path
        path = self.filepath.get()
        # Bring up warning window if user hasn't entered file name
        if self.filepath.get() == "":
            #print("No file selected")
            self.getfilepath = tk.Toplevel(self.window)
            self.app = WarningWindow(self.getfilepath)
        else:
            self.getfilepath = tk.Toplevel(self.window)
            self.app = ShollWindow(self.getfilepath)
            #self.getfilepath = tk.Toplevel(self.window)
            #self.app = ShollStepOnePopupWindow(self.getfilepath)
        
        
        

            
    
    def find_filepath(self):
        
        #####################################################################################################
        print("opening...")
        formats = [('Tiff files', '*.tif'), ('all files', '*.*')]
        self.openfile = askopenfilename(title = "Select file",filetypes = formats)
        
        # put filename into entry box
        self.e1.delete(0, END)
        self.e1.insert(END, self.openfile)
        self.e1.xview(END)
        
        global path
        path = self.filepath.get()
        #print("filepath is:", path)
        
        # Bring up warning window if user hasn't entered file name
        if self.filepath.get() == "":
            #print("No file selected")
            self.getfilepath = tk.Toplevel(self.window)
            self.app = WarningWindow(self.getfilepath)
        else:
            self.getfilepath = tk.Toplevel(self.window)
            self.app = ImageWindow(self.getfilepath)
  



class ImageWindow(tk.Canvas):
    
    def __init__(self, window2):
        self.window2 = window2
        self.window2.wm_title("Neuron image")
        window2.geometry("500x500")
        
        w = Canvas(window2, width=500, height=500)
        w.pack()
        
        
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        w.create_image(250, 250, image=photo)
        w.photo = photo
        w.pack()
        
        
        
class PolygonWindow(tk.Canvas):
    
    def __init__(self, window3):
        self.window3 = window3
        #self.window3.wm_title("Polygon tool")
        self.window3.wm_title(path)
        window3.geometry("500x500")
        
        self.w = Canvas(window3, width=500, height=500)
        self.w.pack()
        
        # add user image to middle of window
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        self.w.create_image(250, 250, image=photo)
        self.w.photo = photo
        
        #
        self.w.bind("<Button-1>", self.callback)
        self.w.pack()
        self.start_coords = None
        self.end_coords = None
        
        # create lists needed to calculate polygon area
        self.t = ()
        self.coord_list_x = ()
        self.coord_list_y = ()
        self.x_area = ()
        self.y_area = ()
        self.num_list = ()
        self.odd_list = ()
        self.even_list = ()
        self.odd_list_sum = ()
        self.even_list_sum = ()
 
       
    def callback(self, event):
        window.focus_set()
        #print("clicked at", event.x, event.y)
        self.x=event.x
        self.y=event.y
        
        #print(self.x)
        #print(self.y)
        
    
        coords = event.x, event.y
        if not self.start_coords:
            self.start_coords = coords
            return
        self.end_coords = coords
        self.w.create_line(self.start_coords[0],
                                self.start_coords[1],
                                self.end_coords[0],
                                self.end_coords[1])
        self.start_coords = self.end_coords
        
        self.t = self.t + (self.start_coords[0],) + (self.start_coords[1],) + (self.end_coords[0],) + (self.end_coords[1],)
        #print(self.t)
        
        """ Trigger polygon drawing and area calculation
        - if polygon contains at least 3 lines (coordinate list >=12)
        - and where user double clicks, i.e. last 2 x and y coordinates are the same
        - create x coordinate and y coordinate list and call polyArea function"""
        if len(self.t) > 11 and self.t[-1] == self.t[-5] and self.t[-2] == self.t[-6]:
            self.w.create_polygon(self.t, fill="", outline = "#000000", width=3)
            self.coord_list_x = self.coord_list_x + (self.t[0::4])
            #print(self.coord_list_x)
            self.coord_list_y = self.coord_list_y + (self.t[1::4])
            #print(self.coord_list_y)
            self.polyArea()
        
            
            
    def polyArea(self):
           
        self.x_area = self.x_area + (self.coord_list_x[0:],)
        self.x_area = self.x_area + (self.coord_list_x[0],)
        self.y_area = self.y_area + (self.coord_list_y,) + (self.coord_list_y[0],)
        #print(self.x_area)
        #print(self.y_area)
        
        """ Remove last element and add 1st x and y elements to ends of coordinate lists 
        to make area calculation easier"""
        self.coord_list_x = self.coord_list_x[:-1]
        for numb, n in enumerate(self.coord_list_x):
            self.x_area = n
            
            for i in self.coord_list_x:
                self.x_area = self.coord_list_x
            self.x_area = self.x_area + (self.coord_list_x[0],) + (self.coord_list_x[0],)
        
        
        self.coord_list_y = self.coord_list_y[:-1]
        for numb, n in enumerate(self.coord_list_y):
            self.y_area = n
            
            for i in self.coord_list_y:
                self.y_area = self.coord_list_y
            self.y_area = self.y_area + (self.coord_list_y[0],) + (self.coord_list_y[0],)
        
        
        for num, n in enumerate(self.x_area, start=1):
            for numy, ny in enumerate(self.y_area, start=1):
               
                if num == numy+1:
                    self.num_list = self.num_list + (n * ny,)

                if num+1 == numy:
                    self.num_list = self.num_list + (n * ny,)

        
        self.odd_list = self.num_list[0::2]
        self.even_list = self.num_list[1::2]
        
        """ now sum all elements in odd_list and even_list and do odd - even for final area
        - area calculation: sum((xn*yn+1)-(xn+1*yn))/2"""
        self.odd_list_sum = sum(self.odd_list)
        self.even_list_sum = sum(self.even_list)
        
        PolygonWindow.PolArea = 0.5 * (self.odd_list_sum - self.even_list_sum)
        #print("Area:", PolygonWindow.PolArea)
        
        """ Scale area according to input scale"""
        # Scale in um
        PolygonWindow.ScaleFactor = 1/Window.imgscale
        
        PolygonWindow.ScaledPolygonArea = PolygonWindow.ScaleFactor * PolygonWindow.PolArea
        #print("Scaled area:", PolygonWindow.ScaledPolygonArea)
        """ Multiply polygon area by -1 in cases where user drew polygon anticlockwise """
        if PolygonWindow.ScaledPolygonArea < 0:
            PolygonWindow.ScaledPolygonArea = PolygonWindow.ScaledPolygonArea * -1
        
        if Window.imgscale == 1:
            print("no scale entered")
    
     
        self.getresults = tk.Toplevel(self.window3)
        self.app = AreaWindow(self.getresults)
        
        
        
 
    
""" ******** Create results window for polygon area if scale entered ******** """   
 
class AreaWindow(tk.Canvas):
    def __init__(self, window4):
        self.window4 = window4
        self.window4.wm_title("Polygon area results")
        
        l1 = Label(window4, text="Polygon area:")
        l1.grid(row=1, column=1)
        
        self.PolArea_text = StringVar()
        e1 = Entry(window4, textvariable=self.PolArea_text)
        e1.grid(row=1, column=2)
        e1.insert(END, PolygonWindow.ScaledPolygonArea)
       
        
        l2 = tk.Text(window4, width=7, height=2, borderwidth=0)
        l2.tag_configure("superscript", offset=+2)
        if Window.enteredimgscale == "":
            l2.insert("insert", "pixels", "", "2", "superscript")
        else:
            l2.insert("insert", "um", "", "2", "superscript")
        
        l2.configure(state="disabled")
        l2.grid(row=1, column=4)
        
 

       
class WarningWindow(tk.Canvas):
    
    def __init__(self, window5):
        self.window5 = window5
        self.window5.wm_title("Warning")
        window5.geometry("200x50")
        
        l1 = Label(window5, compound=tk.CENTER, text="No file selected!", padx=50)
        l1.config(font=("Verdana", 15))
        l1.pack(side="left")
     
        
        
class ShollStepOnePopupWindow(tk.Canvas):
    def __init__(self, window7):
        window.focus_set()
        self.window7 = window7
        self.window7.wm_title("Selecting points for Sholl analysis...")
        window7.geometry("290x130")
        
        # Make labels to form grid to allow buttons to be central
        l1 = Label(window7, text="", width=5)
        l1.grid(row=1, column=1)
        
        l2 = Label(window7, text="", width=5)
        l2.grid(row=2, column=1)
        
        l3 = Label(window7, text="", width=5)
        l3.grid(row=3, column=1)
        
        l4 = Label(window7, text="", width=5)
        l4.grid(row=4, column=1)
        
        l5 = Label(window7, text="", width=5)
        l5.grid(row=5, column=1)
        
        l6 = Label(window7, text="", width=5)
        l6.grid(row=1, column=2)
        
        l7 = Label(window7, text="", width=5)
        l7.grid(row=5, column=2)
        
        l8 = Label(window7, text="", width=5)
        l8.grid(row=1, column=3)
        
        l9 = Label(window7, text="", width=5)
        l9.grid(row=2, column=3)
        
        l10 = Label(window7, text="", width=5)
        l10.grid(row=3, column=3)
        
        l11 = Label(window7, text="", width=5)
        l11.grid(row=4, column=3)
        
        l12 = Label(window7, text="", width=5)
        l12.grid(row=5, column=3)
        
    
        # Make buttons to let user move onto selecting next points
        b1 = Button(window7, text="Start points clicked", width=20, command=self.Start_command)
        b1.grid(row=2, column=2)
        
        b2 = Button(window7, text="Branch points clicked", width=20, command=self.Branch_command)
        b2.grid(row=3, column=2)
        
        b3 = Button(window7, text="Termini points clicked", width=20, command=self.finished_command)
        b3.grid(row=4, column=2)
        
        global randomvar
        randomvar = ""


    def Start_command(self):
        print("clicked Start points done")
        global randomvar
        randomvar = "1"
        
    def Branch_command(self):
        print("clicked Branch points done")
        global randomvar
        randomvar = "2"
    
    def finished_command(self):
        #print("finished")
        #print("init centre coords:", ShollWindow.centre_coords)
        #print("init start coords:", ShollWindow.start_coords)
        #print("init branch coords:", ShollWindow.branch_coords)
        #print("init termini coords:", ShollWindow.termini_coords)     
        
        # Set parameters for Sholl analysis  
        ShollWindow.usershollmax = Window.shollmax
        ShollWindow.usershollinterval = Window.shollinterval
        ShollWindow.startelementspercoordinate = int((ShollWindow.usershollmax/ShollWindow.usershollinterval)+1)
        
        ################################################################################################
        """
        # Trim first "coordinate" from branch and termini arrays created from clicking window
        x = ShollWindow.startelementspercoordinate
        ShollWindow.brancharray = ShollWindow.brancharray[x::1]
        ShollWindow.terminiarray = ShollWindow.terminiarray[x::1]
        """
        #print("start array:", ShollWindow.startarray)
        #print("branch array:", ShollWindow.brancharray)
        #print("termini array:", ShollWindow.terminiarray)
   
        ######
        # Take start coordinates array, convert to array of arrays (for each coordinate) to indicate position relative to Sholl rings
        ######
        
        
        ShollWindow.arrayofstartarrays = []
        i = 0
        while i <= (len(ShollWindow.startarray) - ShollWindow.startelementspercoordinate):
            ShollWindow.slicedstartarray = ShollWindow.startarray[i:(i+ShollWindow.startelementspercoordinate)]
            ShollWindow.arrayofstartarrays.append(ShollWindow.slicedstartarray)
            i = i + ShollWindow.startelementspercoordinate
        
        # Now sum yes(1) or no(0) coordinates at each Sholl ring
        ShollWindow.finalstartarray = []
        ShollWindow.transposedstartarray = np.transpose(ShollWindow.arrayofstartarrays)
        
        for i in ShollWindow.transposedstartarray:
            sumstartelements = sum(i[0:])
            ShollWindow.finalstartarray.append(sumstartelements)
        
        #print("final start array:", ShollWindow.finalstartarray)
        
        
        
        ######
        # Take branch coordinates array, convert to array of arrays (for each coordinate) to indicate position relative to Sholl rings
        ######
        #ShollWindow.startelementspercoordinate = int((ShollWindow.max/ShollWindow.increment)+1)
        
        ShollWindow.arrayofbrancharrays = []
        i = 0
        while i <= (len(ShollWindow.brancharray) - ShollWindow.startelementspercoordinate):
            ShollWindow.slicedbrancharray = ShollWindow.brancharray[i:(i+ShollWindow.startelementspercoordinate)]
            ShollWindow.arrayofbrancharrays.append(ShollWindow.slicedbrancharray)
            i = i + ShollWindow.startelementspercoordinate
        
        # Now sum yes(1) or no(0) coordinates at each Sholl ring
        ShollWindow.finalbrancharray = []
        ShollWindow.transposedbrancharray = np.transpose(ShollWindow.arrayofbrancharrays)
        
        for i in ShollWindow.transposedbrancharray:
            sumbranchelements = sum(i[0:])
            ShollWindow.finalbrancharray.append(sumbranchelements)
        
        #print("final branch array:", ShollWindow.finalbrancharray)
        
        
        
        ######
        # Take termini coordinates array, convert to array of arrays (for each coordinate) to indicate position relative to Sholl rings
        ######
        #ShollWindow.startelementspercoordinate = int((ShollWindow.max/ShollWindow.increment)+1)
        
        ShollWindow.arrayofterminiarrays = []
        i = 0
        while i <= (len(ShollWindow.terminiarray) - ShollWindow.startelementspercoordinate):
            ShollWindow.slicedterminiarray = ShollWindow.terminiarray[i:(i+ShollWindow.startelementspercoordinate)]
            ShollWindow.arrayofterminiarrays.append(ShollWindow.slicedterminiarray)
            i = i + ShollWindow.startelementspercoordinate
        
        # Now sum yes(1) or no(0) coordinates at each Sholl ring
        ShollWindow.finalterminiarray = []
        ShollWindow.transposedterminiarray = np.transpose(ShollWindow.arrayofterminiarrays)
        
        for i in ShollWindow.transposedterminiarray:
            sumterminielements = sum(i[0:])
            ShollWindow.finalterminiarray.append(sumterminielements)
        
        #print("final termini array:", ShollWindow.finalterminiarray)
        #######
        
        #######
        # Now make the Sholl y coordinates array for plotting!
        # This is done by: start + branch - termini
        #######
        
        # y coords
        ShollWindow.sholltemp = [ShollWindow.finalstartarray[0:], ShollWindow.finalbrancharray[0:], ShollWindow.finalterminiarray[0:]]
        ShollWindow.transposedsholltemp = np.transpose(ShollWindow.sholltemp)
        ShollWindow.shollycoordinates = []
        
        for i in ShollWindow.transposedsholltemp:
            shollelement = i[0] + i[1] - i[2]
            ShollWindow.shollycoordinates.append(shollelement)
        
        #print("Sholl y array:", ShollWindow.shollycoordinates)
        
        # x coords made in ShollWindow init
        """ShollWindow.shollxcoordinates = [0]
        
        i = ShollWindow.increment
        while i <= ShollWindow.max:
            ShollWindow.shollxcoordinates.append(i)
            i = i + ShollWindow.increment
        
        #print("Sholl x array:", ShollWindow.shollxcoordinates)
        """
        
        #######
        # Put Sholl x and y coordinates into dataframe to show results
        #######
        ShollWindow.shollcoords = [ShollWindow.shollxcoordinates, ShollWindow.shollycoordinates]
        ShollWindow.shollcoords = np.transpose(ShollWindow.shollcoords)
        ShollWindow.sholldf = pd.DataFrame(ShollWindow.shollcoords[0:], columns=["Distance from soma centre", "Intersections"])
        
        # Calculate AUC for each row (using trapezoid method)
        AUC_series = [0]
        arraylen = int((Window.shollmax/Window.shollinterval) + 1)
        
        for i in range(1, arraylen, 1):
            auc_value = (ShollWindow.sholldf.iloc[i]['Intersections'] + ShollWindow.sholldf.iloc[i-1]['Intersections'])/2 * (ShollWindow.sholldf.iloc[i]['Distance from soma centre'] - ShollWindow.sholldf.iloc[i-1]['Distance from soma centre'])
            AUC_series.append(auc_value)
            
        # Add AUC column to Sholl dataframe
        ShollWindow.sholldf['AUC'] = AUC_series[0:]
        
        # Add extra row at bottom of Sholl dataframe to calculate AUC for Sholl curve (i.e. sum(AUC row))
        cellAUC = sum(AUC_series[0:])
        j = arraylen
        ShollWindow.sholldf.loc[j] = ["", "Cell AUC:", cellAUC]
        
        #print(ShollWindow.sholldf)
        
        
        # Get number of branch coordinate pairs
        ShollWindow.branchlength = len(ShollWindow.brancharray)/31
        #print(ShollWindow.branchlength)
        
        # Get number of termini coordinate pairs
        ShollWindow.terminilength = len(ShollWindow.terminiarray)/31
        #print(ShollWindow.terminilength)
        
        # Open file explorer to save Sholl results as csv
        print("browsing...")
        formats = [('Comma Separated values', '*.csv'), ('text files', '*.txt')]
        self.fname = asksaveasfilename(filetypes=formats)
        ShollWindow.sholldf.to_csv(self.fname, sep=',', encoding='utf-8', index=False)
                  
        
        # Trigger Sholl table and plot windows to open with Sholl results
        self.getplot = tk.Toplevel(self.window7)
        self.app = ShollPlotWindow(self.getplot)
        
        
        ######
        # End of finished_command ##################################################################
        ######
       
    
    

class ShollWindow(tk.Canvas):
    
    def __init__(self, window6):
        self.window6 = window6
        self.window6.wm_title("Sholl Analysis")
        window6.geometry("500x500")
        #window6.attributes("-topmost", True)
        
        self.w = Canvas(window6, width=500, height=500)
        self.w.pack()
        
        # add user image to middle of window
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        self.w.create_image(250, 250, image=photo)
        self.w.photo = photo
        
        #Initiate analysisStepOne after clicking soma centre
        self.w.bind("<Button-1>", self.analysisCentrePoints)
        self.w.pack()
        self.start_coords = None
        self.end_coords = None
        
        
        self.shollpopup = tk.Toplevel(self.window6)
        self.app = ShollStepOnePopupWindow(self.shollpopup)
        
        # Set scale in inches based on user input
        ShollWindow.scalefactor = 1 / Window.imgscale
        
        # Set Sholl max and Sholl ring intervals based on user input
        ShollWindow.usershollmax = Window.shollmax
        ShollWindow.usershollinterval = Window.shollinterval
        
        ShollWindow.start_coords = []
        ShollWindow.branch_coords = []
        ShollWindow.termini_coords = []
        
        # Make arrays for Sholl intersection calculation
        # x coords
        ShollWindow.shollxcoordinates = [0]
        
        i = ShollWindow.usershollinterval
        while i <= ShollWindow.usershollmax:
            ShollWindow.shollxcoordinates.append(i)
            i = i + ShollWindow.usershollinterval
        

        ShollWindow.startarray = []
        ShollWindow.sumstartarray = []
        ShollWindow.brancharray = []
        ShollWindow.sumbrancharray = []
        ShollWindow.terminiarray = []
        ShollWindow.sumterminiarray = []
        ShollWindow.startcounter = 0
        ShollWindow.branchcounter = 0
        ShollWindow.terminicounter = 0
        
    
    def analysisCentrePoints(self, event):
        window.focus_set()
        
        # First step: get centre of cell soma
        #print("Click centre of cell soma")
        self.x=event.x
        self.y=event.y
        
        ShollWindow.centre_coords = event.x, event.y
        #print(ShollWindow.centre_coords)        
        
        self.w.create_oval(self.x-4, self.y-4, self.x+4, self.y+4, fill="white", outline="#e51912", width=1)
         
        self.w.bind("<Button-1>", self.analysisStartPoints)
        self.w.pack()
    
        
        
    def analysisStartPoints(self, event):
        window.focus_set()
        
        if randomvar == "1":
            self.w.bind("<Button-1>", self.analysisBranchPoints)
            self.w.pack()
        else:
            #print("Click branch points")
            self.x2=event.x
            self.y2=event.y
            
            ShollWindow.start_coords.append(self.x2)
            ShollWindow.start_coords.append(self.y2)
            #print(ShollWindow.branch_coords)
            
            #print(self.x2)
            
            self.w.create_oval(self.x2-4, self.y2-4, self.x2+4, self.y2+4, fill="white", outline="#0f9b39", width=1)
      
            # Euclidean distance = SQRT((x1-x2)^2 + (y1-y2)^2)
            distance = ((ShollWindow.centre_coords[0] - self.x2)**2 + (ShollWindow.centre_coords[1] - self.y2)**2)**0.5
            adjdistance = distance * ShollWindow.scalefactor
            #print("Distance is:", adjdistance)
            
            
            i = 0
            for x in ShollWindow.shollxcoordinates:
                #print(x)
                #print(ShollWindow.shollxarray[i])
                if adjdistance > ShollWindow.shollxcoordinates[i]:
 
                    ShollWindow.startarray.append(0)
                else:

                    ShollWindow.startarray.append(1)
                i = i+1
                

        
        
    def analysisBranchPoints(self, event):
        window.focus_set()
        
        if randomvar == "2":
            self.w.bind("<Button-1>", self.analysisTerminiPoints)
            self.w.pack()
        else:
            #print("Click branch points")
            self.x3=event.x
            self.y3=event.y
            
            ShollWindow.branch_coords.append(self.x3)
            ShollWindow.branch_coords.append(self.y3)
            #print(ShollWindow.branch_coords)
            
            #print(self.x2)
            
            self.w.create_oval(self.x3-4, self.y3-4, self.x3+4, self.y3+4, fill="white", outline="#4f8cff", width=1)    
        
             
            # Euclidean distance = SQRT((x1-x2)^2 + (y1-y2)^2)
            distance2 = ((ShollWindow.centre_coords[0] - self.x3)**2 + (ShollWindow.centre_coords[1] - self.y3)**2)**0.5
            adjdistance2 = distance2 * ShollWindow.scalefactor
            #print("Distance is:", adjdistance2)
            
            
            i = 0
            for x in ShollWindow.shollxcoordinates:
                #print(x)
                #print(ShollWindow.shollxarray[i])
                if adjdistance2 > ShollWindow.shollxcoordinates[i]:
                    #print(0)
                    ShollWindow.brancharray.append(0)
                else:
                    #print(1)
                    ShollWindow.brancharray.append(1)
                i = i+1
        
            ShollWindow.branchcounter = ShollWindow.branchcounter + 1
            
        
    def analysisTerminiPoints(self, event):
        window.focus_set()
        
        #print("Click termini points")
        self.x4=event.x
        self.y4=event.y
        
        ShollWindow.termini_coords.append(self.x4)
        ShollWindow.termini_coords.append(self.y4)
        #print(ShollWindow.termini_coords)
        
        
        self.w.create_oval(self.x4-4, self.y4-4, self.x4+4, self.y4+4, fill="white", outline="#bf2aed", width=1)

        # Euclidean distance = SQRT((x1-x2)^2 + (y1-y2)^2)
        distance3 = ((ShollWindow.centre_coords[0] - self.x4)**2 + (ShollWindow.centre_coords[1] - self.y4)**2)**0.5
        adjdistance3 = distance3 * ShollWindow.scalefactor
        #print("Distance is:", adjdistance3)
            
            
        i = 0
        for x in ShollWindow.shollxcoordinates:
            #print(x)
            #print(ShollWindow.shollxarray[i])
            if adjdistance3 > ShollWindow.shollxcoordinates[i]:

                ShollWindow.terminiarray.append(0)
            else:
                
                ShollWindow.terminiarray.append(1)
            i = i+1

        ShollWindow.terminicounter = ShollWindow.terminicounter + 1


class ShollPlotWindow(tk.Frame):

    def __init__(self, window8):
        print("done!")
        window8.wm_title("Sholl Analysis Results")


        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        x = ShollWindow.shollxcoordinates
        y = ShollWindow.shollycoordinates
        
        a.plot(x, y, color = 'red')
        a.set_title('Sholl Plot', fontsize=16, fontweight='bold')
        a.set_xlabel('Distance from soma centre (um)')
        a.set_ylabel('Intersections')
        
        
        canvas = FigureCanvasTkAgg(f, master=window8)
        canvas.show()
        canvas.get_tk_widget().pack(expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, window8)
        toolbar.update()
        canvas._tkcanvas.pack(expand=1)
           
        

###
window = Tk()
app = Window(window)
window.mainloop()
###
