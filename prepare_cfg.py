import os

train_path = "./data/train"
valid_path = "./data/validation"

def main():

    train_names = os.listdir(train_path)
    valid_names = os.listdir(valid_path)

    train_names = list(filter(lambda x:x.endswith((".jpg")), train_names))
    valid_names = list(filter(lambda x:x.endswith((".jpg")), valid_names))

    for name in train_names:
        f = open('./darknet/cfg/train.txt', 'a')
        f.write(os.path.abspath('{}/{}\n'.format(train_path, name)))
        f.close()

    for name in valid_names:
        f = open('./darknet/cfg/test.txt', 'a')
        f.write(os.path.abspath('{}/{}\n'.format(valid_path, name)))
        f.close()

if __name__ == "__main__":
    main()
