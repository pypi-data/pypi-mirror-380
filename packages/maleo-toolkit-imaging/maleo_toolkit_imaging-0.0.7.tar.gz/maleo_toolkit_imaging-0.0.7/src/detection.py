import hashlib
import random
import numpy as np
import torch
import torch.distributed as dist


def set_seed(seed: int):
    """Set random seed untuk reproducibility (Python, NumPy, Torch, CUDA)."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def is_main_process():
    """Cek apakah rank = 0 (utama) pada DDP, atau non-DDP (single)."""
    return (
        (not dist.is_available()) or (not dist.is_initialized()) or dist.get_rank() == 0
    )


def ddp_print(*args, **kwargs):
    """Print hanya di rank utama."""
    if is_main_process():
        print(*args, **kwargs)


def gather_from_all(obj):
    """
    Kumpulkan objek Python dari semua rank ke rank 0.
    Return list semua rank.
    """
    if not dist.is_initialized():
        return [obj]
    gather_list = [None for _ in range(dist.get_world_size())]
    dist.all_gather_object(gather_list, obj)
    return gather_list


def get_sha256(filepath: str) -> str:
    """Generate SHA256 checksum dari file (misal buat cache)."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def to_device(data, device: torch.device):
    """Pindahkan dict/list/tuple/tensor ke device tertentu."""
    if isinstance(data, torch.Tensor):
        return data.to(device)
    elif isinstance(data, dict):
        return {k: to_device(v, device) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_device(x, device) for x in data]
    elif isinstance(data, tuple):
        return tuple(to_device(x, device) for x in data)
    return data
