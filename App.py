import argparse

def get_file():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()
    return args.file

if __name__ == "__main__":
    file = get_file()

    
