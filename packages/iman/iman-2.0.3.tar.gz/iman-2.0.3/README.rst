iman
====

Overview
--------

``iman`` is a comprehensive Python package offering a wide array of utilities for audio processing, file manipulation, machine learning, system operations, web utilities, and more. It provides tools for tasks such as audio feature extraction, voice activity detection, file I/O, system monitoring, and integration with frameworks like PyTorch and TensorFlow. The package is organized into multiple submodules, each designed for specific functionalities, as detailed below.

Installation
------------

Install ``iman`` via pip:

.. code-block:: bash

    pip install iman

Ensure dependencies like ``numpy``, ``torch``, ``tensorflow``, ``speechbrain``, ``librosa``, ``matplotlib``, ``pandas``, and external tools like ``ffmpeg``, ``ffprobe``, and ``WinRAR`` are installed. Some functions require pre-trained models or specific paths (e.g., model files, ``ffmpeg_path``).

Usage
-----

Below are examples of key functionalities from the ``iman`` package. For detailed function signatures and parameters, refer to the sections below or use the built-in help system:

**Example: Audio Processing**

.. code-block:: python

    from iman import Audio

    # Read a WAV file
    data, sr = Audio.Read("audio.wav", sr=16000, start_from=0, dur=None, mono=True, ffmpeg_path="c:\\ffmpeg.exe", ffprobe_path="c:\\ffprobe.exe")

    # Resample and write audio
    resampled = Audio.Resample(data, fs=sr, sr=8000)
    Audio.Write("output.wav", resampled, fs=8000)

**Example: File Operations**

.. code-block:: python

    from iman import *

    # Get files matching a pattern
    files = gf("*.txt")

    # Write a dictionary to a file
    my_dict = {"key1": "value1", "key2": "value2"}
    Write_Dic(my_dict, "output.txt")

**Example: VAD with Segmenter**

.. code-block:: python

    from iman.sad_torch_mfcc import Segmenter

    seg = Segmenter(batch_size=32, vad_type="vad", sr=8000, model_path="c:\\sad_model_pytorch.pth", tq=1, ffmpeg_path="c:\\ffmpeg.exe", complete_output=False, device="cuda", input_type="file")
    isig, wav, mfcc = seg("audio.wav")

Modules and Functions
---------------------

The ``iman`` package is organized into several submodules, each with specific functions. Below is a complete list of modules and their functions as provided.

iman
~~~~

- ``plt``: Matplotlib plotting library.
- ``now()``: Get current time.
- ``F``: Format floating-point number.
- ``D``: Format integer number.
- ``Write_List(MyList, Filename)``: Write a list to a text file.
- ``Write_Dic(MyDic, Filename)``: Write a dictionary to a text file.
- ``Read(Filename)``: Read a text file.
- ``Read_Lines(Filename)``: Read a text file line by line and return a list.
- ``Write(_str, Filename)``: Write a string to a text file.
- ``gf(pattern)``: Get files in a directory matching a pattern.
- ``gfa(directory_pattern, ext="*.*")``: Get files in a directory and subdirectories.
- ``ReadE(Filename)``: Read Excel files.
- ``PM(dir)``: Create a directory.
- ``PB(fname)``: Get basename of a file.
- ``PN(fname)``: Get filename without path.
- ``PE(fname)``: Get file extension.
- ``PD(fname)``: Get directory of a file.
- ``PS(fname)``: Get file size.
- ``PJ(segments)``: Join path segments.
- ``clear()``: Clear command-line interface.
- ``os``: Python os module.
- ``np``: NumPy module.
- ``RI(start_int, end_int, count=1)``: Generate random integers.
- ``RF(start_float, end_float, count=1)``: Generate random floats.
- ``RS(Arr)``: Shuffle an array.
- ``LJ(job_file_name)``: Load job file (details not specified).
- ``SJ(value, job_file_name)``: Save job file (details not specified).
- ``LN(np_file_name)``: Load NumPy file (details not specified).
- ``SN(arr, np_file_name)``: Save NumPy array to file.
- ``cmd(command, redirect=True)``: Run a command in CMD.
- ``PX(fname)``: Check existence of a file.
- ``RC(Arr, size=1)``: Random choice from an array.
- ``onehot(data, nb_classes)``: Convert data to one-hot encoding.
- ``exe(pyfile)``: Convert Python file to executable (requires PyInstaller).
- ``FWL(wavfolder, sr)``: Get total audio length in a folder.
- ``norm(vector)``: Normalize a vector (vector/magnitude(vector)).
- ``delete(pattern)``: Delete files matching a pattern.
- ``rename(fname, fout)``: Rename a file.
- ``separate(pattern, folout)``: Separate vocal from music.
- ``dll(fname)``: Create a .pyd file from a Python file.
- ``get_hard_serial()``: Get hardware serial number.
- ``mute_mic()``: Toggle microphone on/off.
- ``PA(fname)``: Get absolute path of a file.

