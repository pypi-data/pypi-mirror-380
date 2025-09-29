import importlib
import subprocess
import sys

IMPORT_TO_PIP = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "sklearn": "scikit-learn",
    "xgboost": "xgboost",
    "lightgbm": "lightgbm",
    "catboost": "catboost",
    "torch": "torch",
    "torchvision": "torchvision",
    "torchaudio": "torchaudio",
    "tensorflow": "tensorflow",
    "keras": "keras",
    "transformers": "transformers",
    "sentence_transformers": "sentence-transformers",
    "spacy": "spacy",
    "nltk": "nltk",
    "gensim": "gensim",
    "cv2": "opencv-python",
    "PIL": "pillow",
    "imageio": "imageio",
    "pyspark": "pyspark",
    "pyarrow": "pyarrow",
    "tqdm": "tqdm",
    "joblib": "joblib",
    "h5py": "h5py",
    "scipy": "scipy",
    "statsmodels": "statsmodels"
}

def install_and_import(import_name: str, quiet="semi"):
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
        else:
            print(f"{import_name} chưa có, đang cài (đầy đủ log)...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return importlib.import_module(import_name)

def bulk_install_and_import(import_names, quiet="semi"):
    modules = {}
    for name in import_names:
        modules[name] = install_and_import(name, quiet=quiet)
    return modules

def show_versions(modules: dict):
    print("\n=== Versions ===")
    for k, m in modules.items():
        ver = getattr(m, "__version__", "N/A")
        print(f"{k}: {ver}")
