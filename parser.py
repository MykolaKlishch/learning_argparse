"""Calculate X to the power of Y"""
# source: https://docs.python.org/3/howto/argparse.html#id1

import argparse

parser = argparse.ArgumentParser(description=__doc__)
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x ** args.y
if args.quiet:
    print(answer)
elif args.verbose:
    print(f'{args.x} to the power of {args.y} equals {answer}')
else:
    print(f'{args.x}^{args.y} == {answer}')
