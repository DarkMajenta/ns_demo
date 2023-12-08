# Обучение модели
model.fit(train_data_scaled, train_labels, epochs=10, batch_size=32)

# Оценка метрик работы модели
loss = model.evaluate(test_data_scaled, test_labels)

