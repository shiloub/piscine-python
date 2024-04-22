class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dot_product = sum([(a * b) for (a, b) in zip(V1, V2)])
        print(f"Dot product is: {dot_product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        dot_product = [float(a + b) for (a, b) in zip(V1, V2)]
        print(f"Add vector is: {dot_product}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        dot_product = [float(a - b) for (a, b) in zip(V1, V2)]
        print(f"Sous vector is: {dot_product}")
