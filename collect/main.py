from multiprocessing import Queue
from bybitLinear import BybitLinear
from time import sleep
from datetime import datetime
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Collect Bybit data to files.')
parser.add_argument('--output', type=str, help='Output directory for data files')
parser.add_argument('--symbols', nargs='+', help='List of symbols to collect')

args = parser.parse_args()

if args.output is None or args.symbols is None:
    parser.print_help()
    raise ValueError("Arguments please :3")

output = args.output
symbols = args.symbols

queue = Queue()

bl = BybitLinear(queue, symbols)
bl.start()

while True:
    data = queue.get()
    if data is None:
        break
    s = data["data"]["s"]
    ts = data["ts"]
    dt = datetime.utcfromtimestamp(ts / 1000).strftime('%Y-%m-%d')
    with open(os.path.join(output, '%s_%s.dat' % (s, dt)), 'a') as f:
        f.write(str(data))
        f.write("\n")
