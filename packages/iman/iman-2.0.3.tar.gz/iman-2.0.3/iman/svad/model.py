from .utils_vad import init_jit_model, OnnxWrapper
import torch
torch.set_num_threads(1)
import os


def load_silero_vad(onnx=False, opset_version=16):
    available_ops = [16]
    if onnx and opset_version not in available_ops:
        raise Exception(f'Available ONNX opset_version: {available_ops}')

    if onnx:
        if opset_version == 16:
            model_name = 'silero_vad.onnx'
        else:
            model_name = f'silero_vad_16k_op{opset_version}.onnx'
    else:
        model_name = 'silero_vad.jit'
        
        
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, "data")
    model_file_path = os.path.join(data_dir, model_name)
    
    if not os.path.exists(model_file_path):
        raise FileNotFoundError(f"Model file not found: {model_file_path}")

    if onnx:
        model = OnnxWrapper(str(model_file_path), force_onnx_cpu=True)
    else:
        model = init_jit_model(model_file_path)

    return model
