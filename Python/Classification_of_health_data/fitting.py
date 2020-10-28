from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from data import split_data
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

#this function is used only for debugging purposes, but didnt want to delete it, and is not used in the assignment
def test_fordeling(Xtest, Xtrain, Ytest, Ytrain):
    """
    This function takes in the splitted dataset and tests if the number of positives and negatives are approximatly the same in the two
    sets as suggested by the assignment

    args:
    The splitted training set

    returns:
    nothing, but prints out the result to terminal
    """
    #counts the amount of positives in the train set
    train=0
    for i in range(len(Ytrain.values)):
        if Ytrain.values[i]==1:
            train+=1

    #counts the amount of negatives in the test set
    test=0
    for i in range(len(Ytest.values)):
        if Ytest.values[i]==1:
            test+=1

    #prints out the results
    print(test/len(Ytest.values))
    print("Ytest")
    print(train/len(Ytrain.values))
    print("Ytrain")



def make_classifier(data, method="KNN"):
    """
    this function trains and returns classifiers using machine learning

    args:
    data - the splitted dataset
    method[optional] - specifies to use on of the three possible methods implemented. If not passed, then uses KNN

    returns:
    classifier - A trained classifier

    """
    #data is a list when passed to this function, and need to extranct its elements
    Xtrain=data[0]
    Xtest=data[1]
    Ytrain=data[2]
    Ytest=data[3]

    #if sentence checking which of the three classifiers to be used based on the method parameter
    if method=="KNN":
        k_range = range(1, 100)
        scores = []
        #here we run the KNN with different values for k
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(Xtest, Ytest)
            target_pred = knn.predict(Xtrain)
            scores.append(metrics.accuracy_score(Ytrain, target_pred))
        high=scores[0]
        high_index=1
        #here we check which k-value makes the best fit and then we use that value
        for i in range(len(scores)):
            if scores[i]>high:
                high=scores[i]
                high_index=i
        #here we make the actual classifier
        classifier=KNeighborsClassifier(n_neighbors=high_index)
    elif method=="SVC":
        #making the classifier
        classifier=SVC(gamma='scale')
    else:
        #making the classifier
        classifier=LogisticRegression(penalty='l2')

    #trains the classifier
    classifier.fit(Xtest, Ytest)

    #tests the classifier with the validation set
    pred_target=classifier.predict(Xtrain)
    print(metrics.accuracy_score(Ytrain, pred_target))

    return classifier


if __name__=="__main__":
    #this is a list of all the features in the dataset. To test that it works with different features I just removed some of the
    #features from this list, and tried with different ones to see htat it worked
    features=["pregnant",  "glucose",  "pressure",  "triceps",  "insulin",  "mass",  "pedigree",  "age"]

    list=split_data(features)

    make_classifier(list, "KNN")
    make_classifier(list, "SVC")
    make_classifier(list, "IlikeTrains")
