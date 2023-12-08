from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Определение архитектуры модели
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(num_features,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

# Конфигурация функции потерь и оптимизатора
model.compile(loss='mse', optimizer='adam')

