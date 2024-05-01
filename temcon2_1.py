#!/usr/bin/env python
from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

#Main Window
window = tk.Tk()
window.title("TemCon 2")
window.geometry("310x350")
window.configure(background="burlywood")
style=ttk.Style()   # ttk Style Library
menu = tk.Menu(window, background="antiquewhite")
style.theme_use("clam")


# ================================================================================================================================================================
# ================================================= Start of Live Conversion Styling =============================================================================
# ================================================================================================================================================================

# Frames
# ======
style.configure("temconLight.TFrame",  relief=tk.FLAT,takefocus=False, background="burlywood")
style.configure("temconDark.TFrame",  relief=tk.FLAT,takefocus=False, background="#519fd2")

style.configure("convertedFrameLight.TFrame",  relief=tk.FLAT, takefocus=False, pady=5, background="#00ffff")
style.configure("convertedFrameDark.TFrame",  relief=tk.FLAT, takefocus=False, background="#ffff00")

style.configure("lawfulLight.TFrame",  relief=tk.FLAT,takefocus=False, background="#ffe4c4")
style.configure("lawfulDark.TFrame",  relief=tk.FLAT,takefocus=False, background="burlywood")

style.configure("tempResponseFrameLight.TFrame",  relief=tk.FLAT,takefocus=False, pady=5, background="#00ffff")
style.configure("tempResponseFrameDark.TFrame",  relief=tk.FLAT,takefocus=False, background="burlywood")

