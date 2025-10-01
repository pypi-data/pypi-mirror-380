import curses
from curses import panel
from typing import List, Optional
from tkurses.themes import ThemeManager

class App:
    def __init__(self, stdscr, theme=None):
        self.stdscr = stdscr
        if theme==None:
            theme="defalutTheme.json"
            with open(theme,"a") as file:
                file.write('''{
    "colors": {
        "background": "black",
        "forground": "white"
    },
    "input": {
        "style": "default",
        "colors": {
            "focused": {
                "background": "black",
                "forground": "white"
            }, "not-focused": {
                "forground": "black",
                "background": "white"
            }
        }
    },
    "text": {
        "colors": {
            "background": "blue",
            "forground": "black"
        },
        "theme": "None",
        "quitKeys": ["Enter","shift-enter"]
    },
    "buttons": {
        "colors": {
            "focused": { "background": "white", "forground": "black"},
            "not-focused": {"background": "black","forground": "white"}
        },
        "start": {"focused":"[","not-focused":"<"},
        "end": {"focused": "]","not-focused":">"}
    }
}''')
        self.theme = ThemeManager(stdscr=stdscr ,themeFile=theme)
        self.widgets: List["Widget"] = []
        self.focus_index = 0
        self.x=0
        self.y=0
        self.ph = 100
        self.ph = 100

        curses.curs_set(0)  # Hide cursor
        curses.start_color()
        curses.use_default_colors()

        self.running = True

    def add_widget(self, widget, parent):
        widget.set_app(self)
        if parent == self:
            self.widgets.append(widget)
            widget.render()
        else:
            parent.add_child(widget)


    def focus_next(self):
        if not self.widgets:
            return
        self.focus_index = (self.focus_index + 1) % len(self.widgets)
        for widget in self.widgets:
            widget.set_focus(False)
        self.widgets[self.focus_index].set_focus(True)
        self.refresh()

    def refresh(self):
        self.stdscr.clear()
        for widget in self.widgets:
            widget.render()
        self.stdscr.refresh()

    def handle_input(self, key):
        if not self.widgets:
            return

        focused = self.widgets[self.focus_index]
        handled = focused.handle_input(key)

        if not handled and key == 9:  # 9 is ASCII for Tab
            self.focus_next()

    def mainloop(self):
        self.refresh()
        while self.running:
            key = self.stdscr.getch()
            if key == 27:  # ESC key to quit
                self.running = False
            else:
                self.handle_input(key)
                for object in self.widgets:
                    object.update()
                self.refresh()

    def stop(self):
        self.running = False