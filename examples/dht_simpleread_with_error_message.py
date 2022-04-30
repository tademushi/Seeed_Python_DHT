import datetime
import time
import seeed_dht


def main():

    # for DHT11/DHT22
    sensor = seeed_dht.DHT("22", 12)
    # for DHT10
    # sensor = seeed_dht.DHT("10")

    while True:
        humi, temp, error_message = sensor.read_with_error_message()
        if not error_message is None:
            print('{2} DHT{0}, error message: {1}'.format(
                sensor.dht_type, error_message, datetime.datetime.now()))
        elif not humi is None:
            print('{3} DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(
                sensor.dht_type, humi, temp, datetime.datetime.now()))
        else:
            print('{2} DHT{0}, humidity & temperature: {1}'.format(
                sensor.dht_type, temp, datetime.datetime.now()))
        time.sleep(2)


if __name__ == '__main__':
    main()