style.configure("scalesResponseFrameLight.TFrame", relief=tk.FLAT, takefocus=False,  ipady=5, highlightthickness=0,bg="#00ffff", fg="#347898", background="#00ffff", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("scalesResponseFrameDark.TFrame", relief=tk.FLAT, takefocus=False,  highlightthickness=0,  bg="#347898", fg="#00ffff", background="burlywood", foreground="burlywood", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("liveLight.TFrame", relief=tk.FLAT, takefocus=False, highlightthickness=0,bg="#00ffff", fg="#347898", background="burlywood", foreground="#4c7588", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("liveDark.TFrame", relief=tk.FLAT, takefocus=False,  highlightthickness=0,  bg="#347898", fg="#00ffff", background="#ffff00", foreground="#70c5c2", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("weatherFrameLight.TFrame", relief=tk.FLAT, takefocus=False, bd=0, highlightthickness=5,bg="#00ffff", fg="#347898", background="#4c7588", foreground="#1e90ff", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("weatherFrameDark.TFrame", relief=tk.FLAT, takefocus=False, bd=0, highlightthickness=5,  bg="#347898", fg="#00ffff", background="burlywood", foreground="#4c7588", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("heroFrameLight.TFrame", relief=tk.FLAT, takefocus=False,  highlightthickness=0,bg="#00ffff", fg="#347898", background="#4c7588", foreground="#1e90ff", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("heroFrameDark.TFrame", relief=tk.FLAT, takefocus=False,  highlightthickness=0,  bg="#347898", fg="#00ffff", background="#559492", foreground="#4c7588", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

# Labels
# ======
style.configure("scalesLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#347898",  activeforeground="#00ffff", font=("Times New Roman", 11, "bold"), background="#70c5c2", foreground="#347898", highlightbackground='#70c5c2', highlightcolor='#deb887', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("scalesDark.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"), background="#347898", foreground="#70c5c2",  highlightbackground='#deb887', highlightcolor='#70c5c2', highlightthickness=3, takefocus=True, justify="center", anchor="center")

style.configure("temconLight.TLabel", font=("Times New Roman", 12, "bold"), background="#bb9f6a", foreground="#70c5c2", highlightbackground='#ffa500',  highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("temconDark.TLabel", font=("Times New Roman", 12, "bold"), background="#70c5c2", foreground="#bb9f6a", highlightbackground='#deb887',  highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("weatherFrameLabelLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#559492", foreground="#70c5c2", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("weatherFrameLabelDark.TLabel",relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#70c5c2", foreground="#559492", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("heroFrameLabelLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#559492", foreground="#07597f", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("heroFrameLabelDark.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#4f788a", foreground="#00ffff", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("convertedScaleLableFrameLight.TLabel", relief=tk.FLAT, takefocus=False, ipadx=5, ipady=10, bg="#00ffff", fg="#347898", bd=5, highlightthickness=5, background="#347898", foreground="burlywood", highlightbackground='#ffff00', highlightcolor='#fb8604', anchor="center")
style.configure("convertedScaleLableFrameDark.TLabel", relief=tk.FLAT, takefocus=False,  ipadx=5, ipady=10, bg="#70c5c2", fg="#00ffff", bd=5, highlightthickness=5,  background="#fb8604", foreground="#ffff00", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("livedescLabelLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#4c7588", foreground="#6b9ac9", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("livedescLabelDark.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#fb8604", foreground="#ffff00", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("livedescLabelLight1.TLabel", relief=tk.FLAT, takefocus=False, font=("Times New Roman", 12, "bold"), highlightthickness=5 ,bg="#00ffff", fg="#347898", background="#347898", foreground="#70c5c2", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("livedescLabelDark1.TLabel", relief=tk.FLAT, takefocus=False, font=("Times New Roman", 12, "bold"), highlightthickness=5,  bg="#347898", fg="#00ffff", background="#ffff00", foreground="#fb8604", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("lawfulLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("lawfulDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#5c3608", foreground="#ffe4c4", highlightbackground='#deb887', pady=10, highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("tcttkLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("tcttkDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#5c3608", foreground="#ffe4c4", highlightbackground='#deb887', pady=10, highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("convertedScaleLableFrameLableLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"),  ipadx=5, ipady=10, background="#4f788a", foreground="#00ffff", highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True)
style.configure("convertedScaleLableFrameLableDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), ipadx=5, ipady=10, background="#fb8604", foreground="#ffff00",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True)

style.configure("privacyLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#70c5c2", foreground="#347898", highlightbackground='##ffebcd', highlightcolor='#48d1cc', anchor="center")
style.configure("privacyDark.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#347898", foreground="#70c5c2", highlightbackground='#48d1cc', highlightcolor='#ffebcd', anchor="center")

style.configure("temconConToolLight.TLabel", font=("Times New Roman", 11, "bold"), relief=tk.SUNKEN, takefocus=False, bd=(5, 0, 5, 0), highlightthickness=5,bg="#00ffff", fg="#347898", background="#4f788a", foreground="#00ffff", highlightbackground='##ffebcd', highlightcolor='#48d1cc', anchor="center")
style.configure("temconConToolDark.TLabel", font=("Times New Roman", 11, "bold"), relief=tk.SUNKEN, takefocus=False, bd=(5, 0, 5, 0), highlightthickness=5,  bg="#347898", fg="#00ffff", background="#fb8604", foreground="#ffff00",highlightbackground='#48d1cc', highlightcolor='#ffebcd', anchor="center")

# Scales Choice Option Menu
style.configure("ScalesChoiceLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#4f788a",  activeforeground="#00ffff", font=("Times New Roman", 11, "bold"),  background="#4f788a", foreground="#00ffff", highlightbackground='#4f788a', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("ScalesChoiceDark.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"),  background="#fb8604", foreground="#ffff00",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")

style.configure("selectedScaleLableFrameLight.TLabel", relief=tk.SUNKEN, takefocus=False, ipadx=5, ipady=5, bg="#8fbc8f", fg="#347898", bd=5, highlightthickness=5, background="#ffff00", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#fb8604', anchor="center")
style.configure("selectedScaleLableFrameDark.TLabel", relief=tk.SUNKEN, takefocus=False,  ipadx=5, ipady=5, bg="#70c5c2", fg="#00ffff", bd=5, highlightthickness=5,  background="#347898", foreground="#ffff00", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")
style.configure("selectedScaleLableFrameLabelLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#347898",  activeforeground="#00ffff", font=("Times New Roman", 11, "bold"),  background="#00ffff", foreground="#0a3f7c", highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("selectedScaleLableFrameLabelDark.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"),  background="#4f788a", foreground="#00ffff",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("convScalesChoiceLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="#4f788a", foreground="#00ffff", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("convertedScaleSelected.TLabel",relief=tk.RAISED, direction="below", activebackground="#ffff00",  activeforeground="#3d9fe0", font=("Times New Roman", 11, "bold"),  background="#70d38e", foreground="#008000",  highlightbackground='#48d1cc', highlightcolor='#3d9fe0', highlightthickness=3, takefocus=True, justify="center", anchor="center")
# Scales Choice Option Menu
style.configure("tested.TLabel",relief=tk.RAISED, direction="below", font=("Times New Roman", 14, "bold"), activebackground="#4f788a",  activeforeground="#00ffff",  background="#4f788a", foreground="#00ffff", highlightbackground='#4f788a', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("ScalesChoiceDark.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"),  background="#fb8604", foreground="#ffff00",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")


# Buttons
# =======
style.configure("scaleSetButtonLight.TButton", relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#4f788a", foreground="#00ffff", ipady=2, ipadx=5, highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("scaleSetButtonDark.TButton", relief=tk.RAISED, font=("Times New Roman", 11, "bold"),  background="#fb8604", foreground="#ffff00", ipady=2, ipadx=5,   highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")

# Entry
# =====
style.configure("setTempLight.TEntry", background="#4f788a", foreground="#00ffff", insertionwidth=5, insertcolor="#00ffff", font=("Times New Roman", 14, "bold"), selectborderwidth=2, cursor="umbrella", relief=tk.SUNKEN, selectbackground="#99cfe7", selectforeground="#07597f", takefocus=True, fieldbackground="#347898", justify=CENTER, bordercolor="#5c3608")
style.configure("setTempDark.TEntry",  background="#fb8604", foreground="#ffff00", insertionwidth=5, insertcolor="#5c3608", font=("Times New Roman", 14, "bold"), selectborderwidth=2, cursor="umbrella", relief=tk.SUNKEN, selectbackground="#f3e1c9", selectforeground="#ec8c15", takefocus=True, fieldbackground="#fb8604", justify=CENTER, bordercolor="#5c3608")

# ================================================================================================================================================================
# ================================================= End of Live Conversion Styling ===============================================================================
# ================================================================================================================================================================

# ================================================================================================================================================================
# ================================================= Start of Manual Conversion Styling ===========================================================================
# ================================================================================================================================================================
# 1
def ChangeManconv():
    styles = manconv_frame.cget("style")
    if styles == "weatherFrameDark.TFrame":
            temperature_setting_frame.configure(style="weatherFrameLight.TFrame")
    elif styles == "weatherFrameLight.TFrame":
            temperature_setting_frame.configure(style="weatherFrameDark.TFrame")
            breakpoint


# 2
def ChangeTempFrame():
    styles = temperature_setting_frame.cget("style")
    if styles == "convertedFrameDark.TFrame":
            temperature_setting_frame.configure(style="convertedFrameLight.TFrame")
    elif styles == "convertedFrameLight.TFrame":
            temperature_setting_frame.configure(style="convertedFrameDark.TFrame")
            breakpoint


# 3
def changeScales():
    styles = scales.cget("style")
    if styles =="scalesDark.TLabel":
            scales.configure(style="scalesLight.TLabel")
    elif styles == "scalesLight.TLabel":
            scales.configure(style="scalesDark.TLabel")
            breakpoint


# 4
def changeSSB():
    styles = scaleSet_button.cget("style")
    if styles == "scaleSetButtonDark.TButton":
            scaleSet_button.configure(style="scaleSetButtonLight.TButton")
    elif styles == "scaleSetButtonLight.TButton":
            scaleSet_button.configure(style="scaleSetButtonDark.TButton")
            breakpoint


# 5
def changeScaleTemp():
    styles = scaleTemp.cget("style")
    if styles == "setTempDark.TEntry":
            scaleTemp.configure(style="setTempLight.TEntry")
    elif styles == "setTempLight.TEntry":
            scaleTemp.configure(style="setTempDark.TEntry")
            breakpoint


# 6
def changeSCL():
    styles = scaleChoice_label.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
            scaleChoice_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            scaleChoice_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 7
def changeSRF():
    styles = scales_response_frame.cget("style")
    if styles == "scalesResponseFrameDark.TFrame":
            scales_response_frame.configure(style="scalesResponseFrameLight.TFrame")
    elif styles == "scalesResponseFrameLight.TFrame":
            scales_response_frame.configure(style="scalesResponseFrameDark.TFrame")
            breakpoint


# 8
def changeRLF1():
    styles = converted_scale_one_labelframe.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_one_labelframe.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint

# 9
def changeRLF2():
    styles = converted_scale_two_labelframe.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_two_labelframe.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_two_labelframe.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 10
def changeRLF3():
    styles = converted_scale_three_labelframe.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_three_labelframe.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_three_labelframe.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 11
def changeRLF4():
    styles = converted_scale_four_labelframe.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_four_labelframe.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_four_labelframe.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint


# 12
def changeResponse1():
    styles = converted_scale_one_labelframe_label.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 13
def changeResponse2():
    styles = converted_scale_two_labelframe_label.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 14
def changeResponse3():
    styles = converted_scale_three_labelframe_label.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 15
def changeResponse4():
    styles = converted_scale_four_labelframe_label.cget("style")
    if styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
    elif styles == "convertedScaleLableFrameLableLight.TLabel":
            converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
            breakpoint



# 16
def changeResponseF():
    styles = converted_scales_frame.cget("style")
    if styles == "scalesResponseFrameDark.TFrame":
                converted_scales_frame.configure(style="scalesResponseFrameLight.TFrame")
    elif styles == "scalesResponseFrameLight.TFrame":
            converted_scales_frame.configure(style="scalesResponseFrameDark.TFrame")
            breakpoint



# ================================================================================================================================================================
# ================================================= End of Manual Conversion Styling =============================================================================
# ================================================================================================================================================================


# Apps Menu to Open and Close TempCalc and to Exit the Program
apps_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
apps_menu.add_command(label = "Live", command=lambda: showLive())
apps_menu.add_command(label = "Manual", command=lambda: showManual())
apps_menu.add_command(label = "Home", command=lambda: getMain())
apps_menu.add_command(label = "Exit", command = lambda: quit_main())
menu.add_cascade(label ="Apps", menu = apps_menu, foreground="antiquewhite", background="burlywood", activebackground="antiquewhite", activeforeground="burlywood")
# info Menu to display the info page
info_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
info_menu.add_command(label = "Lawful Notice", command=lambda: get_Lawful())
info_menu.add_command(label = "MIT License", command=lambda: open_mit_window())
info_menu.add_command(label = "Contact", command=lambda: open_contact_window())
info_menu.add_command(label = "Donate", command=lambda: open_donate_window())
menu.add_cascade(label ="Info", menu = info_menu, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
# Styles Menu to choose between Light and Dark
#styles_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
#styles_menu.add_command(label = "Flip Style", command=lambda: changeStyle())
#menu.add_cascade(label ="Styles", menu = styles_menu,  activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")

# List of Function Calls

temp_var =BooleanVar()
temp_var = False

global choice
global temp


def display_selected(choice):
        choice = scale.get()
        scale.set(choice)
        scaleTemp.delete(0, END)
        clearManualTable()
        breakpoint

def store_selected(choice):
        choice = scale.get()
        scale.set(choice)
        scaleTemp.delete(0, END)
        clearLiveTable()
        breakpoint
        

def getMain():
        window.geometry("313x359")
        clearLiveTable()
        liveconv_frame.grid_forget()
        manconv_frame.grid_forget()
        lawful_privacy_frame.grid_forget()
        hero_frame.grid(row=1, column=0, columnspan=4)
        temcon_frame.grid(row=1, column=0, columnspan=4)
        breakpoint



def showLive():
        window.geometry("432x218")
        clearLiveTable()
        clearLiveWeather()
        manconv_frame.grid_forget()
        live_report_frame.grid_forget()
        temcon_frame.grid_forget()
        hero_frame.grid_forget()
        lawful_privacy_frame.grid_forget()
        liveconv_frame.grid(row=1, column=0, columnspan=4)
        breakpoint



def showManual():
        window.geometry("282x292")
        clearManualTable()
        clearManualWeather()
        liveconv_frame.grid_forget()
        weather_report_frame.grid_forget()
        temcon_frame.grid_forget()
        hero_frame.grid_forget()
        lawful_privacy_frame.grid_forget()
        manconv_frame.grid(row=1, column=0, columnspan=4)
        breakpoint


def hideManual():
        manconv_frame.grid_forget()
        breakpoint


def get_Lawful():
        window.geometry("285x322")
        temcon_frame.grid_forget()
        manconv_frame.grid_forget()
        hero_frame.grid_forget()
        #liveconv_frame.grid_forget()
        lawful_privacy_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        breakpoint



def hideLawful():
        lawful_privacy_frame.grid_forget()
        window.geometry("310x320")
        #liveconv_frame.grid_forget()
        hero_frame.grid(row=1, column=0, columnspan=4)
        temcon_frame.grid(row=1, column=0, columnspan=4)
        breakpoint



# Apps Menu Item to Exit the Program
def quit_main():
        window.quit()
        breakpoint



def clearLiveTable():
        converted_temps_one_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        converted_temps_two_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        converted_temps_three_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        converted_temps_four_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        breakpoint


def clearManualTable():
        converted_scale_one_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        converted_scale_two_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        converted_scale_three_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        converted_scale_four_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        city_search_entry.delete(0, END)
        breakpoint



def clearLiveWeather():
        convScale.set(convScaleSet[0])
        live_city_temp_entry.delete(0, END)
        live_icon_label.pack_forget()
        live_city_label.configure(style="livedesclLabelLight.TLabel", text="", anchor="center", wraplength=100)
        live_desc_frame_label.configure(style="livedesclLabelLight.TLabel", text= "", anchor="center")
        live_temperature_label.configure(style="livedesclLabelLight.TLabel", font=("Times New Romant", 30, "bold"), text= "", anchor="center")
        breakpoint


def clearManualWeather():
        scaleTemp.delete(0, END)
        scale.set(scaleSet[0])
        weather_icon_label.pack_forget()
        city_label.configure(style="livedesclLabelDark.TLabel", text="", anchor="center", wraplength=100)
        description_frame_label.configure(style="livedesclLabelDark.TLabel", text= "", anchor="center")
        temperature_label.configure(style="livedesclLabelDark.TLabel", font=("Times New Romant", 30, "bold"), text= "", anchor="center")
        breakpoint


# 17
def changeTemconProg():
        styles = temcon_program_frame.cget("style")
        if styles == "liveLight.TFrame":
                        temcon_program_frame.configure(style="liveDark.TLabel")
        elif styles == "liveDark.TFrame":
                        temcon_program_frame.configure(style="liveLight.TFrame")
                        breakpoint



# 18
def changeTUP():
        styles = tup_frame.cget("style")
        if styles == "liveLight.TFrame":
                        tup_frame.configure(style="liveDark.TFrame")
        elif styles == "liveDark.TFrame":
                        tup_frame.configure(style="liveLight.TFrame")
                        breakpoint



# 19
def changeTUPLabel():
        styles = tup_label_title.cget("style")
        if styles == "temconConToolLight.TLabel":
                tup_label_title.configure(style="temconConToolDark.TLabel")
        elif styles == "temconConToolDark.TLabel":
                tup_label_title.configure(style="temconConToolLight.TLabel")
                breakpoint



# 20
def changeTemcon():
        styles =temcon_frame.cget("style")
        if styles == "temconLight.TFrame":
                temcon_frame.configure(style="temconDark.TFrame")
        elif styles == "temconDark.TFrame":
                temcon_frame.configure(style="temconLight.TFrame")
                breakpoint



# 21
def ChangeTemconLabelframe():
        styles = temcon_labelframe.cget("style")
        if styles == "programFrameLight.TLabel":
                temcon_labelframe.configure(style="programFrameDark.TLabel")
        elif styles == "programFrameDark.TLabel":
                temcon_labelframe.configure(style="programFrameLight.TLabel")
                breakpoint



# 22
def ChangeTemconLabelFrameLabel():
        styles = temcon_labelframe_label.cget("style")
        if styles == "temconLight.TLabel":
                temcon_labelframe_label.configure(style="temconDark.TLabel")
        elif styles == "temconDark.TLabel":
                temcon_labelframe_label.configure(style="temconLight.TLabel")
                breakpoint



# 23
def ChangeTemconLogoLabel():
        styles = temcon_logo_label.cget("style")
        if styles == "temconLight.TLabel":
                temcon_logo_label.configure(style="temconDark.TLabel")
        elif styles == "temconDark.TLabel":
                temcon_logo_label.configure(style="temconLight.TLabel")
                breakpoint



# 24
def ChangeWeatherLabelframe():
        styles = weather_labelframe.cget("style")
        if styles == " weatherFrameLabelLight.TLabel":
                weather_labelframe.configure(style=" weatherFrameLabelDark.TLabel")
        elif styles == " weatherFrameLabelDark.TLabel":
                weather_labelframe.configure(style=" weatherFrameLabelLight.TLabel")
                breakpoint



# 25
def ChangeWeatherLabelframeLabel():
        styles = weather_labelframe_label.cget("style")
        if styles == " weatherFrameLabelLight.TLabel":
                weather_labelframe_label.configure(style=" weatherFrameLabelDark.TLabel")
        elif styles == " weatherFrameLabelDark.TLabel":
                weather_labelframe_label.configure(style=" weatherFrameLabelLight.TLabel")
                breakpoint



# 26
def ChangeWeatherLogoLabel():
        styles = weather_logo_label.cget("style")
        if styles == "temconLight.TLabel":
                weather_logo_label.configure(style="temconDark.TLabel")
        elif styles == "temconDark.TLabel":
                weather_logo_label.configure(style="temconLight.TLabel")
                breakpoint



# 27
def changeHeroFrame():
        styles = hero_frame.cget("style")
        if styles == "heroFrameLight.TFrame":
                hero_frame.configure(style="heroFrameDark.TFrame")
        elif styles == "heroFrameDark.TFrame":
                hero_frame.configure(style="heroFrameLight.TFrame")
                breakpoint



# 28
def changeHeroLabel():
        styles = hero_frame_label.cget("style")
        if styles == "heroFrameLabelLight.TLabel":
                hero_frame_label.configure(style="heroFrameLabelDark.TLabel")
        elif styles == "heroFrameLabelDark.TLabel":
                hero_frame_label.configure(style="heroFrameLabelLight.TLabel")
                breakpoint



# 29
def changeFeedback():
        styles = feedback_frame.cget("style")
        if styles == "heroFrameLight.TFrame":
                feedback_frame.configure(style="heroFrameDark.TFrame")
        elif styles == "heroFrameDark.TFrame":
                feedback_frame.configure(style="heroFrameLight.TFrame")
                breakpoint



# 30
def changeDSSLogo():
        styles = dss_logo_label.cget("style")
        if styles == "heroFrameLabelLight.TLabel":
                dss_logo_label.configure(style="heroFrameLabelDark.TLabel")
        elif styles == "heroFrameLabelDark.TLabel":
                dss_logo_label.configure(style="heroFrameLabelLight.TLabel")
                breakpoint



# 31
def changeFeedbackLabel():
        styles = feedback_frame_label.cget("style")
        if styles == "heroFrameLabelLight.TLabel":
                feedback_frame_label.configure(style="heroFrameLabelDark.TLabel")
        elif styles == "heroFrameLabelDark.TLabel":
                feedback_frame_label.configure(style="heroFrameLabelLight.TLabel")
                breakpoint



# 32
def changeTRF():
        styles = temp_response_frame.cget("style")
        if styles == "tempResponseFrameLight.TFrame":
                temp_response_frame.configure(style="tempResponseFrameDark.TFrame")
        elif styles == "tempResponseFrameDark.TFrame":
                temp_response_frame.configure(style="tempResponseFrameLight.TFrame")
                breakpoint



# 33
def changeDesc():
        styles = live_desc_frame_label.cget("style")
        if styles == "livedescLabelLight1.TLabel":
                live_desc_frame_label.configure(style="livedescLabelDark1.TLabel")
        elif styles == "livedescLabelDark1.TLabel":
                live_desc_frame_label.configure(style="livedescLabelLight1.TLabel")
                breakpoint



# 34 
def changeCity():
        styles = live_city_label.cget("style")
        if styles == "livedescLabelLight1.TLabel":
                live_city_label.configure(style="livedescLabelDark1.TLabel")
        elif styles == "livedescLabelDark1.TLabel":
                live_city_label.configure(style="livedescLabelLight1.TLabel")
                breakpoint



# 35
def changeLiveTemp():
        styles = live_temperature_label.cget("style")
        if styles == "livedescLabelLight.TLabel":
                live_temperature_label.configure(style="livedescLabelDark.TLabel")
        elif styles == "livedescLabelDark.TLabel":
                live_temperature_label.configure(style="livedescLabelLight.TLabel")
                breakpoint


 
# 36
def changeTempIcon():
        styles = live_icon_label.cget("style")
        if styles == "livedescLabelLight.TLabel":
                live_icon_label.configure(style="livedescLabelDark.TLabel")
        elif styles == "livedescLabelDark.TLabel":
                live_icon_label.configure(style="livedescLabelLight.TLabel")
                breakpoint



# 37
def ChangeTempFrame():
        styles = temp_frame.cget("style")
        if styles == "convertedFrameLight.TFrame":
                temp_frame.configure(style="convertedFrameDark.TFrame")
        elif styles == "convertedFrameDark.TFrame":
                temp_frame.configure(style="convertedFrameLight.TFrame")
                breakpoint



# 38
def ChangeConvBtn():
        styles = cityButton_frame.cget("style")
        if styles == "convertedFrameLight.TFrame":
                cityButton_frame.configure(style="convertedFrameDark.TFrame")
        elif styles == "convertedFrameDark.TFrame":
                cityButton_frame.configure(style="convertedFrameLight.TFrame")
                breakpoint



# 39
def ChangeCityDescLabel():
        styles = city_description_label.cget("style")
        if styles == "convertedScaleLableFrameLight.TLabel":
                city_description_label.configure(style="convertedScaleLableFrameDark.TLabel")
        elif styles == "convertedScaleLableFrameDark.TLabel":
                city_description_label.configure(style="convertedScaleLableFrameLight.TLabel")
                breakpoint



# 40
def changeLiveCityTemp():
        styles = live_city_temp_entry.cget("style")
        if styles == "setTempLight.TEntry":
                live_city_temp_entry.configure(style="setTempDark.TEntry")
        elif styles == "setTempDark.TEntry":
                live_city_temp_entry.configure(style="setTempLight.TEntry")
                breakpoint



# 41
def changeLiveCityBtn():
        styles = live_city_Search_button.cget("style")
        if styles == "scaleSetButtonLight.TButton":
                live_city_Search_button.configure(style="scaleSetButtonDark.TButton")
        elif styles == "scaleSetButtonDark.TButton":
                live_city_Search_button.configure(style="scaleSetButtonLight.TButton")
                breakpoint



# 42
def changeConvTempFrame():
        styles = converted_temps_frame.cget("style")
        if styles == "scalesResponseFrameLight.TFrame":
                converted_temps_frame.configure(style="scalesResponseFrameDark.TFrame")
        elif styles == "scalesResponseFrameDark.TFrame":
                converted_temps_frame.configure(style="scalesResponseFrameLight.TFrame")
                breakpoint



# 43
def changeLiveResponseFrame1():
        styles = converted_temps_one_labelframe.cget("style")
        if styles == "convertedScaleLableFrameLight.TLabel":
                converted_temps_one_labelframe.configure(style="convertedScaleLableFrameDark.TLabel")
        elif styles == "convertedScaleLableFrameDark.TLabel":
                converted_temps_one_labelframe.configure(style="convertedScaleLableFrameLight.TLabel")
                breakpoint



# 44
def changeLiveResponseFrame2():
        styles = converted_temps_two_labelframe.cget("style")
        if styles == "convertedScaleLableFrameLight.TLabel":
                converted_temps_two_labelframe.configure(style="convertedScaleLableFrameDark.TLabel")
        elif styles == "convertedScaleLableFrameDark.TLabel":
                converted_temps_two_labelframe.configure(style="convertedScaleLableFrameLight.TLabel")
                breakpoint



# 45
def changeLiveResponseFrame3():
        styles = converted_temps_three_labelframe.cget("style")
        if styles == "convertedScaleLableFrameLight.TLabel":
                converted_temps_three_labelframe.configure(style="convertedScaleLableFrameDark.TLabel")
        elif styles == "convertedScaleLableFrameDark.TLabel":
                converted_temps_three_labelframe.configure(style="convertedScaleLableFrameLight.TLabel")
                breakpoint



# 46
def changeLiveResponseFrame4():
        styles = converted_temps_four_labelframe.cget("style")
        if styles == "convertedScaleLableFrameLight.TLabel":
                converted_temps_four_labelframe.configure(style="convertedScaleLableFrameDark.TLabel")
        elif styles == "convertedScaleLableFrameDark.TLabel":
                converted_temps_four_labelframe.configure(style="convertedScaleLableFrameLight.TLabel")
                breakpoint



# 47
def changeLiveResponse1():
        styles = converted_temps_one_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



# 48
def changeLiveResponse2():
        styles = converted_temps_two_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



# 49
def changeLiveResponse3():
        styles = converted_temps_three_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



# 50
def changeLiveResponse4():
        styles = converted_temps_four_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



# 51
def changeLiveLawful():
        styles = lawful_privacy_frame.cget("style")
        if styles == "lawfulLight.TFrame":
                        lawful_privacy_frame.configure(style="lawfulDark.TFrame")
        elif styles == "lawfulDark.TFrame":
                lawful_privacy_frame.configure(style="lawfulLight.TFrame")
                breakpoint
        

# End of Styles 
# ==============================================================================================================================
# I disabled the ChangeStyle function due to malfunctioning widgets, an option to consider for those wishing to script their own
# ==============================================================================================================================

# Calling the Style 

# def changeStyle():
#         ChangeManconv()
#         ChangeTempFrame()
#         changeScales()
#         changeSSB()
#         changeScaleTemp()
#         changeSCL()
#         changeSRF()
#         changeRLF1()
#         changeRLF2()
#         changeRLF3()
#         changeRLF4()
#         changeResponse1()
#         changeResponse2()
#         changeResponse3()
#         changeResponse4()
#         changeResponseF()
#         changeTemconProg()
#         changeTUP()
#         changeTUPLabel()
#         changeTemcon()
#         ChangeTemconLabelframe()
#         ChangeTemconLabelFrameLabel()
#         ChangeTemconLogoLabel()
#         ChangeWeatherLabelframe()
#         ChangeWeatherLabelframeLabel()
#         ChangeWeatherLogoLabel()
#         changeHeroFrame()
#         changeHeroLabel()
#         changeFeedback()
#         changeDSSLogo()
#         changeFeedbackLabel()
#         changeTRF()
#         changeDesc()
#         changeCity()
#         changeLiveTemp()
#         changeTempIcon()
#         ChangeTempFrame()
#         ChangeConvBtn()
#         ChangeCityDescLabel()
#         changeLiveCityTemp()
#         changeLiveCityBtn()
#         changeConvTempFrame()
#         changeLiveResponseFrame1()
#         changeLiveResponseFrame2()
#         changeLiveResponseFrame3()
#         changeLiveResponseFrame4()
#         changeLiveResponse1()
#         changeLiveResponse2()
#         changeLiveResponse3()
#         changeLiveResponse4()
#         changeLiveLawful()    



temcon_program_frame = tk.Frame(master=window)
temcon_program_frame.configure()
temcon_program_frame.pack(fill="both", expand=False, side="top", anchor="center")
tup_frame = tk.Frame(master=temcon_program_frame)
tup_frame.configure()
tup_frame.grid(row=0, column=0, columnspan=4)
tup_label_title = ttk.Label(tup_frame)
tup_label_title.configure(text="TEMPERATURE CONVERSION TOOL", style="temconConToolLight.TLabel", anchor="center") 
tup_label_title.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5, sticky="ew")
temcon_frame = tk.Frame(master=tup_frame)
temcon_frame.configure(bg="#4f788a")
temcon_labelframe = ttk.LabelFrame(master = temcon_frame, text="TEMCON", height=50, width=150)
temcon_labelframe.configure(style="tested.TLabel")
temcon_labelframe.grid(row=0, column=0, columnspan=2, sticky=tk.N, pady=5, padx=5)
# temcon_labelframe_label = ttk.Label(master = temcon_labelframe)
# temcon_labelframe_label.configure(style="temconLight.TLabel", justify="center", anchor="center")
# temcon_labelframe_label.grid(row=0, column=0, padx=5,  sticky="nsew")
# Temcon Logo Image used in Advertising Frame
temcon_logo = ImageTk.PhotoImage(Image.open("imgs/tc2024Logo_100.png"))
temcon_logo_label = ttk.Label(master = temcon_labelframe,image=temcon_logo)
temcon_logo_label.configure(style="temconLight.TLabel", justify="center", anchor="center")
temcon_logo_label.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=10)
# Openweather
weather_labelframe = ttk.LabelFrame(master =temcon_frame, text="OPENWEATHER", height=50, width=150)
weather_labelframe.configure(style="tested.TLabel")
weather_labelframe.grid(row=0, column=2, columnspan=2, sticky=tk.N, pady=5, padx=15)
# weather_labelframe_label = ttk.Label(master = weather_labelframe)
# weather_labelframe_label.configure(style="weatherFrameLabelLight.TLabel",  justify="center", anchor="center")
# weather_labelframe_label.grid(row=0, column=2, columnspan=2, padx=10, sticky="ew")
# Weather Logo Image used in Advertising Frame
weather_logo = ImageTk.PhotoImage(Image.open("imgs/OWM_logo_135.png"))
weather_logo_label = ttk.Label(master = weather_labelframe, image=weather_logo)
weather_logo_label.configure(style="temconLight.TLabel", justify="center", anchor="center")
weather_logo_label.grid(row=0, column=2, columnspan=2, ipadx=10, ipady=10)
temcon_frame.grid(row=1, column=0, columnspan=4, rowspan=2, sticky="nsew")

# Sponsored Advertising Frame
hero_frame = tk.Frame(temcon_frame)
hero_frame.configure(relief="flat", bg="#519fd2")
hero_frame.grid(row=1, column=0, columnspan=4, rowspan=2, sticky="nsew")
# Sponsored Advertiseing Label
hero_frame_label = ttk.Label(hero_frame)
hero_frame_label.configure(style="heroFrameLabelLight.TLabel", font=("Roboto, sans-serif", 7, "bold"), text="Jeanette's Impressions Art\njeanette.elizabeth@dashwoorkz.ca\nCommunity Services Director", justify="center", anchor="center")
hero_frame_label.grid(row=0, column=0, ipady=5, padx=3, ipadx=10, sticky="w")
# jeia Logo Image used in Advertising Frame
jeia_logo = ImageTk.PhotoImage(Image.open("imgs/jeia_thumb.png"))
jeia_logo_label = ttk.Label(master = hero_frame,image=jeia_logo)
jeia_logo_label.configure(background="#ffe4c4")
jeia_logo_label.grid(row=0, column=1, sticky="e", pady=5)
feedback_frame = tk.Frame(master=hero_frame)
feedback_frame.configure(bg="#4f788a")
feedback_frame.grid(row=1, column=0, columnspan=4, padx= 2)
# jeia Logo Image used in Advertising Frame
dss_logo = ImageTk.PhotoImage(Image.open("imgs/dss_logo.png"))
dss_logo_label = ttk.Label(master = feedback_frame,image=dss_logo)
dss_logo_label.configure(style="heroFrameLabelLight.TLabel", anchor="center")
dss_logo_label.grid(row=0, column=0, pady=10, padx=10, ipadx=5, ipady=5, sticky="w")
feedback_frame_label = ttk.Label(master=feedback_frame)
feedback_frame_label.configure(style="heroFrameLabelLight.TLabel", font=("Roboto, sans-serif", 7, "bold"), wraplength=155, anchor="center", justify="center", text="FeedBack:\ndashWoorkZ Sovereign Society would welcome any comments or suggestions.\n Email: dashwoorkz@dashwoorkz.ca")
feedback_frame_label.grid(row=0, column=1, padx=10, ipadx=10, ipady=5, sticky="w")
# End of Main Page
#=================


def store_selected(choice):
        choice = convScale.get()
        convScale.set(choice)
        live_city_temp_entry.delete(0, tk.END)
        clearLiveTable()
        breakpoint
        

# Attempt at creating a function that gets the city and city temperature and then displays the city and city temperature and the temperature is used to activate the conversion table
# Live Temperature Conversion Frame
# =========================

style.configure("liveconv.TFrame", padx=5, pady=5, relief=tk.FLAT, takefocus=False, highlightthickness=0,bg="#00ffff", fg="#347898", background="#4f788a", foreground="#4c7588", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("liveReportLight.TFrame", relief=tk.SUNKEN, borderwidth=5, padx=5, takefocus=False, bd=3, highlightthickness=5,bg="#00ffff", fg="#347898", background="#4c7588", foreground="#1e90ff", highlightbackground='#8fbc8f', justify="center", highlightcolor='#dd8929', anchor="center")
style.configure("livedescLabelLight.TLabel", relief=tk.FLAT, takefocus=False, bd=3, highlightthickness=3,bg="#00ffff", fg="#347898", background="#4c7588", foreground="#6b9ac9", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("livedescLabelLight1.TLabel", relief=tk.FLAT, takefocus=False, font=("Times New Roman", 12, "bold"), highlightthickness=5 ,bg="#00ffff", fg="#347898", background="#347898", foreground="#70c5c2", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")


liveconv_frame = ttk.Frame(master=tup_frame)
liveconv_frame.configure(style="liveconv.TFrame")
# Openweather Program
live_report_frame = tk.Frame(master = liveconv_frame)
live_report_frame.configure(borderwidth=5, bg="#519fd2", highlightthickness=0, highlightbackground='#8fbc8f', highlightcolor='#1e90ff')
live_report_frame.grid(row=0, column=0, columnspan=4, sticky="ns", padx=10)
# Weather Frame - Temperature Reported and City
live_temperature = ttk.Frame(master = live_report_frame)
live_temperature.configure(style="weatherFrameLight.TFrame")
live_temperature.pack(fill="both", expand=True, side="left", padx=5, pady=5)
live_city_label = ttk.Label(master = live_temperature)
live_city_label.pack(fill="both", expand=True, side="top")
live_temperature_label = ttk.Label(master = live_temperature)
live_temperature_label.pack(fill="both", expand=True, side="bottom")
# Description of weather and weather icon
live_desc_frame = ttk.Frame(master = live_report_frame)
live_desc_frame.configure(style="weatherFrameLight.TFrame")
live_desc_frame.pack(fill="both", expand=True, side="right", padx=5, pady=5)
live_icon_label = ttk.Label(master = live_desc_frame)
live_icon_label.pack(fill="both", expand=True, side="top")
live_desc_frame_label = ttk.Label(master = live_desc_frame)
live_desc_frame_label.pack(fill="both", expand=True, side="bottom") 
liveconv_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")  

live_report_frame.columnconfigure(0, weight=1)
live_report_frame.rowconfigure(0, weight=1)
live_report_frame.columnconfigure(1, weight=1)
live_report_frame.rowconfigure(1, weight=1)
live_report_frame.columnconfigure(1, weight=1)
live_report_frame.rowconfigure(1, weight=1)
live_report_frame.columnconfigure(1, weight=1)
live_report_frame.rowconfigure(1, weight=1)

# live_report_frame.columnconfigure(0, weight=1)
# live_report_frame.rowconfigure(0, weight=1)
# live_report_frame.columnconfigure(2, weight=1)
# live_report_frame.rowconfigure(2, weight=1)
    # Attempt at creating a function that gets the city and city temperature 
    # and then displays the city and city temperature and the temperature is used to activate the conversion table
    #Live Weather Report Frame
    # This Weather App is brought to you in part by "Alina Chudnova" from her Youtube Video "Create A Weather App using Python | tutorial for Beginners"
    # https://www.youtube.com/watch?v=VaqYFs7Az50
    
APIKEY = StringVar()
APIKEY = " "
# =========================
def get_temperature(city):
    API_key = APIKEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


    # Search weather for a city
def searchTemp():
    city = live_city_temp_entry.get()
    result = get_temperature(city)
    if result is None:
        return
    # if the city is found, unpack the weather information
    icon_url, temperature, description, city, country = result
    icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))
    live_icon_label.configure(style="livedescLabelLight.TLabel", anchor="center", image=icon)
    live_icon_label.pack(fill="both", expand=True, side="top")
    live_icon_label.image = icon
    # Get the weather icon
    live_city_label.configure(style="livedescLabelLight1.TLabel", text=f"{city}, {country}", anchor="center", justify="center", wraplength=100)
    #live_desc_frame_label = ttk.Label(master = live_desc_frame)
    live_desc_frame_label.configure(style="livedescLabelLight1.TLabel", text= f"{description}", anchor="center", justify="center")
    window.geometry("432x365")
    live_report_frame.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")
    ScaleConverted = convScale.get()
    temp = IntVar()
    temp = round((temperature), 1)
    
    if ScaleConverted == "Kelvin":
            convTemp = round(temp * 1, 1)
            live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}K", anchor="center")
            converted_temps_one_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1), width=7, anchor='center', justify="center")
            converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((convTemp - 273.15) * 1.8) + 32, 2), width=7, anchor='center', justify="center")
            converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp - 273.15, 1), width=7, anchor='center', justify="center")
            converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp + 491.67, 1), width=7, anchor='center', justify="center")
            #window.geometry("310x364")
            #live_report_frame.pack(fill="both", expand=False, side="top", anchor="center")
            return
            
            
    elif ScaleConverted == "Fahrenheit":
            convTemp = round(((temp - 273.15) * 1.8) + 32, 1)
            live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}F", anchor="center")
            converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((convTemp - 32) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
            converted_temps_two_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1), width=7, anchor='center', justify="center")
            converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp - 32) * (5/9), 2),  width=7, anchor='center', justify="center")
            converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp + 459.67, 2) ,width=7, anchor='center', justify="center")
            #window.geometry("310x364")
            #live_report_frame.pack(fill="both", expand=False, side="top", anchor="center")
            return


    elif ScaleConverted == "Rankine":
            convTemp = round(((temp - 273.15) * 1.8) + 491.67, 1)
            live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}R", anchor="center")
            converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((convTemp- 491.67) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
            converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp - 459.67, 2), width=7, anchor='center', justify="center")
            converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp - 491.67) / 1.79999999, 2), width=7, anchor='center', justify="center")
            converted_temps_four_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1), width=7, anchor='center', justify="center")
            #window.geometry("310x364")
            #live_report_frame.pack(fill="both", expand=False, side="top", anchor="center")
            return


    elif ScaleConverted == "Celcius":
            convTemp = round(temp - 273.15, 1)
            live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}C", anchor="center")
            converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp  + 273.15, 2), width=7, anchor='center', justify="center")
            converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp  * (9/5)) + 32, 2), width=7, anchor='center', justify="center")
            converted_temps_three_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 2) , width=7, anchor='center', justify="center")
            converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp * 1.8) + 459.67, 2), width=7, anchor='center', justify="center")
            #window.geometry("310x364")
            #live_report_frame.pack(fill="both", expand=False, side="top", anchor="center")
            return


