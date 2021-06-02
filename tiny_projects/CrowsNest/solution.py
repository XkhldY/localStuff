import argparse


# noinspection PyTypeChecker
def get_args():
    parser = argparse.ArgumentParser(description='say hello',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='a word')
    args = parser.parse_args()
    return args


def crows_nest():
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeuoi' else 'a'
    print(f'aloha, captain  {article} {word}  larboard bow')


if __name__ == '__main__':
    crows_nest()
