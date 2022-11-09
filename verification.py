from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization



# ouvre et lis le fichier.txt
with open("fichier.txt", "rb") as f:
        message = f.read()


# ouvre et lis le fichier signature
with open("signature.txt", "rb") as s:
        signature = s.read()


# ouvre et écris dans private_key.pem
with open("public_key.pem", "rb") as public_file:
    public_key = serialization.load_pem_public_key(
        public_file.read(),
    )

# vérifie si la signature et la même qu'au début
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)