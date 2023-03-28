import pandas as pd
from IPython.display import display
import os
import matplotlib.pyplot as plt
import math
import numpy as np
from nltk.tokenize import sent_tokenize
import string
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from skmultilearn.problem_transform import BinaryRelevance

enc=OneHotEncoder()

class DataFrameSelector(BaseEstimator):

    def __init__(self, attribute_names):
        self.attribute_names= attribute_names

    def fit(self,X, y = None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


local_path = '/content/'

files = ['bahai', 'buddhism', 'christianity', 'hinduism', 'historical', 'islam','judaism', 'p_j_s', 'shinto', 't_c', 'iranian']
additions = ['BA', 'BU', 'CR', 'HD', 'HI', 'IS', 'JU', 'IN', 'JA', 'CH', 'IR']
frames = [0]*11

def addColumn(files, additions, frames):
    for i in range(len(files)):
        csv_path=os.path.join(local_path, files[i] + '.csv')
        df = pd.read_csv(csv_path)
        df2 = df.assign(Religion=additions[i])
        frames[i] = df2

# combine dataframes to one
addColumn(files, additions, frames)
combined_df = pd.concat(frames, ignore_index=True)
combined_df = combined_df.rename(columns={"Language of Original Document": "Language"})

# IMPUTATION
def imputation(combined_df):
    north = ["Hong", "Macau", "Israel", "Japan", "Singapore", "Korea", "Canada", "Europe", "Russia", "Taiwan", "Australia", "Zealand", "Taiwan", "US", "UK", "Germany", "France", "Spain", "Netherlands", "Italy", "Cyprus", "Austria", "Belgium", "Bulgaria", "Croatia", "Czech", "Denmark", "Estonia", "Finland", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Sweden", "Iceland", "Liechtenstein", "Norway", "States", "Kingdom", "Toronto", "Switzerland"]
    # western european languages that spread as  a result of colonisation
    lang_powerhouses = ["English", "French", "Spanish", "Portuguese", "German", "Afrikaans" ]

    # replace funding details with 0 if nan, 1 else
    combined_df["Funding Details"].where(combined_df["Funding Details"] != combined_df["Funding Details"], 1, inplace = True)
    combined_df["Funding Details"].where(combined_df["Funding Details"] == 1, 0, inplace = True)

    # drop column link
    combined_df.drop(columns=["Link"], axis=1, inplace=True)

    # not using get dummies on religion, doing one hot later
    # replace nominal categories (RE) to numerical ->
    combined_df = pd.get_dummies(combined_df, columns=["Religion"])

    # remove rows where affilitations is null
    combined_df = combined_df.dropna(subset=["Affiliations"])
    combined_df.reset_index(drop=True, inplace=True)
    print(len(combined_df))


    # remove punctuation
    for i in range(len(combined_df)-1):
        combined_df.loc[i+1, "Affiliations"] = combined_df.loc[i+1, "Affiliations"].translate(str.maketrans('', '', string.punctuation))


    # if affiliation in north, replace with 0
    for i in range (len(north)):
        combined_df.Affiliations = combined_df.Affiliations.apply(lambda x: '0' if north[i] in x else x)

    # if affiliation not in north, replace with 1
    filter  = (combined_df['Affiliations'] != '0' )
    combined_df.loc[filter, 'Affiliations'] = 1

    # 0 value from string to int
    filter  = (combined_df['Affiliations'] == '0' )
    combined_df.loc[filter, 'Affiliations'] = 0
    # datatype is object.. may be incorrect!


    # replace langauge with binary tooo
    # if lang in western powerhouses, replace with 0
    for i in range (len(lang_powerhouses)):
        combined_df.Language = combined_df.Language.apply(lambda x: '0' if lang_powerhouses[i] in x else x)

    # if lang not in western, replace with 1
    filter  = (combined_df['Language'] != '0' )
    combined_df.loc[filter, 'Language'] = 1

    # 0 value from string to int
    filter  = (combined_df['Language'] == '0' )
    combined_df.loc[filter, 'Language'] = 0

    return combined_df

imputed_df = imputation(combined_df)
train_set, test_set = train_test_split(imputed_df, test_size= 0.3, random_state=42)
# from now on only using train set -> df
df=train_set.copy()
# # religion is goal state -> goal state must be numerical?
# # data_labels=train_set["Year"].copy()
# X = df[["Language", "Year", "Cited by", "Affiliations", "Funding Details"]]
# y = df[['Religion_BA', 'Religion_BU', 'Religion_CR', "Religion_HD", "Religion_HI", "Religion_IS", "Religion_JU", "Religion_IN", "Religion_JA", "Religion_CH", "Religion_IR"]]

df['Affiliations'] = df['Affiliations'].astype(int)
df['Language'] = df['Language'].astype(int)
df['Funding Details'] = df['Funding Details'].astype(int)

def fit():
  enc.fit(df["Affiliations"].values.reshape(-1,1))
  enc.fit(df["Language"].values.reshape(-1,1))
  enc.fit(df["Funding Details"].values.reshape(-1,1))
  # enc.fit(df["Religion"].values.reshape(-1,1))

def transform():
  enc.transform(df["Affiliations"].values.reshape(-1,1)).toarray()
  enc.transform(df["Language"].values.reshape(-1,1)).toarray()
  enc.transform(df["Funding Details"].values.reshape(-1,1)).toarray()
  # enc.transform(df["Religion"].values.reshape(-1,1)).toarray()

def fit_transform():
  fit()
  transform()

# seperate pipelines for numerical and cetegorical data?
num_attribs=["Year", "Cited by"]
cat_attribs=list(df)
cat_attribs.remove("Year")
cat_attribs.remove("Cited by")
# print(cat_attribs)

# test here -> seemed to work indivitually, moves to fit & transform
# enc.fit(df["Religion"].values.reshape(-1,1))
# print(enc.categories_)
# enc.transform(df["Religion"].values.reshape(-1,1)).toarray()

# numeric pipeline: scales values
num_pipeline= Pipeline([
    ('selector', DataFrameSelector(num_attribs)),
    # ('imputer',SimpleImputer(strategy="median")),
    # ('attribs_adder',CombinedAttributesAdder()),
    ('std_scaler',StandardScaler())
])

# categorical pipeline: encodes
cat_pipeline = Pipeline([
    ('selector',DataFrameSelector(cat_attribs)),
    ('one hot',OneHotEncoder())
])


full_pipeline = FeatureUnion(transformer_list=[
    ("num_pipeline",num_pipeline),
    ("cat_pipeline",cat_pipeline)
])


data_prepared = full_pipeline.fit_transform(df)

# set feautures and predictors after fit_transform
# religion is goal state -> goal state must be numerical?
# data_labels=train_set["Year"].copy()
X = df[["Year", "Cited by","Language", "Affiliations", "Funding Details"]]
y = df[['Religion_BA', 'Religion_BU', 'Religion_CR', "Religion_HD", "Religion_HI", "Religion_IS", "Religion_JU", "Religion_IN", "Religion_JA", "Religion_CH", "Religion_IR"]]

# X
df.Language.dtype
df.dtypes
# data_prepared.dtypes


# multiclass classification
binary_rel_clf = BinaryRelevance(MultinomialNB())
binary_rel_clf.fit(X,y)
