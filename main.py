#!/usr/bin/env python2
from __future__ import print_function
import argparse
import model
import logging
from logging.config import fileConfig
from utils import countdown
from config import get_config

fileConfig('logging_config.ini')
logger = logging.getLogger()

def init():
    parser = argparse.ArgumentParser(description='Recommendation engine')
    parser.add_argument('-l',
            action='store',
            type=int,
            dest='latent_factors',
            default=10,
            help='Define number of latent_factors')

    parser.add_argument('-method',
            action='store',
            type=str,
            dest='method',
            default='als',
            help='The method in which to solve train the model')

    parser.add_argument('-to',
            dest='to',
            nargs='+',
            default=['lillt@kth.se'],
            help='Mail address')

    parser.add_argument('-path',
            dest='path',
            type=str,
            default='./',
            help='The path to the dataset directory')
    return parser.parse_args()

if __name__ == "__main__":
    conf = get_config(init())
    # countdown(100, conf)
    model.run(conf)
