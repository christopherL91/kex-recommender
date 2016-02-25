from __future__ import print_function
import json
from pyspin.spin import Default, Spinner
from termcolor import colored, cprint
import sys
import time

def countdown(t, conf):
    cprint('Making the model using the following parameters\n{0}'\
            .format(json.dumps(conf, indent=4, sort_keys=True)), 'red')
    spin = Spinner(Default)
    for i in range(t, 0, -1):
        text = colored('Will start training in', 'green')
        print(u'\r {0} {1} {2}'.format(spin.next(), text, i), end=" ")
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n')
