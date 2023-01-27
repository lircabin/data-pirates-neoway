import os
import pandas as pd

from .create import dimSituations
from .create import dimTypes
from .create import dimUFs
from .create import factLocations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn = create_engine(
    os.getenv('AIRFLOW__DATABASE__SQL_ALCHEMY_CONN')).connect()
dwhConnection = conn.connect()
SessionDwh = sessionmaker(bind=dwhConnection)
sessionDwh = SessionDwh()


def insert_dimension(Model, data):
    records = []
    for record in data['data']:
        new_entry = Model(label=record)
        records.append(new_entry)
    sessionDwh.add_all(records)
    sessionDwh.commit()

    return [record.id for record in records]


def load_insert_from_json(path, Model, prefix=''):
    df = pd.read_json(path)
    df[prefix + '_id'] = insert_dimension(Model, df)
    return df


def load():
    engine = create_engine(os.getenv('AIRFLOW__DATABASE__SQL_ALCHEMY_CONN'))

    uf_df = load_insert_from_json('transformed_uf.json', dimUFs, 'uf')
    situation_df = load_insert_from_json('transformed_situation.json',
                                         dimSituations, 'situation')
    type_df = load_insert_from_json('transformed_type.json', dimTypes, 'type')
    location_df = pd.read_json('transformed_location.json')
    # Now we have all the ids for the relationship, all is left to do is merge the data and insert fact
    location_df = location_df.merge(uf_df,
                                    left_on='UF',
                                    right_on='data',
                                    how='left')
    location_df = location_df.merge(situation_df,
                                    left_on='situation',
                                    right_on='data',
                                    how='left')
    location_df = location_df.merge(type_df,
                                    left_on='type',
                                    right_on='data',
                                    how='left')
    # Bulk insertion of fact. this is less verbose and has more performance
    location_df['Records'] = location_df.apply(
        lambda x: factLocations(location=x.location,
                                cep_min=x.cep_min,
                                cep_max=x.cep_max,
                                type_id=x.type_id,
                                uf_id=x.uf_id,
                                situation_id=x.situation_id),
        axis=1)
    records = location_df['Records'].values.tolist()
    sessionDwh.add_all(records)
    sessionDwh.commit()
    return True