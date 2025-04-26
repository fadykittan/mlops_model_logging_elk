import config
from load.data_loader import DataLoader
from transformer.transformer import Transformer
from model.model import Model

def main():
    # Load
    loader = DataLoader(config)
    df = loader.load()

    # Transform
    transform = Transformer(config)
    df = transform.transform(df)

    # Model
    model = Model(config)
    model.load_model()
    res = model.predict(df)
    
    print(res)
    print(type(res))


if __name__ == "__main__":
    print("start...")
    main()
    print("finish")