temp_response_frame = ttk.Frame(master = liveconv_frame)
temp_response_frame.configure(style="liveconv.TFrame", borderwidth=5)
temp_response_frame.grid(row=2, column=0, columnspan=3, rowspan=4, sticky="nsew")
temp_frame = ttk.Frame(master = temp_response_frame)
temp_frame.configure(style="convertedFrameLight.TFrame")
temp_frame.pack(fill="both", expand=False, side="top", anchor="center")
cityButton_frame = ttk.Frame(master = temp_frame)
cityButton_frame.configure(style="convertedFrameLight.TFrame")
cityButton_frame.pack(fill="x", expand=False, side="top")
city_description_label = ttk.Label(cityButton_frame)
city_description_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "Live City Weather Report", anchor='center', justify="center")
city_description_label.pack(fill="x", expand=False, side="top", ipady=5)
live_city_temp_entry = ttk.Entry(master = cityButton_frame)
live_city_temp_entry.configure(style="setTempLight.TEntry", justify="center")
live_city_temp_entry.pack(fill="both", expand=False, side="left")

temp_response_frame.columnconfigure(0, weight=1)
temp_response_frame.rowconfigure(0, weight=1)
temp_response_frame.columnconfigure(1, weight=1)
temp_response_frame.rowconfigure(1, weight=1)
temp_response_frame.columnconfigure(1, weight=1)
temp_response_frame.rowconfigure(1, weight=1)
# temp_response_frame.columnconfigure(1, weight=1)
# temp_response_frame.rowconfigure(1, weight=1)

