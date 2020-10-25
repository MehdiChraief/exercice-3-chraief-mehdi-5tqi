// conding
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Angry)
})
led.plot(1, 1)
led.plot(3, 1)
led.plot(0, 4)
led.plot(1, 3)
led.plot(2, 3)
led.plot(3, 3)
led.plot(4, 4)
