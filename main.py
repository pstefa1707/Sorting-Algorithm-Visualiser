import asyncio
from random import shuffle
import tkinter as tk
import sorter
import traceback
import math

class App(tk.Tk):

    def __init__(self, loop, interval=1/90):
        super().__init__()
        self.title("Sorting Algorithm Visualiser - Made by Paras")
        self.minsize(800, 600)
        self.interval = interval
        self.loop = loop
        self.size = (800, 500)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.lines = []
        self.generate_lines(300)
        self.tasks = []
        self.window_init()
        self.tasks.append(loop.create_task(self.updater()))
        
    async def updater(self):
        while True:
            if self.view.get() == "Vertical Lines":
                self.draw_lines()
            elif self.view.get() == "Circle":
                self.draw_circle()
            elif self.view.get() == "Pyramid":
                self.draw_pyramid()
            self.update()
            if self.tasks[-1].done():
                self.start_stop()
            await asyncio.sleep(self.interval)
            
    def generate_lines(self, n):
        diff = 1000/int(n)
        self.lines = [i*diff for i in range(int(n))]
        shuffle(self.lines)
        
    def draw_lines(self):
        self.canvas.delete("all")
        for i in enumerate(reversed(self.lines)):
            h = (i[1] / 1000) * self.canvas.winfo_height()
            colour = sorter.hsv2hex((i[1]/1000)*360, 1, 1)
            self.canvas.create_line(i[0] * (self.canvas.winfo_width()/len(self.lines)), self.canvas.winfo_height(), i[0] * (self.canvas.winfo_width()/len(self.lines)), self.canvas.winfo_height() - h, fill=colour)
            
    def draw_circle(self):
        self.canvas.delete("all")
        radians_per_line = (2*math.pi)/len(self.lines)
        if self.canvas.winfo_height() > self.canvas.winfo_width():
            radius = self.canvas.winfo_width()/2
        else:
            radius = self.canvas.winfo_height()/2
        for i in enumerate(self.lines):
            colour = sorter.hsv2hex((i[1]/1000)*360, 1, 1)
            self.canvas.create_line(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, math.cos(i[0]*radians_per_line) * radius + (self.canvas.winfo_width()/2), math.sin(i[0]*radians_per_line) * radius + (self.canvas.winfo_height()/2), fill=colour, width=2)
        
    def draw_pyramid(self):
        self.canvas.delete('all')
        height_per_line = self.canvas.winfo_height()/len(self.lines)
        for i in enumerate(self.lines):
            width = (i[1]/1000) * self.canvas.winfo_width()
            colour = sorter.hsv2hex((i[1]/1000)*360, 1, 1)
            self.canvas.create_line(self.canvas.winfo_width()/2 - width/2, i[0] * height_per_line, self.canvas.winfo_width()/2 + width/2, i[0] * height_per_line, fill=colour)
        
    def start_stop(self):
        if self.control["text"] == "Start":
            self.control["text"] = "Pause"
            self.nLines["state"] = "disabled"
            if sorter.is_sorted(self.lines):
                self.generate_lines(self.nLines.get())
            if self.sort_type.get() == "Bubble Sort": self.tasks.append(loop.create_task(sorter.bubble_sort(self.lines)))
            elif self.sort_type.get() == "Insertion Sort": self.tasks.append(loop.create_task(sorter.insertion_sort(self.lines)))
            elif self.sort_type.get() == "Selection Sort": self.tasks.append(loop.create_task(sorter.selection_sort(self.lines)))
            elif self.sort_type.get() == "Pancake Sort": self.tasks.append(loop.create_task(sorter.pancake_sort(self.lines)))
            elif self.sort_type.get() == "Shell Sort": self.tasks.append(loop.create_task(sorter.shell_sort(self.lines)))
            else: self.tasks.append(loop.create_task(sorter.cocktail_sort(self.lines)))
            
        elif self.control["text"] == "Pause":
            self.tasks[-1].cancel()
            self.tasks.pop(-1)
            self.control["text"] = "Start"
            self.nLines["state"] = "active"

    def window_init(self):
        self.canvas = tk.Canvas(master=self, height=self.size[1], width=self.size[0])
        self.canvas['background'] = 'black'
        self.canvas.pack(fill=tk.BOTH, expand=1)
        controls = tk.Frame(self)
        controls.pack(fill=tk.BOTH, side=tk.BOTTOM)
        controls.columnconfigure(2, weight=1)
        self.nLines = tk.Scale(master=controls, resolution=10, from_=100, to_=600, orient=tk.HORIZONTAL, length=300, command=self.generate_lines)
        self.nLines.set(300)
        self.nLines.grid(column=1, row=0, sticky=tk.N)
        tk.Label(controls, text="Number of lines: ").grid(column=0, row=0, sticky=tk.S, padx=5)
        OptionList = [
        "Bubble Sort",
        "Insertion Sort",
        "Selection Sort",
        "Pancake Sort",
        "Shell Sort",
        "Cocktail Sort"
        ]
        ViewList = [
            "Vertical Lines",
            "Pyramid",
            "Circle"
        ]
        self.view = tk.StringVar(self)
        self.view.set(ViewList[0])
        self.sort_type = tk.StringVar(self)
        self.sort_type.set(OptionList[0])
        self.viewOpt = tk.OptionMenu(controls, self.view, *ViewList)
        self.viewOpt.grid(column=3, row=1, sticky=tk.S)
        self.viewOpt['width'] = 50
        self.opt = tk.OptionMenu(controls, self.sort_type, *OptionList)
        self.opt['width'] = 50
        self.opt.grid(column=3, row=0, sticky=tk.S)
        self.control = tk.Button(master=controls, text="Start", command=self.start_stop)
        self.control.grid(column=0, row=1, columnspan=3, sticky=tk.EW)
        
    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = App(loop)
    loop.run_forever()
    loop.close()