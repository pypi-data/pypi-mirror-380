
import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from .FileEntry import FileEntry
from .FileOutput import FileOutput

class DataModel():
    def __init__(self):
        super().__init__()
        self.inputs = {}
        self.functions = {}
        self.outputs = {}
        
    def addInput(self, label, type="file", id=None):
        id = label if id is None else id
        #1. Check if ID is unique
        if id in self.inputs:
            print(f"ERROR: All input IDs must be unique. '{id}' already in use as input ID.")
            return
        #2. Add input to inputs dictionary
        self.inputs[id] = {
            "label" : label,
            "type": type,
        }
        
    def addFunction(self, func, label, inputMap=None, outputIDs=None):
        #1. Check if name is unique
        if func in self.functions:
            print(f"ERROR: Function name must be unique. '{func}' already in use as function.")
        #2. Add function to functions dictionary
        self.functions[func] = {
                                "label": label,
                                "inputMap": inputMap, # {paramName: inputID}
                                "outputIDs": outputIDs, # [outputID]
                                }
    
    def addOutput(self, label, type="file", id=None):
        id = label if id is None else id
        #1. Check if ID is unique
        if id in self.outputs:
            print(f"ERROR: All output IDs must be unique. '{id}' already in use as output ID.")
            return
        #2. Add output to outputs dictionary
        self.outputs[id] = {
            "label" : label,
            "type": type,
        }
        
    
def buildUI(data, title):
    app = _UIConstructor(data, title=title)
    app.geometry("900x500")
    app.mainloop()



class _UIConstructor(ctk.CTk):
    def __init__(self, dataModel: DataModel, title: str = "IntraDev GUI", browseFirstInput: bool = True):
        super().__init__()
        self.title(title)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.dataModel = dataModel
        self.browseFirstInput = browseFirstInput

        self.inputWidgets = {}
        self.outputWidgets = {}

        # Root layout: single column, everything stacked vertically
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Scrollable container for all sections
        self.scroll = ctk.CTkScrollableFrame(self, corner_radius=12)
        self.scroll.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        self.scroll.grid_columnconfigure(0, weight=1)

        # Build sections: Inputs -> Functions -> Outputs
        self._buildInputsSection()
        self._buildFunctionsSection()
        self._buildOutputsSection()

        # Status bar
        self.statusVar = ctk.StringVar(value="Ready")
        ctk.CTkLabel(self, textvariable=self.statusVar, anchor="w", height=24)\
            .grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))

    # --------- Sections ----------
    def _section(self, titleText: str):
        frame = ctk.CTkFrame(self.scroll, corner_radius=12)
        frame.grid(sticky="ew", padx=0, pady=(0, 12))
        frame.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(frame, text=titleText, font=("", 16, "bold"))
        title.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 6))
        return frame

    def _buildInputsSection(self):
        frame = self._section("Inputs")
        for i, (inpId, data) in enumerate(self.dataModel.inputs.items(), start=1):
            row = ctk.CTkFrame(frame, fg_color="transparent")
            row.grid(row=i, column=0, sticky="ew", padx=12, pady=6)
            row.grid_columnconfigure(0, weight=1)
            entry = FileEntry(master=row, labelText=data.get("label", f"Input {i}"), placeholderText="", selectMode="file")
            entry.grid(row=0, column=0, sticky="ew")
            self.inputWidgets[inpId] = entry

    def _buildFunctionsSection(self):
        frame = self._section("Functions")
        for i, (func, data) in enumerate(self.dataModel.functions.items(), start=1):
            inputIDMap  = data.get("inputMap", {})
            outputIDs = data.get("outputs", [])
            label      = data.get("label") or getattr(func, "__name__", "Run")
            # Build a command that reads inputs at click-time and calls the function
            def runFunc(f=func, inIDs=inputIDMap, outIDs=outputIDs):
                try:
                    kwargs = {}
                    for paramName, inputID in inputIDMap.items():
                        widgetValue = self.inputWidgets.get(inputID).get()
                        kwargs[paramName] = widgetValue
                    
                    outputs = f(**kwargs)
                    self._setStatus(f"Ran '{getattr(f, '__name__', 'function')}' successfully.")
                    self.assignOutputData(outputs)
                except Exception as e:
                    self._setStatus(f"ERROR: {e}")
                    
            ctk.CTkButton(frame, text=label, command=lambda: runFunc()).grid(row=i, column=0, sticky="ew", padx=12, pady=6)

    def _buildOutputsSection(self):
        frame = self._section("Outputs")
        for i, (outId, data) in enumerate(self.dataModel.outputs.items(), start=1):
            label = data.get("label", f"Output {i}")
            row = ctk.CTkFrame(frame, fg_color="transparent")
            row.grid(row=i, column=0, sticky="ew", padx=12, pady=6)
            row.grid_columnconfigure(0, weight=1)
            entry = FileOutput(master=row, labelText=label, initialOutput="")
            entry.grid(row=1, column=0, sticky="ew")
            self.outputWidgets[outId] = entry

    # --------- Actions ----------
    def _setStatus(self, text: str):
        self.statusVar.set(text)
        
    def assignOutputData(self, outputs):
        for id, data in outputs.items():
            widget = self.outputWidgets.get(id, None)
            if widget is None: return
            widget.set(data)
