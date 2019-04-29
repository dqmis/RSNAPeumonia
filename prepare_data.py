import pandas as pd
import os
import numpy as np

data_path = './data/stage_2_train_images_conv'

train_path = './data/train'
validation_path = './data/validation'

pos_split = 0.8
neg_split = 0.7

def write_data(df, path):
    for index, row in df.iterrows():
        f = open('{}/{}.txt'.format(path, row['patientId']),'a')
        if row['Target'] == 1:
            f.write('{} {} {} {} {}\n'.format(row['Target'], row['x'], row['y'], row['width'], row['height']))
        else:
            f.write('{} {} {} {} {}\n'.format(0, 0, 0, 0, 0))
        f.close()

def main():
    if not os.path.exists(os.path.join(train_path)):
        os.makedirs(os.path.join(train_path))
    if not os.path.exists(os.path.join(validation_path)):
        os.makedirs(os.path.join(validation_path))

    print('Gathering data')

    df = pd.read_csv('./data/stage_2_train_labels.csv')
    pos = df.loc[df['Target'] == 1]
    neg = df.loc[df['Target'] == 0]

    n_split = np.random.rand(len(neg)) < neg_split
    p_split = np.random.rand(len(pos)) < pos_split

    print('Writing data')

    write_data(neg[n_split], train_path)
    write_data(pos[p_split], train_path)
    write_data(pos[~p_split], validation_path)
    write_data(neg[~n_split], validation_path)

    print('Done!')


if __name__ == "__main__":
    main()
