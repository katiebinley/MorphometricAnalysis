# Sholl Analysis and Morphometric Analysis for Neurons

This app allows the following analyses of an image (any filetype):
- polygon area calculation
- Sholl analysis (calculated using the equation used by the MATLAB script by Gutierrez & Davies, 2007 https://www.ncbi.nlm.nih.gov/pubmed/17367866) - displayed as line graph and results exported as a csv file
- Area under the Sholl curve - calculated using the trapezoid model. This is included in the Sholl analysis output file. 


### Prerequisites

Python 3. To install python 3, go to https://www.python.org/download/releases/3.0/
Check which version of python you have installed by typing in the terminal/command line:

```
python -V
```

### Installing

Download python file.
Run from terminal/Command prompt by navigating to directory where NoughtsAndCrosses.py is saved and typing:

```
python MorphometricAnalysis.py
```

or if you have more than one version of python installed, type:

```
python3 MorphometricAnalysis.py
```


## Opening the image file

NOTE: This step must be carried out prior to any analysis.

1. Click "Get image", browse to your image and click "open". Your image will appear in a new window.

![alt text](https://github.com/katiebinley/MorphometricAnalysis/blob/master/Step1.png)


## Polygon Area

1. Enter the number of pixels per um in the labelled box (NOTE: if this is not done, analysis may still be carried out but results will be given in pixels, rather than um). Click "Polygon area". Your image will appear in a new window.
2. To begin the analysis click on a terminal dendrite on your image. Continue to click on each terminal dendrite (clockwise or anti-clockwise) around the cell, drawing a polygon around the area of the dendritic tree. Note that a line will not appear until your second click.
3. The final click to close the polygon should be a double click - this will complete the analysis and the polygon area will appear in a new window. The area can be selected and copied into another programme.



## Sholl Analysis

1. Enter the number of pixels per um in the labelled box. Enter the desired maximum radius for analysis and the interval between Sholl rings (smaller will give more accurate analysis but a balance is required between accuracy and an unecessary number of points). Click "Sholl analysis" to open your image in a new window ready for analysis, along with a second new window with buttons indicating the stage of analysis.
2. The first step of Sholl analysis is to define the centre of analysis, or where the Sholl rings will radiate from. To do this, click on the centre of the soma - you will see a red circle appear. 
2. The second step is to define the start points of each dendrite, ie. where they begin at the edge of the soma. To do this, click on each start point - you will see green circles appear. When all have been selected, click "Start points clicked" on the "Selecting points for Sholl analysis..." window.
3. The third step is to define the branch points of each dendrite. To do this, click on each branch point - you will see blue circles appear. When all have been selected, click "Branch points clicked" on the "Selecting points for Sholl analysis..." window.
4. The final step is to define the dendrite termini. To do this, click on the ends of each dendrite - you will see magenta circles appear. When all have been selected, click "Termini points clicked" on the "Selecting points for Sholl analysis..." window. A new window will appear allowing you to select the destination for the output file, as well as the output file name and type (csv or txt) - csv is recommended. Click "save" and the Sholl plot will appear in a new window and the data points for the plot, along with area under the curve data, will be saved in the file you created.


## Closing the Application

Close the app by clicking "Close" or the cross on the title bar of the main window.




## Built With

* [Spyder3] (https://pythonhosted.org/spyder/installation.html) using Anaconda (https://www.anaconda.com/download/#macos)

## Contributers

Please contribute to make the game better and to help me learn more about coding in python!


## Authors

* **Katie Binley** - *Initial work* - [katiebinley](https://github.com/katiebinley)


## Acknowledgments

* Ardit Sulce's Udemy course taught me a lot of python skills needed to build this app (https://www.udemy.com/the-python-mega-course/learn/v4/overview).

