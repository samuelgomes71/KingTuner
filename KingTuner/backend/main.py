"""
Backend do KingTuner - Família King
Sistema de APIs para o aplicativo KingTuner
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'app': 'KingTuner',
        'version': '1.0.0',
        'status': 'running',
        'familia': 'King'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/info')
def info():
    return jsonify({
        'name': 'KingTuner',
        'description': 'API do KingTuner - Família King',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
