import pickle

#creating and training a model
regr = linear_model.LinearRegression()
regr.fit(features, label)

#serializing our model to a file called model.pkl
pickle.dump(regr, open("model.pkl", "wb"))

#loading a model from a file called model.pkl
model = pickle.load(open("model.pkl", "r"))