import logging
import fb_write_birthday
from datetime import date


def main():
    # open log file
    logging.basicConfig(filename='test.log',format='%(asctime)s %(message)s',level=logging.DEBUG)
    
    logging.info(': Starting fb_write_birthday')
    fb_write_birthday.run()
    logging.info(': Finished fb_write_birthday')



if __name__ == '__main__':
    main()
