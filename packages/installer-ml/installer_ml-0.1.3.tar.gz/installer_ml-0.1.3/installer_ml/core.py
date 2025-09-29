import importlib
import subprocess
import sys

# =========================
# 1. Mapping import ↔ pip
# =========================
IMPORT_TO_PIP = {
    # Core data science
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",

    # Machine Learning
    "sklearn": "scikit-learn",
    "xgboost": "xgboost",
    "lightgbm": "lightgbm",
    "catboost": "catboost",

    # Deep Learning
    "torch": "torch",
    "torchvision": "torchvision",
    "torchaudio": "torchaudio",
    "tensorflow": "tensorflow",
    "keras": "keras",

    # NLP
    "transformers": "transformers",
    "sentence_transformers": "sentence-transformers",
    "spacy": "spacy",
    "nltk": "nltk",
    "gensim": "gensim",

    # Image / CV
    "cv2": "opencv-python",
    "PIL": "pillow",
    "imageio": "imageio",

    # Spark / Big Data
    "pyspark": "pyspark",
    "pyarrow": "pyarrow",

    # Utilities
    "tqdm": "tqdm",
    "joblib": "joblib",
    "h5py": "h5py",
    "scipy": "scipy",
    "statsmodels": "statsmodels",
}

# =========================
# 2. Alias phổ biến
# =========================
IMPORT_ALIAS = {
    "numpy": "np",
    "pandas": "pd",
    "matplotlib": "plt",   # matplotlib.pyplot as plt
    "seaborn": "sns",
    "sklearn": "sklearn",
    "xgboost": "xgb",
    "lightgbm": "lgb",
    "catboost": "cb",
    "torch": "torch",
    "tensorflow": "tf",
}

# =========================
# 3. Hàm cài đặt & import 1 thư viện
# =========================
def install_and_import(import_name: str, quiet="semi"):
    """
    Kiểm tra và cài đặt thư viện Python.
    
    Args:
        import_name (str): tên module khi import (ví dụ 'sklearn', 'pandas')
        quiet (bool|str): 
            - True   : cài đặt im lặng hoàn toàn
            - False  : cài đặt đầy đủ log pip
            - "semi" : cài đặt bán im lặng (ẩn warning nhỏ, giữ lại tiến trình) [mặc định]
    
    Returns:
        module: module đã import thành công
    """
    package = IMPORT_TO_PIP.get(import_name, import_name)

    try:
        return importlib.import_module(import_name)
    except ImportError:
        if quiet is True:
            print(f"{import_name} chưa có, đang cài (im lặng)...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-q", package],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        elif quiet == "semi":
            print(f"{import_name} chưa có, đang cài (bán im lặng)...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-q", package]
            )
        else:  # quiet=False
            print(f"{import_name} chưa có, đang cài (đầy đủ log)...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        return importlib.import_module(import_name)

# =========================
# 4. Hàm cài đặt & import nhiều thư viện
# =========================
def bulk_install_and_import(import_names, quiet="semi", use_alias=True):
    """
    Cài đặt & import nhiều thư viện một lúc
    
    Args:
        import_names (list[str]): danh sách tên import
        quiet (bool|str): chế độ cài đặt (True, False, "semi") [mặc định: "semi"]
        use_alias (bool): nếu True thì gán alias quen thuộc (np, pd, plt...)
    
    Returns:
        dict: {alias hoặc import_name: module}
    """
    modules = {}
    for name in import_names:
        mod = install_and_import(name, quiet=quiet)

        # Nếu có alias quen thuộc
        if use_alias and name in IMPORT_ALIAS:
            if name == "matplotlib":
                # Trường hợp đặc biệt: import matplotlib.pyplot as plt
                pyplot = importlib.import_module("matplotlib.pyplot")
                modules[IMPORT_ALIAS[name]] = pyplot
            else:
                modules[IMPORT_ALIAS[name]] = mod
        else:
            modules[name] = mod
    return modules

# =========================
# 5. Hàm kiểm tra version
# =========================
def show_versions(modules: dict):
    """
    In ra version của các module đã import
    """
    print("\n=== Versions ===")
    for k, m in modules.items():
        ver = getattr(m, "__version__", "N/A")
        print(f"{k}: {ver}")
