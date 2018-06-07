/*
 * Filename: main.cpp
 * File Created: Wednesday, May 30th 2018, 20:01:37 
 * ------
 * Author: Davide Sordi
 * GitHub: @sordinho
 * ------
 * Last Modified: Wednesday, May 30th 2018, 20:37:46 
 */


#include "Arduino.h"

// Integrated led
int led = 13;
// Analog pin A0 is 'sensor'
int sensor = A0;
// Set the initial sensor Value to 0
int sensorValue = 0;

// The setup function
void setup()
{
    // Initialize the led as an output
    pinMode(led, OUTPUT);
    // Initialize serial communication at 9600 baud
    Serial.begin(9600);
}

// The loop routine runs forever
void loop()
{
    // Read the analog input from 'sensor'
    sensorValue = analogRead(sensor);
    // Print out the value you read
    Serial.println(sensorValue, DEC);
    // If sensorValue is greater than 500
    if (sensorValue > 500)
    {
        // Turn the led ON
        digitalWrite(led, HIGH);
    }
    else
    {
        // Turn the led OFF
        digitalWrite(led, LOW);
    }
    delay(1000);
}
