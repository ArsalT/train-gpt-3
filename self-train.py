import pandas as pd
import numpy as np

np.random.seed(0)

data = pd.read_csv('intents.csv')
data.head()

data_columns_list = ['Intent', 'text']
data.columns = data_columns_list

data['text'] = data['text'].str.strip()
data['Intent'] = data['Intent'].str.strip()

data['text'] = '' + data['text'] + ' END'
data['Intent'] = data['Intent'] + "\n\nIntent:\n\n"
data.head()

data.columns = ['prompt', 'completion']
print(data)

data.to_json('Intents.jsonl', orient='records', lines=True)

# After running this file, run this command :
                # openai tools fine_tunes.prepare_data -f Intents.jsonl

# After you see another Intents_prepared.jsonl file generated! : RUN 'train.py' FILE