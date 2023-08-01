import tkinter as tk
from pyinjector import inject
import pygame
from pypresence import Presence
import time
import psutil

client_id = '970520923964842004'

RPC = Presence(client_id)
RPC.connect()
pygame.mixer.init()

def play_background_music():
    pygame.mixer.music.load("ariza.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

def stop_background_music():
    pygame.mixer.music.stop()

def on_inject_button():
    print("Injecting DLL...")
    inject(PIDVIEW, "latest.dll")

def update_discord_rpc():
    while True:
        RPC.update(
            details="In The Launcher",
            state="dsc.gg/ariza",
            large_image="a1",
            large_text="Ariza Logo - Main -",
            small_image="a2",
            small_text="dsc.gg/mcarchive"
        )
        time.sleep(15)

def find_minecraft_pid():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Minecraft.Windows.exe':
            return proc.info['pid']
    return None

if __name__ == "__main__":
    PIDVIEW = find_minecraft_pid()

    window = tk.Tk()
    window.geometry("400x300")
    window.title("Ariza Launcher")

    window.columnconfigure(0, weight=1)

    title_label = tk.Label(window, text="Ariza Launcher", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, pady=10)

    inject_button = tk.Button(window, text="Inject DLL", width=15, command=on_inject_button)
    inject_button.grid(row=1, column=0, padx=10, pady=5)

    music_var = tk.BooleanVar()
    music_checkbox = tk.Checkbutton(window, text="Background Music", variable=music_var, command=lambda: play_background_music() if music_var.get() else stop_background_music())
    music_checkbox.grid(row=2, column=0, padx=10, pady=5)

    # Discord RPC Thread
    import threading
    rpc_thread = threading.Thread(target=update_discord_rpc)
    rpc_thread.start()

    window.mainloop()

    # Close the connection when the program ends
    RPC.close()