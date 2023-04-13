### ➡️ Contexto:
Somos un banco que dispone de una base de datos con una gran cantidad de información sobre nuestros clientes. Nuestro objetivo es ayudar a los analistas a predecir la tasa de abandono de estos clientes para así poder reducirla. La base de datos incluye información demográfica como la edad, el sexo, el estado civil y la categoría de ingresos. También contiene información sobre el tipo de tarjeta, el número de meses en cartera y los periodos inactivos. Además, dispone de datos clave sobre el comportamiento de gasto de los clientes que se acercan a su decisión de cancelación. Entre esta última información hay el saldo total renovable, el límite de crédito, la tasa media de apertura a la compra y métricas analizables como el importe total del cambio del cuarto trimestre al primero o el índice medio de utilización.

Frente a este conjunto de datos podemos capturar información actualizada que puede determinar la estabilidad de la cuenta a largo plazo o su salida inminente.

### 📄 Dataset:
- CLIENTNUM: Identificador único para cada cliente. (Integer)
- Attrition_Flag: Indicador de si el cliente ha abandonado el banco o se queda (Boolean)
  - Attrited Customer -> 0
  - Existing Customer -> 1
- Customer_Age: Edad del cliente. (Integer)
- Gender: Sexo del cliente. (String)
- Dependent_count: Número de personas a cargo que tiene el cliente. (Integer)
- Education_Level: Nivel educativo del cliente. (String)
- Marital_Status: Marital status of customer. (String)
- Income_Category: Categoría de ingresos del cliente. (String)
- Card_Category: Tipo de tarjeta del cliente. (String)
- Months_on_book: El tiempo que el cliente ha estado en los libros. (Integer)
- Total_Relationship_Count: Número total de relaciones que tiene el cliente con el proveedor de la tarjeta de crédito. (Integer)
- Months_Inactive_12_mon: Número de meses que el cliente ha estado inactivo en los últimos doce meses.(Integer)
- Contacts_Count_12_mon: Número de contactos que ha tenido el cliente en los últimos doce meses. (Integer)
- Credit_Limit: Límite de crédito del cliente. (Integer)
- Total_Revolving_Bal: Saldo renovable total del cliente. (Integer)
- Avg_Open_To_Buy: Ratio medio de apertura a la compra del cliente. (Integer)
- Total_Amt_Chng_Q4_Q1: Importe total cambiado del trimestre 4 al trimestre 1. (Integer)
- Total_Trans_Amt: Importe total de la transacción. (Integer)
- Total_Trans_Ct: Recuento total de transacciones. (Integer)
- Total_Ct_Chng_Q4_Q1: Recuento total cambiado del trimestre 4 al trimestre 1. (Integer)
- Avg_Utilization_Ratio: Ratio de utilización media del cliente. (Integer)
- Months_Inactive_12_mon: Número de meses que el cliente ha estado inactivo en los últimos doce meses. (Integer)
- Contacts_Count_12_mon: Número de contactos que ha tenido el cliente en los últimos doce meses. (Integer)

- Credit_Limit: Límite de crédito del cliente. (Integer)
- Total_Revolving_Bal: Saldo rotativo total del cliente. (Integer)
-  Avg_Open_To_Buy: Ratio medio de apertura a compra del cliente. (Integer)
- Total_Amt_Chng_Q4_Q1: Importe total cambiado del trimestre 4 al trimestre 1. (Integer)
- Total_Trans_Amt: Importe total de la transacción. (Integer)
- Total_Trans_Ct: Recuento total de transacciones.. (Integer)
- Total_Ct_Chng_Q4_Q1: Recuento total cambiado del trimestre 4 al trimestre 1. (Integer)
- Avg_Utilization_Ratio: Ratio de utilización media del cliente. (Integer)

Para este desafío, tendrás que predecir el Attrition_Flag.

Hay dos archivos descargables:

train.csv: Son los datos descritos anteriormente que se utilizarán para entrenar el modelo. Descargar archivo de training

test.csv: Son los datos descritos anteriormente que se utilizarán en la predicción. Descargar archivo de testing

### 🎯 Objetivo:
Crea un modelo predictivo de clasificación para poder clasificar los datos del archivo de testing. Primero entrena tu modelo con el conjunto de datos de training y una vez que tengas el modelo que maximice la puntuación f1 (macro.) utiliza los datos de testing como entrada para tu modelo.

### ✅ Submission:
Archivo 1: predicciones.json:
Las predicciones deben estar en un archivo JSON llamado predictions.json, un ejemplo se puede encontrar en lo siguiente link.

En este fichero de predicciones, en formato json, cada fila corresponderá al valor predicho del test_idx, es decir, si el primer valor es un 2 significa que este 2 corresponde al primer fichero del conjunto de datos de prueba. Es IMPORTANTE llamar a la columna target tal y como se especifica en el formato. Recuerda que puedes utilizar la función to_json de pandas para convertir tu dataframe a json, la longitud de las predicciones tiene que ser la misma que en test.csv.

La puntuación de los objetivos vendrá de aplicar la puntuación f1 de las predicciones que hayas hecho al conjunto de datos de prueba con nuestra verdad fundamental.

IMPORTANTE: Las predicciones deben estar en formato int (0 o 1).