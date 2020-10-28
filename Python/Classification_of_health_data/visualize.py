import numpy as np
import matplotlib.pyplot as plt
from data import split_data
from fitting import make_classifier
from matplotlib.colors import ListedColormap

def plot_scatter(features, method):
    """
    this function makes a scatterplot of the data with only two features, and also shows the classifiers prediciton in that plot
    Some of the functionality in this function is taken from https://github.com/UiO-IN3110/UiO-IN3110.github.io/blob/master/lectures/12_scikit_learn/fig_code/helpers.py
    under the function plot_iris.

    args:
    features - a list of features(only two) to be plotted against
    method - one of the three possible methods to make a classifier

    returns:
    nothing, but shows the scatterplot
    """
    data=split_data(features)

    if len(features)!=2:
        print("There must be exactly 2 features sent in to this functionm; returns None")
        return None

    if method==None:
        classifier=make_classifier(data)
    else:
        classifier=make_classifier(data, method)


    Xtest=data[1]
    Ytest=data[3]

    x_min, x_max = Xtest.values[:, 0].min() - 0.1, Xtest.values[:, 0].max() + 0.1
    y_min, y_max = Xtest.values[:, 1].min() - 0.1, Xtest.values[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    # Plot also the training points
    plt.scatter(Xtest.values[:, 0], Xtest.values[:, 1], c=Ytest, cmap=cmap_bold)
    plt.xlabel(features[0])
    plt.ylabel(features[1])
    plt.axis('tight')
    plt.show()


if __name__=="__main__":
    #features=["pregnant",  "glucose",  "pressure",  "triceps",  "insulin",  "mass",  "pedigree",  "age"]
    features=["age", "pregnant"]
    method="KNN"
    plot_scatter(features, method)
