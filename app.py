from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "C2 Server is running!"

@app.route('/send_command', methods=['POST'])
def send_command():
    data = request.json
    command = data.get('command')
    if command:
        # Process the command (add your logic here)
        return jsonify({"status": "success", "message": f"Command {command} received"})
    return jsonify({"status": "error", "message": "No command provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
