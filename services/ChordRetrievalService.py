import os
import time
from typing import Tuple
class ChordRetrievalService:
    def __init__(self, wav_path: str,output_base_path: str) -> None:
        self.wav_path = wav_path
        self.output_base_path = output_base_path

    def start_retrieval(self) -> Tuple[str, str]:
        """
        wav_path = "/input/video_id/B.wav

        mid_output_path = "/output/video_id/accompaniment.mid
        csv_output_path = "/output/video_id/accompanimenet.csv

        """
        print("Chord retrieval start!!")
        retrieval_start_time = time.time()
        video_id = self.wav_path.split('/')[-2]

        save_path = os.path.join(self.output_base_path, video_id)
        os.makedirs(save_path, exist_ok=True)

        mid_output_path = os.path.join(save_path, "accompaniment.mid")
        csv_output_path = os.path.join(save_path, "accompaniment.csv")

        # make midi and csv
        os.system(f"omnizart chord transcribe -o {mid_output_path} {self.wav_path}")
        # wav 데이터    

        print(f"Chord retrieval end in {time.time() - retrieval_start_time}s")

        return mid_output_path, csv_output_path



        