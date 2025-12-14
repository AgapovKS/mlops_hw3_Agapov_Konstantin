from sklearn.linear_model import LogisticRegression
import joblib

X = [[0, 0], [1, 1], [2, 2]]
y = [0, 0, 1]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
