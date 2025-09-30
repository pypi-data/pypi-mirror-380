# AletheIA Genetic Optimizers (AGO)

## Equipo de desarrollo

| Nombre                  | Rol                         | Información de contacto  | Perfil de LinkedIn                                          |
|-------------------------|-----------------------------|--------------------------|-------------------------------------------------------------|
| Daniel Sarabia Torres   | Full Stack AI & Q Developer | dsarabiatorres@gmail.com | https://es.linkedin.com/in/danielsarabiatorres              |
| Luciano Ezequiel Bizin  | Full Stack AI & Q Developer | lucianobizin@gmail.com   | https://www.linkedin.com/in/luciano-ezequiel-bizin-81b85497 |

## Instalación

```pip install aletheia-genetic-optimizers```

## Introducción

Este proyecto implementa un algoritmo genético clásico diseñado para abordar problemas de optimización combinatoria. 

La arquitectura del algoritmo utiliza los principios clásicos de la evolución, buscando así, encontrar soluciones óptimas sin la necesidad de recorrer todo el espacio de datos.

El objetivo principal del AletheIA Genetic Optimizar es resolver dos clases generales de problemas:

- *`bounds_restricted`*: Problemas con límites o restricciones estructurales parciales, en los que se permite cierta flexibilidad pero dentro de márgenes definidos (por ejemplo, pensar en la búsqueda de hiperparámetros para un modelo de ML o DL).

- *`totally_restricted`*: Problemas con restricciones estrictas en los valores permitidos y en las configuraciones válidas, como el Traveling Salesman Problem (TSP), donde solo se aceptan permutaciones válidas sin repeticiones.

--------------------------------------------

## Explicación detallada de casos de uso 

Se explica de manera detallada ambos casos de uso: `bounds_restricted` (búsqueda de hiperparámetros para un modelo de ML) y `totally_restricted` (TSP)

## Caso de uso 1: 

En este apartado se describe el caso de uso para resolver el problema de encontrar los mejores hiperparámetros para un modelo de IA, en este caso, para un modelo básico de ML.

### Entendimiento del problema: El problema de encontrar los mejores hiperparámetros para un modelo de IA

El problema encontrar los mejores hiperparámetros para un modelo de IA puede ser abarcado sin ningún problema con los simuladores u ordenadores cuánticos de hoy en día. 

Imaginar que queremos entrenar una red neuronal o un modelo de ML, y para tal situación, necesitamos encontrar los mejores hiperparámetros para nuestro modelo.

El desafío radica en que, a medida que aumenta el número de hiperparámetros a optimizar (aunque también puede ser la estructura de la red neuronal o cantidad de nueronas si se ha categorizado estos valores), es necesario encontrar una muy buena combinación de hiperparámetros, lo que resulta muy costoso utilizando métodos tradicionales.

### Ejemplo de código

```
from sklearn.datasets import fetch_california_housing, fetch_openml, load_breast_cancer
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error
from aletheia_genetic_optimizers import GenethicOptimizer, BoundCreator
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from typing import Literal

import lightgbm as lgb
import pandas as pd
import numpy as np
import datetime



# -- Definimos la función objetivo
def example_1_bounds_no_predefinidos():

    def objective_function(individual, dataset_loader: Literal["fetch_california_housing", "glass", "breast_cancer"] = "breast_cancer", random_state=42):
        # Cargar dataset
        match dataset_loader:
            case "fetch_california_housing":
                data = fetch_california_housing()
                problem_type = 'regression'
                test_size = 0.2
            case "breast_cancer":
                data = load_breast_cancer()
                problem_type = 'binary'
                test_size = 0.7
            case "glass":
                data = fetch_openml(name="glass", version=1, as_frame=True)
                problem_type = 'multiclass'
                test_size = 0.2
            case _:
                data = fetch_california_housing()
                problem_type = 'regression'
                test_size = 0.2

        # print(f"PROBLEMA SKLEARN: {dataset_loader}")
        individual_dict = individual.get_individual_values()
        X, y = data.data, data.target

        # Dividir y normalizar
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        scaler = StandardScaler()
        X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=data.feature_names)
        X_test = pd.DataFrame(scaler.transform(X_test), columns=data.feature_names)

        # Tiempo inicial
        start_time = datetime.datetime.now()

        # Entrenar y predecir
        if problem_type == 'regression':
            model = lgb.LGBMRegressor(
                n_estimators=int(individual_dict["n_estimators"]),
                max_depth=individual_dict["max_depth"],
                verbose=-1,
                random_state=random_state
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)

            # print(f"Mae: {mae} - R2: {score}")

        else:
            model = lgb.LGBMClassifier(
                n_estimators=int(individual_dict["n_estimators"]),
                max_depth=individual_dict["max_depth"],
                verbose=-1,
                random_state=42
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = accuracy_score(y_test, y_pred)

            # print(f"Acc: {score}")

        # Calcular tiempo
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()

        # Penalización por tiempo
        reference_time = 0.5  # segundos
        max_penalty_ratio = 0.01  # 1%
        time_penalty = max_penalty_ratio * score * (elapsed_time / reference_time)
        time_penalty = min(time_penalty, max_penalty_ratio * score)

        penalized_score = score - time_penalty

        # print(f"[{problem_type.upper()}] Score: {score:.4f} | Penalized: {penalized_score:.4f} | Time: {elapsed_time:.2f}s")

        return score

    # -- Creamos el diccionario de bounds
    bounds = BoundCreator()
    bounds.add_interval_bound("n_estimators", 50, 1000, 10, 1500, "int")
    bounds.add_predefined_bound("max_depth", (1, 2, 3, 4, 5, 6, 7, 8, 9), "int")

    return GenethicOptimizer(bounds.get_bound(),
                             50,
                             20,
                             objective_function,
                             "bound_restricted",
                             "maximize",
                             "ea_simple",
                             3,
                             0.25,
                             0.35,
                             )

genetic_optimizer_object: GenethicOptimizer = example_1_bounds_no_predefinidos()
print(genetic_optimizer_object.get_best_individual().get_individual_values())

```

#### El enfoque genético

El código proporcionado implementa un algoritmo genético para abordar el problema de encotrar los mejores hiperparámetros de un modelo de IA. 

A continuación, se explica cómo funciona este algoritmo y sus potenciales ventajas:

