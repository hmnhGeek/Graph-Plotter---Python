import matplotlib
from math import *
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import PIL.ImageTk, PIL.Image
from Tkinter import *
import ttk


from matplotlib import pyplot as plt

LARGE_FONT = ("Verdana", 12)
EXTRA_LARGE_FONT = ("Verdana", 18)
style.use("ggplot")

f = Figure()
a = f.add_subplot(111)
##plt.xlabel("x")
##plt.ylabel("y")

def animate(ll, ul, func):
    f = open('sampleData.txt', 'w')
    f.write('')
    f.close()
    f = open('sampleData.txt', 'a')
    for x in range(ll, ul+1):
        fx = eval(func)
        f.write(str(x)+','+str(fx)+'\n')
    f.close()

def drawNow(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(float(x))
            yList.append(float(y))

    a.clear()
    a.plot(xList, yList)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self, default = "icon.ico")
        Tk.wm_title(self, "Graph Maker")
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        def about():
            f = open('abt.txt', 'r')
            s = f.read()
            f.close()
            root = Tk()
            root.title("About Graph Maker")
            root.geometry('400x150')
            l = ttk.Label(root, text = s).pack()
            root.resizable(height = FALSE, width = FALSE)
            root.mainloop()

        def Help():
            f = open('help.txt', 'r')
            s = f.read()
            f.close()
            root = Tk()
            root.title("About Graph Maker")
            root.geometry('400x250')
            l = ttk.Label(root, text = s).pack()
            root.resizable(height = FALSE, width = FALSE)
            root.mainloop()
        menubar = Menu(container)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "About", command = about)
        filemenu.add_command(label = "Help", command = Help)
        menubar.add_cascade(label = "Know more", menu = filemenu)

        Tk.config(self, menu = menubar)

        self.frames = {}
        # Main tuple is here.
        for F in (StartPage, BTCe_page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        img = PIL.ImageTk.PhotoImage(PIL.Image.open("m.jpg"))
        panel = Label(self)
        panel.image = img
        panel.configure(image = img)
        panel.pack(side = "right", fill = "both", expand = True)
        label = ttk.Label(self, text = "Graph Maker", font = EXTRA_LARGE_FONT)
##        label.place(x = 600, y = 0)
        label.pack(pady = 10, padx = 10)
        
        label = ttk.Label(self, text = "Enter function in terms of 'x'", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        entry = ttk.Entry(self)
        entry.pack(pady = 10, padx = 10)

        label1 = ttk.Label(self, text = "Enter Lower Limit", font = LARGE_FONT)
        label1.pack(pady = 10, padx = 10)

        entry1 = ttk.Entry(self)
        entry1.pack(pady = 10, padx = 10)

        label2 = ttk.Label(self, text = "Enter Upper Limit", font = LARGE_FONT)
        label2.pack(pady = 10, padx = 10)

        entry2 = ttk.Entry(self)
        entry2.pack(pady = 10, padx = 10)

        button = ttk.Button(self, text = "Upload", command = lambda: animate(int(entry1.get()), int(entry2.get()), entry.get()), width = 15)
        button.pack(pady = 5)
        
        button2 = ttk.Button(self, text = "Get its Graph", command = lambda: controller.show_frame(BTCe_page), width = 15)
        button2.pack(pady = 5)

        def _quit():
            f = open('sampleData.txt', 'w')
            f.write('')
            f.close()
            app.destroy()
        
        button3 = ttk.Button(self, text = "Close", command = _quit, width = 15)
        button3.pack(pady = 5)

class AboutPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "Page One", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Back to home",
                         command = lambda: controller.show_frame(StartPage))
        button1.pack()


class BTCe_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        button1 = ttk.Button(self, text = "Back to home",
                         command = lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)


'''To add a new page, create a class of the page as made above, call __init__() method
Add this class to main tuple in the SeaofBTCapp() class.'''

app = SeaofBTCapp()
app.geometry("800x550")
app.config(background = 'light green')
ani = animation.FuncAnimation(f, drawNow, interval = 1000)
app.resizable(height = FALSE, width = FALSE)
app.mainloop()
