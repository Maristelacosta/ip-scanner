import ipaddress


def main():
    address = input("Digite um endereço IP: ").strip()

    try:
        ip = ipaddress.ip_address(address)
    except ValueError:
        print("Endereço IP inválido.")
        return

    version = "IPv4" if ip.version == 4 else "IPv6"
    scope = "privado" if ip.is_private else "público"

    print(f"IP válido: {ip}")
    print(f"Tipo: {version}")
    print(f"Endereço: {scope}")


if __name__ == "__main__":
    main()
