from colorama import Fore, init
import keyboard
import time
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4

# Initialisation de colorama
init()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

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
    try:
        mp3_file = EasyID3(file_name)
    except Exception as e:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error loading MP3 file metadata: {e}")
        return

    while True:
        choix = int(input(f"\n{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] What do you want to edit?\n"
                          "  1- Artist Name\n"
                          "  2- Album Name\n"
                          "  3- Title of the song\n"
                          "  4- Genre of the song\n"
                          "  5- Release Year of the song\n"
                          "  0- Exit\n"
                          "  Choice : "))
        match choix:
            case 1:
                artist_name = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Artist name ? : ")
                mp3_file["artist"] = artist_name
                clear()
            case 2:
                album_name = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Album name ? : ")
                mp3_file["album"] = album_name
                clear()
            case 3:
                title_song = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Title of the song ? : ")
                mp3_file["title"] = title_song
                clear()
            case 4:
                genre_song = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Genre of the song ? : ")
                mp3_file["genre"] = genre_song
                clear()
            case 5:
                year_song = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Release Date ? : ")
                mp3_file["date"] = year_song
                clear()
            case 0:
                break
            case _:
                print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Unknown choice! Try again")
                clear()

    mp3_file.save()
    print(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Saved successfully")


def edit_mp4():
    try:
        mp4_file = MP4(file_name)
    except Exception as e:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error loading MP4 file metadata: {e}")
        return

    while True:
        choix = int(input(f"\n{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] What do you want to edit?\n"
                          "  1- Artist video\n"
                          "  2- Album video\n"
                          "  3- Title of the video\n"
                          "  4- Description of the video\n"
                          "  5- Genre of the video\n"
                          "  6- Release Year of the video\n"
                          "  0- Exit\n"
                          "  Choice : "))
        match choix:
            case 1:
                artist_vid = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Artist name ? : ")
                mp4_file["\xa9ART"] = [artist_vid]
                clear()
            case 2:
                album_vid = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Album name ? : ")
                mp4_file["\xa9alb"] = [album_vid]
                clear()
            case 3:
                title_vid = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Title of the video ? : ")
                mp4_file["\xa9nam"] = [title_vid]
                clear()
            case 4:
                desc_vid = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Description ? : ")
                mp4_file["desc"] = [desc_vid]
                clear()
            case 5:
                genre_vid = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Genre ? : ")
                mp4_file["\xa9gen"] = [genre_vid]
                clear()
            case 6:
                year_vid = input(f"\n{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Release Date ? : ")
                mp4_file["\xa9day"] = [year_vid]
                clear()
            case 0:
                break
            case _:
                print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Unknown choice! Try again")
                clear()

    mp4_file.save()
    print(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Saved successfully")

match file_extension:
    case ".mp3":
        edit_mp3()
    case ".mp4":
        edit_mp4()
    case _:
        print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] File format not supported")