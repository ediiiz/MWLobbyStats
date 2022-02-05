import CoDAPI
import OCR
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re
import getAllPlayers
import configparser

images=[]
Lb =[]

root = tk.Tk()
root.resizable(False, False)
root.title("MW: Lobby Stats")


config = configparser.RawConfigParser()
config.read('./config.ini')
details_dict = dict(config.items('INI'))

CoDAPI.cookie_data.append(details_dict["cookie"])
if CoDAPI.check_api_call_cookie() == False:
    messagebox.showerror("Error", "Cookie incorrect! \nCheck your config.ini")
    root.destroy()

if details_dict["tesseractexe"].find("tesseract.exe") < 0:
    messagebox.showerror("Error", "tesseract.exe not selected! \nCheck your config.ini")
    root.destroy()

def addImagesToList():
    for widget in main_frame.winfo_children():
        widget.destroy()
    src_path = filedialog.askopenfilename(initialdir="./Images", title="select image", filetypes=(("Images", "*.png *.jpg"),                                                                                      ("All Files", ".")))
    images.append(src_path)
    for image in images:
        image = re.search("Images/(.*)", image)
        image = (image.group(1))
        label = tk.Label(main_frame, text=image, bg="#121212", fg="white")
        label.pack()


def runOCRfromImageList():
    if images.__len__() == 0 and OCR.usernamesOCR.__len__() == 0:
        messagebox.showerror("Error", "No Images Selected")
    else:
        for image_src in images:
            print(image_src)
            OCR.get_string(image_src)
        # Rahmen Listbox

        frameAusgabe = tk.Frame(master=main_frame_2, bg='#D5E88F')
        #frameAusgabe.place(x=5, y=90, width=400, height=400)
        # Listbox
        listboxNamen = tk.Listbox(master=main_frame_2, selectmode='browse')
        for x in OCR.usernamesOCR:
            listboxNamen.insert('end', x)
        listboxNamen.place(x=20, y=25, width=350, height=350)
        #listboxNamen.bind('<<ListboxSelect>>', verarbeiten)
        # Scroolbar
        yScroll = tk.Scrollbar(master=main_frame_2, orient='vertical')
        yScroll.place(x=350+15, y=25, width=20, height=350)
        listboxNamen.config(yscrollcommand=yScroll.set)
        yScroll.config(command=listboxNamen.yview)
        # Label Text
        labelText = tk.Label(master=frameAusgabe, bg='white')
        labelText.place(x=5, y=5, width=100, height=20)
        displayDone()
        print(OCR.usernamesOCR)

def clearList():
    images.clear()
    for widget in main_frame.winfo_children():
        widget.destroy()
    for widget in b_frame_5.winfo_children():
        widget.destroy()



def getStats():
    if OCR.usernamesOCR.__len__() == 0:
        messagebox.showerror("Error", "First scan an Image")
    else:
        for widget in b_frame_5.winfo_children():
            widget.destroy()
        label = tk.Label(b_frame_5, text="Exporting!", bg="#121212", fg="white")
        label.pack(pady=5)
        for widget in b_frame_5.winfo_children():
            widget.destroy()
        CoDAPI.check_api_call_cookie()
        getAllPlayers.getStats()
        label = tk.Label(b_frame_5, text="Exported!", bg="#121212", fg="white")
        label.pack(pady=5)

def displayDone():
    label = tk.Label(b_frame_5, text="Done!", bg="#121212", fg="white")
    label.pack(pady=5)


canvas = tk.Canvas(root, height=700, width=400, bg="#121212")
canvas.pack()

b_frame = tk.Frame(root, bg="#121212")
b_frame.place(relwidth=0.20, relheight=0.05, relx=0, rely=0.95)
b_frame_2 = tk.Frame(root, bg="#121212")
b_frame_2.place(relwidth=0.20, relheight=0.05, relx=0.20, rely=0.95)
b_frame_3 = tk.Frame(root, bg="#121212")
b_frame_3.place(relwidth=0.20, relheight=0.05, relx=0.4, rely=0.95)
b_frame_4 = tk.Frame(root, bg="#121212")
b_frame_4.place(relwidth=0.20, relheight=0.05, relx=0.6, rely=0.95)
b_frame_5 = tk.Frame(root, bg="#121212")
b_frame_5.place(relwidth=0.20, relheight=0.05, relx=0.8, rely=0.95)
main_frame = tk.Frame(root, bg="#121212")
main_frame.place(relwidth=1, relheight=0.3, relx=0, rely=0)
main_frame_2 = tk.Frame(root, bg="#121212")
main_frame_2.place(relwidth=1, relheight=0.65, relx=0, rely=0.3)

select_src = tk.Button(b_frame, text="Open Images", padx=15, pady=15, fg="white", bg="#121212", command=addImagesToList)
select_src.pack(side="top")

runOCR = tk.Button(b_frame_2, text="Run Scan", padx=15, pady=15, fg="white", bg="#121212", command=runOCRfromImageList)
runOCR.pack(side="top")

clearListbutton = tk.Button(b_frame_3, text="Clear", padx=22, pady=15, fg="white", bg="red", command=clearList)
clearListbutton.pack(side="top")

getStatsButton = tk.Button(b_frame_4, text="Export Stats", padx=15, pady=15, fg="white", bg="green", command=getStats)
getStatsButton.pack(side="top")

frameAusgabe = tk.Frame(master=main_frame_2, bg='#D5E88F')
# frameAusgabe.place(x=5, y=90, width=400, height=400)
# Listbox
listboxNamen = tk.Listbox(master=main_frame_2, selectmode='browse')
for x in OCR.usernamesOCR:
    listboxNamen.insert('end', x)
listboxNamen.place(x=20, y=25, width=350, height=350)
# listboxNamen.bind('<<ListboxSelect>>', verarbeiten)
# Scroolbar
yScroll = tk.Scrollbar(master=main_frame_2, orient='vertical')
yScroll.place(x=350 + 15, y=25, width=20, height=350)
listboxNamen.config(yscrollcommand=yScroll.set)
yScroll.config(command=listboxNamen.yview)
# Label Text
labelText = tk.Label(master=frameAusgabe, bg='white')
labelText.place(x=5, y=5, width=100, height=20)

root.mainloop()