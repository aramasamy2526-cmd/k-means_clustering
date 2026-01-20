# # # import numpy as np
# # # import pandas as pd


# # # #Creating a car price series with a dictionary
# # # # car_price_dict = {'Swift':  700000,
# # # #                        'Jazz' :  800000,
# # # #                        'Civic' : 1600000,
# # # #                        'Altis' : 1800000,
# # # #                        'Gallardo': 30000000
# # # #                       }
# # # # car_price = pd.Series(car_price_dict)
# # # # # Creating the car manufacturer series with a dictionary
# # # # car_man_dict = {'Swift' : 'Maruti',
# # # #                   'Jazz'   : 'Honda',
# # # #                   'Civic'  : 'Honda',
# # # #                   'Altis'  : 'Toyota',
# # # #                    'Gallardo' : 'Lamborghini'}
# # # # car_man = pd.Series(car_man_dict)
# # # # # print(car_price)
# # # # # print(car_man)

# # # # cars = pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man})
# # # # cars.index.name = 'Car Names'
# # # # #print(cars)
# # # # print(cars['Manufacturer'])
# # # #Using dictionary to create a series
# # # # car_price_dict = {'Swift':  700000,
# # # #                        'Jazz' :  800000,
# # # #                        'Civic' : 1600000,
# # # #                        'Altis' : 1800000,
# # # #                        'Gallardo': 30000000
# # # #                       }
# # # # car_price = pd.Series(car_price_dict)

# # # # #Creating a DataFrame from car_price Series
# # # # # cars = pd.DataFrame(car_price)
# # # # # cars.reset_index(inplace=True)
# # # # # cars.columns = ['Car Name', 'Car Price']
# # # # # print(cars)
# # # # import pandas as pd

# # # # data = [34, 52, 84, 13, 72, 85]
# # # # series = pd.Series(data, dtype=int)
# # # # print(series[1:3])

# # # # car_details = pd.Series(data = [700000, 200000, 1100000, 100000], index = ["swift", "Alto", "slavia", "Kia"], dtype = "int")
# # # # # print(car_details)
# # # # # print(car_details["swift": "slavia"])

# # # # car_details_dict = {
# # # #     "swift": 900000,
# # # #     "kia": 1700000,
# # # #     "Alto": 500000,
# # # #     "i20": 700000

# # # # }
# # # # print(pd.Series(car_details_dict))

# # # import pandas as pd

# # # # car_price_dic = {
# # # #     'Swift': 700000,
# # # #     'Jazz': 2111,
# # # #     'Civic': 32,
# # # #     'Altis': 1800000,
# # # #     'Gallardo': 30000000
# # # # }

# # # # cars_price_ser = pd.Series(car_price_dic)

# # # # car_manufac_dic = {
# # # #     'Swift': 'Maruti',
# # # #     'Jazz': 'Honda',
# # # #     'Civic': 'Honda',
# # # #     'Altis': 'Toyota',
# # # #     'Gallardo': 'Lamborghini'
# # # # }

# # # # car_manufac_ser = pd.Series(car_manufac_dic)

# # # # cars_df = pd.DataFrame({'Price' : car_price_dic, 'manuf' : car_manufac_ser})
# # # # cars_df_sort = cars_df.sort_values(by = 'Price',  ascending=False)
# # # # car_filter = cars_df[cars_df['Price']>10000]
# # # # print(car_filter)

# # # # data = pd.read_json('example.json')
# # # # print(data)

# # # # df = pd.read_csv("customers-100.csv")
# # # # print(df)
# # # # #print(df["First Name"])
# # # # print(df.columns)
# # # # #print(df[['First Name', 'Last Name', 'Company']])
# # # # df_head = df.head()
# # # # set_index = df_head.set_index("Index")
# # # # print(set_index)

# # # # df = pd.read_csv("customers-100.csv")
# # # # print(df.columns)
# # # # df_head = df.head()
# # # # df_head.set_index(['First Name'], inplace= True)
# # # # print(df_head)
# # # # print(df_head.loc['Preston':'Linda',['Customer Id']])
# # # # print(df_head.loc['Preston':'Joanna'])
# # # # #subsetting the upper dataset
# # # # print(df_head.loc[['Roy','Joanna'],['Customer Id']])
# # # # #print(df_head.iloc[2,1])
# # # # print(df.loc[df['City'] == 'Bryanville'])

# # # # print(df.loc[df['City'] == 'Bryanville'].head())
# # # # df_head = df.head()
# # # # x = df_head.set_index('Index')
# # # # print(x)
# # # # df_head.drop(columns = 'Index', inplace = True)
# # # # print(df_head)





