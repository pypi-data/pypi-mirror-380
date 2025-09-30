import random
from typing import Dict, Union, Tuple, List, Literal
from abc import ABC, abstractmethod


# TODO: EN funcion del problem type, se hace un match para llamar a diferentes funciones de creacion de individuo
# TODO: Un match en evaluate malformation

class IndividualMethods(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_individual(self, bounds_dict: Dict[str, Tuple[Union[int, float]]], child_values: List | None) -> Dict[
        str, Union[int, float]]:
        pass

    @abstractmethod
    def exists_malformation(self, individual_values: Dict[str, Union[int, float]],
                            bounds_dict: Dict[str, Tuple[Union[int, float]]]) -> bool:
        pass


class BoundRestrictedIndividualMethods(IndividualMethods):
    def __init__(self):
        super().__init__()

    def exists_malformation(self, individual_values: Dict[str, Union[int, float]],
                            bounds_dict: Dict[str, Tuple[Union[int, float]]]) -> bool:
        """
        Método para saber si el individuo tiene valores fuera del rango.
        Se ha corregido para manejar diferentes tipos de bound.
        """
        for gene_name, gene_value in individual_values.items():
            # Obtiene las restricciones específicas para este gen
            gene_bounds = bounds_dict[gene_name]
            bound_type = gene_bounds["bound_type"]
            malformation_limits = gene_bounds["malformation_limits"]

            # Comprobación para bounds de tipo "interval" (numéricos)
            if bound_type == "interval":
                # Asegura que se compare solo con los valores de los límites de malformación
                if gene_value < min(malformation_limits) or gene_value > max(malformation_limits):
                    return True

            # Comprobación para bounds de tipo "predefined" (valores discretos)
            elif bound_type == "predefined":
                # Verifica si el valor del gen está en la lista de opciones permitidas
                if gene_value not in malformation_limits:
                    return True

        return False

    def create_individual(self, bounds_dict: Dict[str, Tuple[Union[int, float]]], child_values: List | None) -> Dict[
        str, Union[int, float]]:
        individual_values: Dict[str, Union[int, float]] = {}
        # -- En caso de que no se le pasen los child_list de la generacion, se crean aleatoriamente los valores
        if child_values is None:

            for parameter, v in bounds_dict.items():
                if v["bound_type"] == "interval":
                    match v["type"]:
                        case "int":
                            individual_values[parameter] = int(
                                self.generate_random_value((v["limits"][0], v["limits"][1]), v["type"]))
                        case "float":
                            individual_values[parameter] = self.generate_random_value((v["limits"][0], v["limits"][1]),
                                                                                      v["type"])

                else:
                    individual_values[parameter] = self.generate_possible_value(v["limits"], v["type"])
        else:
            for parameter, cv in zip([z for z in bounds_dict.keys()], child_values):
                individual_values[parameter] = cv

        return individual_values

    @staticmethod
    def generate_random_value(val_tuple: tuple, data_type: str):
        if data_type == "int":
            return random.randint(val_tuple[0], val_tuple[1])
        elif data_type == "float":
            return random.uniform(val_tuple[0], val_tuple[1])

    @staticmethod
    def generate_possible_value(val_tuple: tuple, data_type: str):
        if data_type == "int":
            return random.choice(val_tuple)
        elif data_type == "float":
            return random.choice(val_tuple)


class FullRestrictedIndividualMethods(IndividualMethods):

    def __init__(self):
        super().__init__()

    def create_individual(self, bounds_dict: Dict[str, Tuple[Union[int, float]]], child_values: List | None) -> Dict[
        str, Union[int, float]]:
        individual_values: Dict[str, Union[int, float]] = {}
        # -- En caso de que no se le pasen los child_list de la generacion, se crean aleatoriamente los valores
        if child_values is None:

            for parameter, v in bounds_dict.items():
                individual_values[parameter] = self.generate_possible_value(v["limits"], individual_values)
        else:
            for parameter, cv in zip([z for z in bounds_dict.keys()], child_values):
                individual_values[parameter] = cv

        return individual_values

    def exists_malformation(self, individual_values: Dict[str, Union[int, float]],
                            bounds_dict: Dict[str, Tuple[Union[int, float]]]) -> bool:
        """
        Método para saber si el individuo tiene valores fuera del rango.
        Se ha corregido para manejar diferentes tipos de bound.
        """
        for gene_name, gene_value in individual_values.items():
            # Obtiene las restricciones específicas para este gen
            gene_bounds = bounds_dict[gene_name]
            bound_type = gene_bounds["bound_type"]
            malformation_limits = gene_bounds["malformation_limits"]

            # Comprobación para bounds de tipo "interval" (numéricos)
            if bound_type == "interval":
                # Verifica si el valor está fuera del rango de malformación
                if gene_value < min(malformation_limits) or gene_value > max(malformation_limits):
                    return True

            # Comprobación para bounds de tipo "predefined" (valores discretos)
            elif bound_type == "predefined":
                # Verifica si el valor del gen está en la lista de opciones permitidas
                if gene_value not in malformation_limits:
                    return True

        # Comprobación de duplicados para problemas 'full_restricted'
        if len(list(individual_values.values())) > len(set(individual_values.values())):
            return True

        return False

    @staticmethod
    def generate_possible_value(val_tuple: tuple, individual_values):
        return random.choice([z for z in val_tuple if z not in individual_values.values()])


class Individual:
    def __init__(self, bounds_dict: Dict[str, Tuple[Union[int, float]]], child_values: List | None, generation: int, problem_restrictions: str):
        """
        Clase que va a instanciar los distintos individuos que van a competir.
        :param bounds_dict: Diccionario en el que se definen los parámetros a optimizar y sus valores, ej. '{learning_rate: (0.0001, 0.1)}'
        de uso y que desemboca en un individuo que se deshechará por tener una malformación. Por ejemplo, si estamos optimizando un learning_rate y la mutación nos da un valor
        superior a 1, ese individuo, se descarta antes de ser evaluado. ej. '{learning_rate: (0.000001, 1)}', si los supera, consideramos malformación.
        """

        # -- Almaceno parámetros en propiedades
        self.bounds_dict: Dict[str, Tuple[Union[int, float]]] = bounds_dict

        # -- Almaceno los valores que provienen de la generacion del individuo (sus valores reales)
        self.child_values: List | None = child_values

        # -- Almaceno en una propiedad la generación a la que pertenece el individuo
        self.generation: int = generation

        # -- Almaceno en una propiedad las restricciones a aplicar
        self.problem_restrictions: Literal['bound_restricted', 'full_restricted'] = problem_restrictions

        # -- Defino la propiedad en la que almacenaré el valor que la función de coste ha tenido para este individuo
        self.individual_fitness: float | None = None

        # -- Almaceno en IMETHODS la instancia que contiene los metodos para el tipo de problema en cuestion
        self.IMETHODS = BoundRestrictedIndividualMethods() if self.problem_restrictions == "bound_restricted" else FullRestrictedIndividualMethods()

        # -- Creo la propiedad de valores del individuo
        self._individual_values: Dict[str, Union[int, float]] = self.IMETHODS.create_individual(self.bounds_dict, self.child_values)

        # -- Almaceno en una propiedad si el individuo tiene una malformación
        self.malformation: bool = self.exists_malformation()


    def exists_malformation(self) -> bool:
        """
        Método para saber si el individuo tiene valores fuera del rango
        :return: True si existe malformacion, False else
        """

        # -- NOTA: El método varía en funcion de las restricciones de self.problem_restrictions
        return self.IMETHODS.exists_malformation(self._individual_values, self.bounds_dict)

    # <editor-fold desc="Getters y setters    --------------------------------------------------------------------------------------------------------------------------------">

    def get_individual_values(self) -> Dict[str, Union[int, float]]:
        """
        Método que va a devolver los valores del individuo en un diccionario. por ejemplo, si viene asi: {learning_rate: 0.0125, batch_size: 34}
        :return:
        """
        return self._individual_values

    def __eq__(self, other, decimals=4):
        """
        Compara si dos individuos son iguales en base a sus propiedades con precisión decimal.

        :param other: Otro objeto de la clase Individual con el que se realizará la comparación.
        :param decimals: Número de decimales a considerar en la comparación (por defecto 4).

        :return: True si ambos individuos tienen las mismas propiedades con la precisión dada, False en caso contrario.
        """

        # Verificar que el otro objeto es de la clase Individual
        if not isinstance(other, Individual):
            return False

        # Obtener los valores de los individuos
        values_self = self.get_individual_values()
        values_other = other.get_individual_values()

        # Redondear los valores antes de compararlos
        rounded_self = {k: round(v, decimals) if isinstance(v, float) else v for k, v in values_self.items()}
        rounded_other = {k: round(v, decimals) if isinstance(v, float) else v for k, v in values_other.items()}

        return rounded_self == rounded_other

    def add_or_update_variable(self, var_name: str, value: int | float) -> None:
        """
        Agrega o actualiza una variable de instancia en el objeto Individual.

        :param var_name: Nombre de la variable de instancia.
        :param value: Valor de la variable (puede ser de cualquier tipo).
        """
        setattr(self, f"_{var_name}", value)

    def set_individual_value(self, parameter: str, new_value: float | int):
        self._individual_values[parameter] = new_value
        self.malformation = self.exists_malformation()

    def set_individual_values(self, new_value_list: float | int):
        for key, new_value in zip(self._individual_values.keys(), new_value_list):
            self._individual_values[key] = new_value
        self.malformation = self.exists_malformation()

    def get_child_values(self):
        return self.child_values

    # </editor-fold>
