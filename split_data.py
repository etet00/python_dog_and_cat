from sklearn.model_selection import train_test_split
import numpy as np


def split_data(features, labels):
    train_features, test_features, train_labels, test_labels \
        = train_test_split(features, labels, train_size=0.8, random_state=87)  # 切割訓練資料與測試資料
    train_features = np.array(train_features)
    test_features = np.array(test_features)
    train_labels = np.array(train_labels)
    test_labels = np.array(test_labels)
    return train_features, test_features, train_labels, test_labels
