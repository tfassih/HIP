from configparser import ConfigParser
from email import parser

def config(filename='db/db.cfg', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}