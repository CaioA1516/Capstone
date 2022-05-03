#include "Keyboard.h"

/* Arduino to RaspPi Code */
//Define the Buttons we are using in the hardware
#define BUTTON_UP       A5
#define BUTTON_LEFT     A4
#define BUTTON_DOWN     A2
#define BUTTON_RIGHT    A3
#define BUTTON_PAUSE    A1

/* Define the Bytes we need to send for a press of each key. Edit here
  to change the keys pressed for whatever game you want to play. For a list
  of keyboard modifier hex values, check out:
  http://arduino.cc/en/Reference/KeyboardModifiers  */

#define KEY_PRESS_W         0x77  // correct
#define KEY_PRESS_A         0x61  // correct
#define KEY_PRESS_S         0x73  // correct    
#define KEY_PRESS_D         0x64  // correct
#define KEY_PRESS_Q         0x71  // correct             

// This section takes the key presses defined above and maps them to the buttons on the controller
uint8_t buttons[5][2] = {{BUTTON_UP, KEY_PRESS_W}, // Participants must choose what key will be mapped to each button here, for now, this will be D
  {BUTTON_LEFT, KEY_PRESS_A}, // Participants must choose what key will be mapped to each button here, for now, this will be S
  {BUTTON_DOWN, KEY_PRESS_S}, // Participants must choose what key will be mapped to each button here, for now, this will be W
  {BUTTON_RIGHT, KEY_PRESS_D},// Participants must choose what key will be mapped to each button here, for now, this will be A
  {BUTTON_PAUSE, KEY_PRESS_Q} // Participants must choose what key will be mapped to each button here, for now, this will be Q
};

// Communication latency compensation
const int LATENCY  = 75;
int threshold[5] = {125, 125, 125, 125, 125}; // w, a, s, d, q
int whichButtonPressed[5] = {0, 0, 0, 0, 0};
int val; // temporary value
bool prevButtonPressed[5] = {false, false, false, false, false};

void setup() {
  // Setup all buttons as input pins
  for (int i = 0; i < 5; i++) {
    pinMode(buttons[i][0], INPUT_PULLUP);
  }
  // Begin the HID protocol for a keyboard
  Keyboard.begin();
  Serial.begin(115200);
  delay(1000);
  for (int i = 0; i < 5; i++ ) {
    val = analogRead(buttons[i][0]);
    threshold[i] = val + 50;
  }

}

void loop() {
  for (int i = 0; i < 5; i++ ) {
    val = analogRead(buttons[i][0]);
    whichButtonPressed[i] = val;
    Serial.print(val);
    Serial.print(" - ");
    Serial.print(threshold[i]);
    Serial.print(", ");
    if (val > threshold[i]) {
      delayMicroseconds(100);
    }
  }
  Serial.println("");


  for (int i = 0; i < 5; i++ ) {
    if (whichButtonPressed[i] > threshold[i] && prevButtonPressed[i] == false) {
      Keyboard.write(buttons[i][1]);
      prevButtonPressed[i] = true;
    } else if (whichButtonPressed[i] <= threshold[i] && prevButtonPressed[i] == true) {
      prevButtonPressed[i] = false;
    }
  }

  delay(LATENCY);
}
