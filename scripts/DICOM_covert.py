import pydicom
import os
import cv2

test_path = "./data/stage_2_test_images"
train_path = "./data/stage_2_train_images"

test_path_jpg = "./data/stage_2_test_images_conv"
train_path_jpg = "./data/stage_2_train_images_conv"

def main():
    if not os.path.exists(os.path.join(test_path_jpg)):
        os.makedirs(os.path.join(test_path_jpg))
    if not os.path.exists(os.path.join(train_path_jpg)):
        os.makedirs(os.path.join(train_path_jpg))

    convert(test_path, test_path_jpg)
    convert(train_path, train_path_jpg)

    print('Done!')

def convert(f_p, j_p):
    images_path = os.listdir(f_p)
    print('{} {} images found'.format(len(images_path),f_p))
    for n, image in enumerate(images_path):
        ds = pydicom.dcmread(os.path.join(f_p, image))
        pixel_array_numpy = ds.pixel_array
        image = image.replace('.dcm', '.jpg')
        cv2.imwrite(os.path.join(j_p, image), pixel_array_numpy)
    print('Sucessfully converted all {} files'.format(f_p))

if __name__ == "__main__":
    main()
