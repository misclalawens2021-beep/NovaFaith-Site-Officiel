from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Configuration SMTP (Exemple pour Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
VOTRE_EMAIL = "votre.email@gmail.com"
VOTRE_MDP = "votre_mot_de_passe_application"    # A générer dans votre compte Google

@app.route('/send-email', methods=['POST'])
def send_email():
    # Récupération des données envoyées par le formulaire HTML
    data = request.json
    nom = data.get('name')
    email_client = data.get('email')
    message_client = data.get('message')

    # Création de l'email
    msg = EmailMessage()
    msg.set_content(f"Nouveau message de : {nom}\nEmail : {email_client}\n\nMessage :\n{message_client}")
    msg['Subject'] = f"NovaFaith - Nouveau contact de {nom}"
    msg['From'] = VOTRE_EMAIL
    msg['To'] = VOTRE_EMAIL # Vous recevrez le mail sur votre propre boite

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(VOTRE_EMAIL, VOTRE_MDP)
            server.send_message(msg)
        return jsonify({"status": "success", "message": "Email envoyé !"}), 200
    except Exception as e: 
        return jsonify({"status": "error", "message": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True, port=5000)