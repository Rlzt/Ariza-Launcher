import tkinter as tk
from pyinjector import inject
import json
import pygame
from pypresence import Presence
import time

# Your Discord application's Client ID
client_id = '970520923964842004'

# Initialize the Discord RPC client
RPC = Presence(client_id)
RPC.connect()
window = tk.Tk()
# Set the initial presence status
RPC.update(
    details="Playing Ariza 1.01",
    state="Download: dsc.gg/ariza",
    large_image="a1",
    large_text="Ariza Logo - Main -",
    small_image="a2",
    small_text="dsc.gg/mcarchive"
)

def play_background_music():
    pygame.mixer.music.load("ariza.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

def stop_background_music():
    pygame.mixer.music.stop()

def on_inject_button():
    print("Injecting DLL...")
    inject(PIDVIEW, "latest.dll")

def on_settings_button():
    print("Settings Loading...")
    print("Copyright: dsc.gg/ariza 2023")
    open_second_gui()

def open_second_gui():
    second_window = tk.Toplevel(window)
    second_window.title("Settings")
    
    def on_checkbox_click():
        if checkbox_var.get():
            print("Checkbox Selected!")
            Music = True
            play_background_music()
        else:
            print("Checkbox Deselected!")
            Music = False
            stop_background_music()

    label = tk.Label(second_window, text="Settings!")
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(second_window, text="Background Music", variable=checkbox_var, command=on_checkbox_click)
    checkbox.pack()
    label.pack()

def right_menu_show(event):
    context_menu.post(event.x_root, event.y_root)

def right_menu_click(option):
    print(f"FAILURE SELECTED: {option} EVEN THO IT'S BS")

# Create the context menu
context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="Music From: rb.gy/cc9v4", command=lambda: right_menu_click("Option 1"))
context_menu.add_command(label="dsc.gg/ariza", command=lambda: right_menu_click("Option 2"))
context_menu.add_separator()
context_menu.add_command(label="Exit", command=window.quit)

# Bind the right-click event to show the context menu
window.bind("<Button-3>", right_menu_show)

# Initialize Pygame Mixer
pygame.mixer.init()

import psutil

def find_minecraft_pid():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Minecraft.Windows.exe':
            return proc.info['pid']
    return None

if __name__ == "__main__":
    minecraft_pid = find_minecraft_pid()
    if minecraft_pid is not None:
        print(f"Minecraft is running with PID: {minecraft_pid}")
    else:
        print("Minecraft is not running.")


PIDVIEW = minecraft_pid



window.geometry("450x325")
window.title("Ariza Launcher")

PIDV = tk.Label(window, text=PIDVIEW)
PIDV.place(x=100, y=35)
DIn = tk.Button(window, text="Inject DLL", command=on_inject_button)
DIn.place(x=200, y=69)

Settings = tk.Button(window, text="Settings", command=on_settings_button)
Settings.place(x=210, y=95)

def update_discord_rpc():
    while True:
        RPC.update(
            details="Playing Ariza 1.01",
            state="Download: dsc.gg/ariza",
            large_image="a1",
            large_text="Ariza Logo - Main -",
            small_image="a2",
            small_text="dsc.gg/mcarchive"
        )
        time.sleep(15)

try:
    # Start the Discord RPC presence update loop in a separate thread
    import threading
    rpc_thread = threading.Thread(target=update_discord_rpc)
    rpc_thread.start()

    window.mainloop()

except KeyboardInterrupt:
    print("bozo")

# Don't forget to close the connection when your program ends
RPC.close()
