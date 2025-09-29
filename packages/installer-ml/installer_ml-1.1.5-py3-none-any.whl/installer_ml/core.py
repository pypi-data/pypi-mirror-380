import importlib
import subprocess
import sys
import inspect

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
# 2. Alias
# =========================
IMPORT_ALIAS = {
    # Core
    "numpy": "np",
    "pandas": "pd",
    "matplotlib": "plt",   # matplotlib.pyplot as plt
    "seaborn": "sns",

    # ML / DL
    "sklearn": "sklearn",
    "xgboost": "xgb",
    "lightgbm": "lgb",
    "catboost": "cb",
    "torch": "torch",
    "torchvision": "tv",
    "torchaudio": "ta",
    "tensorflow": "tf",
    "keras": "keras",

    # NLP
    "transformers": "trf",
    "sentence_transformers": "stf",
    "spacy": "spacy",
    "nltk": "nltk",
    "gensim": "gs",

    # CV / Image
    "cv2": "cv2",
    "PIL": "pil",
    "imageio": "imio",

    # Big Data
    "pyspark": "spark",
    "pyarrow": "pa",

    # Utils
    "tqdm": "tqdm",
    "joblib": "joblib",
    "h5py": "h5",
    "scipy": "sp",
    "statsmodels": "sm",
}

# =========================
# 3. Hàm import chính
# =========================
def import_libs(import_names="*", quiet="semi", use_alias=True, inject_globals=True):
    """
    Import multiple libraries, auto-install if missing.

    Args:
        import_names (str|list): 
            - "*"  : import all libraries in IMPORT_TO_PIP
            - list : list of module names
            - str  : single module name
        quiet (bool|str): 
            - True   : fully silent installation
            - False  : full pip logs
            - "semi" : semi-silent (suppress warnings, keep progress) [default]
        use_alias (bool): assign common aliases (np, pd, plt...)
        inject_globals (bool): if True, inject alias/module into caller globals()

    Returns:
        dict: {alias_or_name: module}
    """
    if import_names == "*":
        import_names = list(IMPORT_TO_PIP.keys())
    elif isinstance(import_names, str):
        import_names = [import_names]

    modules = {}
    caller_globals = inspect.currentframe().f_back.f_globals  # lấy scope caller

    for name in import_names:
        package = IMPORT_TO_PIP.get(name, name)

        try:
            mod = importlib.import_module(name)
        except ImportError:
            if quiet is True:
                print(f"{name} not found. Installing silently...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "-q", package],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            elif quiet == "semi":
                print(f"{name} not found. Installing (semi-silent)...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
            else:
                print(f"{name} not found. Installing with full logs...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])

            mod = importlib.import_module(name)

        # Alias hoặc giữ nguyên
        alias = IMPORT_ALIAS.get(name, name) if use_alias else name
        modules[alias] = mod

        # Inject vào scope notebook
        if inject_globals:
            if name == "matplotlib":
                pyplot = importlib.import_module("matplotlib.pyplot")
                caller_globals["plt"] = pyplot
                modules["plt"] = pyplot
            else:
                caller_globals[alias] = mod

        ver = getattr(mod, "__version__", "N/A")
        print(f"Imported: {alias} ({package}) - version {ver}")

    return modules

# =========================
# 4. Hàm kiểm tra version
# =========================
def show_versions(modules: dict):
    """
    Print versions of imported modules
    """
    print("\n=== Versions ===")
    for k, m in modules.items():
        ver = getattr(m, "__version__", "N/A")
        print(f"{k}: {ver}")