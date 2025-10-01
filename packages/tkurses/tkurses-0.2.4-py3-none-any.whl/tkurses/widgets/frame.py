from .base import Widget
from curses.textpad import rectangle as rect
import curses
import os

class Frame(Widget):
    def __init__(self, title, pos, size):
        super().__init__(pos[0],pos[1], size[0], size[1])
        self.title = title
        self.children = []
        self.currentSellection = 0

    def render(self):
        # Skip rendering if size is invalid or exceeds terminal
        if self.width is None or self.height is None:
            return
        try:
            terminal_size = [os.get_terminal_size().columns - 1, os.get_terminal_size().lines - 1]
            if self.x + self.width > terminal_size[0] or self.y + self.height > terminal_size[1]:
                return  # Skip rendering instead of exiting
        except OSError:
            return  # Skip rendering if terminal size cannot be determined

        # Draw frame border
        rect(self.app.stdscr, self.y, self.x, self.y + self.height - 1, self.x + self.width - 1)

        # Draw title with theme color
        if self.title:
            max_title_width = self.width - 4  # Account for border and padding
            if max_title_width > 0:
                truncated_title = self.title[:max_title_width]
                self.app.stdscr.addstr(self.y, self.x + 2, f" {truncated_title} ")

        # Render children
        for child in self.children:

            child.render()

    def handle_input(self, key: int) -> bool:
        if self.children[self.currentSellection].handle_input(key):
            return True
        if key == curses.KEY_RIGHT:
            self.currentSellection += 1
            self.currentSellection %= len(self.children)-1
        return False
    
    def add_child(self, widget):
        self.children.append(widget)