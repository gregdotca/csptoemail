import json
import os
import smtplib
import ssl
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()


class Config:
    SOFTWARE_NAME = "CSP To Email"
    EMAIL_SUBJECT = "CSP Report Received"
    EMAIL_SERVER = os.environ.get("CSP2E_SERVER")
    EMAIL_PROTOCOL = os.environ.get("CSP2E_PROTOCOL", "tls")
    EMAIL_PORT = int(os.environ.get("CSP2E_PORT", 587))
    EMAIL_USERNAME = os.environ.get("CSP2E_USERNAME")
    EMAIL_PASSWORD = os.environ.get("CSP2E_PASSWORD")
    EMAIL_SENDER = os.environ.get("CSP2E_SENDER")
    EMAIL_RECEIVER = os.environ.get("CSP2E_RECEIVER")


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["POST"])
def csp_reports():
    send_email(json.dumps(request.get_json(), indent=4))
    return jsonify({"status": "success"}), 200


def send_email(email):
    context = ssl.create_default_context()
    server = smtplib.SMTP(app.config["EMAIL_SERVER"], app.config["EMAIL_PORT"])
    server.starttls(context=context)
    server.login(app.config["EMAIL_USERNAME"], app.config["EMAIL_PASSWORD"])
    server.sendmail(
        app.config["EMAIL_SENDER"], app.config["EMAIL_RECEIVER"], build_email(email)
    )
    server.quit()


def build_email(email):
    full_email = (
        "From: "
        + app.config["SOFTWARE_NAME"]
        + " <"
        + app.config["EMAIL_SENDER"]
        + ">\n"
    )
    full_email += "To: " + app.config["EMAIL_RECEIVER"] + "\n"
    full_email += "Subject: " + app.config["EMAIL_SUBJECT"] + "\n\n"
    full_email += email
    return full_email


if __name__ == "__main__":
    app.run()
