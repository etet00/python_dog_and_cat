from read_figs import read_figs
from split_data import split_data


def main():
    features, labels = read_figs()
    train_features, test_features, train_labels, test_labels = split_data(features, labels)
    print(len(train_features))


if __name__ == "__main__":
    main()

