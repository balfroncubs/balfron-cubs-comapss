let degrees = 0
basic.forever(function () {
    degrees = input.compassHeading()
    if (degrees > 350 || degrees < 10) {
        basic.showString("N")
    } else if (true) {
        basic.showString("E")
    } else if (degrees == 180) {
        basic.showString("S")
    } else if (degrees == 270) {
        basic.showString("W")
    } else {
        basic.showString("")
    }
})
