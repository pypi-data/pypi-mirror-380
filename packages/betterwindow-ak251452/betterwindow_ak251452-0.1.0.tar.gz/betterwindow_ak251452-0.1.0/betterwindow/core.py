"""
BetterWindow - Custom Tkinter Window Library
============================================

A library for creating custom windows in tkinter with custom title bars,
buttons, and hover effects.

Classes:
    CustomWindow: Base class for custom windows
    CButton: Custom button with hover effects  
    CustomTk: Custom main window
    CustomToplevel: Custom dialog window

Colors:
    LGRAY: Light gray (#232323)
    DGRAY: Dark gray (#161616) 
    RGRAY: Regular gray (#2c2c2c)
    MGRAY: Medium gray (#1D1c1c)
"""

import tkinter as tk
from tkinter import ttk

# Import specific tkinter components for convenience
from tkinter import Tk, Toplevel, Frame, Button, Label
from tkinter import LEFT, RIGHT, X, BOTH

# Color constants
LGRAY = '#232323'
DGRAY = '#161616'
RGRAY = '#2c2c2c'
MGRAY = '#1D1c1c'

class CustomWindow:
    """
    Custom window base class with custom title bar and window controls.
    
    This class provides a custom title bar with minimize and close buttons,
    window dragging functionality, and custom styling.
    
    Attributes:
        tk_title (str): Window title text
        LGRAY, DGRAY, RGRAY, MGRAY (str): Color constants for styling
        title_bar (Frame): Custom title bar frame
        close_button (Button): Window close button
        minimize_button (Button): Window minimize button
        title_bar_title (Label): Title label in title bar
        window (Frame): Main content area frame
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize custom window with default settings."""
        self.tk_title = "BetterWindow"
        self.LGRAY = LGRAY
        self.DGRAY = DGRAY
        self.RGRAY = RGRAY
        self.MGRAY = MGRAY
        self._setup_window()
    
    def _setup_window(self):
        """Setup custom window elements including title bar and controls."""
        try:
            # Create title bar
            self.title_bar = Frame(self, bg=self.RGRAY, relief='raised', bd=0, 
                                  highlightthickness=1, highlightbackground=self.MGRAY)
            
            # Create control buttons
            self.close_button = Button(self.title_bar, text='  ×  ', command=self._safe_destroy, 
                                      bg=self.RGRAY, padx=2, pady=2, font=("calibri", 13), 
                                      bd=0, fg='lightgray', highlightthickness=0)
            
            self.minimize_button = Button(self.title_bar, text=' 🗕 ', command=self.minimize_me, 
                                         bg=self.RGRAY, padx=2, pady=2, bd=0, fg='lightgray', 
                                         font=("calibri", 13), highlightthickness=0)
            
            # Create title label
            self.title_bar_title = Label(self.title_bar, text=self.tk_title, bg=self.RGRAY, 
                                        bd=0, fg='lightgray', font=("helvetica", 10))
            
            # Create main content area
            self.window = Frame(self, bg=self.DGRAY, highlightthickness=1, 
                               highlightbackground=self.MGRAY)
            
            # Pack elements
            self._pack_elements()
            
            # Bind events
            self._bind_events()
            
            # Setup window behavior
            self.after(10, lambda: self._setup_window_behavior())
            
        except Exception as e:
            print(f"Warning: Error setting up custom window: {e}")
    
    def _pack_elements(self):
        """Pack title bar and window elements in correct order."""
        self.title_bar.pack(fill=X)
        self.title_bar_title.pack(side=LEFT, padx=10)
        self.close_button.pack(side=RIGHT, ipadx=7, ipady=1)
        self.minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
        self.window.pack(expand=1, fill=BOTH)
        self.window.pack_propagate(1)

    def _bind_events(self):
        """Bind mouse events for window dragging and button hover effects."""
        self.title_bar.bind('<Button-1>', self.get_pos)
        self.title_bar_title.bind('<Button-1>', self.get_pos)
        self.close_button.bind('<Enter>', lambda e: self.changex_on_hovering())
        self.close_button.bind('<Leave>', lambda e: self.returnx_to_normalstate())
        
        if hasattr(self, 'winfo_class') and self.winfo_class() == 'Tk':
            self.bind("<Expose>", lambda e: self.deminimize())
    
    def _setup_window_behavior(self):
        """Setup platform-specific window behavior."""
        self.set_appwindow()
    
    def _safe_destroy(self):
        """Safely destroy the window with error handling."""
        try:
            self.destroy()
        except Exception as e:
            print(f"Warning: Error destroying window: {e}")
            # Force exit if normal destroy fails
            try:
                if hasattr(self, 'quit'):
                    self.quit()
            except:
                pass
    
    def get_pos(self, event):
        """
        Handle window dragging functionality.
        
        Args:
            event: Mouse click event to start dragging
        """
        try:
            xwin = self.winfo_x()
            ywin = self.winfo_y()
            startx = event.x_root
            starty = event.y_root
            ywin = ywin - starty
            xwin = xwin - startx
            
            def move_window(event):
                try:
                    self.config(cursor="fleur")
                    new_x = event.x_root + xwin
                    new_y = event.y_root + ywin
                    # Prevent window from going completely off-screen
                    new_x = max(-self.winfo_width() + 100, new_x)
                    new_y = max(0, new_y)
                    self.geometry(f'+{new_x}+{new_y}')
                except Exception as e:
                    print(f"Warning: Error moving window: {e}")

            def release_window(event):
                try:
                    self.config(cursor="arrow")
                except Exception as e:
                    print(f"Warning: Error releasing window: {e}")

            self.title_bar.bind('<B1-Motion>', move_window)
            self.title_bar_title.bind('<B1-Motion>', move_window)
            self.title_bar.bind('<ButtonRelease-1>', release_window)
            self.title_bar_title.bind('<ButtonRelease-1>', release_window)
            
        except Exception as e:
            print(f"Warning: Error setting up window dragging: {e}")
    
    def set_appwindow(self):
        """
        Set window to appear in taskbar (Windows-specific).
        This function handles Windows-specific window behavior.
        """
        try:
            # Only attempt this on Windows
            import platform
            if platform.system() != "Windows":
                return
                
            from ctypes import windll
            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080
            
            hwnd = windll.user32.GetParent(self.winfo_id())
            if hwnd:
                stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                stylew = stylew & ~WS_EX_TOOLWINDOW
                stylew = stylew | WS_EX_APPWINDOW
                windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
                self.wm_withdraw()
                self.after(10, lambda: self.wm_deiconify())
        except Exception as e:
            print(f"Info: Could not set window appearance (this is normal on non-Windows systems): {e}")
    
    def minimize_me(self):
        """
        Minimize window with improved state management.
        """
        try:
            if hasattr(self, 'wm_state'):
                self.overrideredirect(False)
                self.wm_state('iconic')
                # Store the fact that we're minimized
                self._is_minimized = True
        except Exception as e:
            print(f"Warning: Error minimizing window: {e}")
    
    def deminimize(self):
        """
        Restore window from minimized state.
        """
        try:
            if hasattr(self, '_is_minimized') and self._is_minimized:
                self.overrideredirect(True) 
                self.wm_state('normal')
                self._is_minimized = False
        except Exception as e:
            print(f"Warning: Error restoring window: {e}")
    
    def changex_on_hovering(self):
        """Apply hover effect to close button."""
        try:
            self.close_button['bg'] = 'red'
        except Exception as e:
            print(f"Warning: Error changing close button color: {e}")
    
    def returnx_to_normalstate(self):
        """Return close button to normal state."""
        try:
            self.close_button['bg'] = self.RGRAY
        except Exception as e:
            print(f"Warning: Error resetting close button color: {e}")
    
    def set_title(self, title):
        """
        Set window title.
        
        Args:
            title (str): New window title
        """
        try:
            self.tk_title = title
            if hasattr(self, 'title_bar_title'):
                self.title_bar_title.config(text=self.tk_title)
            if hasattr(self, 'title'):
                self.title(self.tk_title)
        except Exception as e:
            print(f"Warning: Error setting window title: {e}")


