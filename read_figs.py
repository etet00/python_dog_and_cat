import os
import cv2
from setting import CAT_DIR
from setting import DOG_DIR


def read_figs():
    feature = []
    labels = []
    dic = {"Cat": 0, "Dog": 1}
    size = (40, 40)  # 固定圖片尺寸大小
    for DIR in (CAT_DIR, DOG_DIR):
        label = DIR.split("\\")[-1]
        # print(label)
        print(DIR, "loading figs....")
        for img in os.listdir(DIR):
            try:
                fig = cv2.imread(os.path.join(DIR, img))
                if fig is not None:
                    fig = cv2.resize(fig, dsize=size)
                    feature.append(fig)
                    labels.append(dic[label])
            except:
                pass

    return feature, labels
