from src.api import collect_todos
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dir", type=str, default="./daily_example/", help="Path to the directory containing markdown files")
args = parser.parse_args()

if __name__ == "__main__":
    print(f"The directory is {args.dir}")
    collect_todos(args.dir)