# # # marks = [{'Chemistry': 67, 'Physics': 45, 'Mathematics': 50, 'English' : 19},
# # #         {'Chemistry': 90, 'Physics': 92, 'Mathematics': 87, 'English' : 90}, 
# # #         {'Chemistry': 66, 'Physics': 72, 'Mathematics': 81, 'English' : 72}, 
# # #         {'Chemistry': 32, 'Physics': 40, 'Mathematics': 12, 'English' : 6}        ]
# # # mark_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])

# # # # encrypt_marks = np.sin(mark_df)
# # # # encrypt_marks.reset_index(inplace = True)

# # # # print(encrypt_marks)


# # # # # print(mark_df)


# # # # # mark_df['Physics'] = mark_df['Physics'].mask(mark_df['Physics'] < 50, 'Fail')
# # # # # print(mark_df)

# # # # # mark_df.sort_values(by = 'Chemistry', inplace= True)
# # # # # mark_df.sort_index(inplace= True)
# # # # # mark_df.sort_values(['Mathematics', 'Physics'], ascending= (0,1))

# # # # # print(mark_df)
# # # # # import numpy as np
# # # # list_a = [54,62,742,12,62,73,13,1]
# # # # list_array = np.array(list_a)
# # # # mean = np.median(list_array)
# # # # #a_sort = np.sort(list_array)
# # # # print(mean)

# # # import pandas as pd
# # # import numpy as np
# # # # student_mark = {'chemistry': [23,54,64,12,53],
# # # #     'Physics': [31,41,64,12,63],
# # # #     "Biology":[31,52,66,73,21],
# # # #     "Mathematics": [65,23,75,53,64]}

# # # # df = pd.DataFrame(student_mark, index = ['Rahul', 'Suresh', 'Vignesh','Kumar','Gokul'], dtype = int)
# # # # import pandas as pd

# # # # data = {
# # # #     'model_year': [2010, 2010, 2011, 2011, 2011, 2012],
# # # #     'name': ['Honda Civic', 'Ford Focus', 'Toyota Corolla',
# # # #              'Honda Accord', 'BMW 3 Series', 'Audi A4'],
# # # #     'price': [7000, 5000, 9000, 11000, 15000, 20000]
# # # # }
# # # # df = pd.DataFrame(data)
# # # # df_group = df.groupby(by = 'model_year').count()[['name']]
# # # # print(df_group)
# # # # df_group_multiple = df.groupby(['acceration', 'mpg']).agg({'horsepower': ['mean', 'min', 'max']})
# # # # df_group_multiple.columns = ['hp_mean','hp_min','hp_max'] 
# # # # df = pd.DataFrame(data)
# # # # df_grouped = df.groupby(by = 'model_year').count()[['name']]


# # # # print(df_grouped)

# # # # df = pd.DataFrame({
# # # #     'name': ['Civic', 'Corolla', 'Accord'],
# # # #     'model_year': [2010, 2011, 2012],
# # # #     'mpg': [30.5, 32.0, 28.0],
# # # #     'weight': [2800, 2900, 3000]
# # # # })


# # # # numeric_cols = [column for column in df.columns if df[column].dtype in ['int64', 'float64']]
# # # # print(numeric_cols)
# # # # print(df.apply(lambda x: [x.min(), x.max()], axis=0, result_type='expand'))
# # # # print(df.apply(np.mean, axis=1, result_type='reduce'))
# # # # # print(df.apply(np.mean, axis=0, result_type='broadcast'))
# # # # df_grouped = df.groupby(by = ['Physics'])
# # # # # li_a = [31,56,12,62,75,21,11]
# # # # print(df_grouped)
# # # # li_arr = np.array(li_a)
# # # # print(np.min(li_arr))
# # # # list1 = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
# # # # agg = df[list1].agg(['min','max'])
# # # # print(agg)


# # # # df['total'] = df['Physics']+df["Biology"]+df['Mathematics']+df['chemistry']

# # # # df['rank'] = df['total'].rank(ascending=False).astype(int)
# # # # print(df)

# # # marks_A = {'Chemistry': [67,90,66,32], 
# # #         'Physics': [45,92,72,40],  
# # #           }
# # # marks_A_df = pd.DataFrame(marks_A, index = ['Subodh', 'Ram', 'Abdul', 'John'])
# # # marks_B = {'Chemistry': [72,45,60,98], 
# # #         'Physics': [78,34,72,95],  
# # #           }
# # # marks_B_df = pd.DataFrame(marks_B, index = ['Nandini', 'Zoya', 'Shivam', 'James'])

# # # combine_mark = pd.concat([marks_A_df,marks_B_df])
# # # print(combine_mark)

# # # import pandas as pd
# # # employee_table_1 = {
# # #     "Group": ['Accounting', 'Engineering', 'Engineering', 'HR']

# # # }
# # # employee_table_2 = {
# # #     "Hire_date": ['2004', '2008', '2012', '2014']
# # # }

