import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
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

print(int(parsed_args.square) ** 2)
