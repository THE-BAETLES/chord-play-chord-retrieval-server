from services.ChordRetrievalService import ChordRetrievalService
import dotenv
from fastapi import FastAPI
import os

dotenv.load_dotenv()

listen_port = os.environ.get("SERVER_PORT")
output_midi_save_path = os.environ.get("OUTPUT_MIDI_SAVE_PATH")

app = FastAPI()

@app.get('/chord')
async def chord(wavPath: str) -> str:
    wav_path: str = wavPath
    
    with ChordRetrievalService(wav_path, output_midi_save_path) as chordRet:
        midi_path, csv_path = chordRet.start_retrieval()
        
    response = {
        'csvPath': csv_path,
        'midiPath': midi_path
    }
    return response

if __name__ == "__main__":
    print(f"[Chord Retrieval Engine Server] start listen on {1202}")
    app.run(host='0.0.0.0', port=1201)