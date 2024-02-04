degrees = 0

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees > 350 or degrees < 10:
        basic.show_string("N")
    elif True:
        basic.show_string("E")
    elif degrees == 180:
        basic.show_string("S")
    elif degrees == 270:
        basic.show_string("W")
    else:
        basic.show_string("")
basic.forever(on_forever)
