import os

img_path = "./data/stage_2_test_images_conv"

def main():

    img_names = os.listdir(img_path)

    for name in img_names:
        f = open('./darknet/prediction.txt', 'a')
        f.write(os.path.abspath('{}/{}\n'.format(img_path, name)))
        f.close()

if __name__ == "__main__":
    main()
