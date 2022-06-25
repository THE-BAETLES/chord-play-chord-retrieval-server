from ast import Str
import os
import time

class ChordRetrievalService:
    def __init__(self, wav_path: str,output_base_path: str) -> None:
        self.wav_path = wav_path
        self.output_base_path = output_base_path

    def start_retrieval(self):
        """
        wav_path = "/input/video_id/B.wav

        mid_output_path = "/output/video_id/accompaniment.mid
        csv_output_path = "/output/video_id/accompanimenet.csv

        """
        print("Chord retrieval start!!")
        retrieval_start_time = time.time()
        video_id = self.wav_path.split('/')[-2]

        mid_output_path = os.path.join("/output", video_id, "accompaniment.mid")
        csv_output_path = os.path.join("/output", video_id, "accompaniment.csv")


        # 추후에 두 로직을 통합하는 코드 작성해야 함
        # make midi
        os.system(f"omnizart chord transcribe -o {mid_output_path}")

        # make csvxs
        os.system(f"omnizart chord transcribe -o {csv_output_path}")
        # wav 데이터    

        print(f"Chord retrieval end in {time.time() - retrieval_start_time}s")




        