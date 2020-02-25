import argparse


def print_error(message):
    print(f'ERROR: {message}!!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('message', type=str)
    args = parser.parse_args()
    print('Welcome to my program')
    print_error(args.message)

# python web_argparse_err_message.py message
