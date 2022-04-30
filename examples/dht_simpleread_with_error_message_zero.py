import datetime
import time
import subprocess
from subprocess import PIPE

DHTTYPE = '22'


def main():

    while True:
        proc = subprocess.run("python3 dht_read_with_error_message.py " +
                              DHTTYPE, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        text = proc.stdout
        now = datetime.datetime.now()
        if text[0:2] == '  ':
            print("{0} DHT{1}, error message: {2}".format(
                now, DHTTYPE, text.strip()))
        else:
            values = text.split()
            print("{0} DHT{1}, humidity {2}%, temperature {3}*".format(now,
                  DHTTYPE, values[0], values[1]))
        time.sleep(2)


if __name__ == '__main__':
    main()
