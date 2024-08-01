from flask import Flask, send_file
from datetime import datetime

app = Flask(__name__)

# Dictionary to store email open logs
email_open_logs = {}

@app.route('/track/<email_id>.png')
def track_email(email_id):
    # Log the email open event
    email_open_logs[email_id] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Return a 1x1 transparent pixel
    return send_file('1x1.png', mimetype='image/png')

@app.route('/logs', methods=['GET'])
def get_logs():
    # Return the email open logs
    return email_open_logs

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)