iman.Audio
~~~~~~~~~~

- ``Read(filename, sr, start_from, dur, mono, ffmpeg_path, ffprobe_path)``: Read WAV, ALAW, MP3, and other audio formats.
- ``Resample(data, fs, sr)``: Resample audio data.
- ``Write(filename, data, fs)``: Write audio data to a file.
- ``frame(y)``: Frame audio data (details not specified).
- ``split(y)``: Split audio data (details not specified).
- ``ReadT(filename, sr, mono=True)``: Read and resample WAV file with torchaudio.
- ``VAD(y, top_db=40, frame_length=200, hop_length=80)``: Voice activity detection.
- ``compress(fname_pattern, sr=16000, ext='mp3', mono=True, ffmpeg_path='c:\\ffmpeg.exe', ofolder=None, worker=4)``: Compress audio files.
- ``clip_value(wav)``: Return clipping percentage in an audio file.
- ``WriteS(filename, data, fs)``: Convert and write audio to stereo.

iman.info
~~~~~~~~~

- ``get()``: Get information about CPU and GPU (requires torch).
- ``cpu()``: Get CPU percentage usage.
- ``gpu()``: Get GPU memory usage.
- ``memory()``: Get RAM usage in GB.
- ``plot(fname="log.txt", delay=1)``: Plot system metrics from a log file.

iman.metrics
~~~~~~~~~~~~

- ``EER(lab, score)``: Compute Equal Error Rate.
- ``cosine_distance(v1, v2)``: Compute cosine distance between two vectors.
- ``roc(lab, score)``: Compute ROC curve.
- ``wer(ref, hyp)``: Compute Word Error Rate.
- ``cer(ref, hyp)``: Compute Character Error Rate.
- ``wer_list(ref_list, hyp_list)``: Compute WER for lists.
- ``cer_list(ref_list, hyp_list)``: Compute CER for lists.
- ``DER(ref_list, res_list, file_dur=-1, sr=8000)``: Compute Detection Error Rate.

iman.tsne
~~~~~~~~~

- ``plot(fea, label)``: Plot t-SNE visualization of features.

iman.xvector
~~~~~~~~~~~~

- ``xvec, lda_xvec, gender = get(filename, model(model_path, model_name, model_speaker_num))``: Extract x-vectors for speaker recognition.

iman.web
~~~~~~~~

- ``change_wallpaper()``: Change system wallpaper.
- ``dl(url)``: Download a file from a URL.
- ``links(url, filter_text=None)``: Extract links from a URL.
- ``imgs(url, filter_text=None)``: Extract images from a URL.

iman.matlab
~~~~~~~~~~~

- ``np2mat(param, mat_file_name)``: Convert NumPy array to MATLAB file.
- ``dic2mat(param, mat_file_name)``: Convert dictionary to MATLAB file.
- ``mat2dic(mat_file_name)``: Convert MATLAB file to dictionary.

iman.Features
~~~~~~~~~~~~~

- ``mfcc_fea, mspec, log_energy = mfcc.SB.Get(wav, sample_rate)``: Compute MFCC with SpeechBrain (input must be read with torchaudio).
- ``mfcc.SB.Normal(MFCC)``: Mean-variance normalization of MFCC with SpeechBrain.
- ``mfcc_fea, log_energy = mfcc.LS.Get(wav, sample_rate, le=False)``: Compute MFCC with Librosa (input is NumPy array).
- ``mfcc.LS.Normal(MFCC, win_len=150)``: Mean-variance normalization (local, 150 frames left and right).

iman.AUG
~~~~~~~~

