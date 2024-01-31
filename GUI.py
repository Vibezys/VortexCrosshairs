import sys
import customtkinter
import os
import subprocess
from PIL import Image


if os.path.exists("config.ini") == False:
    f = open("config.ini", "w")
    f.write("[RGB]\n")
    f.write("[R]\n")
    f.write("255\n")
    f.write("[G]\n")
    f.write("0\n")
    f.write("[B]\n")
    f.write("0\n")
    f.write("\n[Other]\n")
    f.write("[Crosshair Type]\n")
    f.write("1\n")
    f.close()

# Config
f = open("config.ini", "r")
n = f.readline()
n = f.readline()
R = f.readline()
n = f.readline()
G = f.readline()
n = f.readline()
B = f.readline()
n = f.readline()
n = f.readline()
n = f.readline()
ctype = f.readline()

R = int(R)
G = int(G)
B = int(B)
transparency = 0.0
ctype = int(ctype)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.vcsd_process = None

        self.title("VCSD")
        self.geometry("650x400")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = "gui_images/"
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "GUI_logo_single.png")), size=(26, 26)
        )
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "GUI_large_single.jpg")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "GUI_icon_light.png")), size=(20, 20)
        )
        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "GUI_home_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "GUI_home_light.png")),
            size=(20, 20),
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
            size=(20, 20),
        )

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="VCSD V.4",
            image=self.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image,
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.help_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Help",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.chat_image,
            anchor="w",
            command=self.help_button_event,
        )
        self.help_button.grid(row=2, column=0, sticky="ew")

        self.config_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Config",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.chat_image,
            anchor="w",
            command=self.config_button_event,
        )
        self.config_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.large_test_image
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text="Start", command=self.run_start_process
        )
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame, text="Stop", command=self.stop_vcsd_process
        )
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )

        # create third frame
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )

        # create config frame
        self.config_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.config_frame.grid_columnconfigure(0, weight=1)

        # create help frameby
        self.help_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.help_frame.grid_columnconfigure(0, weight=1)

        self.help_content_text = customtkinter.CTkTextbox(
            self.help_frame, wrap="word", state="normal", width=500, height=200
        )
        self.help_content_text.grid(row=0, column=0, padx=20, pady=10)

        # set help content dynamically
        self.update_help_content()

        # Add entry fields for configuration parameters
        # Red
        self.r_label = customtkinter.CTkLabel(self.config_frame, text="R Value:")
        self.r_label.grid(row=2, column=0, padx=20, pady=10)

        self.r_entry = customtkinter.CTkEntry(self.config_frame)
        self.r_entry.grid(row=2, column=1, padx=20, pady=10)
        self.r_entry.insert(0, str(R))

        # Green
        self.g_label = customtkinter.CTkLabel(self.config_frame, text="G Value:")
        self.g_label.grid(row=3, column=0, padx=20, pady=10)

        self.g_entry = customtkinter.CTkEntry(self.config_frame)
        self.g_entry.grid(row=3, column=1, padx=20, pady=10)
        self.g_entry.insert(0, str(G))

        # Blue
        self.b_label = customtkinter.CTkLabel(self.config_frame, text="B Value:")
        self.b_label.grid(row=4, column=0, padx=20, pady=10)

        self.b_entry = customtkinter.CTkEntry(self.config_frame)
        self.b_entry.grid(row=4, column=1, padx=20, pady=10)
        self.b_entry.insert(0, str(B))

        # Crosshair
        self.ctype_label = customtkinter.CTkLabel(
            self.config_frame, text="Crosshair Type (1 or 2):"
        )
        self.ctype_label.grid(row=5, column=0, padx=20, pady=10)

        self.ctype_entry = customtkinter.CTkEntry(self.config_frame)
        self.ctype_entry.grid(row=5, column=1, padx=20, pady=10)
        self.ctype_entry.insert(0, str(ctype))

        # Save command
        self.save_config_button = customtkinter.CTkButton(
            self.config_frame, text="Save Config", command=self.save_config
        )
        self.save_config_button.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        self.help_button.configure(
            fg_color=("gray75", "gray25") if name == "help" else "transparent"
        )
        self.config_button.configure(
            fg_color=("gray75", "gray25") if name == "config" else "transparent"
        )

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "help":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()
        if name == "config":
            self.config_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.config_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def help_button_event(self):
        self.select_frame_by_name("help")

    def config_button_event(self):
        self.select_frame_by_name("config")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def update_help_content(self):
        # You can customize this method to fetch and display help content dynamically.
        # For now, let's just update the text.
        help_text = "You can contact me on Github - https://github.com/Vibezys.\n This is the help section, where you'll find everything about VCSD you'll need to know.\n With the newest update, Version 4 it brings a whole new UI and everything. Now it's all very simple, click buttons and go.\n\n\n STILL UPDATING"
        self.help_content_text.configure(state="normal")
        self.help_content_text.delete("1.0", "end")
        self.help_content_text.insert("0.0", help_text)
        self.help_content_text.configure(state="disabled")

    def run_start_process(self):
        if self.vcsd_process is None or self.vcsd_process.poll() is not None:
            # we're in an virtual environment, so we need to use the python from the venv
            # self.vcsd_process = subprocess.Popen([sys.executable, "VCSD.py"]) this is for non-compiled
            # below is for the compiled version, i.e VCSD.exe
            self.vcsd_process = subprocess.Popen(["VCSD.exe"])

    def stop_vcsd_process(self):
        if self.vcsd_process is not None and self.vcsd_process.poll() is None:
            # Terminate VCSD.py if it's currently running
            self.vcsd_process.terminate()
            self.vcsd_process = None

    def save_config(self):
        # Get values from entry fields
        new_R = int(self.r_entry.get())
        new_G = int(self.g_entry.get())
        new_B = int(self.b_entry.get())
        new_ctype = int(self.ctype_entry.get())

        # Update the global variables
        global R, G, B, ctype
        R, G, B, ctype = new_R, new_G, new_B, new_ctype

        # Update the configuration file
        with open("config.ini", "w") as f:
            f.write(
                "[RGB]\n[R]\n{}\n[G]\n{}\n[B]\n{}\n\n[Other]\n[Crosshair Type]\n{}".format(
                    R, G, B, ctype
                )
            )


if __name__ == "__main__":
    app = App()
    app.mainloop()