1. *Introducción programática:* 

* El `individual` que recibe la función `objective_function` representa un conjunto de hiperparámetros (-por ejemplo: {max_depth: 2, n_estimators: 325-).
* El algoritmo genético se ejecuta al momento de generarse la primera generación, se obtienen los fitness de cada Individual y se pasa a la fase de torneo y reproducción.
* ¿Cómo sucede este proceso de selección? Partimos de los individuos de la generación previa, se seleccionan aleatoriamente un número 'podium_size' de individuos y se ponen a competir. Esta competición consiste en que el mejor de los 'podium_size' pasa a la siguiente fase y el resto es descartado.
* ¿Cómo sucede este proceso de reproducción? Dependiendo del tipo de problema, se mezclan los genes de los individuos de una forma u otra, obteniendo así los descendientes
* Finalmente, se lleva a cabo el proceso de mutación (en el que cada gen tiene una probabilidad x de mutar) para agregar variabilidad extra

2. *Función objetivo (`objective_function`):*

Esta función calcula el accuracy o el MAE dependiendo del problema, o cualquier otra métrica de interés.

* Toma un `individual` (un objeto que posee como valores la solución potencial) como entrada.
* Recupera los hiperparámetros del `individual` (reproducido y mutado en el algorítmo genético cuántico).
* Utiliza esos hiperparámetros para calcular el resultado de la función objetivo.
* Se devuelve el `score`, que el algoritmo genético busca minimizar/maximizar según el tipo de problema.

3. *Algoritmo genético (`GenethicOptimizer`):* Esta clase implementa la lógica central del algoritmo genético cuántico.

    * *Inicialización:* Comienza creando una población de soluciones potenciales (rutas). La naturaleza cuántica se utiliza para generar esta población inicial.
    * *Evaluación:* La función `objective_function` se utiliza para evaluar la "aptitud" de cada individuo en la población.
    * *Selección:* Los individuos con mejor aptitud tienen más probabilidades de ser seleccionados como "mejores padres" para crear la siguiente generación.
    * *Cruce:* El material genético (hiperparámetros) de dos individuos padres se combinan para crear nuevos individuos descendientes. 
    * *Mutación:* Se introducen pequeños cambios aleatorios en los valores de los hiperparámetros de los descendientes para mantener la diversidad en la población y evitar quedar atrapado en óptimos locales.
    * *Terminación:* El algoritmo continúa durante un número específico de generaciones (`num_generations`) o hasta que se cumple un criterio de detención (`early_stopping_generations`).

4*Límites (`BoundCreator`):* Los límites definen los posibles valores para cada "gen" en el individuo (en este caso, el índice de una ciudad).

### Posibles usos reales

El Aletheia Genetic Optimizers está diseñado para resolver varios tipos de problemas de optimización. Uno de los escenarios para los que se ha programado, es encontrar los mejores hiperparámetros de modelos de IA, o problemas de tipo similar. 

A nivel real -al momento- puede ser utilizado para resolver cuantiosos problemas de este tipo:

| Industria             | Tipo de datos                                   | Ejemplos de modelos a usar   | Beneficio del enfoque cuántico-genético                                      |
|-----------------------|--------------------------------------------------|------------------------------------|--------------------------------------------------------------------------------|
| Finanzas              | Transacciones bancarias                          | LGBMClassifier, XGBoost            | Detección más precisa de fraude, menos falsos positivos, búsqueda más rápida  |
| Energía               | Variables climáticas, consumo histórico          | LGBMRegressor, Redes neuronales    | Mejor predicción de demanda, optimización eficiente de recursos energéticos   |
| Salud                 | Datos clínicos, imágenes médicas                 | RandomForest, CNNs, LGBMClassifier | Diagnósticos automáticos más precisos y rápidos                               |
| Marketing y Ventas    | Historial de usuarios, CRM                       | XGBoost, CatBoost, Árboles         | Mejor segmentación y predicción de abandono (churn)                           |
| Ciberseguridad        | Logs de red, sesiones de conexión                | RandomForest, SVM, LSTM            | Mejora en la detección de tráfico malicioso, reducción de falsos negativos    |
| Agricultura           | Condiciones ambientales, suelo, clima            | LGBMRegressor, Redes neuronales    | Predicción precisa del rendimiento, decisiones agronómicas más acertadas      |
| Industria 4.0         | Datos sensoriales de maquinaria                  | LSTM, RandomForest, SVM            | Mantenimiento predictivo, detección temprana de fallas                        |
| Educación             | Comportamiento de estudiantes, resultados        | Sistemas de recomendación, Árboles | Personalización del aprendizaje, mayor engagement y retención de alumnos      |
| Transporte y Logística| Rutas, tiempos de entrega, demanda               | Regresión, KNN, RandomForest       | Optimización del reparto, predicción de demanda, mejora en eficiencia logística|
| Recursos Humanos      | CVs, entrevistas, datos de rendimiento laboral   | NLP + árboles, XGBoost             | Mejora del proceso de selección, predicción de rendimiento de empleados       |
| Medioambiente         | Datos satelitales, sensores ambientales          | LGBM, CNN, RandomForest            | Monitoreo ambiental en tiempo real, predicción de fenómenos climáticos        |
| Telecomunicaciones    | Datos de llamadas, uso de apps, geolocalización  | CatBoost, Redes neuronales         | Predicción de churn, optimización de red, segmentación de usuarios            |
| eCommerce             | Historial de compras, comportamiento de navegación| XGBoost, Recommender Systems       | Mejora en sistemas de recomendación y personalización                         |
| Sector Legal          | Documentos legales, jurisprudencia, contratos    | NLP + Transformers, Decision Trees | Análisis automatizado de textos legales, detección de cláusulas de riesgo     |
| Juegos y Entretenimiento | Comportamiento de jugadores, patrones de uso  | RandomForest, Deep Q-Learning      | Optimización de diseño de niveles, detección de comportamiento irregular      |


### Ventajas de usar el AletheIA Genetic Optimizers para este tipo de problemas

* *Exploración mejorada del espacio de soluciones:* En lugar de usar metodos de fuerza bruta como RandomSearch o GridSearch, el algoritmo genético converge más rápido y mejor por la búsqueda guiada.

#### Conclusiones luego de ver los resultados

Para este tipo de problemas, el AletheIA Genetic Optimizers ha demostrado ser una herramienta útil y versátil a la hora de encontrar soluciones a este tipo de problemas .

En general, en las pruebas realizadas para contrastar su potencialidad con respecto a otros algoritmos genético cuánticos, ha sido superado por el AletheIA Quantum Genetic Optimizers, en cantidad de generaciones requeridas para alcanzar la mejor métrica posible para el modelo y problema evaluado, tanto para problemas de clasificación como de regresión. Sin embargo, se debe tener en cuenta, que no converge a la manera que lo hace un optimizador clásico donde se puede notar que toda la población va acompañando la suba o baja de la métrica evaluada. En el caso del AletheIA Quantum Genetic Optimizers se aprecia un procedimiento más elitista, es decir, encuentra por capacidad explotaria máximos o mínimos globales muy buenos, pero lo hacen pocos individuos de cada población.

--------------------------------------------

## Caso de uso 2: 

En este apartado se describe el caso de uso para resolver el Problema del Viajero (TSP, por sus siglas en inglés) en sus variantes de ciclo cerrado y abierto.

### Entendimiento del problema: El problema del viajante de comercio (TSP)

El problema del viajante de comercio es un problema clásico de optimización combinatoria. 

Imaginar un viajante que necesita visitar un conjunto de ciudades, cuyo objetivo es encontrar la ruta más corta posible que visite cada ciudad exactamente una vez y, dependiendo de la variante:

* *Ciclo cerrado (con retorno al origen):* El viajante debe regresar a la ciudad de inicio después de visitar todas las demás ciudades, formando un tour o ciclo completo.
* *Ciclo abierto (sin retorno al origen):* El viajante visita cada ciudad exactamente una vez, pero no necesita regresar a la ciudad de inicio.

El desafío radica en que, a medida que aumenta el número de ciudades, la cantidad de posibles rutas crece factorialmente, lo que hace que encontrar la solución óptima sea computacionalmente muy costoso utilizando métodos de fuerza bruta. Por lo que el algoritmo genético se presenta como una solución eficiente que consigue muy buenos resultados en tiempos reducidos. 

### Ejemplo de código

```
from sklearn.datasets import fetch_california_housing, fetch_openml, load_breast_cancer
from aletheia_genetic_optimizers import GenethicOptimizer, BoundCreator, Individual
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from typing import Literal

import lightgbm as lgb
import pandas as pd
import numpy as np
import datetime


def example_2_tsp():
    # Coordenadas de ciudades (ejemplo con 5 ciudades)

    def objective_function(individual):
        original_cities = {
            0: (4.178515558765522, 3.8658505110962347),
            1: (9.404615166221248, 8.398020682045034),
            2: (0.3782334121284714, 8.295288013706802),
            3: (9.669161753695562, 5.593501025856912),
            4: (9.870966532678576, 4.756484445482374),
            5: (3.5045826424785007, 1.1043994011149494),
            6: (5.548867108083866, 5.842473649079045),
            7: (1.11377627026643, 1.304647970128091),
            8: (5.133591646349645, 3.8238217557909038),
            9: (7.074655346940579, 3.6554091142752734),
            10: (9.640123872995837, 1.3285594561699254),
            11: (0.021205320973052277, 7.018385604153457),
            12: (2.048903069073358, 2.562383464533476),
            13: (2.289964825687684, 4.325937821712228),
            14: (6.315627335092245, 3.7506598107821656),
            15: (1.0589427543395036, 6.2520630725232),
            16: (9.218474645470067, 4.106769373018785),
            17: (4.62163288328154, 9.583091224200263),
            18: (7.477615269848112, 7.597659062497909),
            19: (0.25092704950321565, 6.699275814039302),
        }

        # Obtener valores únicos en route y ordenarlos
        route = list(individual.get_individual_values().values())
        unique_cities = sorted(set(route))  # Se asegura de tener un orden fijo

        # Crear nuevo índice de ciudades dinámico
        cities = {idx: original_cities[city] for idx, city in enumerate(unique_cities)}

        num_cities = len(cities)
        distance_matrix = np.zeros((num_cities, num_cities))

        # Calcular la matriz de distancias con los nuevos índices
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    x1, y1 = cities[i]
                    x2, y2 = cities[j]
                    distance_matrix[i][j] = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # Convertir route a los nuevos índices
        route_mapped = [unique_cities.index(city) for city in route]

        # Calcular distancia total
        total_distance = sum(
            distance_matrix[route_mapped[i]][route_mapped[(i + 1) % len(route_mapped)]]
            for i in range(len(route_mapped))
        )

        return total_distance

    # -- Creamos el diccionario de bounds
    range_list: tuple = tuple([z for z in range(0, 20)])
    bounds = BoundCreator()
    bounds.add_predefined_bound("city_zero", range_list, "int")
    bounds.add_predefined_bound("city_one", range_list, "int")
    bounds.add_predefined_bound("city_two", range_list, "int")
    bounds.add_predefined_bound("city_three", range_list, "int")
    bounds.add_predefined_bound("city_four", range_list, "int")
    bounds.add_predefined_bound("city_five", range_list, "int")
    bounds.add_predefined_bound("city_six", range_list, "int")
    bounds.add_predefined_bound("city_seven", range_list, "int")
    bounds.add_predefined_bound("city_eight", range_list, "int")
    bounds.add_predefined_bound("city_nine", range_list, "int")
    bounds.add_predefined_bound("city_ten", range_list, "int")
    bounds.add_predefined_bound("city_eleven", range_list, "int")
    bounds.add_predefined_bound("city_twelve", range_list, "int")
    bounds.add_predefined_bound("city_trece", range_list, "int")
    bounds.add_predefined_bound("city_14", range_list, "int")
    bounds.add_predefined_bound("city_15", range_list, "int")
    bounds.add_predefined_bound("city_16", range_list, "int")
    bounds.add_predefined_bound("city_17", range_list, "int")
    bounds.add_predefined_bound("city_18", range_list, "int")
    bounds.add_predefined_bound("city_19", range_list, "int")

    return GenethicOptimizer(bounds.get_bound(),
                             500,
                             100,
                             objective_function,
                             "full_restricted",
                             "minimize",
                             "ea_simple",
                             3,
                             0.25,
                             0.1,
                             'normal',
                             True
                             )

genetic_optimizer_object: GenethicOptimizer = example_2_tsp()
print(genetic_optimizer_object.get_best_individual().get_individual_values())
```

#### El enfoque genético

El código proporcionado implementa un algoritmo genético cuántico para abordar el problema del Traveling Salesman Problem (TSP). 

A continuación, se explica cómo funciona este algoritmo y sus potenciales ventajas:

1. *Introducción programática:* 

* El `individual` que recibe la función `objective_function` representa una ruta potencial (una permutación específica de las ciudades -por ejemplo: [2, 9, 4, 5, 7, ... 1]).
* Se evalúa el fitness de cada individuo y se pasan al toneo para quedarnos con los mejores
* Se realiza la reproducción ox1 en la que se cruzan segmentos de los genes de dos padres para obtener los hijos
* Se realiza la mutación bit_flip en la que un gen puede cambiarse de posición con el otro
* Volvemos a evaluar los nuevos individuos en la función objetivo y repetimos lo anterior

2. *Función objetivo (`objective_function`):*

Esta función calcula la distancia total de una ruta dada.

* Toma un `individual` (un objeto que posee como valores la solución potencial) como entrada.
* Recupera el orden de las ciudades visitadas del `individual` (reproducido y mutado en el algorítmo genético cuántico).
* Utiliza las coordenadas de `original_cities` para calcular las distancias entre ciudades consecutivas en la ruta.
* El parámetro `return_to_origin` controla si se incluye la distancia desde la última ciudad de vuelta a la primera (para un ciclo cerrado).
* Devuelve la `total_distance`, que el algoritmo genético busca minimizar.

3. *Algoritmo genético (`GenethicOptimizer`):* Esta clase implementa la lógica central del algoritmo genético.

    * *Inicialización:* Comienza creando una población de soluciones potenciales (rutas).
    * *Evaluación:* La función `objective_function` se utiliza para evaluar la "aptitud" de cada individuo en la población (menor distancia = mayor aptitud, ya que se está minimizando).
    * *Selección:* Los individuos con mejor aptitud tienen más probabilidades de ser seleccionados como "mejores padres" para crear la siguiente generación.
    * *Cruce OX1 (recombinación):* El material genético (partes de las rutas) de dos individuos padres se combina para crear nuevos individuos descendientes.  
    * *Mutación:* Se introducen pequeños cambios aleatorios en las rutas de los descendientes para mantener la diversidad en la población y evitar quedar atrapado en óptimos locales.
    * *Terminación:* El algoritmo continúa durante un número específico de generaciones (`num_generations`) o hasta que se cumple un criterio de detención (`early_stopping_generations`).

4. *Restricciones del problema (`problem_restrictions="totally_restricted"`):* Este parámetro indica que el algoritmo debe encontrar una ruta válida donde cada ciudad se visite exactamente una vez (y regrese al origen si `return_to_origin` es `True`). En el problema del TSP solo se revisa que estén todas las ciudades.

5. *Límites (`BoundCreator`):* Los límites definen los posibles valores para cada "gen" en el individuo (en este caso, el índice de una ciudad).

### Posibles usos reales

A nivel real -al momento- puede ser utilizado para resolver problemas TSP del ámbito de:

* *Logística y servicios de entrega:*
    * *Optimización de rutas (en este caso solo euclidianas, por el momento):* Encontrar las rutas de entrega más eficientes para mensajeros, servicios postales o minoristas en línea para minimizar el tiempo de viaje, el consumo de combustible y los costos. Esto podría ser un ciclo cerrado si el conductor necesita regresar a un depósito o un ciclo abierto si termina en un destino final.

* *Fabricación y robótica:*
    * *Perforación de placas de circuito impreso:* Optimizar la trayectoria de una máquina perforadora para crear agujeros en una placa de circuito, minimizando el tiempo necesario para moverse entre los puntos de perforación.
    * *Soldadura/pintura robótica:* Encontrar la secuencia más eficiente de puntos para que un brazo robótico suelde o pinte componentes.
    * *Corte láser o fresado CNC:* Determinar la mejor secuencia de cortes en una pieza de material para reducir los movimientos innecesarios de la herramienta.

* *Transporte y viajes:*
    * *Planificación de tours:* Crear el itinerario más corto o eficiente para un turista que visita múltiples atracciones.
    * *Mantenimiento de infraestructuras:* Definir la ruta óptima para un equipo de mantenimiento que debe inspeccionar una serie de ubicaciones (por ejemplo, torres de telecomunicaciones, estaciones eléctricas o pozos petroleros).

* *Ciencias biológicas y medicina:* 
  * Reconstruir el orden de los fragmentos de ADN encontrando el camino más corto que visita cada fragmento basándose en la información de superposición.
  * Automatización en laboratorios: Optimizar el recorrido de brazos robóticos que deben dispensar líquidos o recolectar muestras en distintos puntos.

* *Agricultura de precisión*:
  * Monitoreo de cultivos: Determinar la mejor ruta para drones o tractores autónomos que deben visitar múltiples puntos de monitoreo o tratamiento dentro de un campo.

* *Astronomía:* 
  * Optimizar la secuencia de observaciones para telescopios para minimizar el tiempo dedicado a moverse entre objetos celestes.
  
* Mantenimiento de flotas aéreas o ferroviarias:*
  * Inspección de unidades: Encontrar la secuencia más eficiente de revisiones técnicas o inspecciones a realizar en una base o red distribuida de vehículos.

#### Ciclo cerrado vs. ciclo abierto

La variable `return_to_origin: bool = True` dentro de su función `objective_function` es clave para manejar ambas variantes del TSP:

* *Ciclo cerrado:* Cuando `return_to_origin` es `True` (como en su `objective_function`), la distancia desde la última ciudad de la ruta de vuelta a la primera ciudad se suma a la distancia total, cerrando efectivamente el ciclo.
* *Ciclo abierto:* Para resolver un TSP de ciclo abierto, simplemente se necesita establecer `return_to_origin` en `False`. En este caso, el algoritmo intentaría encontrar el camino más corto que visita todas las ciudades, partiendo del primer elemento (ciudad 0) sin requerir un retorno al punto de partida.

--------------------------------------------

## 1. Clase principal: GeneticOptimizer

La clase `GenethicOptimizer` implementa un algoritmo genético cuántico para resolver problemas de optimización combinatoria con restricciones específicas. 

Esta clase utiliza tanto computación cuántica o simuladores cuánticos para generar individuos y optimizar el espacio de soluciones mediante la evolución de una población.

### 1.1. Atributos

- **bounds_dict**: Diccionario de parámetros a optimizar y sus valores. Ejemplo: `{'learning_rate': (0.0001, 0.1)}`
- **num_generations**: Número de generaciones a ejecutar.
- **num_individuals**: Número de individuos iniciales a generar.
- **max_qubits**: Número máximo de qubits a emplear para reproducir individuos.
- **objective_function**: Función objetivo que se utiliza para puntuar a cada individuo. Debe retornar un valor numérico (float).
- **metric_to_optimize**: Métrica a optimizar (e.g., 'accuracy', 'recall', 'f1', 'mae').
- **problem_restrictions**: Restricciones aplicadas al problema ('bound_restricted' o 'totally_restricted').
- **return_to_origin**: Indica si el problema debe terminar en el origen (solo para problemas 'totally_restricted').
- **problem_type**: Tipo de optimización ('minimize' o 'maximize').
- **tournament_method**: Método de selección de individuos para reproducción (e.g., 'ea_simple').
- **podium_size**: Tamaño del grupo de individuos que competirá en el torneo para selección.
- **mutate_probability**: Probabilidad de mutación en cada gen.
- **mutate_gen_probability**: Probabilidad de mutar un gen.
- **mutation_policy**: Política de mutación ('soft', 'normal', 'hard').
- **verbose**: Indica si se deben mostrar mensajes detallados sobre la evolución.
- **early_stopping_generations**: Número de generaciones para considerar el "early stopping".
- **variability_explossion_mode**: Modo de explosión de variabilidad ('crazy').
- **variability_round_decimals**: Número de decimales para redondear estadísticas de la variabilidad.

### 1.2. Métodos

#### 1.2.2. `__init__()`
Este es el constructor de la clase `GenethicOptimizer`. 

Se encarga de inicializar todos los parámetros del algoritmo, como el tipo de optimización, las restricciones, las configuraciones de la mutación, entre otros. 

Además, se prepara el entorno de computación cuántica, si es necesario.


```
        :param bounds_dict: Diccionario en el que se definen los parámetros a optimizar y sus valores, ej. '{learning_rate: (0.0001, 0.1)}'
        :param num_generations: Numero de generaciones que se van a ejecutar
        :param num_individuals: Numero de Individuos iniciales que se van a generar
        :param max_qubits: Numero máximo de qubits a emplear para reproducir individuos (define el numero entero y la parte decimal de los numeros enteros y flotantes que se quieren generar)
        :param objective_function: Función objetivo que se va a emplear para puntuar a cada individuo (debe retornar un float)
        :param metric_to_optimize: Metrica que se quiere optimizar ['accuracy', 'recall', 'specificity', 'f1',
        'aur_roc', 'precision', 'negative_precision', 'mae', 'mse', 'other'] -> other significa cualquier otra genérica.
        Por ejemplo, se puede utilizar other para un problema de optimización de tipo viajante de comercio.
        :param problem_restrictions: ['bound_restricted', 'totally_restricted'] Restricciones que se van a aplicar a la hora de crear individuos, reprocirlos y mutarlos
        :param return_to_origin: [Literal['return_to_origin', 'no_return'] | None] En caso de problemas totally_restricted es necesario saber si el problema termina en el origen o no es necesario que suceda esto
        :param problem_type: [minimize, maximize] Seleccionar si se quiere minimizar o maximizar el resultado de la función objetivo. Por ejemplo si usamos un MAE es minimizar,
         un Accuracy sería maximizar.
        :param tournament_method: [easimple, .....] Elegir el tipo de torneo para seleccionar los individuos que se van a reproducir.
        :param podium_size: Cantidad de individuos de la muestra que van a competir para elegir al mejor. Por ejemplo, si el valor es 3, se escogen iterativamente 3 individuos
        al azar y se selecciona al mejor. Este proceso finaliza cuando ya no quedan más individuos y todos han sido seleccionados o deshechados.
        :param mutate_probability:Tambien conocido como indpb ∈[0, 1]. Probabilidad de mutar que tiene cada gen. Una probabilidad de 0, implica que nunca hay mutación,
        una probabilidad de 1 implica que siempre hay mutacion.
        :param mutate_gen_probability: [float] Probabilidad de mute un gen
        :param mutation_policy: Literal['soft', 'normal', 'hard'] Política de mutación (liviana, estandar y agresiva),
        :param verbose: Variable que define si se pinta información extra en consola y si se generan los graficos de los circuitos cuánticos.
        :param early_stopping_generations: Cantidad de generaciones que van a transcurrir para que en caso de repetirse la moda del fitness, se active el modo variability_explosion
        :param variability_explossion_mode: Modo de explosion de variabilidad, es decir, que se va a hacer para intentar salir de un minimo local establecido
        :param variability_round_decimals: Decimales a los que redondear las estadisticas de cálculo de moda necesarias para la explosion de variabilidad. Por ejemplo,
        en un caso de uso que busque accuracy, podría ser con 2 o 3 decimales. para casos de uso que contengan números muy bajos, habría que agregar más.
 
```

#### 1.2.1. Proceso de evolución

##### Creación y evaluación de la población inicial

1. *Inicialización de la población*: Se crea la población inicial de individuos, asignando valores aleatorios dentro de los límites definidos por `bounds_dict`.
   
2. *Evaluación de la función objetivo*: Cada individuo en la población inicial pasa por la función objetivo para obtener su fitness.

##### Evolución por generaciones

1. *Selección por torneo*: Cada generación selecciona a los mejores individuos utilizando un torneo. Los individuos ganadores serán los padres de la siguiente generación.

2. *Reproducción*: Los padres seleccionados se reproducen para crear nuevos individuos.

3. *Mutación*: 
    - *Mutación de los hijos*: Los nuevos individuos generados pasan por un proceso de mutación. Dependiendo de la probabilidad y política de mutación (`mutate_probability`, `mutate_gen_probability`, `mutation_policy`), se modifican algunos de los genes de los hijos.
    - *Actualización de la población*: Los individuos mutados se agregan a la población de la generación actual.

4. *Evaluación de la función objetivo*: Los nuevos individuos generados son evaluados nuevamente utilizando la función objetivo para obtener sus valores de fitness.

##### Estadísticas y seguimiento

1. *Estadísticas de la generación*: 
    - Después de cada generación, se muestra la información relevante sobre los mejores individuos y su fitness.
    - Se imprime la mejor solución obtenida de cada generación.
    - Si se activa el modo de "explosión de variabilidad", se muestra si se ha superado un mínimo local.

2. *Early Stopping y variabilidad*: 
    - Si se detecta que el modelo está atrapado en un mínimo local, se aplica una "explosión de variabilidad" para tratar de escapar de este mínimo, modificando las probabilidades de mutación y ajustando la política de mutación.

3. *Condición de parada*: 
    - El algoritmo puede detenerse antes de llegar al número máximo de generaciones si se cumplen ciertas condiciones de parada temprana (por ejemplo, si no se mejora el fitness en un número determinado de generaciones).

##### Resultado final

1. *Impresión de resultados finales*: 
    - Al finalizar el proceso, se muestran los resultados finales de cada generación y el mejor individuo encontrado, incluyendo su fitness y valores.

---

### 1.3. Flujo de trabajo

1. Inicialización de la población con parámetros aleatorios dentro de los límites de `bounds_dict`.
2. Evaluación de la función objetivo para cada individuo.
3. Selección de los mejores individuos mediante un torneo.
4. Reproducción y mutación de los individuos seleccionados.
5. Evaluación de la función objetivo nuevamente para los nuevos individuos.
6. Impresión de estadísticas de cada generación y el mejor individuo.
7. Aplicación de "explosión de variabilidad" si el algoritmo detecta un mínimo local.
8. Continuación hasta completar el número máximo de generaciones o alcanzar el criterio de parada.

## 2. Clase Population

### 2.1. Descripción general
La clase `Population` gestiona una población de individuos para algoritmos genéticos cuánticos de optimización. 

Permite la creación y evolución de poblaciones utilizando tecnología cuántica para la generación de parámetros y propiedades de los individuos.

### 2.1.1 Constructor

```
def __init__(self,
             bounds_dict: Dict[str, Tuple[Union[int, float]]],
             num_individuals: int,
             problem_restrictions: Literal['bound_restricted', 'totally_restricted'],
             round_decimals: int = 3):
```

#### 2.1.2. Parámetros
- *bounds_dict*: Diccionario que define las propiedades y límites de cada individuo
- *num_individuals*: Número de individuos en la población
- *problem_restrictions*: Tipo de restricciones del problema ('bound_restricted' o 'totally_restricted')
- *round_decimals*: Número de decimales para redondeo en comparaciones de similitud (predeterminado: 3)

#### 2.1.3. Atributos principales
- *IT*: Instancia de InfoTools para mostrar información
- *bounds_dict*: Diccionario con los límites de cada propiedad
- *num_individuals*: Cantidad de individuos en la población
- *problem_restrictions*: Tipo de restricción del problema
- *populuation_dict*: Diccionario que almacena los individuos por generación
- *hyperparameters*: Diccionario con los hiperparámetros extraídos de bounds_dict

### 2.2.1 create_population()

```
def create_population(self)
```

Crea la población inicial

#### 2.2.2. Parámetros
- ** None

### 2.3.1. add_generation_population()
```
def add_generation_population(self, children_list: List[Individual], generation: int) -> None
```
Añade una nueva generación de individuos a la población.

### 2.4.1. get_generation_fitness_statistics()
```
def get_generation_fitness_statistics(self, generation: int)
```
Calcula y devuelve estadísticas de fitness para una generación específica.

### 2.5.1. plot_generation_stats()
```
def plot_generation_stats(self, variability_explosion_starts_in_generation: int | None)
```
Genera un gráfico interactivo con la evolución de las estadísticas por generación.

### 2.6.1. plot_evolution_animated()
```
def plot_evolution_animated(self, problem_type: Literal['minimize', 'maximize'] = "maximize", transition_duration_ms: int = 50) -> None
```
Crea una visualización animada de la evolución de la población a lo largo de las generaciones.

### 2.7.1. plot_evolution()
```
def plot_evolution(self) -> None
```
Genera un gráfico estático de la evolución de la población.


## 3. Clase Reproduction

### 3.1. Descripción General
La clase `Reproduction` gestiona el proceso de reproducción en algoritmos genéticos cuánticos de optimización. Es responsable de crear una nueva generación de individuos (hijos) a partir de individuos seleccionados (ganadores) mediante técnicas de optimización cuántica.

#### 3.1.1. Constructor

```
def __init__(self, 
             winners_list: List[Individual],
             number_of_children: int,
             problem_restrictions: Literal['bound_restricted', 'totally_restricted'],
             return_to_origin: Literal['return_to_origin', 'no_return'] | None,
             problem_type: Literal["minimize", "maximize"],
             metric_to_optimize: Literal['accuracy', 'recall', 'specificity', 'f1', 'aur_roc', 'precision', 'negative_precision', 'mae', 'mse', 'other', 'r2'],
             verbose: bool = True)
```

#### 3.1.2. Parámetros
- *winners_list*: Lista de individuos ganadores que serán los padres
- *number_of_children*: Cantidad de individuos hijos que se desean generar
- *problem_restrictions*: Tipo de restricciones del problema ('bound_restricted' o 'totally_restricted')
- *return_to_origin*: Para problemas 'totally_restricted', indica si el recorrido debe volver al origen
- *problem_type*: Indica si el problema busca minimizar o maximizar la función objetivo
- *metric_to_optimize*: Métrica específica que se desea optimizar en la función objetivo
- *verbose*: Determina si se muestran mensajes y gráficos durante el proceso (predeterminado: True)

#### 3.1.3. Atributos principales
- *winners_list*: Lista de individuos ganadores (padres)
- *number_of_children*: Número de hijos a generar
- *problem_restrictions*: Tipo de restricción del problema
- *return_to_origin*: Indicador de retorno al origen para problemas 'totally_restricted'
- *children_list*: Lista donde se almacenarán los individuos hijos generados
- *parents_generation*: Generación a la que pertenecen los padres
- *problem_type*: Tipo de problema (minimización o maximización)
- *metric_to_optimize*: Métrica específica a optimizar
- *verbose*: Indicador de verbosidad de la ejecución
- *IT*: Instancia de InfoTools para mostrar información


#### 3.1.4. Atributos configurables en ejecución
Estos atributos se definen posteriormente mediante el método `run_reproduction`:

- *generations_fitness_statistics_df*: DataFrame con estadísticas de fitness por generación

#### 3.1.5. Comportamiento según configuración
La clase Reproduction adapta su comportamiento según:

1. *Tipo de restricción* ('bound_restricted' o 'totally_restricted'):
   - Para problemas con límites restringidos, genera valores dentro de los rangos especificados
   - Para problemas totalmente restringidos, trabaja con permutaciones válidas

2. *Retorno al origen* (para 'totally_restricted'):
   - En problemas como TSP, puede exigir que el recorrido vuelva al punto inicial

3. *Tipo de problema* ('minimize' o 'maximize'):
   - Adapta el proceso de selección y evaluación según se busque minimizar o maximizar

4. *Métrica a optimizar*:
   - Ajusta la evaluación de individuos según la métrica específica indicada

### 3.2. Método run_reproduction

#### 3.2.1. Descripción
El método `run_reproduction` de la clase `Reproduction` inicia el proceso de reproducción para generar una nueva generación de individuos a partir de los ganadores de la generación anterior. Configura el entorno de ejecución y selecciona la estrategia de reproducción según el tipo de restricciones del problema.

#### 3.2.2. Firma del método

```
def run_reproduction(self) -> List[Individual]
```

#### 3.2.3 Parámetros
- No tiene

#### 3.2.4 Valor de retorno
- Lista de individuos (`List[Individual]`) que constituye la nueva generación


#### 3.2.5. Notas importantes
- El porcentaje de elitismo está configurado al 15% (con un mínimo de 1 individuo)
- Los individuos seleccionados por elitismo mantienen todos sus atributos, incluyendo sus parámetros cuánticos
- El método actúa como un dispatcher que delega la reproducción específica a métodos especializados según el tipo de problema


## 4. Clase CrazyVariabilityExplossion

La clase `CrazyVariabilityExplossion` hereda de `VariabilityExplossion` e implementa una estrategia específica para activar y gestionar la explosión de variabilidad.

#### 4.1. Herencia

`CrazyVariabilityExplossion` hereda de la clase base abstracta `VariabilityExplossion`.

#### 4.2. Inicialización (`__init__`)

```
def __init__(self, early_stopping_generations: int, problem_type: Literal['maximize', 'minimize'], round_decimals: int = 3, verbose: bool = False):
```

##### 4.2.1. Parámetros

Hereda los parámetros de la clase base `VariabilityExplossion`.

##### 4.2.2. Funcionalidad

Llama al constructor de la clase base (`super().__init__(...)`) para inicializar los atributos relacionados con el early stopping y la explosión de variabilidad.

#### 4.3. Métodos implementados

```
def evaluate_early_stopping(self, generations_fitness_statistics_df: pd.DataFrame | None) -> tuple:
```

#### 4.3.1. `evaluate_early_stopping`

Evalúa si se deben activar las condiciones para la explosión de variabilidad basándose en la repetición de la moda del fitness en las últimas generaciones.

* `generations_fitness_statistics_df` (`pd.DataFrame | None`): DataFrame con la información general de la generación.
* Retorna `tuple`:
    * `m_proba` (`float | None`): Probabilidad de mutación de un individuo.
    * `m_gen_proba` (`float | None`): Probabilidad de mutación de un gen.
    * `m_policy` (`Literal['soft', 'normal', 'hard'] | None`): Política de mutación.
    * `early_stopping_generations_execute` (`bool | None`): Indica si se debe ejecutar el early stopping. Retorna `None` si no se cumplen las condiciones.

##### 4.3.1.1. Funcionalidad

1.  Verifica si se proporciona un DataFrame de estadísticas de generaciones.
2.  Si el número de generaciones es al menos el doble de `early_stopping_generations`, analiza las últimas `early_stopping_generations`.
3.  Determina la moda de la columna 'min' (para problemas de minimización) o 'max' (para problemas de maximización) en las últimas generaciones.
4.  Si todos los valores de la moda son iguales, se considera que el algoritmo está estancado y se llama a `self.execute_variability_explossion()` para activar la explosión.
5.  Si la explosión de variabilidad ya está activa (`self.early_stopping_generations_executed`), se vuelve a ejecutar en cada iteración.
6.  Si no se cumplen las condiciones, retorna `None` para las probabilidades de mutación, la política y el flag de ejecución.

```
def execute_variability_explossion(self):
```

#### 4.3.2. `execute_variability_explossion`

Ejecuta la explosión de variabilidad aumentando las probabilidades de mutación y cambiando la política de mutación.

* Retorna `tuple`:
    * `mutate_probability` (`float`): Probabilidad de mutación de un individuo.
    * `mutate_gen_probability` (`float`): Probabilidad de mutación de un gen.
    * `mutation_policy` (`Literal['soft', 'normal', 'hard']`): Política de mutación.
    * `early_stopping_generations_executed` (`bool`): Indica si se debe ejecutar el early stopping (`True` en este caso).

##### 4.3.2.1. Funcionalidad

1.  Si la explosión de variabilidad ya está activa, restablece las probabilidades de mutación y la política a valores "suaves".
2.  Si la explosión de variabilidad no estaba activa, aumenta drásticamente las probabilidades de mutación (individuo y gen) y establece la política de mutación en 'hard' para introducir una gran cantidad de diversidad. También establece el flag `self.early_stopping_generations_executed` en `True`.
3.  Retorna las nuevas probabilidades de mutación, la política y el flag de ejecución.

```
def stop_genetic_iterations(self, generations_fitness_statistics_df: pd.DataFrame | None):
```

#### 4.3.3. `stop_genetic_iterations`

Evalúa si se debe detener el proceso de evolución después de que la explosión de variabilidad ha estado activa durante un cierto número de generaciones sin mejorar el mejor resultado encontrado hasta el momento.

* `generations_fitness_statistics_df` (`pd.DataFrame | None`): DataFrame con los resultados estadísticos de los individuos.
* Retorna `bool`: `True` si se debe detener la evolución, `False` si se debe continuar.

##### 4.3.3.1. Funcionalidad

1.  Verifica si la explosión de variabilidad está activa (`self.early_stopping_generations_executed`).
2.  Si está activa, incrementa los contadores de generaciones de early stopping.
3.  Cuando el contador de generaciones activas alcanza `self.early_stopping_generations`:
    * Compara el mejor valor de fitness global con el mejor valor de fitness en las últimas `self.early_stopping_generations` generaciones.
    * Si no ha habido mejora (o ha empeorado en el caso de maximización), se considera que la explosión de variabilidad no ha sido efectiva y se retorna `True` para detener la evolución.
    * Si ha habido mejora, se restablece el contador de generaciones activas para dar más margen al algoritmo.
4.  Si `self.verbose` es `True`, se llama a `self.print_variability_status()` para mostrar el estado de la explosión.
5.  Retorna `False` si la explosión de variabilidad no está activa o si aún no se ha alcanzado el límite de generaciones sin mejora.

```
def print_variability_status(self):
```

#### 4.3.4. `print_variability_status`

Imprime el estado actual de la explosión de variabilidad.

#### 4.3.4.1. Funcionalidad

1.  Imprime un encabezado con el resumen del estado de `CrazyVariabilityExplossion`.
2.  Indica si la explosión está activa (`self.early_stopping_generations_executed`) con un color diferente según el estado.
3.  Si la explosión está activa, muestra el número total de generaciones que lleva activa y el número de generaciones transcurridas desde la última mejora.


### 5. Clase `VariabilityExplossion` (Abstracta)

La clase abstracta `VariabilityExplossion` define la interfaz para implementar mecanismos de explosión de variabilidad en algoritmos genéticos. El objetivo de estos mecanismos es evitar la convergencia prematura y escapar de óptimos locales aumentando la diversidad de la población cuando se detecta estancamiento.

#### 5.1. Importaciones

```
from abc import ABC, abstractmethod
from info_tools import InfoTools
from typing import Literal

import pandas as pd
import numpy as np
```

#### 5.2. Descripción

Esta clase base proporciona la estructura para gestionar el early stopping y la activación de la explosión de variabilidad. Las subclases concretas deben implementar los métodos abstractos para definir la lógica específica de evaluación, ejecución y detención de la explosión de variabilidad.

#### 5.3. Inicialización (`__init__`)

```
def __init__(self, early_stopping_generations: int, problem_type: Literal['maximize', 'minimize'], round_decimals: int = 3, verbose: bool = False):
```

#### 5.4. Parámetros

* `early_stopping_generations` (`int`): Número de generaciones consecutivas con una moda de fitness similar que deben ocurrir para considerar la activación de la explosión de variabilidad.
* `problem_type` (`Literal['maximize', 'minimize']`): Indica si el problema es de maximización o minimización, lo que influye en la evaluación del estancamiento.
* `round_decimals` (`int`, opcional): Número de decimales a redondear al analizar las estadísticas de variabilidad. Por defecto es 3.
* `verbose` (`bool`, opcional): Flag para habilitar la impresión de mensajes detallados sobre el estado de la explosión de variabilidad. Por defecto es `False`.

#### 5.5. Atributos

* `early_stopping_generations` (`int`): Almacena el número de generaciones de espera para el early stopping.
* `problem_type` (`Literal['maximize', 'minimize']`): Almacena el tipo de problema.
* `IT` (`InfoTools`): Instancia de la clase `InfoTools` para facilitar la impresión informativa.
* `round_decimals` (`int`): Almacena el número de decimales para el redondeo.
* `verbose` (`int`): Almacena el valor del flag verbose.
* `early_stopping_generations_executed_counter` (`int`): Contador de las generaciones transcurridas desde la última explosión de variabilidad.
* `total_early_stopping_generations_executed_counter` (`int`): Contador total de generaciones transcurridas desde la primera explosión de variabilidad.
* `early_stopping_generations_executed` (`bool`): Flag que indica si la explosión de variabilidad está actualmente activa.
* `mutate_probability` (`float`): Probabilidad de mutación de un individuo (valor por defecto inicial).
* `mutate_gen_probability` (`float`): Probabilidad de mutación de un gen dentro de un individuo (valor por defecto inicial).
* `mutation_policy` (`Literal['soft', 'normal', 'hard']`): Política de mutación a aplicar (valor por defecto inicial).

#### 5.6. Métodos abstractos

```
@abstractmethod
def evaluate_early_stopping(self, generations_fitness_statistics_df: pd.DataFrame | None) -> None:
    pass
```

##### 5.6.1. `evaluate_early_stopping`

Método abstracto que debe implementar la lógica para determinar si se deben activar las condiciones de early stopping y la explosión de variabilidad. Por ejemplo, podría verificar si la moda de la aptitud se ha mantenido constante durante un cierto número de generaciones.

* `generations_fitness_statistics_df` (`pd.DataFrame | None`): DataFrame que contiene las estadísticas de fitness de las generaciones.

```
@abstractmethod
def execute_variability_explossion(self):
    pass
```

##### 5.6.2. `execute_variability_explossion`

Método abstracto que define cómo se ejecuta la explosión de variabilidad. Esto podría implicar el aumento de las probabilidades de mutación o la aplicación de otras estrategias para introducir mayor diversidad en la población.

```
@abstractmethod
def stop_genetic_iterations(self, generations_fitness_statistics_df: pd.DataFrame | None):
    pass
```

##### 5.6.3. `stop_genetic_iterations`

Método abstracto que evalúa si el proceso de evolución genética debe detenerse basándose en las condiciones de early stopping. Por ejemplo, si la explosión de variabilidad no ha logrado mejorar los resultados después de un cierto número de generaciones.

* `generations_fitness_statistics_df` (`pd.DataFrame | None`): DataFrame con las estadísticas de fitness de las generaciones.
* Retorna `bool`: `True` si se debe detener la evolución, `False` si debe continuar.

```
@abstractmethod
def print_variability_status(self):
    pass
```

##### 5.6.4. `print_variability_status`

Método abstracto que imprime el estado actual de la explosión de variabilidad, como si está activa, cuánto tiempo lleva activa y si se han observado mejoras.

