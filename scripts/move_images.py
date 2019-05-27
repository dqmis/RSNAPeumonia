import os
from shutil import copyfile

train_path = './data/train'
valid_path = './data/validation'
images_path = './data/stage_2_train_images_conv'


def main():
    train_names = os.listdir(train_path)
    valid_names = os.listdir(valid_path)
    images = os.listdir(images_path)

    for idx, n in enumerate(train_names):
        train_names[idx] = n[:-4]
    for idx, n in enumerate(valid_names):
        valid_names[idx] = n[:-4]
    for idx, n in enumerate(images):
        images[idx] = n[:-4]

    for name in train_names:
        if os.path.isfile('./data/stage_2_train_images_conv/{}.jpg'.format(name)) and not os.path.isfile('./data/train/{}.jpg'.format(name)):
            copyfile('{}/{}.jpg'.format(images_path, name), '{}/{}.jpg'.format(train_path, name))

    for name in valid_names:
        if os.path.isfile('./data/stage_2_train_images_conv/{}.jpg'.format(name)) and not os.path.isfile('./data/valid/{}.jpg'.format(name)):
            copyfile('{}/{}.jpg'.format(images_path, name), '{}/{}.jpg'.format(valid_path, name))

if __name__ == '__main__':
    main()

