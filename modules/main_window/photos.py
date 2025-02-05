from PIL import Image, ImageTk

class Images:
    def load_images():
        Images.add_music = ImageTk.PhotoImage(Image.open("images/Button ADD.png"))
        Images.stop_image = ImageTk.PhotoImage(Image.open("images/Button STOP.png"))
        Images.pause_image = ImageTk.PhotoImage(Image.open("images/Button PAUSE.png"))
        Images.play_image = ImageTk.PhotoImage(Image.open("images/Button PLAY.png"))
        Images.background = ImageTk.PhotoImage(Image.open("images/Window treks.png"))
        Images.delete_image = ImageTk.PhotoImage(Image.open("images/Button Delete.png"))
        Images.mix_music = ImageTk.PhotoImage(Image.open("images/Button MIX.png"))
        Images.button_skip = ImageTk.PhotoImage(Image.open("images/Button _.png"))