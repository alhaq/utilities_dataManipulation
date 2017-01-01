import pandas as pd
import numpy as np
from IPython.display import display

#define functions
def createHistoricalPredictors(df, key_list, dim_list, attr2incement, yrs, remove_n0s):
    df_agg = df.groupby(key_list, as_index=0)[dim_list].agg('sum') 
    df_dict = {}
    
    for i in range(0,yrs): 
        df_temp = df_agg.copy()
        df_temp.columns = key_list + [dim + "_n" + str(i) for dim in dim_list]
        df_temp[attr2incement] = df_temp[attr2incement] + i
        df_dict
        df_dict['df_n' + str(i)] = df_temp
    
    cnt=0
    for i in df_dict.keys():
        if cnt == 0:
            df_temp = df_dict[i]
        else:
            df_temp = df_temp.merge(df_dict[i], on=key_list, how='outer')
        cnt=cnt+1
        #display(df_temp.head(3))
    
    cols = list(np.sort(list(set(df_temp.columns) - set(key_list))))
    
    if remove_n0s == 1:
        for i in cols:
            if "_n0" in i: cols.remove(i)
    
    df_final = df_temp[key_list + list(cols)]
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
df_ana = createHistoricalPredictors(df, key_list, dim_list, 'yr', 4, 1)
print(df_ana.head(3))

