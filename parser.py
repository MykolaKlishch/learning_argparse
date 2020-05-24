import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--verbose",
    help="increase output verbosity",
    action='store_true'
)
parsed_args = parser.parse_args()

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
if parsed_args.verbose:
    print('verbosity turned on')