# creating Option Menu widget
convScaleSet = ['Choose A Scale','Celcius','Fahrenheit', 'Kelvin', 'Rankine']
# setting variable for Integers and Strings
convScale = StringVar()
convScale.set(convScaleSet[0])
convScales = ttk.OptionMenu(
    cityButton_frame,
    convScale,
    *convScaleSet,
    command=store_selected
    )
convScales.configure(style="convScalesChoiceLight.TLabel", width=20)
convScales.pack(fill="both", expand=True, side="left", ipady=5, anchor="center", before=live_city_temp_entry)
live_city_Search_button = ttk.Button(master = cityButton_frame)
live_city_Search_button.configure(style="scaleSetButtonLight.TButton", takefocus=True, command=searchTemp, text="Get Temp")
live_city_Search_button.pack(fill="y", expand=False, side="right", anchor="ne")
#Converted temp Frame
converted_temps_frame = ttk.Frame(master = temp_frame)
converted_temps_frame.configure(style="scalesResponseFrameLight.TFrame")
converted_temps_frame.pack(fill='both', expand=True, side="bottom", anchor="center")
converted_temps_one_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_one_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text="  Kelvin ", width=7)
converted_temps_one_labelframe.pack(fill="both", expand=True, side="left")
converted_temps_one_labelframe_label = ttk.Label(master = converted_temps_one_labelframe)
converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor='center', justify="center")
converted_temps_one_labelframe_label.pack(fill="both", expand=True, side="bottom")
converted_temps_two_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_two_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Fahrenheit ", width=7)
converted_temps_two_labelframe.pack(fill="both", expand=True, side="top", ipady=5)
converted_temps_two_labelframe_label = ttk.Label(converted_temps_two_labelframe)
converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor='center', justify="center")
converted_temps_two_labelframe_label.pack(fill="both", expand=True, side="bottom")
converted_temps_three_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_three_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Celcius ", width=7)
converted_temps_three_labelframe.pack(fill="both", expand=True, side="right")
converted_temps_three_labelframe_label = ttk.Label(converted_temps_three_labelframe)
converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor='center', justify="center")
converted_temps_three_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)
converted_temps_four_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_four_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Rankine ", width=7)
converted_temps_four_labelframe.pack(fill="both", expand=True, side="right")
converted_temps_four_labelframe_label = ttk.Label(master = converted_temps_four_labelframe)
converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor="center", justify="center")
converted_temps_four_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)

