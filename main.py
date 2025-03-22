from colorama import Fore, init
import keyboard
import time
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4

# Initalisation de colorama
init()

print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] MetaData Editor / Credit : @00j5y")
print("")
print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Press 'space' to start")
keyboard.wait('space')  
time.sleep(0.1)

print("")

file_name = input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] File name :")
split_tup = os.path.splitext(file_name)
file_extension = split_tup[1]

def edit_mp3():
    mp3_file = EasyID3(file_name)
    if not mp3_file:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error loading MP3 file metadata.")
        return

    while True:
        choix = int(input(f"\n{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] What do you want edit ?\n  1- Artist Name\n  2- Album Name\n  3- Title of the song\n  4- Genre of the song\n  5- Release Year of the song\n  0- Exit\n  Choice : "))
        match choix:
            case 1:
                artist_name = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Artist name ? :")
                mp3_file["artist"] = artist_name
            case 2: 
                album_name = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Album name ? :")
                mp3_file["album"] = album_name
            case 3:
                title_song = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Title of the song ? :")
                mp3_file["title"] = title_song
            case 4:
                genre_song = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Genre of the song ? :")
                mp3_file["genre"] = genre_song
            case 5:
                year_song = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Release Date ? :")
                mp3_file["date"] = year_song
            case 0:
                break
            case _:
                print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Unknow choice ! Try again")
    mp3_file.save()
    print(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Saved with sucess")

def edit_mp4():
    mp4_file = MP4(file_name)
    if not mp4_file:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error loading MP4 file metadata.")
        return

match file_extension:
    case ".mp3":
        edit_mp3()
    case ".mp4":
        edit_mp4()
    case _:
        print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] File Format not supported")
            

