# src/donnes_des_sous_hakim/__init__.py

from .banque import donnes_des_sous_hakim

def main() -> None:
    print("Hello from donnes-des-sous!")

    result = donnes_des_sous_hakim(100, 200)
    print(f"Le résultat est : {result}")

    result = donnes_des_sous_hakim(250, 300)
    print(f"Le résultat est : {result}")
