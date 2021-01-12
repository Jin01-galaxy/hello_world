def on_forever():
    basic.show_string("Hello!")
    basic.show_icon(IconNames.HEART)
    basic.pause(1000)
    basic.show_string("Python_mode")
basic.forever(on_forever)
