import os
import tempfile
import argparse
import logging
import coloredlogs

RPI_PICO = '/dev/tty.usbmodem14601'
FIRMWARE_PATH = 'awg/firmware.py'

def setup():
    logging.info(f'Copying firmware to Raspberry Pi Pico ({RPI_PICO})...')
    os.system(f'ampy -p {RPI_PICO} put {FIRMWARE_PATH} main.py')

def main():
    logging.debug('Starting awg...')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--setup', action='store_true')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        coloredlogs.install('DEBUG')
    else:
        coloredlogs.install('INFO')
    
    if args.setup:
        setup()
    else:
        main()
