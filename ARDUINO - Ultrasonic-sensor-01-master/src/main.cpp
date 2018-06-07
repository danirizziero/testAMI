/*
 * Filename: main.cpp
 * File Created: Monday, May 14th 2018, 22:44:12 
 * ------
 * Author: Davide Sordi
 * GitHub: @sordinho
 * ------
 * Last Modified: Monday, May 14th 2018, 22:51:16 
 */

#include "Arduino.h"

// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;
const int led = 13;

// defines variables
long duration;
int distance;

void setup() {
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT);  // Sets the echoPin as an Input
    pinMode(led, OUTPUT);     //Sets the integrated led as Output
    Serial.begin(9600);       // Starts the serial communication
}

void loop() {
    // Clears the trigPin
    digitalWrite(trigPin, LOW);

    delayMicroseconds(5);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Reads from the echoPin the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);

    // Calculating the distance
    distance = duration * 0.034 / 2;

    // Turn on the led if distance is above 5cm
    if (distance < 5) {
        digitalWrite(led, HIGH);
    }
    else {
        digitalWrite(led, LOW);
    }

    // Prints the distance on the Serial Monitor
    Serial.print("Distance: ");
    Serial.println(distance);

    // set a delay of 1 second between misurations
    delay(1000);
}
