
import customtkinter as ctk

def themeColor(widgetKey, prop):
    """Return the current theme color for a widget/prop, resolved to current mode."""
    val = ctk.ThemeManager.theme[widgetKey][prop]
    if isinstance(val, (list, tuple)):
        return val[0] if ctk.get_appearance_mode() == "Light" else val[1]
    return val