#include "Keyboard.h"

/* Arduino to RaspPi Code */
//Define the Buttons we are using in the hardware
#define BUTTON_UP       A5
#define BUTTON_LEFT     A4
#define BUTTON_DOWN     A3
#define BUTTON_RIGHT    A2

/* Define the Bytes we need to send for a press of each key. Edit here
  to change the keys pressed for whatever game you want to play. For a list
  of keyboard modifier hex values, check out:
  http://arduino.cc/en/Reference/KeyboardModifiers  */

#define KEY_PRESS_W         0x77  // correct
#define KEY_PRESS_A         0x61  // correct
#define KEY_PRESS_S         0x73  // correct    
#define KEY_PRESS_D         0x64  // correct             

// This section takes the key presses defined above and maps them to the buttons on the controller
uint8_t buttons[4][2] = {{BUTTON_UP, KEY_PRESS_W}, // Participants must choose what key will be mapped to each button here, for now, this will be D
  {BUTTON_LEFT, KEY_PRESS_A}, // Participants must choose what key will be mapped to each button here, for now, this will be S
  {BUTTON_DOWN, KEY_PRESS_S}, // Participants must choose what key will be mapped to each button here, for now, this will be W
  {BUTTON_RIGHT, KEY_PRESS_D} // Participants must choose what key will be mapped to each button here, for now, this will be A
};

// Button contact bounce compensation
const int DEBOUNCE = 100;
// Communication latency compensation
const int LATENCY  = 75;
int threshold = 100;
int buttonPressed = -1;
int whichButtonPressed[4] = {0, 0, 0, 0};
int val; // temporary value

void setup() {
  // Setup all buttons as input pins
  for (int i = 0; i < 4; i++) {
    pinMode(buttons[i][0], INPUT_PULLUP);
  }

  // Begin the HID protocol for a keyboard
  Keyboard.begin();
  Serial.begin(112500);

}

void loop() {
  for (int i = 0; i < 4; i++ ) {
    val = analogRead(buttons[i][0]);
    whichButtonPressed[i] = val;
    Serial.print(val);
    Serial.print(", ");
    if (val > threshold) {
      buttonPressed = 1;
      delayMicroseconds(100);
    }
  }
  Serial.println("");

  if (buttonPressed == 1) {
    for (int i = 0; i < 4; i++ ) {
      if (whichButtonPressed[i] > threshold) {
        Keyboard.write(buttons[i][1]);
      }
    }
    buttonPressed = -1;
  }
  delay(LATENCY);
}
