from scipy.spatial.distance import euclidean

class Case:
    def __init__(self, features, solution):
        self.features = features
        self.solution = solution

class CBRSystem:
    def __init__(self, case_base=None):
        self.case_base = case_base if case_base is not None else []

    def add_case(self, case):
        self.case_base.append(case)

    def retrieve_similar_cases(self, new_problem_features, num_neighbors=1):
        similarities = []
        for case in self.case_base:
            # Example: using Euclidean distance as a similarity metric
            distance = euclidean(new_problem_features, case.features)
            similarities.append((distance, case))

        # Sort by distance (ascending) to get most similar cases
        similarities.sort(key=lambda x: x[0])
        return [case for _, case in similarities[:num_neighbors]]

    def solve_problem(self, new_problem_features):
        similar_cases = self.retrieve_similar_cases(new_problem_features)

        if similar_cases:
            # Simple reuse: use the solution of the most similar case
            most_similar_case = similar_cases[0]
            print(f"Found similar case with features: {most_similar_case.features}")
            print(f"Reusing solution: {most_similar_case.solution}")
            return most_similar_case.solution
        else:
            print("No similar cases found. Cannot solve.")
            return None

# Usage example
cbr_system = CBRSystem()
cbr_system.add_case(Case([1, 2, 3], "Solution A"))
cbr_system.add_case(Case([1.5, 2.1, 2.9], "Solution B"))
cbr_system.add_case(Case([5, 6, 7], "Solution C"))

new_problem = [1.2, 2.0, 3.1]
cbr_system.solve_problem(new_problem)