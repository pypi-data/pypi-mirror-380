#include <Arduino.h>
#include "ApplicationDefines.h"
#include "TempController.hpp"

TempController tempController;

void NanoReset() {
  Serial.write(0xE1);
  Serial.flush();
  delay(100);
  void (*goodbye_cruel_world)(void) = 0;
  goodbye_cruel_world();
}

void SetMotorDirection(int motor, int direction) {
  switch (motor) {
    case 0:
      if (direction == 0) {
        digitalWrite(MOTOR_1D_PIN, LOW);
        digitalWrite(MOTOR_1L_PIN, HIGH);
      } else if (direction == 1) {
        digitalWrite(MOTOR_1L_PIN, LOW);
        digitalWrite(MOTOR_1D_PIN, HIGH);
      } else {
        digitalWrite(MOTOR_1L_PIN, LOW);
        digitalWrite(MOTOR_1D_PIN, LOW);
      }
      break;
    case 1:
      if (direction == 0) {
        digitalWrite(MOTOR_2D_PIN, LOW);
        digitalWrite(MOTOR_2L_PIN, HIGH);
      } else if (direction == 1) {
        digitalWrite(MOTOR_2L_PIN, LOW);
        digitalWrite(MOTOR_2D_PIN, HIGH);
      } else {
        digitalWrite(MOTOR_2L_PIN, LOW);
        digitalWrite(MOTOR_2D_PIN, LOW);
      }
      break;
    case 2:
      if (direction == 0) {
        digitalWrite(MOTOR_3D_PIN, LOW);
        digitalWrite(MOTOR_3L_PIN, HIGH);
      } else if (direction == 1) {
        digitalWrite(MOTOR_3L_PIN, LOW);
        digitalWrite(MOTOR_3D_PIN, HIGH);
      } else {
        digitalWrite(MOTOR_3L_PIN, LOW);
        digitalWrite(MOTOR_3D_PIN, LOW);
      }
      break;
    case 3:
      if (direction == 0) {
        digitalWrite(MOTOR_4D_PIN, LOW);
        digitalWrite(MOTOR_4L_PIN, HIGH);
      } else if (direction == 1) {
        digitalWrite(MOTOR_4L_PIN, LOW);
        digitalWrite(MOTOR_4D_PIN, HIGH);
      } else {
        digitalWrite(MOTOR_4L_PIN, LOW);
        digitalWrite(MOTOR_4D_PIN, LOW);
      }
      break;
  }
}

void setup() {
  Serial.begin(115200);
  TC_PRINTLN("etera-uart-bridge expander " EUB_VERSION_STR " ('h' for help)");

  pinMode(MOTOR_1L_PIN, OUTPUT);
  pinMode(MOTOR_1D_PIN, OUTPUT);
  pinMode(MOTOR_2L_PIN, OUTPUT);
  pinMode(MOTOR_2D_PIN, OUTPUT);
  pinMode(MOTOR_3L_PIN, OUTPUT);
  pinMode(MOTOR_3D_PIN, OUTPUT);
  pinMode(MOTOR_4L_PIN, OUTPUT);
  pinMode(MOTOR_4D_PIN, OUTPUT);

  SetMotorDirection(0, 2);
  SetMotorDirection(1, 2);
  SetMotorDirection(2, 2);
  SetMotorDirection(3, 2);

  for (int i = 0; i < 8; i++) {
    pinMode(EXPANDER_PIN_START + i, OUTPUT);
    digitalWrite(EXPANDER_PIN_START + i, LOW);
  }

  unsigned long start_timeout = millis();
  while (tempController.GetLastReadMillis() == 0 && millis() - start_timeout < 5000) {
    tempController.Process();
  }
  if (tempController.GetLastReadMillis() == 0) {
    TC_PRINTLN("Cannot start the temperature controller, restarting...");
    delay(1000);
    NanoReset();
    return;
  }

  // Notify the host that the device is ready
  Serial.write(0xE0);
}

unsigned long motor_move_millis[4] = {0, 0, 0, 0};
unsigned long motor_move_duration[4] = {0, 0, 0, 0};

void ProcessMotor() {
  for (int i = 0; i < 4; i++) {
    if (motor_move_millis[i] != 0) {
      if (millis() - motor_move_millis[i] >= motor_move_duration[i]){
        SetMotorDirection(i, 2);
        motor_move_millis[i] = 0;
        motor_move_duration[i] = 0;
        Serial.write(0b11010000 | i);
      }
    }
  }
}

void PrintHex8(uint8_t *data, uint8_t length) // prints 8-bit data in hex with leading zeroes
{
        for (int i=0; i<length; i++) { 
          if (data[i]<0x10) {Serial.print("0");} 
          Serial.print(data[i],HEX); 
          Serial.print(" "); 
        }
}

