import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from core.constants import *

class HomeScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DocDiff")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(1200, 800)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color=BACKGROUND)

        self.old_file_path = ""
        self.new_file_path = ""

        self.compare_mode = ctk.StringVar(value="excel")

        self.build_ui()

    def build_ui(self):
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=SIDEBAR)
        self.sidebar.pack(side="left", fill="y")

        self.content = ctk.CTkFrame(self, fg_color=BACKGROUND)
        self.content.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(self.sidebar, text="DocDiff", font=TITLE_FONT).pack(pady=(40,5))
        ctk.CTkLabel(self.sidebar, text="v0.1", text_color=SUBTEXT).pack(pady=(0,30))

        for txt in ["🏠 Home","📊 Compare","🔍 Review","📄 Reports","⚙ Settings","🚪 Exit"]:
            ctk.CTkButton(self.sidebar,text=txt,width=180,fg_color="transparent",
                          hover_color="#303030",anchor="w").pack(pady=6)

        ctk.CTkLabel(self.content,text="Engineering Revision Verification Tool",
                     font=TITLE_FONT).pack(anchor="w",padx=30,pady=(25,5))

        cards=ctk.CTkFrame(self.content,fg_color="transparent")
        cards.pack(fill="x",padx=30,pady=20)

        self.old_label=self._card(cards,"📄 OLD FILE",self.browse_old)
        self.new_label=self._card(cards,"📄 NEW FILE",self.browse_new,right=True)

        opts=ctk.CTkFrame(self.content,fg_color="transparent")
        opts.pack(fill="x",padx=30)

        ctk.CTkRadioButton(opts,text="Excel ↔ Excel",variable=self.compare_mode,
                           value="excel").pack(anchor="w")
        ctk.CTkRadioButton(opts,text="PDF ↔ PDF",variable=self.compare_mode,
                           value="pdf").pack(anchor="w",pady=5)

        self.compare_btn=ctk.CTkButton(self.content,text="Compare Files",
                                       state="disabled")
        self.compare_btn.pack(pady=20)

    def _card(self,parent,title,command,right=False):
        pad=(10,0) if right else (0,10)
        card=ctk.CTkFrame(parent,fg_color=CARD,corner_radius=15,height=180)
        card.pack(side="left",expand=True,fill="both",padx=pad)
        ctk.CTkLabel(card,text=title,font=HEADING_FONT).pack(pady=(20,10))
        label=ctk.CTkLabel(card,text="No file selected",text_color=SUBTEXT)
        label.pack()
        ctk.CTkButton(card,text="Browse",command=command).pack(pady=20)
        return label

    def browse_old(self):
        path=self.pick_file()
        if path:
            self.old_file_path=path
            self.old_label.configure(text=Path(path).name)
            self.update_compare()

    def browse_new(self):
        path=self.pick_file()
        if path:
            self.new_file_path=path
            self.new_label.configure(text=Path(path).name)
            self.update_compare()

    def pick_file(self):
        if self.compare_mode.get()=="excel":
            types=[("Excel Files","*.xlsx *.xls")]
        else:
            types=[("PDF Files","*.pdf")]
        return filedialog.askopenfilename(filetypes=types)

    def update_compare(self):
        if self.old_file_path and self.new_file_path:
            self.compare_btn.configure(state="normal")