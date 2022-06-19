# TemperatureGauger

## Requirements

Have [rtl_433](https://github.com/merbanan/rtl_433) installed and setup

## Setup

To setup and run use `curl <insert url to raw setup file script> | python3`

**--OR--**

clone this repository and run `git clone https://github.com/N8Deathrider/rtl_433-Temperature-Reader.git && cd ./rtl_433-Temperature-Reader && python3 ./Temperature-reader.py`

___

### Plan

My plan is to eventually get to a point to where 

1. The script will detect if you have everything for an rtlsdr setup and ready to use
2. Detect if you already have [rtl_433](https://github.com/merbanan/rtl_433) installed
3. If not ask the user if they would like either one or both of those to be set up for them automatically by the script
4. Gather some basic settings / preferences from the user and create a settings file
5. Also dependant on the answers to the setup questions create a config file to run [rtl_433](https://github.com/merbanan/rtl_433) with
6. Sugest the command for the user to run [rtl_433](https://github.com/merbanan/rtl_433)
    * That would basically be just be a command to run [rtl_433](https://github.com/merbanan/rtl_433) in a detached screen session and including the arguments to make [rtl_433](https://github.com/merbanan/rtl_433) use the config file that was generated

___

<br><br><br><br><br><br><br>

### Disclaimer

This thus far has only been written to work on unix machines
