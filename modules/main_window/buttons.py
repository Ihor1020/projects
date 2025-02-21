import customtkinter as tk
import pygame
import tkinter as ctk
from tkinter import filedialog, messagebox
import os
from .photos import Images 
from .window import *
import functools
import random


pygame.mixer.init()

list_of_music = []
current_music = None

def play_music():
    global current_music, list_of_music
    file_path = filedialog.askopenfilename(filetypes=[("Аудио Файлы", "*.mp3")])
    if file_path:
        try:
            if pygame.mixer.music.get_busy():
                # Если уже играет песня, добавить новую песню в очередь
                list_of_music.append(file_path)
                update_queue_label() 
            else:
                # Если песня не играет, начать воспроизведение новой песни
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                current_music = file_path 
                update_queue_label() 
        except pygame.error:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл")

def stop_music():
    global current_music, list_of_music
    pygame.mixer.music.stop()
    current_music = None
    if list_of_music:
        # Если очередь не пуста, начать воспроизведение следующей песни
        next_song = list_of_music.pop(0)
        try:
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
            current_music = next_song 
            update_queue_label()
        except pygame.error:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл")

def pause_music():
    pygame.mixer.music.pause()

def delete_music():
    list_of_music.pop(0)
    update_queue_label()

def play_next_song():
    if list_of_music:
        next_song = list_of_music.pop(0)
        try:
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
            update_queue_label()
        except pygame.error:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл")

def mix_music():
    random.shuffle(list_of_music)
    update_queue_label()

def unpause_music():
    pygame.mixer.music.unpause()

def set_music(volume):
    pygame.mixer.music.set_volume(float(volume))

def get_current_music():
    global current_music
    if current_music:
        return os.path.basename(current_music).encode('utf-8').decode('utf-8')  # Возвращает название файла без пути
    main_window.after(1000, get_current_music)
    return "Нет"


def update_queue_label():
    queue_text = "\n".join([os.path.basename(track) for track in list_of_music])
    background_player_queue.config(state=tk.NORMAL)  # Разрешить редактирование текста
    background_player_queue.delete(1.0, tk.END)  # Удалить весь текст
    background_player_queue.insert(tk.END, queue_text)  # Вставить новый текст
    background_player_queue.config(state=tk.DISABLED)  # Запретить редактирование текста


def create_buttons(main_window):
    Images.load_images()

    # Кнопка "Добавить музыку"
    play_button = tk.CTkButton(main_window, 
                               image=Images.add_music, 
                               text="",
                               width=61,
                               height=58,
                               fg_color="#808080",
                               hover_color="#808080",  
                               border_width=0, 
                               command=play_music)
    play_button.place(x=25, y=397)

    # Кнопка "Стоп"
    stop_button = tk.CTkButton(main_window, 
                               image=Images.stop_image, 
                               text="", 
                               width=169,
                               height=60,
                               fg_color="#808080",
                               hover_color="#808080", 
                               border_width=0,
                               command=stop_music)
    stop_button.place(x=268, y=323)

    # Кнопка "Пауза"
    pause_button = tk.CTkButton(main_window, 
                            image=Images.pause_image, 
                            text="", 
                            width=169,
                            height=60,
                            fg_color="#808080",  
                            hover_color="#808080", 
                            border_width=0,  
                            command=pause_music)
    pause_button.place(x=268, y=243)

    # Кнопка "Возобновить"
    unpause_button = tk.CTkButton(main_window, 
                                  image=Images.play_image, 
                                  text="", 
                                  width=169,
                                  height=60,
                                  fg_color="#808080",  
                                  hover_color="#808080",
                                  border_width=0,
                                  command=unpause_music)
    unpause_button.place(x=268, y=87)  


    delete_button = tk.CTkButton(main_window,
                                image=Images.delete_image,
                                text="",
                                width=61,
                                height=58,
                                fg_color="#808080",
                                #bg_color= "transparent",
                                hover_color="#808080",
                                border_width=0, 
                                command = delete_music)
    delete_button.place(x=111, y=397)

    # Скип текущей музыки
    skip_button = tk.CTkButton(main_window,
                                width=61,
                                height=58,
                                image = Images.button_skip,
                                command = play_next_song,
                                text = "",
                                fg_color= "#808080",
                                hover_color= "#808080",
                                border_width=0,
                               )
    skip_button.place(x=274, y=165)

    # Кнопка "Перемешать"
    mix_music_button = tk.CTkButton(main_window,
                                    image=Images.mix_music,
                                    text="",
                                    width= 61,
                                    height= 58,
                                    fg_color= "#808080",
                                    hover_color= "#808080",
                                    border_width=0,
                                    command= mix_music)
    mix_music_button.place(x=197, y=397)

    # Надпись "Громкость"
    volume_label = tk.CTkLabel(main_window, text="Громкость")
    volume_label.place(x=318, y=390)

    # Ползунок громкости
    volume_slider = tk.CTkSlider(main_window, 
                                 from_=0, 
                                 to=1, 
                                 width=150,
                                 command=set_music)
    volume_slider.set(0.5) 
    volume_slider.place(x=278, y=420)

    
    # Надпись "Текущий трек"
    current_track_label = tk.CTkLabel(main_window, 
                                  width=15,  
                                  height=5,
                                  bg_color=main_window.cget("bg"),  
                                  fg_color="#808080", 
                                  font=("Arial", 12), 
                                  text = f"Текущий трек: {get_current_music()}",
                                  wraplength= 110,
                                  
                                  )
    

    # Надпись "Текущий трек"
    # current_track_label = ctk.Text(main_window, 
    #                               width=15,  
    #                               height=5,  
    #                               #wrap=tk.WORD,  # Автоматический перенос текста
    #                               bg=main_window.cget("bg"),  
    #                               fg="BLUE", 
    #                               font=("Arial", 12), 
    #                               #text = f"Текущий трек: {get_current_music()}",
    #                               #wraplength= 30,
    #                               #text = "фывфыввфывфывфывывфыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы"
    #                               bd=0,  
    #                               highlightthickness=0)
    
    # current_track_label.insert(tk.END, f"Текущий трек: {get_current_music()}") # Вставить текст
    # current_track_label.config(state=tk.DISABLED)  # Запретить редактирование текста
    current_track_label.place(x=305, y=20)

    # Фоновое изображение
    background_player = tk.CTkLabel(main_window, 
                                    text = "",
                                    image = Images.background)
    background_player.place(x=8, y=15)


    # Очередь треков
    global background_player_queue
    background_player_queue = ctk.Text(main_window, 
                                    width=23,
                                    height=19,
                                    wrap=tk.WORD,
                                    bg="#BDBDBD", 
                                    fg="#808080",
                                    font=("Arial", 12),
                                    bd=0,
                                    ) 
    background_player_queue.insert(tk.END, "\n".join([os.path.basename(track) for track in list_of_music]))
    background_player_queue.config(state=tk.DISABLED)
    background_player_queue.place(x=25, y=25)

    
    def update_current_track_label():
        # current_track_label.config(state=tk.NORMAL)  # Разрешить редактирование текста
        # current_track_label.delete(1.0, tk.END)  # Удалить весь текст
        # current_track_label.insert(tk.END, f"Текущий трек: {get_current_music()}")  # Вставить новый текст
        # current_track_label.config(state=tk.DISABLED)  # Запретить редактирование текста
        current_track_label.configure(text=f"Текущий трек: {get_current_music()}")
        main_window.after(1000, update_current_track_label)
    

    update_current_track_label()