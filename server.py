from flask import app, Flask, request,  jsonify
from services.ChordRetrievalService import ChordRetrievalService

import os

listen_port = 3000
output_midi_save_path = os.environ.get("OUTPUT_MIDI_SAVE_PATH")

app = Flask(__name__)

@app.route('/chord', methods=["GET"])
def chord() -> str:
    request_params = request.args.to_dict()
    wav_path: str = request_params["wavPath"]

    retrieval_service = ChordRetrievalService(wav_path, output_midi_save_path)
    
    csv_path, midi_path = retrieval_service.start_retrieval()

    response = {
        'csv_path': csv_path,
        'midi_path': midi_path
    }
    
    return jsonify(response)


if __name__ == "__main__":
    print(f"[Chord Retrieval Engine Server] start listen on {1202}")
    app.run(host='0.0.0.0', port=1202)