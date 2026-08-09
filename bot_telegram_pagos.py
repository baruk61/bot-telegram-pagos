import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Configuración
TELEGRAM_TOKEN = "8863388863:AAHe8uhjNLZUy42lLdUG3j3FKVZRuiFDJyE"
STRIPE_LINK = "https://buy.stripe.com/dRm28q467g67cL1dsnaIM05"
PAYPAL_EMAIL = "baruk61@protonmail.com"

# Palabras clave que activan el bot
PALABRAS_CLAVE = ["renovar", "cuanto cuesta", "cuánto cuesta", "precio", "pagar"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja mensajes y responde si contienen palabras clave"""
    
    mensaje = update.message.text.lower()
    
    # Verificar si el mensaje contiene palabras clave
    contiene_palabra_clave = any(palabra in mensaje for palabra in PALABRAS_CLAVE)
    
    if contiene_palabra_clave:
        # Mensaje con instrucciones de pago
        respuesta = """
🎯 **¡Perfecto! Aquí están tus opciones de pago:**

respuesta = """
🎯 **¡Bienvenido a Exclusives Soportes!**

Ofrecemos dos servicios premium:

📺 **SERVICIO TV**
Acceso a TV en vivo con múltiples canales

🎬 **SERVICIO STREAMING**
Plex, Emby, Jellyfin y más

---

**PRECIOS - TV (por pantalla)**

3️⃣ **3 MESES**
  • 1 pantalla: €30
  • 2 pantallas: €45

6️⃣ **6 MESES**
  • 1 pantalla: €45
  • 2 pantallas: €55

1️⃣2️⃣ **1 AÑO**
  • 1 pantalla: €70
  • 2 pantallas: €90

---

**PRECIOS - STREAMING** 🎬
(Mismo precio que TV)

---

**¿QUIERES AMBOS SERVICIOS?** 
Contáctame en privado para un presupuesto personalizado.

---

**PAGA AHORA:**

💳 **STRIPE** → 🔗 {}

💰 **PAYPAL** 
Envía a: {}
⚠️ **IMPORTANTE:** Selecciona "Amigos y familiares" y NO escribas nada en concepto

---

❓ ¿Dudas? ¡Escribe aquí! Respondo al instante. 🚀
"""
