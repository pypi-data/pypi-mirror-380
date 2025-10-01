from .model import load_silero_vad

vad_model = load_silero_vad()
print("silero_vad jit model Loaded")

from .utils_vad import (get_speech_timestamps,
                                  save_audio,
                                  read_audio,
                                  VADIterator,
                                  collect_chunks,
                                  drop_chunks)


def svad(filename , sampling_rate=16000 , min_speech_duration_ms=250 , max_speech_duration_s=float('inf'),min_silence_duration_ms=100):
    wav = read_audio(filename)
    speech_timestamps = get_speech_timestamps(
        wav,
        vad_model,
        return_seconds=True,  # Return speech timestamps in seconds (default is samples)
        sampling_rate=sampling_rate,
        min_speech_duration_ms=min_speech_duration_ms,
        max_speech_duration_s=max_speech_duration_s,
        min_silence_duration_ms=min_silence_duration_ms,     
    )
    return(speech_timestamps , wav)