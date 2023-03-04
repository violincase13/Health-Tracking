counted_steps = int(0)
burnt_calories_number = int(1)
total_consumed_water_glasses = int(0)
sleep_time_counter = int(0)
compass_degrees = input.compass_heading()
luminosity = input.light_level()
temperature = input.temperature()

def on_button_pressed_a():
    global counted_steps
    global burnt_calories_number
    while True:
        if input.is_gesture(Gesture.SHAKE):
            counted_steps += 1
            burnt_calories_number = 0.04 * counted_steps
            basic.show_number(burnt_calories_number)
            if counted_steps > 100:
                music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.FOREVER)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.stop_all_sounds()
    global total_consumed_water_glasses
    total_consumed_water_glasses += 1
    if total_consumed_water_glasses <= 8:
        basic.show_string("You have consumed: ")
        basic.show_number(total_consumed_water_glasses)
    else:
        basic.show_string("Congratulations! You have reached the limit")
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_till_right():
    global sleep_time_counter
    global compass_degrees    
    while True:
        pause(1800000)
        if pause(1800000):
            sleep_time_counter += 1
        if compass_degrees == 135:
            basic.show_string("Good morning")
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_till_right)

def on_gesture_till_left():
    global sleep_time_counter
    global compass_degrees
    while True:
        pause(1800000)
        if pause(1800000):
            sleep_time_counter += 1
        if compass_degrees == 135:
            basic.show_string("Good morning")
input.on_gesture(Gesture.TILT_LEFT, on_gesture_till_left)

def on_logo_event_pressed():
    print("The actual number of steps is: " + counted_steps)
    print("The actual number of burnt calories is: " + burnt_calories_number)
    print("The actual sleep time frequency is: " + sleep_time_counter )
    if total_consumed_water_glasses <= 0:
        print("The actual number of consumed water glasses is: " + total_consumed_water_glasses)
    if luminosity > 150 and temperature > 20:
        basic.show_string("Take a walk")
    else:
        basic.show_string("Stay inside")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def onEvery_interval():
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
loops.every_interval(120000, onEvery_interval)
