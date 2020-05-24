"""source: https://docs.python.org/3/howto/argparse.html"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", type=int,
                    help="increase output verbosity",
                    action='store_true')
args = parser.parse_args()
answer = args.square ** 2

# print("========")
# print(parser)
# print("========")
# print(dir(parser))
# print("========")
# print(parser.add_argument)
# print("========")
# print(parser.parse_args)
# print("========")
# print(parsed_args)
# print("========")
# print(parsed_args.echo)
# print("========")
# print(argparse.ArgumentParser.mro())
if args.verbose == 2:
    print(f'the square of {args.square} equals {answer}')
elif args.verbose == 1:
    print(f'{args.square}^2 == {answer}')
else:
    print(answer)
