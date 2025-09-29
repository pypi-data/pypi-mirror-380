import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.cuda")

try:
    import pynvml as nv  # provided by nvidia-ml-py
    NVML_OK = True
except Exception:
    nv = None
    NVML_OK = False

def _safe(fn, *a, **kw):
    try:
        return fn(*a, **kw)
    except Exception:
        return None

def list_gpus():
    if not NVML_OK:
        return []
    try:
        nv.nvmlInit()
    except Exception:
        return []
    count = _safe(nv.nvmlDeviceGetCount) or 0
    out = []
    for i in range(count):
        h = _safe(nv.nvmlDeviceGetHandleByIndex, i)
        if not h:
            continue
        name = _safe(nv.nvmlDeviceGetName, h)
        if isinstance(name, (bytes, bytearray)): name = name.decode()
        mem = _safe(nv.nvmlDeviceGetMemoryInfo, h)
        temp = _safe(nv.nvmlDeviceGetTemperature, h, nv.NVML_TEMPERATURE_GPU)
        power_mw = _safe(nv.nvmlDeviceGetPowerUsage, h)
        util = _safe(nv.nvmlDeviceGetUtilizationRates, h)
        uuid = _safe(nv.nvmlDeviceGetUUID, h)
        if isinstance(uuid, (bytes, bytearray)): uuid = uuid.decode()
        out.append({
            "index": i,
            "name": name,
            "memory_total_gb": round((mem.total if mem else 0)/(1024**3), 2),
            "memory_used_gb": round((mem.used if mem else 0)/(1024**3), 2),
            "temperature_c": temp,
            "power_w": round(power_mw/1000.0, 1) if power_mw else None,
            "gpu_util": util.gpu if util else None,
            "mem_util": util.memory if util else None,
            "uuid": uuid,
        })
    return out

def sample_gpu(index: int = 0):
    if not NVML_OK:
        return {}
    try:
        nv.nvmlInit()
        h = nv.nvmlDeviceGetHandleByIndex(index)
        mem = _safe(nv.nvmlDeviceGetMemoryInfo, h)
        temp = _safe(nv.nvmlDeviceGetTemperature, h, nv.NVML_TEMPERATURE_GPU)
        power_mw = _safe(nv.nvmlDeviceGetPowerUsage, h)
        util = _safe(nv.nvmlDeviceGetUtilizationRates, h)
        return {
            "memory_used_gb": round((mem.used if mem else 0)/(1024**3), 2),
            "temperature_c": temp,
            "power_w": round(power_mw/1000.0, 1) if power_mw else None,
            "gpu_util": util.gpu if util else None,
            "mem_util": util.memory if util else None,
        }
    except Exception:
        return {}
