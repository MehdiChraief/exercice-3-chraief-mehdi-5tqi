#conding

def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.ANGRY)
input.on_button_pressed(Button.B, on_button_pressed_b)
led.plot(1, 1)
led.plot(3,1)
led.plot(0,4)
led.plot(1,3)
led.plot(2,3)
led.plot(3,3)
led.plot(4,4)