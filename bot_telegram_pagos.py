import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Configuración
TELEGRAM_TOKEN = "8863388863:AAHe8uhjNLZUy42lLdUG3j3FKVZRuiFDJyE"
STRIPE_LINK = "https://buy.stripe.com/dRm28q467g67cL1dsnaIM05"
PAYPAL_LINK = "https://paypal.me/osset233"

# Palabras clave LEGÍTIMAS que activan el bot
PALABRAS_CLAVE = ["renovar", "cuanto cuesta", "cuánto cuesta", "precio", "pagar"]

# Palabras de SPAM/MALICIOSAS (bloquea estas)
PALABRAS_BLOQUEADAS = ["void", "enigma", "telegram", "instagram", "vk", "pasaporte", "fotos", "documentos", "datos", "estafa", "crypto", "bitcoin", "casino", "apuestas"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja mensajes y responde si contienen palabras clave legítimas"""
    
    mensaje = update.message.text.lower()
    
    # Bloquear mensajes que contienen palabras sospechosas
    contiene_spam = any(palabra_spam in mensaje for palabra_spam in PALABRAS_BLOQUEADAS)
    
    if contiene_spam:
        return  # Ignora el mensaje de spam silenciosamente
    
    # Verificar si el mensaje contiene palabras clave legítimas
    contiene_palabra_clave = any(palabra in mensaje for palabra in PALABRAS_CLAVE)
    
    if contiene_palabra_clave:
        # Mensaje con instrucciones de pago
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

💰 **PAYPAL** → 🔗 {}
⚠️ **IMPORTANTE:** Selecciona "Amigos y familiares" y NO escribas nada en concepto

---

❓ ¿Dudas? ¡Escribe aquí! Respondo al instante. 🚀
""".format(STRIPE_LINK, PAYPAL_LINK)
        
        await update.message.reply_text(respuesta, parse_mode='Markdown')

def main():
    """Inicia el bot"""
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Manejador de mensajes de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Inicia el bot
    print("🤖 Bot iniciado. Escuchando mensajes...")
    application.run_polling()

if __name__ == '__main__':
    main()
