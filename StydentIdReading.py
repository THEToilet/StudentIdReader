#!/usr/bin/env python2

import nfc
import time


def on_connect(tag):
    try:
        sc1 = nfc.tag.tt3.ServiceCode(4, 0x010B)
        bc1 = nfc.tag.tt3.BlockCode(0, service=0)
        data = tag.read_without_encryption([sc1], [bc1])
        print("HELLO! ID: " + data[3:10])
        ID = data[3:5]
        NUMBER = data[5:10]
        file = open('student_id.txt', 'a')
        file.write(ID.lower() + NUMBER + "@shibaura-it.ac.jp\n")
        file.close()
        print("wait a minute.....")
        time.sleep(5)
    except nfc.tag.TagCommandError as e:
        print("NFC tag read error")
    except KeyboardInterrupt:
        sys.exit


def main():
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect': on_connect})


if __name__ == '__main__':
    while True:
        print("READY!")
        main()
