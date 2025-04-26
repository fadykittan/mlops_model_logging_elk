import config
from load.data_loader import DataLoader


def main():
    # Load
    loader = DataLoader(config)
    df = loader.load()

    print(df.head())


if __name__ == "__main__":
    print("start...")
    main()
    print("finish")

