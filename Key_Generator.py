from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#Ce script permet de générer les clefs : privé & public
#Il crée des fichier PEM où il écrit les clefs dedans

# Generate the RSA private key with public_exponent=65537 and key size 2048. Note that the key size of 2048 is the smallest recommended key size.
key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
)

# génère la clef privée
private_key = key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.PKCS8,
        encryption_algorithm = serialization.NoEncryption()
)

# génère la clef publique
public_key = key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format= serialization.PublicFormat.SubjectPublicKeyInfo
)


# créer et écris dans un fichier .pem la clef privée
with open("private_key.pem", "wb") as pk:
        pk.write(private_key)


# créer et écris dans un fichier .pem la clef publique
with open("public_key.pem", "wb") as pb:
        pb.write(public_key)