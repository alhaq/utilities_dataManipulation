import pandas as pd
import numpy as np
from IPython.display import display

#define functions
def createHistoricalPredictors(df, key_list, dim_list, attr2incement):
    print(dim_list)
    df_agg = df.groupby(key_list, as_index=0)[dim_list].agg('sum')
    
    df_n0 = df_agg.copy()
    df_n1 = df_agg.copy()
    df_n2 = df_agg.copy()
    
    df_n0.columns = key_list + [i + "_n0" for i in dim_list]
    df_n1.columns = key_list + [i + "_n1" for i in dim_list]
    df_n2.columns = key_list + [i + "_n2" for i in dim_list]

    #step 5)
    #incrementing years
    df_n0[attr2incement] = df_n0[attr2incement] + 0 
    df_n1[attr2incement] = df_n1[attr2incement] + 1 
    df_n2[attr2incement] = df_n2[attr2incement] + 2

    #step 6)
    #merge
    df_merged = df_n0.merge(df_n1, on=key_list, how='outer')
    df_merged = df_merged.merge(df_n2, on=key_list, how='outer')

    
    df_final = df_merged
    return(df_final)

#create store/sku dataset
items = [('prd', np.random.randint(1,10,100)),
         ('node', np.random.randint(1000,1010,100)),
         ('yr', np.random.randint(2011,2016,100)),
         ('sales_summ', np.random.randint(10,200,100)),
         ('sales_wint', np.random.randint(10,250,100)),
         ('sales_yr', np.random.randint(10,300,100)),
         ('sold_summ', np.random.randint(0,2,100)),
         ('sold_wint', np.random.randint(0,2,100)),
         ('sold_yr', np.random.randint(0,2,100))]
df = pd.DataFrame.from_items(items)

#execute function and create predictors
key_list = ['prd', 'yr']; dim_list = ['sales_summ', 'sales_yr']
df_agg = createHistoricalPredictors(df, key_list, dim_list, 'yr')
print(df_agg.head(3))

