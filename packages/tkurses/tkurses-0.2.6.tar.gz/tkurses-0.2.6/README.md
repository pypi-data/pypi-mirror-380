# TKurses

tkurses is a library for tkinter like interface in curses

# basic program

```
import curses
import tkurses.core as core
import tkurses.widgets as widgits

def main(stdscr):
    app = core.App(screen, "theme.json")
    app.addWidget(app.Label("Hello World!", 0,0))

    app.main_loop()

curses.wrapper(main)
```

## Widgets

### Label

Declaring one

```
app.Label("what To Write",posX,posY)
```

### Button

Declaring one

```
app.Button("what To Write",(posX,posY),(sizeX,sizeY),on_press=function_to_run)
```

### Input prompt

declaring one

```
app.Input("prompt",(posX,posY),(sizeX,sizeY),on_press=function_to_run_on_enter_pressed)

```

### TextBox (Experemental)

Declaring one

```
app.TextBox((PosX,posY),(sizeX,sizeY),enterOnEnter=true)
```

getting current Contents

```
currentTextbox.text
```

## adding Widgets to app

```
app.add_widget(Variable)
```

## Theming files

### example Theme

```
{
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
}
```
