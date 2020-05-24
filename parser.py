import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
parsed_args = parser.parse_args()

print("========")
print(parser)
print(parser.add_argument)
print(parser.parse_args)
print(parsed_args)
print(parsed_args.echo)