temp_response_frame.rowconfigure(0, weight = 1)
temp_response_frame.columnconfigure(0, weight = 1)
temp_response_frame.rowconfigure(1, weight = 1)
temp_response_frame.columnconfigure(1, weight = 1)
temp_response_frame.rowconfigure(2, weight = 1)
temp_response_frame.columnconfigure(2, weight = 1)


# End Live Weather Report Frame

# ================================================================================================================================================================
# ================================================= Start of Manual Conversion Layout ============================================================================
# ================================================================================================================================================================


# Temcon and Open Weather Programs
# Openweather Program
manconv_frame = ttk.Frame(master=tup_frame)
manconv_frame.configure(style="weatherFrameDark.TFrame")
manconv_frame.grid(row=1, column=0, columnspan=4)
manual_frame = ttk.Frame(master=manconv_frame)
manual_frame.configure(style="weatherFrameDark.TFrame")


weather_report_frame = ttk.Frame(master = manual_frame)
weather_report_frame.configure(style="temconDark.TFrame")
weather_report_frame.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")

# Description of weather and weather icon
description_frame = ttk.Frame(master = weather_report_frame)
description_frame.configure(style="weatherFrameDark.TFrame")
description_frame.pack(fill="both", expand=True, side="left", anchor="center")
weather_icon_label = ttk.Label(master = description_frame)
weather_icon_label.pack(fill="both", expand=True, side="top", anchor="center")
# Description Frame - Description of Weather and Weather
description_frame_label = ttk.Label(master = description_frame)
description_frame_label.pack(fill="x", expand=False, side="bottom", ipady=5, ipadx=5)