class CButton(Button):
    """
    Custom button with hover effects and press animations.
    
    This button provides visual feedback through color changes on hover
    and relief changes on press/release events.
    
    Inherits from tkinter.Button and adds:
    - Hover color effects
    - Press/release visual feedback
    - Consistent styling with the custom window theme
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize custom button with default styling and event bindings.
        
        Args:
            *args: Arguments passed to tkinter.Button
            **kwargs: Keyword arguments passed to tkinter.Button
        """
        Button.__init__(self, *args, **kwargs)
        
        # Apply default styling
        self.config(
            bg=RGRAY, 
            padx=2, 
            pady=2, 
            bd=0, 
            fg='lightgray',
            highlightthickness=0, 
            relief='flat',
            font=("helvetica", 10)
        )
        
        # Bind hover and press events
        self._bind_events()

    def _bind_events(self):
        """Bind mouse events for interactive effects."""
        try:
            self.bind('<Enter>', self.on_enter)
            self.bind('<Leave>', self.on_leave)
            self.bind('<ButtonPress-1>', self.on_press)
            self.bind('<ButtonRelease-1>', self.on_release)
        except Exception as e:
            print(f"Warning: Error binding button events: {e}")

    def on_enter(self, event, color='gray'):
        """
        Handle mouse enter event (hover effect).
        
        Args:
            event: Mouse enter event
            color (str): Color to change to on hover
        """
        try:
            self.config(bg=color)
        except Exception as e:
            print(f"Warning: Error changing button hover color: {e}")

    def on_leave(self, event):
        """
        Handle mouse leave event (return to normal color).
        
        Args:
            event: Mouse leave event
        """
        try:
            self.config(bg=RGRAY)
        except Exception as e:
            print(f"Warning: Error resetting button color: {e}")

    def on_press(self, event):
        """
        Handle mouse press event (pressed appearance).
        
        Args:
            event: Mouse press event
        """
        try:
            self.config(relief='sunken')
        except Exception as e:
            print(f"Warning: Error changing button press appearance: {e}")

    def on_release(self, event):
        """
        Handle mouse release event (return to flat appearance).
        
        Args:
            event: Mouse release event
        """
        try:
            self.config(relief='flat')
        except Exception as e:
            print(f"Warning: Error resetting button relief: {e}")


