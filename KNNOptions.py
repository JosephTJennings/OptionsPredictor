import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

def predictKNN(filename):
    seeds = pd.read_csv(filename, sep = ',')
    data = seeds.iloc[:, [0, 5, 6, 7, 8, 9, 10]] #Select optionsExpire,strikePrice,volume,delta,gamma,iv,rho,theta,vega
                                                #           0                3       4      5     6    7  8    9    10
                                                
                                                #Can increase accuracy by only selecting: optionsExpire, delta, gamma, iv, rho, theta, gamma  (0, 5, 6, 7, 8, 9, 10)
    labels = seeds.iloc[:, [1]] #Select inTheMoney
    x_train, x_test, y_train, y_test = train_test_split(data,labels, test_size=0.2, random_state=1 )
    knn = KNeighborsClassifier() #n_neighbors=30
    knn.fit(x_train, y_train.values.ravel())

    y_pred = knn.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    optionsType = filename.split("_")[1].split(".")[0]
    print("-------" + optionsType + " PREDICITON-------")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("")
    
def main():
    predictKNN("AAPL_main.csv")
    predictKNN("AAPL_puts.csv")
    predictKNN("AAPL_calls.csv")
    
if __name__ == "__main__":
    main()