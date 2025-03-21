from colorama import Fore, init
import keyboard
import time
import os
import eyed3

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
    mp3_file= eyed3.load(file_name)
    if not mp3_file:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error loading MP3 file metadata.")
        return

    choix = int(input(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] Que voulez vous modifié ?\n  1- Artist Name\n  2- Album Name\n  3- Title of the song\n  0- Exit"))
    while choix !=0:
        match choix:
            case 1:
                artist_name = input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Artist name ? :")
                mp3_file.tag.artist = artist_name
                break
            case 2: 
                album_name = input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Album name ? :")
                mp3_file.tag.album = album_name
                break
            case 3:
                title_song = input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Title of the song ? :")
                mp3_file.tag.title = title_song
                break
            case 0:
                break
            case _:
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Unknow choice ! Try again")
                break
    mp3_file.tag.save()
    print(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Saved with sucess")

match file_extension:
    case ".mp3":
        edit_mp3()
    case _:
        print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] Unknown file format")
            

