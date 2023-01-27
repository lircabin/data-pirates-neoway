import jsonlines
import pandas as pd

mapping = {
    "Situação": 'situation',
    'Localidade': 'location',
    'Tipo de Faixa': 'type'
}


def transform():
    with jsonlines.open('result.jsonl') as reader:
        df = pd.DataFrame(reader)

    uf_df = pd.Series(df['UF'].unique())
    uf_df.name = 'label'
    df = df.rename(columns=mapping)
    situation_df = pd.Series(df['situation'].unique())
    df[['cep_min', 'cep_max']] = df['Faixa de CEP'].str.split(' a ',
                                                              1,
                                                              expand=True)
    type_df = pd.Series(df['type'].unique())
    type_df.name = 'label'

    df.to_json('transformed_location.json', orient="records")
    uf_df.to_json('transformed_uf.json', orient="split", index=False)
    situation_df.to_json('transformed_situation.json',
                         orient="split",
                         index=False)
    type_df.to_json('transformed_type.json', orient="split", index=False)

    return True