# Weather Frame - Temperature Reported and City
weather_frame = ttk.Frame(master = weather_report_frame)
weather_frame.configure(style="temconDark.TLabel")
weather_frame.pack(fill="both", expand=True, side="right", anchor="center")
city_label = ttk.Label(master = weather_frame)
city_label.pack(fill="both", expand=True, side="top", anchor="center", ipadx=5)
temperature_label = ttk.Label(master = weather_frame)
temperature_label.pack(fill="both", expand=True, side="bottom", ipadx=5)
manual_frame.pack(fill="both", expand=True, side="top", anchor="center")
 
# This Weather App is brought to you in part by "Alina Chudnova" from her Youtube Video "Create A Weather App using Python | tutorial for Beginners"
# https://www.youtube.com/watch?v=VaqYFs7Az50
# Weather Report Frame
def get_weather(city):
    API_key = APIKEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    #Get the icon URL and return all the weather information
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


# Search weather for a city
def search():
    city = city_search_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # if the city is found, unpack the weather information
    icon_url, temperature, description, city, country = result
    # Get the weather icon
    icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))   
    weather_icon_label.configure(style="livedescLabelDark.TLabel", anchor="center", image=icon)
    weather_icon_label.pack(fill="x", expand=False, side="top", anchor="center")
    weather_icon_label.image = icon
    city_label.configure(style="livedescLabelDark1.TLabel", text=f"{city}, {country}", anchor="center")
    description_frame_label.configure(style="livedescLabelDark1.TLabel", text= f"{description}", anchor="center")
    temperature_label.configure(style="livedescLabelDark.TLabel", font=("Times New Romant", 30, "bold"), text= f"{round(int(temperature))}C", anchor="center")
    window.geometry("283x430")
    weather_report_frame.grid(row=0, column=0, columnspan=4,sticky="nsew")

