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

**Opción 1️⃣ - STRIPE (Tarjeta de crédito/débito)**
1️⃣ Haz clic aquí: 🔗 {}
2️⃣ Sigue los pasos en pantalla
3️⃣ ¡Listo! Recibirás confirmación por email

---

**Opción 2️⃣ - PAYPAL**
1️⃣ Accede a PayPal.com
2️⃣ Haz clic en "Enviar dinero"
3️⃣ Usa este email: 💳 {}
4️⃣ Ingresa el monto que deseas pagar
5️⃣ ¡Completado! Te confirmaremos de inmediato

---

❓ Si tienes dudas o necesitas ayuda, escribe aquí y te responderé ASAP.

¡Gracias por confiar en nuestros servicios! 🙌
""".format(STRIPE_LINK, PAYPAL_EMAIL)
        
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
