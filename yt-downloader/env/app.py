import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

...

# Обработчик для вставки текста
def on_entry_paste(event):
    content = root.clipboard_get()
    entry_url.delete(0, 'end')  # Очищаем текущее содержимое entry_url
    entry_url.insert('end', content)  # Вставляем скопированный текст

# Привязываем событие вставки к CTkEntry
    entry_url.bind("<Control-v>", on_entry_paste)



def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(padx=10, pady=5)
    progress_bar.pack(padx=10, pady=5)
    status_label.pack(padx=10, pady=5)

    try:
       yt = YouTube(url)
       stream = yt.streams.filter(res=resolution).first()
       print(yt.title)
       stream.download()
    except Exception as e:
        status_label.configure(text=f"Error{str(e)}", text_color="white", fg_color="red")    


# создаем корневое окно
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Название окна
root.title("Youtube Downloader!")

# set min and max width and the height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080,720)

# ramka
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create a label and entry widget for the video URL
url_label = ctk.CTkLabel(content_frame, text="Enter the YouTube URL here:")
entry_url = ctk.CTkEntry(content_frame, width=400)
url_label.pack(pady=10)
entry_url.pack(pady=5)

# create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(padx=10, pady=5)

# create a resolutions combo box
resolutions = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var)
resolution_combobox.pack(padx=10, pady=5)
resolution_combobox.set("720p")

# nadpisi progress dowlnad
progress_label = ctk_CTkLabel = ctk.CTkLabel(content_frame, text="0%")


progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.6)


# metka statusa
status_label = url_label = ctk.CTkLabel(content_frame, text="Downloaded")




# start
root.mainloop()
