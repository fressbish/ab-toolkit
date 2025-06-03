# kda_ab_toolkit

`kda_ab_toolkit` — инструмент для анализа A/B-тестов с поддержкой очистки данных, бутстрэпа, CUPED, стратификации и генерации отчетов.

## Установка

```bash
pip install kda_ab_toolkit
```

## Пример использования

```python
import kda_ab_toolkit abt

# Пример вызова одной из функций
abt.run_ab_analysis(data=df,
                  metric_type='mean',
                  stratification_column=None,
                  cleaning_method='auto',
                  alpha=0.05,
                  test_type='t-test',
                  cuped_flag=False,
                  mc_method=None,
                  silent=False)
```

## Описание параметров
- data – датафрейм с данными с колонками ['user_id',	'metric',	'metric_predperiod']
- metric_type – тип оцениваемой метрики (mean, median, conversion)
- stratification_column – колонка со значениями страт
- cleaning_method – метод очистки выбросов ('percentile', 'IQR', 'winsorization', 'Isolation Forest', 'DBSCAN', 'auto')
- alpha – порог значимости
- test_type – статистический тест для оценки гипотез ('t-test', 'z-test', 'mannwhitney', 'bootstrap', 'auto')
- cuped_flag – применение CUPED-анализа (необходима колонка 'metric_predperiod' в data)
- mc_method – метод корректировки p-value при множественных сравнениях (по умолчанию BH)
- silent – не выводит результаты анализа при значении True (необходимо при анализе в цикле)

## Возможности

- Очистка выбросов (DBSCAN, IsolationForest)
- Расчет доверительных интервалов через бутстрэп
- Методы повышения чувствительности: CUPED, стратификация
- Генерация текстового и визуального отчета
