import random
from info_tools import InfoTools
from aletheia_genetic_optimizers.individuals import Individual
from typing import List, Literal, Dict
import numpy as np


class Reproduction:
    def __init__(self, winners_list: List[Individual], number_of_children: int, problem_restrictions: str,
                 problem_type: Literal["minimize", "maximize"], verbose: bool = True):
        self.winners_list: List[Individual] = winners_list
        self.number_of_children: int = number_of_children
        # -- Almaceno en una propiedad las restricciones a aplicar
        self.problem_restrictions: Literal['bound_restricted', 'full_restricted'] = problem_restrictions
        self.children_list: List[Individual] = []
        self.parents_generation: int = self.winners_list[0].generation
        self.problem_type: Literal["minimize", "maximize"] = problem_type
        self.verbose: bool = verbose
        self.IT: InfoTools = InfoTools()

    def run_reproduction(self) -> List[Individual]:
        if self.verbose:
            self.IT.intro_print(
                f"RUN REPRODUCTION generacion: {self.parents_generation} -> sacará la generación {self.parents_generation + 1}")

        # -- Elitismo: Se seleccionan a los mejores individuos (15% del total de la población a mantener)
        # -- Se crea una copia de estos individuos con la nueva generacion.
        num_to_keep = int(self.number_of_children * 0.15)
        elite_individuals = sorted(self.winners_list, key=lambda ind: ind.individual_fitness,
                                   reverse=self.problem_type == "maximize")[:num_to_keep]

        # -- CORRECCIÓN: Se clonan los valores de cada individuo élite
        # Se pasa una lista de los valores (list(ind.get_individual_values().values())) en lugar del diccionario completo.
        self.children_list = [
            Individual(ind.bounds_dict, list(ind.get_individual_values().values()), self.parents_generation + 1,
                       self.problem_restrictions)
            for ind in elite_individuals
        ]

        # -- Se itera hasta que la lista de hijos tenga el tamaño definido de la población
        while len(self.children_list) < self.number_of_children:

            # -- Se escogen dos padres al azar de la lista de ganadores
            parent1 = random.choice(self.winners_list)

            # -- Se crea una lista de competidores, asegurando que no esté vacía
            competitors = [ind for ind in self.winners_list if ind != parent1]
            if not competitors:
                # -- Caso de borde: si solo hay un ganador, el padre se reproduce consigo mismo
                parent2 = parent1
            else:
                parent2 = random.choice(competitors)

            # -- Se realiza el cruce entre los dos padres para obtener los valores de los hijos
            child_one_values_list, child_two_values_list = self.crossover_parents(parent1, parent2)

            # -- Se crean los nuevos individuos (hijos)
            child_individual_1 = Individual(parent1.bounds_dict, child_one_values_list, self.parents_generation + 1,
                                            self.problem_restrictions)
            child_individual_2 = Individual(parent1.bounds_dict, child_two_values_list, self.parents_generation + 1,
                                            self.problem_restrictions)

            # -- Se añaden los hijos a la lista si son válidos (no duplicados y sin malformación)
            for ind in [child_individual_1, child_individual_2]:
                if len(self.children_list) >= self.number_of_children:
                    break

                is_duplicate = any(existing_indv == ind for existing_indv in self.children_list)
                if not is_duplicate and not ind.malformation:
                    self.children_list.append(ind)

        # -- Se trunca la lista de hijos si se excedió el tamaño debido a la creación de parejas
        if len(self.children_list) > self.number_of_children:
            self.children_list = self.children_list[:self.number_of_children]

        return self.children_list

    def crossover_parents(self, parent1: Individual, parent2: Individual):
        """Método helper para realizar el cruce entre dos padres."""
        bounds_dict = parent1.bounds_dict
        child_one_values_list = []
        child_two_values_list = []

        for parameter, bound in bounds_dict.items():
            match bound['bound_type']:
                case 'predefined':
                    c1, c2 = self.cx_uniform(parent1.get_individual_values()[parameter],
                                             parent2.get_individual_values()[parameter])
                    child_one_values_list.append(c1)
                    child_two_values_list.append(c2)
                case 'interval':
                    c1, c2 = self.cx_blend(parent1.get_individual_values()[parameter],
                                           parent2.get_individual_values()[parameter])
                    child_one_values_list.append(c1 if bound["type"] == "float" else int(c1))
                    child_two_values_list.append(c2 if bound["type"] == "float" else int(c2))

        return child_one_values_list, child_two_values_list

    @staticmethod
    def cx_uniform(parent1, parent2, indpb=0.5):
        """Cruce uniforme con probabilidad indpb para valores individuales."""
        if np.random.rand() < indpb:
            return parent2, parent1
        return parent1, parent2

    @staticmethod
    def cx_blend(parent1, parent2, alpha=0.5):
        """Cruce blend para valores continuos con dos padres individuales."""
        diff = abs(parent1 - parent2)
        low, high = min(parent1, parent2) - alpha * diff, max(parent1, parent2) + alpha * diff
        return np.random.uniform(low, high), np.random.uniform(low, high)

    @staticmethod
    def ox1(parent1, parent2):
        """Aplica Order Crossover (OX1) a dos padres de un problema basado en permutaciones."""
        size = len(parent1)
        offspring = [None] * size
        start, end = sorted(random.sample(range(size), 2))
        offspring[start:end + 1] = parent1[start:end + 1]
        p2_genes = [gene for gene in parent2 if gene not in offspring]
        idx = 0
        for i in range(size):
            if offspring[i] is None:
                offspring[i] = p2_genes[idx]
                idx += 1
        return offspring

    def full_restricted_reproduction(self) -> List[Individual]:
        """
        Método de reproducción para el tipo "full_restricted".
        """
        # -- Obtengo el bounds dict fijo para que cada tipo de parametro tenga su propio cruce (rangos con cx_blend, fijos con cx_uniform)
        bounds_dict = self.winners_list[0].bounds_dict

        # -- Primero, iteramos hasta que la children_list tenga number_of_children individuos
        while len(self.children_list) < self.number_of_children:
            for individual in self.winners_list:

                if len(self.children_list) >= self.number_of_children:
                    break

                # -- Se escogen dos padres al azar de la lista de ganadores
                parent1 = random.choice(self.winners_list)

                # -- Se crea una lista de competidores, asegurando que no esté vacía
                competitors = [ind for ind in self.winners_list if ind != parent1]
                if not competitors:
                    # -- Caso de borde: si solo hay un ganador, el padre se reproduce consigo mismo
                    parent2 = parent1
                else:
                    parent2 = random.choice(competitors)

                if self.verbose:
                    self.IT.sub_intro_print(f"Padres que se van a reproducir:")
                    self.IT.info_print(f"Padre 1: {individual.get_individual_values()}")
                    self.IT.info_print(f"Padre 2: {parent2.get_individual_values()}")

                # Realizamos los cruces entre dos padres para sacar un hijo
                c1 = self.ox1([z for z in individual.get_individual_values().values()],
                              [z for z in parent2.get_individual_values().values()])
                c2 = self.ox1([z for z in individual.get_individual_values().values()],
                              [z for z in parent2.get_individual_values().values()])

                # Creamos los individuos y los agregamos a la lista si no existe ya uno similar
                child_individual_1: Individual = Individual(bounds_dict, c1, self.parents_generation + 1,
                                                            self.problem_restrictions)
                child_individual_2: Individual = Individual(bounds_dict, c2, self.parents_generation + 1,
                                                            self.problem_restrictions)

                if self.verbose:
                    self.IT.sub_intro_print(f"Hijos resultantes:")
                    self.IT.info_print(f"Hijo 1: {child_individual_1.get_individual_values()}")
                    self.IT.info_print(f"Hijo 2: {child_individual_2.get_individual_values()}")

                # Validamos que no existan individuos muy similares en la lista y que no tengan malformacion
                for ind in [child_individual_1, child_individual_2]:
                    is_duplicate = any(existing_indv == ind for existing_indv in self.children_list)
                    if not is_duplicate and not child_individual_1.malformation:
                        self.children_list.append(ind)

        return self.children_list