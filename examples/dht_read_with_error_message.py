import seeed_dht
import sys


def main():
    sensor = seeed_dht.DHT(sys.argv[1], 12)
    humi, temp, error_message = sensor.read_with_error_message()
    if not error_message is None:
        print('  {0}'.format(error_message))
    elif not humi is None:
        print('{0:.1f} {1:.1f} '.format(humi, temp))
    else:
        print(' {0} '.format(temp))


if __name__ == '__main__':
    main()
