# installer-ml

A simple Python utility for **auto-installing and importing** common Data Science / Machine Learning libraries.  
It helps you avoid `ModuleNotFoundError` by checking, installing (via pip), and importing automatically with aliases like `np`, `pd`, `plt`, `sns`, etc.

---

## 🚀 Features

- Auto-install missing packages using `pip`.
- Support for **common ML/DL/NLP/CV libraries** (scikit-learn, PyTorch, TensorFlow, XGBoost, LightGBM, Transformers, etc.).
- Automatic **alias assignment** (`np`, `pd`, `plt`, `sns`, `tf`, `torch`, …).
- Multiple installation modes:
  - **Silent** (`quiet=True`) → no logs at all.
  - **Semi-silent** (`quiet="semi"`) → minimal logs (default).
  - **Verbose** (`quiet=False`) → full pip logs.
- Import one, many, or all libraries (`"*"`).
- Mapping `import` name ↔ pip package name (e.g., `cv2 ↔ opencv-python`, `PIL ↔ pillow`).
- Display version after import.

---

## 📦 Installation

Clone or copy the file `installer_ml.py` into your project.  
(If you later publish it to PyPI, you can install via `pip install installer-ml`).

---

## 🔑 Usage

### 1. Import a single library
```python
from installer_ml import import_libs

import_libs("pandas")
print(pd.DataFrame({"a":[1,2,3]}))
```

---

### 2. Import multiple libraries
```python
from installer_ml import import_libs

import_libs(["numpy", "pandas", "matplotlib"])

print(np.arange(5))
print(pd.DataFrame({"x":[1,2,3]}))
plt.plot([1,2,3], [2,4,6])
plt.show()
```

---

### 3. Import all supported libraries
```python
from installer_ml import import_libs

import_libs("*")
```

---

### 4. Control logging
```python
# Fully silent (no logs, no print)
import_libs(["numpy", "pandas"], True)

# Semi-silent (minimal messages, default)
import_libs(["numpy", "pandas"], "semi")

# Full logs
import_libs(["numpy", "pandas"], False)
```

---

## 📚 Supported Libraries & Aliases

| Library               | Alias  |
|-----------------------|--------|
| numpy                 | np     |
| pandas                | pd     |
| matplotlib (pyplot)   | plt    |
| seaborn               | sns    |
| scikit-learn          | sklearn|
| xgboost               | xgb    |
| lightgbm              | lgb    |
| catboost              | cb     |
| torch                 | torch  |
| torchvision           | tv     |
| torchaudio            | ta     |
| tensorflow            | tf     |
| keras                 | keras  |
| transformers          | trf    |
| sentence-transformers | stf    |
| spacy                 | spacy  |
| nltk                  | nltk   |
| gensim                | gs     |
| cv2 (OpenCV)          | cv2    |
| pillow (PIL)          | pil    |
| imageio               | imio   |
| pyspark               | spark  |
| pyarrow               | pa     |
| tqdm                  | tqdm   |
| joblib                | joblib |
| h5py                  | h5     |
| scipy                 | sp     |
| statsmodels           | sm     |

---

## ⚙️ Example with all aliases

```python
from installer_ml import import_libs

import_libs("*")

print(np.arange(5))
print(pd.DataFrame({"x":[1,2,3]}))
plt.plot([1,2,3], [2,4,6])
plt.show()

print(tf.__version__)    # tensorflow
print(torch.__version__) # pytorch
print(trf.__version__)   # transformers
```

---

## 📌 License
MIT License. Free to use and modify.
