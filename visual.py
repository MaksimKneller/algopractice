import tkinter as tk
from random import randint
from Sorting import selection_sort, insertion_sort
from utils import AlgoType

class VisualSort():

    # main Tk context
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(810, 300))

    def __init__(self, sort):

        # drawing context
        self.canvas = tk.Canvas(self.root, width=810, height=300, bg="white")
        self.canvas.pack()

        self.input = [randint(1,100) for _ in range(50)]
        self.intermediateSorts = []

        if(sort == AlgoType.INSERTION_SORT):
            insertion_sort.run(self.input, self.intermediateSorts)
        elif(sort == AlgoType.SELECTION_SORT):
            selection_sort.run(self.input, self.intermediateSorts)

        self.plotBars()
        self.root.mainloop()


    def plotBars(self):

        # bar drawing settings
        xoffset = 150
        barwidth = 5
        barspacing = 10

        highlightedIndx = self.intermediateSorts[0][0]
        intermediateSort = self.intermediateSorts[0][1]

        self.canvas.delete("all")

        for x in range(len(self.input)):
            barFill = "white"
            if x == highlightedIndx: barFill = "red"

            self.canvas.create_rectangle(xoffset+barspacing*x,200,
                                         xoffset+barspacing*x+barwidth,200-intermediateSort[x],
                                         fill=barFill)

        self.intermediateSorts.pop(0)

        if(self.intermediateSorts): self.root.after(100,self.plotBars)


if __name__ == '__main__':

    v = VisualSort(AlgoType.INSERTION_SORT)

