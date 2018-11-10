# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from tkinter import *
from tkinter import ttk

from neopixel import *
from init_strip import *
# import timer_threading
from led_functions import *

root = Tk()
 
# root properties
root.title("Daya Electric Forest Control Panel")
root.geometry('550x600')


#### TIMER SECTION ####
trow=2          # -2 to 0
tcol=0          # 0 to 6
timer_frame = Frame(root, bd=2, relief="groove", padx=20, pady=20)
timer_frame.pack()

# timer_on_button handler
def timer_on_click():
  timer_status.configure(text="Timer SET")

# timer_off_button handler
def timer_off_click():
  timer_status.configure(text="Timer OFF")

# time entry label
lbl = Label(timer_frame, text="Enter on/off times below")
lbl.grid(row=trow-2, column=tcol+3, columnspan=4)

# timer_on_button properties
timer_on_button = Button(timer_frame, text="Start Timer", command=timer_on_click)
timer_on_button.grid(row=trow+0, column=tcol+0)

# timer_off_button properties
timer_off_button = Button(timer_frame, text="Stop Timer", command=timer_off_click)
timer_off_button.grid(row=trow+0, column=tcol+1)

# timer status properties
timer_status = Label(timer_frame, text="Timer OFF", font=("Arial Bold", 30))
timer_status.grid(row=trow+1, column=tcol+0, columnspan=2)

# timer input properties
on_hour = Spinbox(timer_frame, from_=0, to=23, width=5)
on_hour.grid(row=trow+0, column=tcol+3)
lbl = Label(timer_frame, text="hour")
lbl.grid(row=trow-1, column=tcol+3)

on_min = Spinbox(timer_frame, from_=0, to=59, width=5)
on_min.grid(row=trow+0, column=tcol+4)
lbl = Label(timer_frame, text="minute")
lbl.grid(row=trow-1, column=tcol+4)

off_hour = Spinbox(timer_frame, from_=0, to=23, width=5)
off_hour.grid(row=trow+0, column=tcol+5)
lbl = Label(timer_frame, text="hour")
lbl.grid(row=trow-1, column=tcol+5)

off_min = Spinbox(timer_frame, from_=0, to=59, width=5)
off_min.grid(row=trow+0, column=tcol+6)
lbl = Label(timer_frame, text="minute")
lbl.grid(row=trow-1, column=tcol+6)



#### SLIDER SECTION ####
srow=0          # 0 to 2
scol=0          # 0 to 0
slider_frame = Frame(root, bd=2, relief="groove", padx=20, pady=20)
slider_frame.pack()

# red slider
red = Scale(slider_frame, from_=0, to=255, orient="horizontal")
red.grid(row=srow+0, column=scol+1, columnspan=2)
lbl = Label(slider_frame, text="Red")
lbl.grid(row=srow+0, column=scol+0)

# green slider
green = Scale(slider_frame, from_=0, to=255, orient="horizontal")
green.grid(row=srow+1, column=scol+1, columnspan=2)
lbl = Label(slider_frame, text="Green")
lbl.grid(row=srow+1, column=scol+0)

# blue slider
blue = Scale(slider_frame, from_=0, to=255, orient="horizontal")
blue.grid(row=srow+2, column=scol+1, columnspan=2)
lbl = Label(slider_frame, text="Blue")
lbl.grid(row=srow+2, column=scol+0)

# apply_slider handler
def apply_slider_click():
  custom_on(strip, red.get(), green.get(), blue.get())

# apply_slider properties
apply_slider = Button(slider_frame, text="Apply Slider", command=apply_slider_click)
apply_slider.grid(row=srow+1, column=scol+3, columnspan=2)



#### PRESET SECTION ####
row=0          # 0 to 2
col=0          # 0 to 0
preset_frame = Frame(root, bd=2, relief="groove", padx=20, pady=20)
preset_frame.pack()

# preset dropdown
preset_drop = ttk.Combobox(preset_frame)
preset_drop['values']=("dark and moody", "sultry dancing", "awake evening")
preset_drop.current(1)
preset_drop.grid(row=row+0, column=col+0)

# apply_preset click handler
def apply_preset_click():
  # check value, call function by same name
  val = preset_drop.get()
  preset_lookup = {"dark and moody": dark_and_moody, "sultry dancing": sultry_dancing, "awake evening": awake_evening}
  preset_lookup[val](strip)

# apply_preset button
apply_preset = Button(preset_frame, text="Apply Preset", command=apply_preset_click)
apply_preset.grid(row=row+0, column=col+1)

#### MASTER TOGGLE SECTION ####
row=0          # 0 to 2
col=0          # 0 to 0
master_toggle_frame = Frame(root, bd=2, relief="groove", padx=20, pady=20)
master_toggle_frame.pack()

# master_on click handler
def master_on_click():
  all_on(strip)

# master_off click handler
def master_off_click():
  all_off(strip)

# master_on button properties
master_on = Button(master_toggle_frame, text="Lights ON", command=master_on_click)
master_on.grid(row=row+0, column=col+0)

# master_off button properties
master_off = Button(master_toggle_frame, text="Lights OFF", command=master_off_click)
master_off.grid(row=row+0, column=col+1)


 
root.mainloop()