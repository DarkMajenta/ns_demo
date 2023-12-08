from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Разделение данных на обучающий и тестовый наборы
train_data, test_data = train_test_split(data, test_size=0.2)

# Масштабирование данных
scaler = MinMaxScaler()
train_data_scaled = scaler.fit_transform(train_data.values)
test_data_scaled = scaler.transform(test_data.values)