- ``Add_Noise(data, noise, snr)``: Add noise to audio data.
- ``Add_Reverb(data, rir)``: Add reverberation to audio data.
- ``Add_NoiseT(data, noise, snr)``: Add noise using torchaudio.
- ``Add_ReverbT(data, rir)``: Add reverberation using torchaudio.
- ``mp3(fname, fout, sr_out, ratio, ffmpeg_path='c:\\ffmpeg.exe')``: Convert to MP3.
- ``speed(fname, fout, ratio, ffmpeg_path='c:\\ffmpeg.exe')``: Change audio speed.
- ``volume(fname, fout, ratio, ffmpeg_path='c:\\ffmpeg.exe')``: Adjust audio volume.

iman.sad_torch_mfcc | iman.sad_tf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Initializer** (PyTorch):

  .. code-block:: python

      seg = Segmenter(batch_size, vad_type=['sad'|'vad'], sr=8000, model_path="c:\\sad_model_pytorch.pth", tq=1, ffmpeg_path='c:\\ffmpeg.exe', complete_output=False, device='cuda', input_type='file')

- **Initializer** (TensorFlow):

  .. code-block:: python

      seg = Segmenter(batch_size, vad_type=['sad'|'vad'], sr=16000, model_path="c:\\keras_speech_music_noise_cnn.hdf5", gender_path="c:\\keras_male_female_cnn.hdf5", ffmpeg_path='c:\\ffmpeg.exe', detect_gender=False, complete_output=False, device='cuda', input_type='file')

- ``isig, wav, mfcc = seg(fname)``: Process audio file (MFCC output only in PyTorch model).
- ``nmfcc = filter_fea(isig, mfcc, sr, max_time)``: Filter features (PyTorch only).
- ``mfcc = MVN(mfcc)``: Mean-variance normalization (PyTorch only).
- ``isig = filter_output(isig, max_silence, ignore_small_speech_segments, max_speech_len, split_speech_bigger_than)``: Filter output when ``complete_output=False``.
- ``seg2aud(isig, filename)``: Convert segments to audio.
- ``seg2json(isig)``: Convert segments to JSON.
- ``seg2Gender_Info(isig)``: Extract gender information from segments.
- ``seg2Info(isig)``: Extract segment information.
- ``wav_speech, wav_noise = filter_sig(isig, wav, sr)``: Get speech and noise parts (when ``complete_output=False``).

- **sad_tf.segmentero**:

  .. code-block:: python

      from sad_tf.segmentero import Segmenter  # Use ONNX models (requires onnxruntime)

iman.sad_torch_mfcc_speaker
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Initializer**:

  .. code-block:: python

      seg = Segmenter(batch_size, vad_type=['sad'|'vad'], sr=8000, model_path="c:\\sad_model_pytorch.pth", max_time=120, tq=1, ffmpeg_path='c:\\ffmpeg.exe', device='cuda', pad=False)

- ``mfcc, len(sec) = seg(fname)``: Process audio file, MFCC padded to ``max_time`` if ``pad=True``.

iman.sad_tf_mlp_speaker
~~~~~~~~~~~~~~~~~~~~~~~

- **Initializer**:

  .. code-block:: python

      seg = Segmenter(batch_size, vad_type=['sad'|'vad'], sr=8000, model_path="sad_tf_mlp.h5", max_time=120, tq=1, ffmpeg_path='c:\\ffmpeg.exe', device='cuda', pad=False)

- ``mfcc, len(sec) = seg(fname)``: Process audio file, MFCC padded to ``max_time`` if ``pad=True``.

iman.Report
~~~~~~~~~~~

- **Initializer**:

  .. code-block:: python

      r = Report.rep(log_dir=None)

- ``WS(_type, _name, value, itr)``: Add scalar to TensorBoard.
- ``WT(_type, _name, _str, itr)``: Add text to TensorBoard.
- ``WG(pytorch_model, example_input)``: Add graph to TensorBoard.
- ``WI(_type, _name, images, itr)``: Add image to TensorBoard.

iman.par
~~~~~~~~

- **Parallel Processing**:

  .. code-block:: python

      if __name__ == '__main__':
          res = par.par(files, func, worker=4, args=[])  # func defined as: def func(fname, _args): ...

iman.Image
~~~~~~~~~~

