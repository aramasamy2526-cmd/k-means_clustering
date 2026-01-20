import pandas as pd
import numpy as np

# Create the data dictionary with NaN values
data = {
    'ColA': [1, 2, 5],
    'ColB': [np.nan, 3, 4],
    'ColC': [32, 5, np.nan],
    'ColD': [3, 4, 5]
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)

print("\nNull Counts:")
print(df.isnull().sum())

# Fill nulls using fillna() with a dictionary
df = df.fillna({
    'ColB': df['ColB'].mean(),      # Fill ColB nulls with mean
    'ColC': df['ColC'].median()     # Fill ColC nulls with median
})

print("\n--- DataFrame After Filling Nulls ---")
print(df)


import pandas as pd
import numpy as np

data = {
    'col_a' : [2,3,4],
    'col_b' : [1, np.nan, 3]

}
df = pd.DataFrame(data)

ds = df.fillna({
    'col_b':df['col_b'].mean()
    })
df = df.fillna({
    'col_b': df['col_b'].mean()
})
print(ds)

