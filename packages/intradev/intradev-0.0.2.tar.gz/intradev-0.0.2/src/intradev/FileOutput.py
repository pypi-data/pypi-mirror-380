
import tkinter as tk
import customtkinter as ctk
from pathlib import Path
import os
import sys
import subprocess

from .util import themeColor

class FileOutput(ctk.CTkFrame):

    def __init__(
        self,
        master,
        labelText: str = "Path",
        initialOutput: str = "Output data has not been generated.",
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
        self._textVar = ctk.StringVar(value=initialOutput)
        self._textVar.set(initialOutput)
        self.initialOutput = initialOutput
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

        linkText = "Open" #"Open File"
        self.selectLink = ctk.CTkLabel(
            self, text=linkText, font=self.linkFont, text_color=self.linkTextColor
        )
        self.selectLink.grid(row=0, column=1, sticky="w", padx=(0, 2), pady=(2, 0))
        self.selectLink.bind("<Button-1>", lambda _e: self.openDialog())

        # Entry
        entryKw = dict(font=self.entryFont, fg_color=self.surfaceColor)#, width=width)
        if entryKwargs:
            entryKw.update(entryKwargs)
        self.entry = ctk.CTkLabel(self, textvariable=self._textVar, anchor="w", **entryKw)
        self.entry.grid(row=1, column=0, columnspan=3, sticky="ew", padx=0, pady=(0, 0))

        # Underline
        self.underline = ctk.CTkFrame(
            self, height=underlineThickness, fg_color=self.underlineActive, corner_radius=0
        )
        self.underline.grid(row=2, column=0, columnspan=3, sticky="ew", padx=0, pady=(2, 0))

        # Focus color behavior
        self.entry.bind("<FocusIn>", self._onFocusIn)
        self.entry.bind("<FocusOut>", self._onFocusOut)

        # Click label/underline focuses entry
        for w in (self, self.label, self.underline):
            w.bind("<Button-1>", lambda _e: self.entry.focus_set())


    # --- Public API ---
    def openDialog(self):
        """Open the file at the stored path with the system default application."""
        if self._textVar.get() == "" or self._textVar.get() == self.initialOutput: return
        file_path = Path(self._textVar.get()).expanduser()
        if not file_path.exists():
            tk.messagebox.showerror("File not found", f"The file '{file_path}' does not exist.")
            return

        try:
            if sys.platform.startswith('darwin'):  # macOS
                subprocess.call(['open', file_path])
            elif os.name == 'nt':  # Windows
                os.startfile(file_path)
            elif os.name == 'posix':  # Linux
                subprocess.call(['xdg-open', file_path])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not open file:\n{e}")

    def get(self) -> str:
        return self._textVar.get()

    def set(self, text: str) -> None:
        self._textVar.set(text)

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
        pass

    def _onFocusOut(self, _=None):
        pass

