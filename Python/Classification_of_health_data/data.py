import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import train_test_split

def Scatter_plot(feature1, feature2, outfile):
    """
    takes in two features and makes and saves a scatterplot in the working directory as outfile. It also reads a file with statistical data from a
    file called diabetes.csv

    args:
    feature1 - the first paramtere/feature one wants to make the scatterplot of in the x-axis. A string
    feature2 - the second parameter/feature one wants to make the scatterplot of in the y-axis. Also a string
    outfile - the name of the file the plot is saved to

    returns
    Nothing, but saves the scatterplot to outfile in working direcctory
    """

    data=pd.read_csv("diabetes.csv")

    #drops all the rows that contain a null in diabetes.csv
    data=data.dropna()

    #this part is to make the positive dots on the scatterplot to be red, and negatives to be blue
    c=[]
    diabetes=data["diabetes"]
    for k in diabetes:
        if k=="pos":
            c.append("red")
        else:
            c.append("blue")

    #extract only the data that is under the chosen features
    x=data[feature1]
    y=data[feature2]

    #makes the plot, puts on labels and saves the figure to a file
    plt.scatter(x,y,c=c)
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.savefig(outfile)


def split_data(features):
    """
    This function splits the dataset from diabetes.csv in a training and validating set, with the training set to be 80%, and the validating set to be 20%.
    the function takes in a list of features, and makes nd cuts the dataset down to only contain those features, and then splits this pruned dataset.

    args:
    features - a list of all the features that one wants to have in the dataset

    returns:
    list - A list containing four elements, that is the splitted dataset
    list = [Xtrain, Xtest, Ytrain, Ytest]

    """
    #read the data
    data=pd.read_csv("diabetes.csv")
    #drop all rows with null
    data=data.dropna()
    d={"pos":1, "neg":0}
    #replace all pos and neg with 1 and 0
    data=data.replace(d)

    #prunes/cuts the dataset down to only contain the features
    data1=data[features]

    #the actual splitting into train and test happens here
    Xtrain, Xtest, Ytrain, Ytest=train_test_split(data1, data["diabetes"], test_size=0.8)

    #puts the splitted dataset in a list and returns the list
    list=[Xtrain, Xtest, Ytrain, Ytest]
    return list


if __name__=="__main__":
    #tar inn parametre som commandlinearguments
    feature1=sys.argv[1]
    feature2=sys.argv[2]
    outfile=sys.argv[3]

    Scatter_plot(feature1, feature2, outfile)
