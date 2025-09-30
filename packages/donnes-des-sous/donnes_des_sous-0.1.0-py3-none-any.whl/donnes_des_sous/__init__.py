from .banque import donnes_des_sous


def main() -> None:
    print("Hello from donnes-des-sous!")
    result = donnes_des_sous(150, 100)
    print(f"Result of donnes_des_sous(150, 100): {result}")
    result = donnes_des_sous(250, 100)
    print(f"Result of donnes_des_sous(250, 100): {result}")
