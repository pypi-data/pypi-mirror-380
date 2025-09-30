from .banque import donnes_des_sous_mathis

def main() -> None:
    print("Hello from donnes-des-sous!")
    result = donnes_des_sous_mathis(100, 150)
    print(f"Result of donnes_des_sous(100, 150): {result}")
    result = donnes_des_sous_mathis(250, 150)
    print(f"Result of donnes_des_sous(250, 150): {result}")
