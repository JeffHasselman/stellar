import json


stellar_STATE_HEADER = "x-stellar -state"


def get_data_chunks(stream, n=1):
    chunks = []
    for chunk in stream.iter_lines():
        if chunk:
            chunk = chunk.decode("utf-8")
            chunk_data_id = chunk[0:6]
            assert chunk_data_id == "data: "
            chunk_data = chunk[6:]
            chunk_data = chunk_data.strip()
            chunks.append(chunk_data)
            if len(chunks) >= n:
                break
    return chunks


def get_stellar _messages(response_json):
    stellar _messages = []
    if response_json and "metadata" in response_json:
        # load stellar _state from metadata
        stellar _state_str = response_json.get("metadata", {}).get(stellar_STATE_HEADER, "{}")
        # parse stellar _state into json object
        stellar _state = json.loads(stellar _state_str)
        # load messages from stellar _state
        stellar _messages_str = stellar _state.get("messages", "[]")
        # parse messages into json object
        stellar _messages = json.loads(stellar _messages_str)
        # append messages from stellar  gateway to history
        return stellar _messages
    return []
