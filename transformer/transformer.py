import pandas as pd

class Transformer:

    def __init__(self, config):
        self.config = config

    def transform(self, df):
        df.columns = ['gender', 'race', 'parentDegree', 'lunch', 'course', 'mathScore', 'readingScore', 'writingScore']
        df['total'] = (df['mathScore']+df['readingScore']+df['writingScore'])/3

        for i in range(len(df)):
            if df.iloc[i,2] in ['high school', 'some high school']:
                df.iloc[i,2] = 'No_Degree'
            else:
                df.iloc[i,2] = 'has_Degree'

        final_df = df.groupby(['gender','parentDegree','course','lunch','race']).mean().reset_index()
        after_sort = final_df.sort_values(by= ['total'],ascending = False)
        after_sort.drop(columns=['mathScore','readingScore','writingScore'],inplace = True)
        after_sort

        base = pd.get_dummies(final_df,columns=['gender','race','parentDegree','course','lunch'],dtype = int)
        base.sample()
        base.info()

        # return base
        return base.iloc[:, 4:]

