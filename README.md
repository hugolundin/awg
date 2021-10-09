# awg

Arbitrary Waveform Generator based on the Raspberry Pi Pico (RP2040). 

## Setup

Install dependencies:

```bash
$ brew install python-tk
$ pip3 install pipenv
$ pipenv run install # --dev
```

Install the firmware to the Raspberry Pi Pico:

```bash
$ pipenv run setup
```

Run the application

```
$ pipenv run awg
```