- ``Image.convert(fname_pattern, ext='jpg', ofolder=None, w=-1, h=-1, level=100, worker=4, ffmpeg_path='c:\\ffmpeg.exe')``: Convert images to specified format.
- ``Image.resize(fname_pattern, ext='jpg', ofolder=None, w=2, h=2, worker=4, ffmpeg_path='c:\\ffmpeg.exe')``: Resize images to 1/w and 1/h.

iman.Boors
~~~~~~~~~~

- ``Boors.get(sahm)``: Get stock information.

iman.Text
~~~~~~~~~

- **Initializer**:

  .. code-block:: python

      norm = Text.normal("c:\\Replace_List.txt")

- ``norm.rep(str)``: Replace text based on normalization rules.
- ``norm.from_file(filename, file_out=None)``: Normalize text from a file.

iman.num2fa
~~~~~~~~~~~

- ``words(number)``: Convert number to Persian words.

iman.Rar
~~~~~~~~

- ``rar(fname, out="", rar_path=r"C:\\Program Files\\WinRAR\\winrar.exe")``: Create RAR archive.
- ``zip(fname, out="", rar_path=r"C:\\Program Files\\WinRAR\\winrar.exe")``: Create ZIP archive.
- ``unrar(fname, out="", rar_path=r"C:\\Program Files\\WinRAR\\winrar.exe")``: Extract RAR archive.
- ``unzip(fname, out="", rar_path=r"C:\\Program Files\\WinRAR\\winrar.exe")``: Extract ZIP archive.

iman.Enhance
~~~~~~~~~~~~

- ``Enhance.Dereverb(pattern, out_fol, sr=16000, batchsize=16, device="cuda", model_path=r"C:\\UVR-DeEcho-DeReverb.pth")``: Dereverberate audio files.
- ``Enhance.Denoise(pattern, out_fol, sr=16000, batchsize=16, device="cuda", model_path=r"C:\\UVR-DeNoise-Lite.pth")``: Denoise audio files.

iman.tf
~~~~~~~

- ``flops(model)``: Get FLOPs of a TensorFlow model.
- ``param(model)``: Get parameter count of a TensorFlow model.
- ``paramp(model)``: Get parameter count and print model layers.
- ``gpu()``: Return True if GPU is available.
- ``gpun()``: Return number of GPUs.
- ``limit()``: Limit GPU memory allocation for TensorFlow models.

iman.torch
~~~~~~~~~~

- ``param(model)``: Get parameter and trainable count of a PyTorch model.
- ``paramp(model)``: Get parameter count and print model layers.
- ``layers(model)``: Get layers of a PyTorch model.
- ``gpu()``: Return True if GPU is available.
- ``gpun()``: Return number of GPUs.

iman.yt
~~~~~~~

- ``dl(url)``: Download a YouTube video.
- ``list_formats(url)``: List available formats for a YouTube link.

iman.svad
~~~~~~~~~

- ``segments, wav = svad(filename, sampling_rate=16000, min_speech_duration_ms=250, max_speech_duration_s=float('inf'), min_silence_duration_ms=100)``: Run fast speech activity detection and return speech segments.

Dependencies
------------

The ``iman`` package requires the following:

- **Python Packages**: ``numpy``, ``torch``, ``tensorflow``, ``speechbrain``, ``librosa``, ``matplotlib``, ``pandas``, ``onnxruntime`` (for ONNX models).
- **External Tools**: ``ffmpeg``, ``ffprobe``, ``WinRAR`` (for RAR/ZIP operations).
- **Optional**: Pre-trained models (e.g., for VAD, x-vector, dereverberation) specified in function arguments.

Check the package's ``requirements.txt`` for specific versions.

Documentation
-------------

For detailed usage, refer to the source code or use the built-in help system:

.. code-block:: python

    from iman import examples
    examples.help("Audio")  # Get help on the Audio module

Contributing
------------

Contributions are welcome! Submit bug reports, feature requests, or pull requests via the project's GitHub repository (if available). Follow contribution guidelines and include tests for new features.

License
-------

``iman`` is licensed under the MIT License (assumed). See the LICENSE file for details.

Contact
-------

For support, contact the maintainers via the project's GitHub page or email (if provided).

.. note::

    Some functions require external tools (e.g., ``ffmpeg``, ``WinRAR``) or pre-trained models. Ensure these are configured correctly. Paths like ``c:\\ffmpeg.exe`` are Windows-specific; adjust for other operating systems.
