# Raspberry Pi Motor Control with Web API

This project provides a simple web interface and API to control a DC motor connected to a Raspberry Pi using a DROK DC motor driver. The motor can be controlled in terms of direction and speed via a web interface.

## Requirements

- Raspberry Pi (any model with GPIO pins)
- DROK DC motor driver
https://a.co/d/9asvajf
- DC motor(s)
- Power supply (12V or 24V DC)
- Jumper wires
https://a.co/d/flmxawH (more then enough here)
- Python 3
- Flask
- RPi.GPIO library

## Installation

1. **Set up your Raspberry Pi:**
   Ensure your Raspberry Pi is set up with a suitable operating system (e.g., Raspbian).

2. **Install required libraries:**
   Open a terminal and run the following commands:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install Flask
   sudo apt-get install python3-rpi.gpio
