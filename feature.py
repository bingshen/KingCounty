import pandas as pd
from numpy import *

def load_data():
    df_train=pd.read_csv("data\\kc_train.csv")
    df_test=pd.read_csv("data\\kc_test.csv")
    return df_train,df_test

def normalize(column,min_arg,max_arg):
    return column.apply(lambda x:(x-min_arg)/(max_arg-min_arg))

def fill_feature(df,path):
    sell_year,sell_month,sell_day=[],[],[]
    house_old,fix_old=[],[]
    for [sell_date,bulid_year,fix_year] in df[['sell_date','bulid_year','fix_year']].values:
        year,month,day=sell_date//10000,sell_date%10000//100,sell_date%100
        sell_year.append(year)
        sell_month.append(month)
        sell_day.append(day)
        house_old.append(year-bulid_year)
        if fix_year==0:
            fix_old.append(0)
        else:
            fix_old.append(year-fix_year)
    del df['sell_date']
    df['sell_year']=pd.DataFrame({'sell_year':sell_year})
    df['sell_month']=pd.DataFrame({'sell_month':sell_month})
    df['sell_day']=pd.DataFrame({'sell_day':sell_day})
    df['house_old']=pd.DataFrame({'house_old':house_old})
    df['fix_old']=pd.DataFrame({'fix_old':fix_old})
    # for column in df.columns:
    #     if column!='sell_price':
    #         df[column]=normalize(df[column],df[column].min(),df[column].max())
    df.to_csv(path,index=False)

if __name__ == '__main__':
    a=array([[1],[2],[3],[4],[5],[6]])
    print(a.reshape(1,-1)[0])
    # df_train,df_test=load_data()
    # fill_feature(df_train,"data\\train.csv")
    # fill_feature(df_test,"data\\test.csv")