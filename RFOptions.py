import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score


def predictRF(filename):
    df = pd.read_csv(filename)

    # [0, 3, 4, 5, 6, 7, 8, 9, 10]
    X = df.iloc[:, [0, 5, 6, 7, 8, 9, 10]]
    y = df.iloc[:, [1]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, shuffle=False)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print(f'!! Scores for {filename}:')
    print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')
    print(f'Precision: {precision_score(y_test, y_pred):.2f}')
    print(f'Recall: {recall_score(y_test, y_pred):.2f}\n')



if __name__ == "__main__":
    predictRF('./AAPL_main.csv')
    predictRF('./AAPL_calls.csv')
    predictRF('./AAPL_puts.csv')
