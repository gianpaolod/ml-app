import pandas as pandas

#loading our data as panda
df = pd.read_csv('winequality-red.csv', delimiter=";")

#getting only the column called quality
label = df['quality']

#getting every column called quality
features = df.drop('quality', axis=1)
