from .banque import ap_donnes_des_sous

def main() -> None:
    print("Hello from donnes-des-sous!")
    result = ap_donnes_des_sous(150, 100)
    print(f"Result of donnes des sous(150, 100): {result}")
    result = ap_donnes_des_sous(250, 100)
    print(f"Result of donnes des sous(250, 100): {result}")
