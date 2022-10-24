FROM mctlab/omnizart:latest

LABEL maintainer "chobe1<chobe0719@gmail.com>"
LABEL serverType="Chord Retrieval Server"

COPY . /chordRetrievalServer
WORKDIR /chordRetrievalServer

ENV OUTPUT_MIDI_SAVE_PATH /output
ENV SERVER_PORT 3000

RUN pip install fastapi && pip install "uvicorn[standard]" && pip install python-dotenv
EXPOSE 3000

ENTRYPOINT ["uvicorn", "server:app", "--reload" ,"--host","0.0.0.0", "--port","3000"]