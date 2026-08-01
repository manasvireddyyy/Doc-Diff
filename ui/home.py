import customtkinter as ctk
from core.constants import *


class HomeScreen(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("DocDiff")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(1200, 800)

        ctk.set_appearance_mode("dark")

        self.configure(fg_color=BACKGROUND)

        self.compare_mode = ctk.StringVar(value="excel")

        self.create_layout()

    # ==================================================
    # MAIN LAYOUT
    # ==================================================

    def create_layout(self):

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.sidebar.pack(side="left", fill="y")

        # Main Content
        self.content = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.content.pack(side="right", fill="both", expand=True)

        self.create_sidebar()
        self.create_header()
        self.create_file_cards()
        self.create_compare_section()
        self.create_statistics()
        self.create_footer()

    # ==================================================
    # SIDEBAR
    # ==================================================

    def create_sidebar(self):

        title = ctk.CTkLabel(
            self.sidebar,
            text="DocDiff",
            font=TITLE_FONT
        )

        title.pack(pady=(40, 5))

        version = ctk.CTkLabel(
            self.sidebar,
            text="v0.1",
            text_color=SUBTEXT,
            font=TEXT_FONT
        )

        version.pack(pady=(0, 30))

        buttons = [
            "🏠 Home",
            "📊 Compare",
            "🔍 Review",
            "📄 Reports",
            "⚙ Settings",
            "🚪 Exit"
        ]

        for item in buttons:

            btn = ctk.CTkButton(
                self.sidebar,
                text=item,
                width=180,
                height=45,
                fg_color="transparent",
                hover_color="#303030",
                anchor="w"
            )

            btn.pack(pady=8)

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        header.pack(fill="x", padx=30, pady=(25, 15))

        title = ctk.CTkLabel(
            header,
            text="Engineering Revision Verification Tool",
            font=TITLE_FONT
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Compare Excel and PDF revisions quickly",
            text_color=SUBTEXT,
            font=TEXT_FONT
        )

        subtitle.pack(anchor="w")

    # ==================================================
    # FILE CARDS
    # ==================================================

    def create_file_cards(self):

        files = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        files.pack(fill="x", padx=30, pady=10)

        self.create_single_card(files, "📄 OLD FILE").pack(
            side="left",
            expand=True,
            fill="both",
            padx=(0, 10)
        )

        self.create_single_card(files, "📄 NEW FILE").pack(
            side="left",
            expand=True,
            fill="both",
            padx=(10, 0)
        )

    def create_single_card(self, parent, title):

        card = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=15,
            height=180
        )

        heading = ctk.CTkLabel(
            card,
            text=title,
            font=HEADING_FONT
        )

        heading.pack(pady=(20, 10))

        filename = ctk.CTkLabel(
            card,
            text="No file selected",
            text_color=SUBTEXT
        )

        filename.pack()

        browse = ctk.CTkButton(
            card,
            text="Browse",
            width=140
        )

        browse.pack(pady=20)

        return card

    # ==================================================
    # COMPARE SECTION
    # ==================================================

    def create_compare_section(self):

        compare = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        compare.pack(fill="x", padx=30, pady=20)

        left = ctk.CTkFrame(compare, fg_color="transparent")
        left.pack(side="left")

        ctk.CTkRadioButton(
            left,
            text="Excel ↔ Excel",
            variable=self.compare_mode,
            value="excel"
        ).pack(anchor="w")

        ctk.CTkRadioButton(
            left,
            text="PDF ↔ PDF",
            variable=self.compare_mode,
            value="pdf"
        ).pack(anchor="w", pady=5)

        right = ctk.CTkFrame(compare, fg_color="transparent")
        right.pack(side="right")

        dropdown = ctk.CTkComboBox(
            right,
            values=["Equipment Name"]
        )

        dropdown.pack()

        button = ctk.CTkButton(
            self.content,
            text="Compare Files",
            width=250,
            height=50
        )

        button.pack(pady=20)

    # ==================================================
    # STATISTICS
    # ==================================================

    def create_statistics(self):

        stats = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        stats.pack(fill="x", padx=30)

        titles = [
            "Compared",
            "Changed",
            "Added",
            "Deleted"
        ]

        for title in titles:

            card = ctk.CTkFrame(
                stats,
                fg_color=CARD,
                corner_radius=15,
                width=180,
                height=110
            )

            card.pack(
                side="left",
                padx=10,
                expand=True
            )

            label = ctk.CTkLabel(
                card,
                text=title,
                font=HEADING_FONT
            )

            label.pack(pady=(15, 5))

            number = ctk.CTkLabel(
                card,
                text="0",
                font=("Arial", 28, "bold")
            )

            number.pack()

    # ==================================================
    # FOOTER
    # ==================================================

    def create_footer(self):

        footer = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        footer.pack(fill="x", padx=30, pady=30)

        buttons = [
            "Review Differences",
            "Export Report",
            "Settings",
            "Exit"
        ]

        for text in buttons:

            btn = ctk.CTkButton(
                footer,
                text=text,
                width=180,
                height=45
            )

            btn.pack(side="left", padx=10)