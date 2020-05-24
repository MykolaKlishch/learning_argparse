"""source: https://docs.python.org/3/howto/argparse.html"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent", default=2)
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square ** 2
if args.verbosity >= 2:
    print(f"Running '{__file__}' ...")
if args.verbosity >= 1:
    print(f'{args.square}^2 == {answer}')
else:
    print(answer)
