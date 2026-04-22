import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv("bmi.csv")

# 1. Convert Gender to numeric (Male: 0, Female: 1)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Separating Feature and Target Variables
X = df[['Height', 'Weight', 'Gender']]
y = df['Index']

# 2. Scale the features (CRITICAL for SGD)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Preparing Data for training
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# List of Learning rates
learning_rates = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5]
train_errors_list = []
test_errors_list = []

plt.figure(figsize=(12, 10)) # Make the plot large enough to see

for i in range(len(learning_rates)):
    # Using 'constant' learning rate as per your logic
    model = SGDRegressor(learning_rate='constant', eta0=learning_rates[i], random_state=42)
    
    train_errors = []
    test_errors = []

    for _ in range(200):
        model.partial_fit(X_train, y_train)
        
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        train_errors.append(mean_squared_error(y_train, y_train_pred))
        test_errors.append(mean_squared_error(y_test, y_test_pred))

    train_errors_list.append(train_errors)
    test_errors_list.append(test_errors)

    # Plotting
    plt.subplot(4, 2, (i + 1))
    plt.plot(train_errors, label='train')
    plt.plot(test_errors, label='test')
    plt.title(f'LR = {learning_rates[i]}')
    plt.legend()

plt.tight_layout()
plt.suptitle('Impact of Learning Rates on Linear Regression', y=1.02)
plt.show()