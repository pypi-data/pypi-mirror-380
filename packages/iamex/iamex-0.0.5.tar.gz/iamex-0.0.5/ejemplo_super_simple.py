"""
EJEMPLO SÚPER SIMPLE - Exactamente lo que necesitas
"""

from iamex import IAMEX

# TU API KEY AQUÍ
API_KEY = "070644fc3192dfb2a98c9f66bcbf8c6b26fa9296004cfb4f2c3453438db5cfba"

# TU PROMPT AQUÍ
PROMPT = "Explica qué es la inteligencia artificial en una frase"

# TU MODELO AQUÍ
MODEL = "IAM-advanced"

# PARÁMETROS OPCIONALES
MAX_TOKENS = 100  # Limitar respuesta a 100 tokens

# ¡SOLO 3 PARÁMETROS OBLIGATORIOS + max_tokens opcional!
client = IAMEX(api_key=API_KEY)
response = client.completions.create(
    model=MODEL,
    prompt=PROMPT,
    max_tokens=MAX_TOKENS,
)

print("🤖 RESPUESTA:")
print(response)

# Si quieres solo el texto de la respuesta:
if isinstance(response, dict) and 'choices' in response and len(response['choices']) > 0:
    choice = response['choices'][0]
    text = choice.get('text')
    if text is None and isinstance(choice.get('message'), dict):
        text = choice['message'].get('content')
    if text is not None:
        print("\n📝 TEXTO DE LA RESPUESTA:")
        print(text)
