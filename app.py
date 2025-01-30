from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Obtener los datos del mensaje
    incoming_msg = request.values.get("Body", "").lower()
    sender = request.values.get("From", "")

    # Procesar mensaje
    response = MessagingResponse()
    msg = response.message(f"Hola, recibí tu mensaje: {incoming_msg}")

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
