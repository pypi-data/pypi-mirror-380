# iamex

Librería Python simple y poderosa para acceder a múltiples modelos de inteligencia artificial de forma unificada.

[![PyPI version](https://badge.fury.io/py/iamex.svg)](https://badge.fury.io/py/iamex)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Instalación

```bash
pip install iamex
```

## 🔑 Clave de API (requerida)

Necesitas una API key para usar el SDK.

- Dónde obtenerla: `dev.iamex.io`
- Cómo configurarla (elige 1):
  - Variable de entorno
    - Windows PowerShell: `$env:IAMEX_API_KEY="TU_API_KEY"`
    - Linux/macOS: `export IAMEX_API_KEY="TU_API_KEY"`
  - Archivo `.env`
    ```
    IAMEX_API_KEY=TU_API_KEY
    ```
  - Pasarla directo en el código
    ```python
    from iamex import IAMEX
    client = IAMEX(api_key="TU_API_KEY")
    ```

### Hello World (stream)

```python
from iamex import IAMEX

client = IAMEX()  # usa IAMEX_API_KEY del entorno
for chunk in client.chat.completions.create(
    model="IAM-advanced",
    messages=[{"role": "user", "content": "Di hola en 3 palabras."}],
    stream=True,
):
    piece = (chunk.get("choices") or [{}])[0].get("delta", {}).get("content") or ""
    if piece:
        print(piece, end="", flush=True)
```

### Async (nuevo)

```python
import asyncio
from iamex import AsyncIAMEX

async def main():
    async with AsyncIAMEX() as client:  # usa IAMEX_API_KEY del entorno
        buffer = []
        async for chunk in client.chat.completions.create(
            model="IAM-advanced",
            messages=[{"role": "user", "content": "Di hola en 3 palabras."}],
            stream=True,
        ):
            try:
                choice = (chunk.get("choices") or [])[0]
                delta = choice.get("delta") or {}
                piece = delta.get("content")
                if piece:
                    buffer.append(piece)
                    print(piece, end="", flush=True)
            except Exception:
                pass
        print("\n\nFinal:\n" + "".join(buffer))

asyncio.run(main())
```

Dependencias para async

Para usar el cliente asíncrono instala `httpx`:

```bash
pip install httpx
```

## ✅ Compatibilidad estilo OpenAI (Nuevo en v0.0.5)

Ahora puedes usar `iamex` en proyectos pensados para el SDK de OpenAI sin reescribir tu app. Solo instala el paquete y cambia el import. Así de fácil.

### Migración en 1 línea

```python
# Antes (OpenAI):
# from openai import OpenAI

# Ahora (iamex con interfaz OpenAI):
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")
```

### Responses API (estilo v1)

```python
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")

response = client.responses.create(
    model="IAM-advanced",
    input="Dime un haiku sobre Python"
)

print(response.output_text)
```

### Chat Completions

```python
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")

chat = client.chat.completions.create(
    model="IAM-advanced",
    messages=[
        {"role": "system", "content": "Eres un asistente útil"},
        {"role": "user", "content": "Explica la recursión en una frase"}
    ]
)

print(chat["choices"][0]["message"]["content"])
```

### Text Completions

```python
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")

comp = client.completions.create(
    model="IAM-advanced",
    prompt="Crea una lista de 3 ideas de apps"
)

print(comp["choices"][0]["text"])  # si el proveedor devuelve 'text'
```

### Listado de modelos

```python
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")
models = client.models.list()
print(models)
```

## 🤖 Modelos Disponibles

- **iam-adv-mex** - Modelo avanzado en español
- **IAM-lite** - Modelo ligero en español
- **IAM-advanced** - Modelo avanzado en español (recomendado)
- **iam-lite-mex** - Modelo ligero en español

## 📝 Uso Rápido

### Estilo compatible (recomendado)

```python
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")

# Responses API
resp = client.responses.create(model="IAM-advanced", input="¿Qué es Python?")
print(resp.output_text)

# Chat Completions
chat = client.chat.completions.create(
    model="IAM-advanced",
    messages=[{"role": "user", "content": "Explica una función lambda"}]
)
print(chat["choices"][0]["message"]["content"])
```

### Listar modelos

```python
models = client.models.list()
print(models)
```

## ⚡ Streaming (Nuevo en v0.0.5)

Soportamos respuestas en streaming con `stream=True` en `chat.completions.create`, `completions.create` y `responses.create`.

- Formato de stream: líneas `data: { ... }` y cierre `data: [DONE]`.
- Los chunks intermedios traen el texto parcial; `finish_reason` llega al final.
- Métricas `usage` normalmente no vienen dentro del stream.

### Ejemplo: Chat Completions (stream)

```python
from iamex import IAMEX

client = IAMEX(api_key="tu_api_key")

buffer = []
for chunk in client.chat.completions.create(
    model="IAM-advanced",
    messages=[{"role": "user", "content": "Escribe un haiku sobre Python"}],
    stream=True,
):
    try:
        choice = (chunk.get("choices") or [])[0]
        delta = choice.get("delta") or {}
        piece = delta.get("content")
        if piece:
            buffer.append(piece)
            print(piece, end="", flush=True)
    except Exception:
        pass

print("\n\nFinal:\n" + "".join(buffer))
```

Chunk típico (simplificado):

```text
data: {"id":"chatcmpl_x","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"role":"assistant","content":"Hola"},"finish_reason":null}]}
data: {"id":"chatcmpl_x","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":", mundo"},"finish_reason":null}]}
data: {"id":"chatcmpl_x","object":"chat.completion.chunk","choices":[{"index":0,"delta":{},"finish_reason":"stop"}]}
data: [DONE]
```

### Ejemplo: Text Completions (stream)

```python
buffer = []
for chunk in client.completions.create(
    model="IAM-advanced",
    prompt="Di hola en 3 palabras.",
    stream=True,
):
    try:
        choice = (chunk.get("choices") or [])[0]
        piece = choice.get("text") or (choice.get("delta") or {}).get("content")
        if piece:
            buffer.append(piece)
            print(piece, end="", flush=True)
    except Exception:
        pass

print("\n\nFinal:\n" + "".join(buffer))
```

Chunk típico (simplificado):

```text
data: {"id":"cmpl_x","object":"text_completion.chunk","choices":[{"index":0,"text":"Hola","finish_reason":null}]}
data: {"id":"cmpl_x","object":"text_completion.chunk","choices":[{"index":0,"text":", mundo","finish_reason":null}]}
data: {"id":"cmpl_x","object":"text_completion.chunk","choices":[{"index":0,"text":"","finish_reason":"stop"}]}
data: [DONE]
```

### Ejemplo: Responses (stream)

```python
for chunk in client.responses.create(
    model="IAM-advanced",
    input="Escribe un haiku de Python.",
    stream=True,
):
    # Si el chunk trae texto directo
    if isinstance(chunk, dict) and chunk.get("output_text"):
        print(chunk["output_text"], end="", flush=True)
        continue
    # Fallback: mostrar chunk crudo para debugging
    print(chunk)
```

Notas rápidas:
- Imprime texto a medida que llegan los chunks; al final, llega `finish_reason` con "stop" o similar.
- Si tu app necesita el texto completo, acumúlalo en un buffer y únelo al final.

## 🔧 Funcionalidades Principales

### 1. Solo Contenido vs Respuesta Completa (v0.0.4)

Por defecto, `iamex` devuelve solo el texto de la respuesta. Si necesitas metadatos adicionales, usa `full_response=True`:

```python
# Solo contenido (default)
content = send_prompt("Hola", api_key, "IAM-advanced")
print(content)  # "¡Hola! ¿En qué puedo ayudarte?"

# Respuesta completa con metadatos
full_response = send_prompt("Hola", api_key, "IAM-advanced", full_response=True)
print(full_response)  # {"choices": [...], "usage": {"tokens": 25}, ...}
```

### 2. Parámetros de Control

```python
# Con límite de tokens
response = send_prompt(
    prompt="Explica la IA en detalle",
    api_key="tu_api_key",
    model="IAM-advanced",
    max_tokens=100  # Limitar respuesta
)

# Con mensaje del sistema
response = send_prompt(
    prompt="¿Cómo funciona un bucle for?",
    api_key="tu_api_key",
    model="IAM-advanced",
    system_prompt="Eres un tutor de programación para principiantes"
)
```

### 3. Conversaciones Avanzadas (v0.0.4)

```python
# Conversación multi-turno
messages = [
    {"role": "system", "content": "Eres un asistente de cocina"},
    {"role": "user", "content": "¿Cómo hago pasta?"},
    {"role": "assistant", "content": "Para hacer pasta necesitas..."},
    {"role": "user", "content": "¿Y qué salsa me recomiendas?"}
]

response = send_messages(messages, api_key, "IAM-advanced")
```

## 🛠️ Uso Avanzado

### Cliente Personalizado

```python
from iamex import PromptClient

# Inicializar el cliente con tu API key
client = PromptClient(api_key="tu_api_key_aqui")

# Enviar un prompt (usa modelo por defecto 'IAM-advanced')
response = client.send_prompt(
    prompt="Explica qué es la inteligencia artificial"
)
print(response)

# Con respuesta completa
full_response = client.send_prompt("¿Qué es la IA?", full_response=True)
print(full_response['usage']['total_tokens'])  # Ver tokens usados
```

### Parámetros Avanzados

El método `send_prompt` y `PromptClient` aceptan parámetros adicionales para control fino:

```python
response = client.send_prompt(
    prompt="Tu prompt aquí",
    model="IAM-advanced",
    temperature=0.5,        # Controla la creatividad (0.0 - 1.0)
    max_tokens=1000,        # Máximo número de tokens en la respuesta
    top_p=0.9,             # Controla la diversidad de la respuesta
    top_k=50,              # Limita las opciones de tokens
    repetition_penalty=1.1, # Evita repeticiones
    presence_penalty=0.1,   # Penaliza tokens ya presentes
    frequency_penalty=0.1,  # Penaliza tokens frecuentes
    stream=False            # Respuesta en streaming
)
```

### Parámetros por Defecto

Si no especificas parámetros, se usan estos valores optimizados:

- `model`: `"IAM-advanced"`
- `temperature`: `0.3`
- `max_tokens`: `12000`
- `top_p`: `0.9`
- `top_k`: `50`
- `repetition_penalty`: `1.1`
- `presence_penalty`: `0.1`
- `frequency_penalty`: `0.1`
- `stream`: `False`

## 📊 Estructura de Datos

### Estructura del Payload

La función `send_prompt` envía automáticamente este payload a la API:

```json
{
  "apikey": "tu_api_key_aqui",
  "model": "tu_modelo",
  "prompt": "tu_prompt"
}
```

Para `send_messages`:

```json
{
  "apikey": "tu_api_key_aqui",
  "model": "tu_modelo",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ]
}
```

**Parámetros obligatorios:**
- `apikey`: Tu clave de API para autenticación
- `model`: El modelo de IA a usar
- `prompt` o `messages`: Tu consulta o conversación

**Parámetros opcionales:**
- `system_prompt`: Instrucciones del sistema (solo con `send_prompt`)
- `max_tokens`: Límite de tokens en la respuesta
- `temperature`, `top_p`, `top_k`: Parámetros de generación
- `full_response`: Control del tipo de respuesta (v0.0.4)

## 📚 Funciones Disponibles

### `send_prompt()`
```python
send_prompt(
    prompt: str,           # Tu pregunta o instrucción
    api_key: str,          # Clave de API (obtén en dev.iamex.io)
    model: str,            # Modelo a usar
    full_response: bool = False,  # Respuesta completa o solo contenido
    max_tokens: int = None,       # Límite de tokens (opcional)
    system_prompt: str = None,    # Mensaje del sistema (opcional)
    **kwargs                      # Parámetros adicionales
)
```

### `send_messages()` (Nuevo en v0.0.4)
```python
send_messages(
    messages: list,        # Lista de mensajes de conversación
    api_key: str,          # Clave de API
    model: str,            # Modelo a usar
    full_response: bool = False,  # Respuesta completa o solo contenido
    max_tokens: int = None,       # Límite de tokens (opcional)
    **kwargs                      # Parámetros adicionales
)
```

### `PromptClient`
```python
client = PromptClient(api_key="tu_api_key")
client.send_prompt(prompt, model="IAM-advanced", **kwargs)
client.send_messages(messages, model="IAM-advanced", **kwargs)
client.get_models()  # Obtener modelos disponibles
```

## 🔐 Obtener API Key

1. Visita [dev.iamex.io](https://dev.iamex.io)
2. Regístrate o inicia sesión
3. Obtén tu API key
4. Adquiere tokens según tus necesidades

## ⚠️ Manejo de Errores

```python
try:
    response = send_prompt("Test", "api_key_invalida", "IAM-advanced")
    print(response)
except Exception as e:
    print(f"Error: {e}")
    # Salida: Error 401: API Key inválida o no encontrada
```

### Errores Comunes
- **401**: API Key inválida o no encontrada
- **400**: Parámetros incorrectos
- **500**: Error interno del servidor
- **502**: Servidor temporalmente no disponible

## 📚 Ejemplos Completos

### Chat Básico
```python
from iamex import send_messages

def chat_simple():
    api_key = "tu_api_key_aqui"
    model = "IAM-advanced"
    
    messages = [
        {"role": "system", "content": "Eres un asistente útil y amigable"}
    ]
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            break
            
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = send_messages(messages, api_key, model)
            print(f"IA: {response}")
            messages.append({"role": "assistant", "content": response})
        except Exception as e:
            print(f"Error: {e}")

chat_simple()
```

### Análisis de Texto
```python
from iamex import send_prompt

def analizar_sentimiento(texto, api_key):
    prompt = f"Analiza el sentimiento del siguiente texto: '{texto}'"
    
    response = send_prompt(
        prompt=prompt,
        api_key=api_key,
        model="IAM-advanced",
        system_prompt="Eres un experto en análisis de sentimientos. Responde solo: Positivo, Negativo o Neutral."
    )
    
    return response

# Uso
sentimiento = analizar_sentimiento("¡Me encanta este producto!", "tu_api_key")
print(sentimiento)  # "Positivo"
```

### Uso con Métricas (v0.0.4)
```python
from iamex import send_prompt

# Para obtener información de uso
response = send_prompt(
    "Explica brevemente qué es Python",
    api_key="tu_api_key",
    model="IAM-advanced",
    full_response=True
)

# Extraer métricas
if isinstance(response, dict):
    usage = response.get('data', {}).get('response', {}).get('usage', {})
    print(f"Tokens usados: {usage.get('total_tokens', 'N/A')}")
    print(f"Costo estimado: ${usage.get('total_tokens', 0) * 0.001:.4f}")
```

## 🏗️ Desarrollo

### Instalación para Desarrollo
```bash
git clone https://github.com/IA-Mexico/iamex.git
cd iamex
pip install -e ".[dev]"
```

### Ejecutar Tests
```bash
pytest tests/
```

### Formatear Código
```bash
black src/ tests/
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 🆘 Soporte

- **Documentación**: [GitHub](https://github.com/IA-Mexico/iamex)
- **Issues**: [GitHub Issues](https://github.com/IA-Mexico/iamex/issues)
- **Email**: hostmaster@iamex.io
- **Portal de desarrolladores**: [dev.iamex.io](https://dev.iamex.io)

## 📋 Changelog

### v0.0.5 (Actual)
- ✅ **NUEVO**: Compatibilidad estilo OpenAI SDK v1 (Responses y Completions)
- ✅ **NUEVO**: Streaming en `chat.completions`, `completions` y `responses` con `stream=True`
- ✅ **NUEVO**: Migración en 1 línea: usa la clase `IAMEX` (interfaz estilo OpenAI)
- ✅ **MEJORADO**: Documentación para usar `responses.create`, `chat.completions.create` y `completions.create`
- ✅ **NOTA**: No es necesario cambiar endpoints en tu código

### v0.0.4
- ✅ **NUEVO**: Parámetro `full_response` para controlar el tipo de respuesta
- ✅ **NUEVO**: Función `send_messages` para conversaciones con formato de mensajes
- ✅ **NUEVO**: Soporte para conversaciones multi-turno
- ✅ **MEJORADO**: Extracción inteligente de contenido de respuestas
- ✅ **MEJORADO**: Compatibilidad hacia atrás mantenida
- ✅ **DOCUMENTACIÓN**: Guías completas y ejemplos prácticos

### v0.0.3
- ✅ **NUEVO**: Parámetro opcional `max_tokens` en función `send_prompt`
- ✅ **MEJORADO**: Control de longitud de respuestas del modelo
- ✅ **MEJORADO**: Endpoint real de iam-hub implementado
- ✅ **OPTIMIZADO**: Estructura de payload exacta para la API
- ✅ **DOCUMENTACIÓN**: Guías de uso para max_tokens

### v0.0.2
- ✅ **NUEVO**: Función simple `send_prompt(prompt, api_key, model)`
- ✅ **NUEVO**: Soporte completo para autenticación con API key
- ✅ **NUEVO**: Conexión directa al endpoint real de iam-hub
- ✅ **MEJORADO**: Estructura de payload exacta que espera la API

### v0.0.1
- Versión inicial con cliente básico `PromptClient`
- Soporte para múltiples modelos de inferencia
- Modelo por defecto: `IAM-advanced`
- Parámetros optimizados según la API

---

**¡Desarrollado con ❤️ por Inteligencia Artificial México!**