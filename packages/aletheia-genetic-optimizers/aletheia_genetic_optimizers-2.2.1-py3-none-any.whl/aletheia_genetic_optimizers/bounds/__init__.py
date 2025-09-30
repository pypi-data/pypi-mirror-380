from typing import Iterable, Literal


class BoundCreator:
    def __init__(self):
        """
        Clase para crear el diccionario de bounds y de restricciones
        """
        self.bound_object: dict = {}

    def add_interval_bound(self, parameter: str,
                           parameter_low_limit: int | float,
                           parameter_high_limit: int | float,
                           malformation_low_limit: int | float | None,
                           malformation_high_limit: int | float | None,
                           parameter_type: Literal['int', 'float'] = "int",
                           ):
        """
        Método para crear bounds que se pasarán al algoritmo genético cuántico
        :param parameter: nombre del parametro, ej 'learning_rate'
        :param parameter_low_limit: Limite inferior que quieres que pueda tener el parametro, ej, 0.00001
        :param parameter_high_limit: limite superior que quieres que tenga el parametro, ej: 0.1
        :param malformation_low_limit: Limite inferior a partir del cual se considerará que el individuo tiene una malformacion
        :param malformation_high_limit: Limite superior a partir del cual se considerará que el individuo tiene una malformacion
        :param parameter_type: Elegir entre ['int', 'float']. int para parametros que no pueden tener valores continus, como el batch_size, float para los que sí como learning rate
        """
        self.bound_object = self.bound_object | IntervalBound(parameter, parameter_low_limit, parameter_high_limit, malformation_low_limit, malformation_high_limit, parameter_type)

    def add_predefined_bound(self, parameter: str,
                             parameter_list: Iterable,
                             parameter_type: Literal['int', 'float'] = "int",
                             ):
        """
        Método para crear bounds que se pasarán al algoritmo genético cuántico
        :param parameter: nombre del parametro, ej 'learning_rate'
        :param parameter_list: tupla que va a contener los posibles valores para el parámetro
        :param parameter_type: Elegir entre ['int', 'float']. int para parametros que no pueden tener valores continus, como el batch_size, float para los que sí como learning rate
        """
        self.bound_object = self.bound_object | PredefinedBound(parameter, parameter_list, parameter_type)

    def get_bound(self):
        return self.bound_object


class IntervalBound(dict):
    def __init__(self,
                 parameter: str,
                 parameter_low_limit: int | float,
                 parameter_high_limit: int | float,
                 malformation_low_limit: int | float | None,
                 malformation_high_limit: int | float | None,
                 parameter_type: Literal['int', 'float'] = "int"):
        """
        Clase para crear bounds que se pasarán al algoritmo genético cuántico
        :param parameter: nombre del parametro, ej 'learning_rate'
        :param parameter_low_limit: Limite inferior que quieres que pueda tener el parametro, ej, 0.00001
        :param parameter_high_limit: limite superior que quieres que tenga el parametro, ej: 0.1
        :param malformation_low_limit: Limite inferior a partir del cual se considerará que el individuo tiene una malformacion
        :param malformation_high_limit: Limite superior a partir del cual se considerará que el individuo tiene una malformacion
        :param parameter_type: Elegir entre ['int', 'float']. int para parametros que no pueden tener valores continus, como el batch_size, float para los que sí como learning rate
        """

        if parameter_type not in ['int', 'float']:
            raise ValueError(f"Bound: Error al crear el Bound, el parameter type solo puede contener estos valores: ['int', 'float']. Valor asignado: {parameter_type}")

        bound_data = {
            parameter: {
                "limits": (parameter_low_limit, parameter_high_limit),
                "type": parameter_type,
                "malformation_limits": (malformation_low_limit, malformation_high_limit),
                "bound_type": "interval"
            }
        }

        super().__init__(bound_data)


class PredefinedBound(dict):
    def __init__(self,
                 parameter: str,
                 parameter_list: Iterable,
                 parameter_type: Literal['int', 'float'] = "int"):
        """
        Clase para crear bounds que se pasarán al algoritmo genético
        :param parameter: nombre del parametro, ej 'learning_rate'
        :param parameter_type: Elegir entre ['int', 'float']. int para parametros que no pueden tener valores continus, como el batch_size, float para los que sí como learning rate
        """

        if parameter_type not in ['int', 'float']:
            raise ValueError(f"Bound: Error al crear el Bound, el parameter type solo puede contener estos valores: ['int', 'float']. Valor asignado: {parameter_type}")

        bound_data = {
            parameter: {
                "limits": parameter_list,
                "type": parameter_type,
                "malformation_limits": parameter_list,
                "bound_type": "predefined"
            }
        }

        super().__init__(bound_data)