# Scale Temperature Setting

# Function retrieves the Scale Chosen and the Temperature to convert, then displays the Conversion Table
def setScaleTemp():
        if temp_var == True:
                choice = scale.set[1]
                temp = main.temp.get()           
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text=int(temp)  + 273.15, width=7, anchor='center', justify="center")
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= (int(temp)  * (9/5) + 32), width=7, anchor='center', justify="center")
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= int(temp) * 1, width=7, anchor='center', justify="center")
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text=((int(temp) * 1.8) + 459.67), width=7, anchor='center', justify="center")
                scales_response_frame.pack( fill="x", expand=True)
                return
        else: 
                choice = scale.get()
                temp = scaleTemp.get()
                if choice == "Kelvin":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(((int(temp) - 273.15) * 1.8) + 32, 2), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) - 273.15, 1), width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) + 491.67, 1), width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return
                        
                elif choice == "Fahrenheit":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(((int(temp) - 32) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round((int(temp) - 32) * (5/9), 2),  width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) + 459.67, 2) ,width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return

                elif choice == "Rankine":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(((int(temp)- 491.67) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) - 459.67, 2), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round((int(temp) - 491.67) / 1.79999999, 2), width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return
                
                elif choice == "Celcius":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp)  + 273.15, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp)  * (9/5) + 32, 2), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 2) , width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round((int(temp) * 1.8) + 459.67, 2), width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return


        # Math note: Source of information regarding Rounding Numbers in Python : https://bobbyhadz.com/blog/python-round-float-3-decimal-places         


# Main Frame
temperature_frame = ttk.Frame(master = manual_frame)
temperature_frame.configure(style="convertedFrameDark.TFrame") 
temperature_frame.grid(row=1, column=0, columnspan=4, rowspan=4, sticky="nsew")
manual_search_frame = ttk.Frame(master = temperature_frame)
manual_search_frame.configure(style="convertedFrameDark.TFrame") 
manual_search_frame.pack(fill="both", expand=True, side="top")
city_description_label = ttk.Label(manual_search_frame)
city_description_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "Manual City Weather Report", anchor='center', justify="center")
city_description_label.pack(fill="x", expand=False, side="top", ipady=5) 
city_search_entry = ttk.Entry(master = manual_search_frame)
city_search_entry.configure(style="setTempDark.TEntry", justify="center") 
city_search_entry.pack(fill="both", expand=True, side="left", anchor="nw")
citySearch_button = ttk.Button(master = manual_search_frame)
citySearch_button.configure(style="scaleSetButtonDark.TButton", takefocus=True, command=search, text="Search")
citySearch_button.pack(fill="y", expand=True, side="right", anchor="ne")

scaleChoice_title = ttk.Frame(master = temperature_frame)
scaleChoice_title.configure(style="convertedFrameDark.TFrame")
scaleChoice_title.pack(fill="both", expand=True, side="top")
scaleChoice_label = ttk.Label(scaleChoice_title)
scaleChoice_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text='Enter a Number To Convert', justify="center", anchor="center")
scaleChoice_label.pack(fill="x", expand=True, side="right", ipady=5)
# =========  Temperature Setting Frame Start
scaleChoice = ttk.Frame(master = temperature_frame)
scaleChoice.configure(style="convertedFrameDark.TFrame")
scaleChoice.pack(fill="both", expand=True, side="top")                        
temperature_setting_frame = ttk.Frame(master = scaleChoice) 
temperature_setting_frame.configure(style="convertedFrameDark.TFrame")
temperature_setting_frame.pack(side="top", fill="both", expand=True)
scaleSet_button = ttk.Button(master = temperature_setting_frame)
scaleSet_button.configure(style="scaleSetButtonDark.TButton", takefocus=True, command=setScaleTemp, text="Convert")
scaleSet_button.pack(fill="x", expand=False, padx=(3, 0), side="right")
# Scale Temperature Setting
scaleTemp = ttk.Entry(master = temperature_setting_frame)
scaleTemp.configure(style="setTempDark.TEntry", width=4, justify="center") 
scaleTemp.pack(fill="x", expand=False, padx=3, side="right", ipadx=2, ipady=2)
# creating Option Menu widget
scaleSet = ['Choose A Scale','Celcius','Fahrenheit', 'Kelvin', 'Rankine']
# setting variable for Integers and Strings
scale = StringVar()
scale.set(scaleSet[0])
scales = ttk.OptionMenu(
    temperature_setting_frame,
    scale,
    *scaleSet,
    command=display_selected)
scales.configure(style="ScalesChoiceDark.TLabel", width=7)
scales.pack(fill="both", expand=True, side="left", ipady=5, ipadx=5, anchor="center")
# ====== Scales Conversion Frame 
scales_response_frame = ttk.Frame(master = scaleChoice)
scales_response_frame.configure(style="scalesResponseFrameDark.TFrame")
scales_response_frame.pack( fill="both", expand=True, ipady=5)
setTemp = StringVar()
temp = 0

def setTemp(temp):
    temp = round(setTemp)
 
            
#Converted Scales Frame
converted_scales_frame = ttk.Frame(master = scales_response_frame)
converted_scales_frame.configure(style="scalesResponseFrameDark.TFrame")
converted_scales_frame.pack(fill='both', expand=True, ipady=3, side="bottom", anchor="center")
# Converted Scale Kelvin
converted_scale_one_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_one_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text="  Kelvin ", width=7)
converted_scale_one_labelframe.pack(fill="both", expand=True, side="left", ipady=5)
converted_scale_one_labelframe_label = ttk.Label(master = converted_scale_one_labelframe)
converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "", justify="center", width=7)
converted_scale_one_labelframe_label.pack(fill="both", expand=True, side="bottom")
# Converted Scale Fahrenheit
converted_scale_two_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_two_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text=" Fahrenheit ", width=7)
converted_scale_two_labelframe.pack(fill="both", expand=True, side="top", ipady=5)
converted_scale_two_labelframe_label = ttk.Label(converted_scale_two_labelframe)
converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text="", justify="center", width=7)
converted_scale_two_labelframe_label.pack(fill="both", expand=True, side="bottom")
# Converted Scale Celcius
converted_scale_three_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_three_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text=" Celcius ", width=7)
converted_scale_three_labelframe.pack(fill="both", expand=True, side="right")
converted_scale_three_labelframe_label = ttk.Label(converted_scale_three_labelframe)
converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "", justify="center", width=7)
converted_scale_three_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)
# Converted Scale Rankine
converted_scale_four_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_four_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text=" Rankine ", width=7)
converted_scale_four_labelframe.pack(fill="both", expand=True, side="right")
converted_scale_four_labelframe_label = ttk.Label(master = converted_scale_four_labelframe)
converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "", justify="center", width=7)
converted_scale_four_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)

