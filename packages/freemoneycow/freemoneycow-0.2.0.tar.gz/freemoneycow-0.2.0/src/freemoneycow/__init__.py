from .banque import donnes_des_sous 

def main() -> None:
    print("Hello from donnes-des-sous!")

    result = donnes_des_sous(100, 200)
    print(f"Le résultat est : {result}")

    result = donnes_des_sous(250, 300)
    print(f"Le résultat est : {result}")