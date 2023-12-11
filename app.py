from flask import Flask, jsonify
import pyotp
import hashlib
import os

app = Flask(__name__)

def generate_totp_sha256(secret):
    """
    Generate a TOTP code based on the given secret using SHA256 algorithm.

    Args:
    secret (str): The secret key for the TOTP generation.

    Returns:
    str: The TOTP code.
    """
    totp = pyotp.TOTP(secret, digest=hashlib.sha256)
    return totp.now()

@app.route('/otp/get', methods=['GET'])
def get_otp():
    # For demo purposes, using a fixed secret key. In a real application, 
    # this should be dynamically retrieved from a secure store or user input.
    print(os.environ.get("OTPSECRET"))
    otp_code = generate_totp_sha256(os.environ.get("OTPSECRET"))
    return jsonify({'otp': otp_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
