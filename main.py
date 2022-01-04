import os
import time
import sys
from utils import count_down, bangkok_zone

try:
    sys.argv[1]
    assert sys.argv[1] in ['cli','web']
except IndexError or AssertionError:
    print("Please specify the mode: cli or web")
    exit(1)

if sys.argv[1].lower() == "cli":
    while True:
        print("{day} Days {hour} Hours {min} Minutes and {sec} Seconds".format(**count_down(bangkok_zone)),end="\r")
elif sys.argv[1].lower() == "web":
    from app import app
    app.run('0.0.0.0',80,debug=True)
else:
    print("Please specify the mode: cli or web")
    exit(1)