void ProcessUart() {
  if (Serial.available() > 0) {
    char c = Serial.read();

    if (c == 'h') {
      TC_PRINT_START();
      Serial.println("etera-uart-bridge");
      Serial.println("Version: " EUB_VERSION_STR );
      Serial.println("Lenart Arvo Kos (c) 2024");
      Serial.println();
      Serial.println("Commands:");
      Serial.println("\t`h` - help");
      Serial.println("\t`c` - get temperature sensors count (uint8_t)");
      Serial.println("\t`t` - get temperature sensor temperature (int16_t[count])");
      Serial.println("\t`a` - get temperature sensor address (int8_t[8][count])");
      Serial.println("\t`0xE1` - (r)eset device");
      Serial.println("\t`0b11000mmd [mm(motor 0-3)][d 0-1]``duration_ms(uint16_t)` - set motor direction (0 - left, 1 - right)");
      Serial.println("\t`0b1010rrrv [rrr(gpio 0-7)][v 0-1]` - set gpio value (0 - low, 1 - high)");
      Serial.println("Received messages:");
      Serial.println("\t`0xE0` - device reset and ready");
      Serial.println("\t`0xE1` - device starting to reset");
      Serial.println("\t`0xEA` - start of ascii message");
      Serial.println("\t`0xEB` - end of ascii message");
      Serial.println("\t`0b110100mm [motor 0-3]` - motor finished moving");
      int n = tempController.GetDeviceCount();
      Serial.println("Temperature sensors:");
      for (int i = 0; i < n; i++) {
	uint8_t* address = tempController.GetAddress(i);
	Serial.print("\t #"); Serial.print(i+1, DEC);
	Serial.print("\t"); PrintHex8(address, 8);
	uint16_t temp = tempController.GetTemperature(i);
	Serial.print("\t"); Serial.print(temp/128.0, 2); Serial.println("ºC");
      }
      TC_PRINT_END();
    } else if (c == 'c') {
      Serial.write('c');
      Serial.write(tempController.GetDeviceCount());
    } else if (c == 't') {
      Serial.write('t');
      // If TC did not read the temperature for more than 30 seconds, we will send 0x7FFF
      const unsigned long last = tempController.GetLastReadMillis();
      if (last == 0 || (millis() - last) > 30000) {
        int n = tempController.GetDeviceCount();
        for (int i = 0; i < n; i++) {
          uint16_t temp = 0x7FFF;
          Serial.write((uint8_t*)&temp, 2);
        }
        return;
      }

      int n = tempController.GetDeviceCount();
      for (int i = 0; i < n; i++) {
        uint16_t temp = tempController.GetTemperature(i);
        Serial.write((uint8_t*)&temp, 2);
      }
#ifdef DEBUG_TEMP
      TC_PRINT_START();
      for (int i = 0; i < n-1; i++) {
        uint8_t* address = tempController.GetAddress(i);
	Serial.print("\t #"); Serial.print(i+1, DEC);
	Serial.print("\t"); PrintHex8(address, 8);
	uint16_t temp = tempController.GetTemperature(i);
	Serial.print("\t"); Serial.print(temp/128.0, 2); Serial.print("ºC");
	int16_t raw_temp = tempController.GetRawTemperature(i);
	Serial.print("\t"); Serial.print(raw_temp/2.0, 1);
	uint16_t count_remain = tempController.GetCountRemain(i);
	Serial.print("\t"); Serial.print(count_remain, HEX);
	Serial.print("\t"); Serial.print((char)count_remain, DEC);
	Serial.print("\t"); Serial.println((char)(count_remain>>8), DEC);
      }
      TC_PRINT_END();
#endif
    }
    else if (c =='a') {
      Serial.write('a');
      int n = tempController.GetDeviceCount();
      for (int i = 0; i < n; i++) Serial.write(tempController.GetAddress(i), 8);
    } else if ((c & 0b11110000) == 0b11000000) { // Motor
      int motor = (c & 0b110) >> 1;
      int direction = (c & 1);
      uint16_t duration = 0;
      auto n = Serial.readBytes((char*)&duration, 2);
      if (n != 2) {
        TC_PRINTLN("Timeout reading duration");
        return;
      }
      if (duration == 0) {
        SetMotorDirection(motor, 2);
        motor_move_millis[motor] = 0;
        motor_move_duration[motor] = 0;
        return;
      }
      motor_move_millis[motor] = millis();
      if (motor_move_millis[motor] == 0) motor_move_millis[motor] = 1;
      motor_move_duration[motor] = duration;
      SetMotorDirection(motor, direction);
      Serial.write(c);
    } else if ((c & 0b11110000) == 0b10100000) { // Gpio
      int gpio = (c & 0b1110) >> 1;
      int value = c & 1;
      digitalWrite(EXPANDER_PIN_START + gpio, value);
      Serial.write(c);
    } else if (c == 0xE1 || c == 'r') {
      NanoReset();
    } else {
      TC_PRINT_START();
      Serial.print("Unknown command: ");
      Serial.println(c);
      TC_PRINT_END();
    }
  }
}

void loop() {
  tempController.Process();
  if (tempController.GetLastReadMillis() == 0) {
    TC_PRINTLN("Something went wrong with the temperature controller, restarting...");
    NanoReset();
  }
  ProcessMotor();
  ProcessUart();
}
