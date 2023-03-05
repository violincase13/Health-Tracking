# Health-Tracking
A Python script to run a health monitor on a Microbit board

Firstly, I created all the necessary variables to use in the program.
Those of integer type have an "int" input, and those that already take data from board components have an "input" input.
ex: counted_steps = int(0), temperature = input.temperature()

For each button, a special function has been created that performs the respective tasks when the user presses the button on the plate.

ex: def on_button_pressed_a():
        ...
input.on_button_pressed(Button.A, on_button_pressed_a)

When the user presses the A button, the number of calories burned so far is displayed on the screen. One step equals 0.04 calories burned. This happens when the plate has been shaken. In other words, if the user pressed button A and the plate was shaken, the corresponding value of calories burned up to that moment will be displayed on the screen. If the number of steps taken has exceeded 100, the song JUMP_UP will be played. From a code implementation point of view, all the necessary conditions have been imposed (with IF statements, incrementation, specific equations and basic.show_number to display the value).

Every 2 minutes, the plate will play the song BA_DING. From an implementation point of view, this is possible by creating the onEvery_interval() function, in which it is programmed to start the respective song at the respective time interval.
ex: loops.every_interval(120000, onEvery_interval)
The value of 120,000 was noted because it is the ms equivalent of 2 minutes

If the user presses the B button, the sounds/melody playing on the board will stop and the number of glasses of water the user still has to drink will be displayed on the screen, in ascending order. If the user had a drink, the message "You have consumed: " will be displayed followed by the corresponding number. If the limit of 8 drinks consumed is reached, the message "Congratulations! You have reached the limit" will be displayed on the screen. At the level of the implementation of the code, all the necessary conditions have been imposed (with IF instructions, incrementation, basic.show_string instructions to display the message, basic.show_number to display the value, and basic.clear_screen() for the DELETE).

Each time the user tilts the plate left or right, it will pause for 30 minutes (1800000ms). If this event has occurred, the appropriate counter will increase so that you can monitor the frequency of its occurrence. If the compass is tilted 135 degrees (east), the message "Good morning" will not be displayed until the standby time has elapsed. At the level of the implementation of the code, all the necessary conditions have been imposed (with IF instructions, incrementation and basic.show_string instructions to display the message).

When the user clicks on the logo, the data collected up to the moment he touches the logo (step count, calories burned, sleep time, glasses of water) will be displayed on the console. In terms of implementation, the print function was used. In addition, depending on the light level and the temperature, the following messages are displayed on the LED matrix: "Take a walk" for the light level > 150 and the temperature > 20 C and "Stay inside" for the opposite case. At the implementation level, the necessary conditions have been imposed.
