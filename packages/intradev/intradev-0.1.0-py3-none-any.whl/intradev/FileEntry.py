
import os
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

from .util import themeColor

class FileEntry(ctk.CTkFrame):
    """
    A labeled entry with an underline that turns orange when focused.
    Includes a small clickable 'Select Folder' or 'Select File' link next to the label.
    Users may type a path OR click the link to open a dialog. The chosen path
    replaces the entry content.

    Parameters (camelCase):
        labelText: str                           -> Title text above the entry
        selectMode: str = "folder"               -> "folder" or "file" (compile-time / code-set, not user toggle)
        surfaceColor: (light, dark) tuple        -> Uniform background for frame & entry
        underlineInactive: (light, dark) tuple   -> Unfocused underline color (gray in light, white in dark)
        underlineActive: str                     -> Focused underline color (orange)
        linkTextColor: (light, dark) tuple       -> Color for the "Select ..." link
        width: int                               -> Entry width (px)
        entryFont, labelFont: CTkFont|None       -> Fonts
        underlineThickness: int                  -> Underline thickness (px)
        entryKwargs: dict|None                   -> Extra CTkEntry kwargs (e.g., placeholder_text)
        fileTypes: list[tuple[str, str]]         -> Used when selectMode == "file"
        dialogTitle: str|None                    -> Custom dialog title (defaults based on selectMode)
    """
    def __init__(
        self,
        master,
        labelText: str = "Path",
        placeholderText: str = "Choose a File or Type a Path",
        selectMode: str = "folder",  # "folder" or "file"
        surfaceColor = themeColor("CTkFrame", "fg_color"),
        underlineInactive = themeColor("CTkButton", "hover_color"),   # gray (light) / white (dark)
        underlineActive = themeColor("CTkButton", "fg_color"),                                 # orange when focused
        linkTextColor = ("#1a73e8", "#8ab4f8"),                         # blue-ish
        #width: int = 320,
        entryFont: ctk.CTkFont | None = None,
        labelFont: ctk.CTkFont | None = None,
        underlineThickness: int = 2,
        entryKwargs: dict | None = None,
        fileTypes = (("All Files", "*.*"),),
        dialogTitle: str | None = None,
        **kwargs
    ):
        super().__init__(master, fg_color=surfaceColor, **kwargs)

        # --- Config ---
        self.selectMode = "folder" if str(selectMode).lower() != "file" else "file"
        self.surfaceColor = surfaceColor
        self.underlineInactive = underlineInactive
        self.underlineActive = underlineActive
        self.linkTextColor = linkTextColor
        self.fileTypes = fileTypes
        self.dialogTitle = dialogTitle

        # Fonts
        self.labelFont = labelFont or ctk.CTkFont(size=11)
        self.entryFont = entryFont or ctk.CTkFont(size=13)
        self.linkFont = ctk.CTkFont(size=10)  # smaller "Select ..." text

        # --- Layout ---
        self.grid_columnconfigure(0, weight=0)  # label
        self.grid_columnconfigure(1, weight=0)  # clickable link
        self.grid_columnconfigure(2, weight=1)  # spacer for entry below

        # Top row: label + select link
        self.label = ctk.CTkLabel(self, text=labelText, font=self.labelFont, anchor="w")
        self.label.grid(row=0, column=0, sticky="w", padx=(2, 6), pady=(2, 0))

        linkText = "Select Folder" if self.selectMode == "folder" else "Select File"
        self.selectLink = ctk.CTkLabel(
            self, text=linkText, font=self.linkFont, text_color=self.linkTextColor
        )
        self.selectLink.grid(row=0, column=1, sticky="w", padx=(0, 2), pady=(2, 0))
        self.selectLink.bind("<Button-1>", lambda _e: self.openDialog())

        # Entry
        entryKw = dict(font=self.entryFont, border_width=0, fg_color=self.surfaceColor)#, width=width)
        if entryKwargs:
            entryKw.update(entryKwargs)
        self.entry = ctk.CTkEntry(self, placeholder_text=placeholderText, **entryKw)
        self.entry.grid(row=1, column=0, columnspan=3, sticky="ew", padx=0, pady=(0, 0))

        # Underline
        self.underline = ctk.CTkFrame(
            self, height=underlineThickness, fg_color=self.underlineInactive, corner_radius=0
        )
        self.underline.grid(row=2, column=0, columnspan=3, sticky="ew", padx=0, pady=(2, 0))

        # Focus color behavior
        self.entry.bind("<FocusIn>", self._onFocusIn)
        self.entry.bind("<FocusOut>", self._onFocusOut)

        # Click label/underline focuses entry
        for w in (self, self.label, self.underline):
            w.bind("<Button-1>", lambda _e: self.entry.focus_set())

        # Start inactive
        self._applyInactive()

    # --- Public API ---
    def openDialog(self):
        """Open folder/file dialog and replace entry text with the chosen path."""
        initDir = self._initialDirFromEntry()
        path = ""

        if self.selectMode == "folder":
            title = self.dialogTitle or "Select Folder"
            path = filedialog.askdirectory(parent=self.winfo_toplevel(), title=title, initialdir=initDir)
        else:
            title = self.dialogTitle or "Select File"
            path = filedialog.askopenfilename(
                parent=self.winfo_toplevel(), title=title, initialdir=initDir, filetypes=self.fileTypes
            )

        if path:
            self.set(os.path.normpath(path))  # replace existing text with the new path
            # briefly show active underline to acknowledge selection
            self._applyActive()
            self.after(120, self._applyInactive)

    def get(self) -> str:
        return self.entry.get()

    def set(self, text: str) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def focusEntry(self) -> None:
        self.entry.focus_set()

    def configureEntry(self, **kwargs):
        self.entry.configure(**kwargs)

    # Optional: expose textvariable for external binding
    @property
    def textvariable(self):
        return self.entry.cget("textvariable")
    @textvariable.setter
    def textvariable(self, var):
        self.entry.configure(textvariable=var)

    # --- Internal helpers ---
    def _initialDirFromEntry(self) -> str:
        txt = self.get().strip()
        if txt and os.path.isdir(txt):
            return txt
        if txt and os.path.isfile(txt):
            return os.path.dirname(txt)
        return os.path.expanduser("~")  # default

    def _onFocusIn(self, _=None):
        self._applyActive()

    def _onFocusOut(self, _=None):
        self._applyInactive()

    def _applyActive(self):
        self.underline.configure(fg_color=self.underlineActive)

    def _applyInactive(self):
        self.underline.configure(fg_color=self.underlineInactive)


# --- Minimal demo ---
if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    root = ctk.CTk()
    root.geometry("560x220")

    # Folder mode (default)
    folderField = FileEntry(
        root,
        labelText="Assets Directory",
        selectMode="folder",
        entryKwargs={"placeholder_text": "Choose a folder or type a path…"}
    )
    folderField.pack(fill="x", padx=16, pady=(16, 8))

    # File mode
    fileField = FileEntry(
        root,
        labelText="Config File",
        selectMode="file",
        fileTypes=(("JSON Files", "*.json"), ("YAML Files", "*.yml *.yaml"), ("All Files", "*.*")),
        entryKwargs={"placeholder_text": "Select a file or type a path…"}
    )
    fileField.pack(fill="x", padx=16, pady=(0, 16))

    root.mainloop()
