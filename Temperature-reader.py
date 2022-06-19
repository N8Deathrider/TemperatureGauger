#!/usr/bin/env python3
"""
This program is meant to ingest a JSON
output file that is being generated
from a running instance of rtl_433 and
every two minutes print out a message
in the terminal reporting the average
temperature and some simple statistics
like how many unique devices it heard
from in the two minute window and how
many tempeture readings where recorded
within the two minute window
"""
from json import loads
from time import sleep
from sys import exit
from statistics import mean

def main():
    """
    This is the main function of the program
    """
    try:
        import settings  # TODO: redo this to work like my cookie loader and saver so that if the check to see if the file exits fails to then make it otherwise import it
    except ModuleNotFoundError:
        generate_settings()
        try:
            import settings
        except ModuleNotFoundError:
            exit('Exiting due to not being able to find settings')

    f = "./rtl_433-data.json"  # DEBUG: in the end I want this read from the settings file

    try:
        process_data(f)
    except KeyboardInterrupt:
        # exit('\nCtrl+c was detecte. Stopping now.')  # Alternative
        exit('\nSignal caught, exiting!')  # Alternative


def process_data(thefile: str):
    """
    Processes the data from the json output file from rtl_433

    :param ``thefile``: The file refers to the path of the json output file
    from a running instance of rtl_433
    :return: ``None``
    """
    ids = set()
    temperatures = list()
    fresh = False
    first_time = True
    with open(thefile, 'r') as file:
        while True:
            where = file.tell()
            line = file.readline().strip()
            if not line:
                if fresh:
                    prompt(id_list=ids, temperature_list=temperatures, fr=first_time)
                    ids.clear()
                    temperatures.clear()
                    first_time = False
                fresh = False
                sleep(120)
                file.seek(where)
            else:
                fresh = True
                data = loads(line)

                try:
                    ids.add(data['id'])
                except KeyError:
                    pass

                try:
                    temperatures.append(data['temperature_F'])
                except KeyError:
                    pass
    return None



def prompt(id_list: set, temperature_list: list, fr:bool = True) -> None:
    """
    Handles displaying the data

    :param ``fr``: Stands for First Run and is there to signal when to start writing over the other text in the prompt
    :param ``id_list``: The list of id numbers
    :param ``temerature_list``: The list of temperatures
    :return: ``None``
    """
    mean_temerature = mean(temperature_list)
    line1 = f'The Average temerature in the area is {mean_temerature:.2f}°F'
    line2 = f'This was calculated using {len(temperature_list)} reading(s) received over approximately'
    line3 = f'the last 2 Minutes and gathered from, {len(id_list)} sensor(s)'
    width = len(line2)
    frame = '#' * (width + 6)

    message =(
        f'{frame:^{width}}\n'
        f'#  {line1:^{width}}  #\n'
        f'#  {line2:^{width}}  #\n'
        f'#  {line3:^{width}}  #\n'
        f'{frame:^{width}s}'
    )

    if not fr:
        print('\033[1A\033[2K' * 5, end='')

    print(message)

    return None




def generate_settings():
    pass  # TODO: Finish making this so that it will ask the user the questions and then write
          #       the answers to a file named settings.py


if __name__ == '__main__':
    main()