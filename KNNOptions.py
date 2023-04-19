import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

def predictCalls():
    seeds = pd.read_csv('AAPL_calls.csv', sep = ',')
    data = seeds.iloc[:, [0, 5, 6, 7, 8, 9, 10]] #Select optionsExpire,strikePrice,volume,delta,gamma,iv,rho,theta,vega
                                                #Can increase accuracy by only selecting: optionsExpire, delta, gamma, iv, rho, theta, gamma
    labels = seeds.iloc[:, [1]] #Select inTheMoney
    x_train, x_test, y_train, y_test = train_test_split(data,labels, test_size=0.2, random_state=1 )
    knn = KNeighborsClassifier() #n_neighbors=30
    knn.fit(x_train, y_train.values.ravel())

    y_pred = knn.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    print("-------CALLS PREDICITON-------")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("")
    
def predictPuts():
    seeds = pd.read_csv('AAPL_puts.csv', sep = ',')
    data = seeds.iloc[:, [0, 5, 6, 7, 8, 9, 10]] #Select optionsExpire,strikePrice,volume,delta,gamma,iv,rho,theta,vega
                                                #Can increase accuracy by only selecting: optionsExpire, delta, gamma, iv, rho, theta, gamma
    labels = seeds.iloc[:, [1]] #Select inTheMoney
    x_train, x_test, y_train, y_test = train_test_split(data,labels, test_size=0.2, random_state=1 )
    knn = KNeighborsClassifier() #n_neighbors=30
    knn.fit(x_train, y_train.values.ravel())

    y_pred = knn.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    print("-------PUTS PREDICITON-------")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("")

def predictMain():
    seeds = pd.read_csv('AAPL_main.csv', sep = ',')
    data = seeds.iloc[:, [0, 5, 6, 7, 8, 9, 10]] #Select optionsExpire,strikePrice,volume,delta,gamma,iv,rho,theta,vega
                                                #Can increase accuracy by only selecting: optionsExpire, delta, gamma, iv, rho, theta, gamma
    labels = seeds.iloc[:, [1]] #Select inTheMoney
    x_train, x_test, y_train, y_test = train_test_split(data,labels, test_size=0.2, random_state=1 )
    knn = KNeighborsClassifier() #n_neighbors=30
    knn.fit(x_train, y_train.values.ravel())

    y_pred = knn.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    print("-------MAIN PREDICITON-------")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("")
    
def main():
    predictCalls()
    predictPuts()
    predictMain()
    
if __name__ == "__main__":
    main()