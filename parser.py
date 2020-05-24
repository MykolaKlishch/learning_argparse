import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--verbosity",
    help="increase output verbosity",
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
if parsed_args.verbosity:
    print('verbosity turned on')