temperature_frame.rowconfigure(0, weight = 1)
temperature_frame.columnconfigure(0, weight = 1)
temperature_frame.rowconfigure(1, weight = 1)
temperature_frame.columnconfigure(1, weight = 1)
temperature_frame.rowconfigure(2, weight = 1)
temperature_frame.columnconfigure(2, weight = 1)
temperature_frame.rowconfigure(3, weight = 1)
temperature_frame.columnconfigure(3, weight = 1)

scales_response_frame.rowconfigure(0, weight = 1)
scales_response_frame.columnconfigure(0, weight = 1)
scales_response_frame.rowconfigure(1, weight = 1)
scales_response_frame.columnconfigure(1, weight = 1)
scales_response_frame.rowconfigure(2, weight = 1)
scales_response_frame.columnconfigure(2, weight = 1)

# ================================================================================================================================================================
# ================================================= Start of Manual Conversion Layout ============================================================================
# ================================================================================================================================================================


# Lawful Privacy Statement
lawful_privacy_frame = ttk.Frame(master=temcon_program_frame)
lawful_privacy_frame.configure(style="lawfulLight.TFrame")
lawful_privacy_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
logo_frame = ttk.Frame(master=lawful_privacy_frame)
logo_frame.configure(style="lawfulLight.TFrame")
logo_frame.pack(fill="both", expand=True, side="top")
# tcttk Logo Image used in Frame
tcttk_logo = ImageTk.PhotoImage(Image.open("imgs/dss_logo.png"))
tcttk_logo_label = ttk.Label(master = logo_frame,image=tcttk_logo)
tcttk_logo_label.configure(style="tcttkLight.TLabel", anchor="center", justify="center")
tcttk_logo_label.pack(fill="both", expand=True, side="top",)
privacy_frame = ttk.Frame(master=lawful_privacy_frame)
privacy_frame.configure(style="privacyLight.TFrame")
privacy_frame.pack(fill="both", expand=True)
privacy_frame_label = ttk.Label(master=privacy_frame)
privacy_frame_label.configure(style="privacyLight.TLabel", font=("Times New Roman", 10, "bold"), anchor="center", justify="center", wraplength=290, text="dashWoorkz Sovereign Society\n is a Private Society, we will not invade Your Privacy, or provide anyone any information we may have about you, any information we have about you will have been acquired with Your Consent, if we were to do anything with the information we have about you, it would be with Your Consent")
privacy_frame_label.pack(fill="x", expand="True", side="top", ipady=5, ipadx=5)
lawful_frame = ttk.Frame(master=lawful_privacy_frame)
lawful_frame.configure(style="lawfulLight.TFrame")
lawful_frame.pack(fill="both", expand=True)
lawful_frame_label = ttk.Label(master=lawful_frame)
lawful_frame_label.configure(style="lawfulLight.TLabel", font=("Times New Roman", 10, "bold"), justify="center", anchor="center", wraplength=300, text="dashWoorkz Sovereign Society\nEstablished: 2023\nTemCon TTK Version One(1)\nTemperature Conversion Tool\nConverts:\n Celcius, Kelvin, Fahrenheit and Rankine")
lawful_frame_label.pack(fill="x", expand="True", side="top", ipady=5, ipadx=5)

lawful_privacy_frame.rowconfigure(0, weight = 1)
lawful_privacy_frame.columnconfigure(0, weight = 1)
lawful_privacy_frame.rowconfigure(1, weight = 1)
lawful_privacy_frame.columnconfigure(1, weight = 1)
lawful_privacy_frame.rowconfigure(2, weight = 1)
lawful_privacy_frame.columnconfigure(2, weight = 1)
lawful_privacy_frame.rowconfigure(3, weight = 1)
lawful_privacy_frame.columnconfigure(3, weight = 1)

# End of Lawful Privacy Statement
# ===================

# Donation Window
def open_donate_window():
    donate_window = Toplevel(window)
    donate_window.title("Donate")
    donate_window.geometry("310x200")
    donate_window.configure(bg="#f0f0f0")
    donate_label = Label(donate_window)
    donate_label.configure(font=("Times New Roman", 11, "bold"),highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True,  background="#ffe4c4", foreground="#5c3608", text="Donate:\nIf you enjoyed this program and would\n like to contribute to our work,\n you can donate by emailing:\ndashWoorkz Sovereign Society:\nEmail: dashwoorkz@dashwoorkz.ca\nor through E-Transfer to:\nLord :Dash: La Londe\nManaging Director\ndash@dashwoorkz.ca")
    donate_label.pack(fill="both", expand=True)

# End of Donation Window
# ===================

# Contact Information Window
def open_contact_window():
    contact_window = Toplevel(window)
    contact_window.title("Contact Us")
    contact_window.geometry("310x200")
    contact_window.configure(bg="#f0f0f0")
    
    label_contact = Label(contact_window, text="Contact Information", foreground="#fd3adf", bg="#f7d4f6", font=("Helvetica", 12, "bold"))
    label_contact.pack(fill="both", expand=True)

    label_society = Label(contact_window, text="dashWoorkZ Sovereign Society", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10, "bold"))
    label_society.pack(fill="both", expand=True)
    
    label_email = Label(contact_window, text="Email: dashwoorkz@dashwoorkz.ca", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10))
    label_email.pack(fill="both", expand=True)
    
    label_mdirector = Label(contact_window, text="Managing Director:", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
    label_mdirector.pack(fill="both", expand=True)
    
    label_mdName = Label(contact_window, text="Lord :Dash: La Londe", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10))
    label_mdName.pack(fill="both", expand=True)

    label_md_email = Label(contact_window, text="Email: dash@dashwoorkz.ca", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
    label_md_email.pack(fill="both", expand=True)

    label_csDirector = Label(contact_window, text="Community Services Director:", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10, "bold"))
    label_csDirector.pack(fill="both", expand=True)
    
    label_csdName = Label(contact_window, text="Lady :Jeanette-Elizabeth: Hiuser", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
    label_csdName.pack(fill="both", expand=True)

    label_cs_email = Label(contact_window, text="Email: jeanette.elizabeth@dashwoorkz.ca", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
    label_cs_email.pack(fill="both", expand=True)

# End of Contact Information Window
# ===================


# MIT License
def open_mit_window():
    mit_window = Toplevel(window)
    mit_window.title("MIT License")
    mit_window.geometry("350x400")
    mit_window.configure(bg="#f0f0f0")
    mit_label = Label(mit_window)
    mit_label.configure(font=("Times New Roman", 9, "bold"),highlightbackground='#2391ff', wraplength=280, pady=10, highlightcolor='#35cbe6', highlightthickness=3, takefocus=True,  background="#85c0ea", foreground="#206eff", 
    text= "Copyright (c) 2024 dashWoorkZ Sovereign Society\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
    mit_label.pack(fill="both", expand=True)


def changeStyle():
    styles_window = Toplevel(window)
    styles_window.title("Change Styles Function")
    styles_window.geometry("300x250")
    styles_window.configure(bg="#f0f0f0")
    styles_label = Label(styles_window)
    styles_label.configure(font=("Times New Roman", 12, "bold"),highlightbackground='#2391ff', wraplength=200, pady=10, highlightcolor='#35cbe6', highlightthickness=3, takefocus=True,  background="#85c0ea", foreground="#206eff", text= "Change Styles Function has been disabled due to malfunctioning widgets, particularly the 'scaleset' array, please feel free to make adjustments")
    styles_label.pack(fill="both", expand=True)

hideLawful()
getMain()


window.configure(menu = menu)




window.mainloop()
