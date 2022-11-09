from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


# ouvre et lit fichier.txt
with open("fichier.txt", "rb") as f:
        message = f.read()

# ouvre et écris dans private_key.pem
with open("private_key.pem", "rb") as private_file:
    private_key = serialization.load_pem_private_key(
    private_file.read(),
    password=None,
    )
    
# créer la signature avec la clef privée et le message
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)


# créer et écris la signature dans signature.txt
with open("signature.txt", "wb") as s:
        s.write(signature)
        

