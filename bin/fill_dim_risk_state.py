import argparse

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:andrea1990@localhost/britcore1')


def main(filename):
    df = pd.read_csv(filename)
    df = df[['STATE_ABBR']]
    df.columns = ['id']
    df = df.drop_duplicates()
    df.to_sql('dim_risk_state', engine, if_exists='replace', index=False)
    print(df.head())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    args = parser.parse_args()
    main(args.file)