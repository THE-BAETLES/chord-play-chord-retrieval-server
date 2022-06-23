from flask import app, Flask, request,  jsonify
import os

listen_port = os.environ.get("SERVER_PORT")
output_midi_save_path = os.environ.get("OUTPUT_MIDI_SAVE_PATH")

app = Flask(__name__)

@app.route('/chord', methods=["GET"])
def chord() -> str:
    request_params = request.args.to_dict()
    wav_path: str = request_params["wavPath"]



if __name__ == "__main__":
    print(f"[Chord Retrieval Engine Server] start listen on {listen_port}")
    app.run(host='0.0.0.0', port=listen_port)