class CustomTk(Tk, CustomWindow):
    """
    Custom main window based on tkinter.Tk.
    
    This is the main application window with custom title bar,
    borderless design, and custom styling.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize custom main window.
        
        Args:
            *args: Arguments passed to tkinter.Tk
            **kwargs: Keyword arguments passed to tkinter.Tk
        """
        Tk.__init__(self, *args, **kwargs)
        CustomWindow.__init__(self, *args, **kwargs)
        
        # Set default title
        self.tk_title = "BetterWindow App"
        
        # Configure window appearance
        try:
            self.overrideredirect(True)  # Remove default title bar
            self.config(bg=self.DGRAY, highlightthickness=0)
            
            # Set initial size and position
            self.geometry("800x600")
            self._center_window()
            
        except Exception as e:
            print(f"Warning: Error configuring CustomTk: {e}")
    
    def _center_window(self):
        """Center the window on screen."""
        try:
            self.update_idletasks()
            x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
            y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
            self.geometry(f"+{x}+{y}")
        except Exception as e:
            print(f"Warning: Error centering window: {e}")


class CustomToplevel(Toplevel, CustomWindow):
    """
    Custom dialog window based on tkinter.Toplevel.
    
    This is used for additional windows like dialogs, popups,
    or secondary windows in the application.
    """
    
    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize custom toplevel window.
        
        Args:
            parent: Parent window (optional)
            *args: Arguments passed to tkinter.Toplevel
            **kwargs: Keyword arguments passed to tkinter.Toplevel
        """
        Toplevel.__init__(self, parent, *args, **kwargs)
        CustomWindow.__init__(self, *args, **kwargs)
        
        # Set default title
        self.tk_title = "BetterWindow Dialog"
        
        # Configure window appearance
        try:
            self.overrideredirect(True)  # Remove default title bar
            self.config(bg=self.DGRAY, highlightthickness=0)
            
            # Set initial size and make modal if parent exists
            self.geometry("400x300")
            if parent:
                self.transient(parent)
                self.grab_set()
                
            self._center_on_parent(parent)
            
        except Exception as e:
            print(f"Warning: Error configuring CustomToplevel: {e}")
    
    def _center_on_parent(self, parent):
        """Center this window on its parent window."""
        try:
            if parent:
                self.update_idletasks()
                parent.update_idletasks()
                
                # Get parent position and size
                px = parent.winfo_x()
                py = parent.winfo_y()
                pw = parent.winfo_width()
                ph = parent.winfo_height()
                
                # Calculate center position
                x = px + (pw // 2) - (self.winfo_width() // 2)
                y = py + (ph // 2) - (self.winfo_height() // 2)
                
                self.geometry(f"+{x}+{y}")
            else:
                # Center on screen if no parent
                self.update_idletasks()
                x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
                y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
                self.geometry(f"+{x}+{y}")
                
        except Exception as e:
            print(f"Warning: Error centering dialog: {e}")