# # # emp_df_1 = pd.DataFrame(employee_table_1, index= ['Jyoti', 'Sapna', 'Raj', 'Ramasamy'], dtype= str)
# # # emp_df_2 = pd.DataFrame(employee_table_2, index= ['Jyoti', 'Sapna', 'Raj', 'Ramasamy'], dtype= str)

# # # emp_df_1 = emp_df_1.reset_index().rename(columns={'index': 'Name'})
# # # emp_df_2 = emp_df_2.reset_index().rename(columns={'index':'Name'})
# # # emp_df_1 = emp_df_1.reset_index().rename(columns={'index':'Name'})
# # # emp_df_2 = emp_df_2.reset_index().rename(columns={'index':'Name'})
# # # print(emp_df_1)

# # # print(emp_df_2)

# # # merge_df = pd.merge(emp_df_1, emp_df_2, on='Name')
# # # pivot_table = pd.pivot_table(merge_df, values= 'Hire_date', index = 'Name', columns= 'Group', aggfunc='first')
# # # print(pivot_table)
# # # # merge_df = pd.merge(emp_df_1,emp_df_2,on='Name')
# # # print(merge_df)
# # import pandas as pd

# # employee_table_1 = {
# #     "Group": ['Accounting', 'Engineering', 'Engineering', 'HR']
# # }

# # employee_table_2 = {
# #     "Hire_date": ['2004', '2008', '2012', '2014']
# # }

# # emp_df_1 = pd.DataFrame(employee_table_1, index=['Jyoti', 'Sapna', 'Raj', 'Ramasamy'], dtype=str)
# # emp_df_2 = pd.DataFrame(employee_table_2, index=['Jyoti', 'Sapna', 'Raj', 'Ramasamy'], dtype=str)

# # # Reset index ONLY ONCE
# # emp_df_1 = emp_df_1.reset_index().rename(columns={'index': 'Name'})
# # emp_df_2 = emp_df_2.reset_index().rename(columns={'index': 'Name'})

# # # print(emp_df_1)
# # # print(emp_df_2)

# # merge_df = pd.merge(emp_df_1, emp_df_2, on='Name')

# # pivot_table = pd.pivot_table(
# #     merge_df,
# #     values='Hire_date',
# #     index='Name',
# #     columns='Group',
# #     aggfunc='first'
# # )
# # print(pivot_table)
# # cleaned = pivot_table.stack()
# # print(cleaned)


# # # print(merge_df)


# import pandas as pd

# df = pd.read_csv('auto-mpg.csv')
# # df.head()
# df_size = df.size
# df_column= df.columns
# df_non_missing_horsepower = df['horsepower'].count()
# df_how_many_missing_horsepower = df['horsepower'].isnull().sum()
# df_unique_value_count = df['origin'].value_counts()
# df_remove_duplicaties = df.drop_duplicates(subset=['origin'])

# #print(df.duplicated().sum())
# #extract the first name only of the manufacturer
# df['manufacturer_name'] = (
#     df['name']
#     .str.split()
#     .str[0]
# )
# #print(df['manufacturer_name'])
# manufacturer_count = df['manufacturer_name'].value_counts()
# most_frequent_manufacturer = manufacturer_count.iloc(1)
# group_by_manfacture_year = df.groupby(['year']).count()[['name']]
# print(most_frequent_manufacturer )


import numpy as np
import pandas as pd

# data = {
#     "A": [1, 2, 3, 3, np.nan, 4],
#     "B": [34, 52, '?', '*', 31, 53],
#     "C": [32, 42, 62, 4, 32, 52]
# }

# df = pd.DataFrame(data)
# find_null= df.isnull().sum()
# fill_spl = df.replace(['?','*'],np.nan)
# fill_mean = fill_spl.fillna(fill_spl.mean(numeric_only=True))
# remove_null = fill_spl.dropna()
# print(fill_mean)

df1 = pd.DataFrame({'key': ['A','B','C','D','E'], 'Col1': [1,2,3,4,5]})
df2 = pd.DataFrame({'key': ['B','C','D','E','F'], 'Col2': [5,6,7,8,9]})
print(df1)
print(df2)
mergeinner= pd.merge(df1,df2,on='key', how='inner')
mergeouter= pd.merge(df1,df2, on= 'key', how = 'outer')
mergeleft= pd.merge(df1,df2, on='key', how='left')
mergeright= pd.merge(df1,df2, on='key', how='right')
#print(mergeright)

df1_indexed = df1.set_index('key')
df2_indexed = df2.set_index('key')
inner_indexed = df1_indexed.join(df2_indexed,how='inner')
outer_indexed = df1_indexed.join(df2_indexed,how='outer')
left_indexed = df1_indexed.join(df2_indexed,how='left')
right_indexed = 
print(left_indexed)
