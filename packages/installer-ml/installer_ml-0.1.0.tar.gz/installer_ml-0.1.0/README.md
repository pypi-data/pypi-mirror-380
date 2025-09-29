# installer-ml

[![PyPI version](https://badge.fury.io/py/installer-ml.svg)](https://pypi.org/project/installer-ml/)
[![Python Versions](https://img.shields.io/pypi/pyversions/installer-ml.svg)](https://pypi.org/project/installer-ml/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`installer-ml` là một tiện ích nhỏ giúp **tự động kiểm tra, cài đặt và import các thư viện Python** thường dùng trong **Machine Learning / Data Science / Deep Learning**.  
Bạn chỉ cần gọi một hàm duy nhất, không cần quan tâm tên pip khác tên import.  

---

## 🚀 Cài đặt

```bash
pip install installer-ml
```

---

## 🛠️ Tính năng

- Kiểm tra thư viện đã có chưa, nếu chưa thì tự động `pip install`.
- Mapping sẵn các thư viện phổ biến:  
  - `scikit-learn` → `sklearn`  
  - `pillow` → `PIL`  
  - `opencv-python` → `cv2`  
- 3 chế độ cài đặt:
  - `quiet=True`  → Im lặng hoàn toàn  
  - `quiet=False` → Hiện log pip đầy đủ  
  - `quiet="semi"` → Bán im lặng (chỉ hiện tiến trình, ẩn warning nhỏ) *(mặc định)*  
- Cài nhiều thư viện một lúc (`bulk_install_and_import`)  
- Hiển thị phiên bản thư viện (`show_versions`)  

---

## 📦 Cách dùng

### Import 1 thư viện

```python
from installer import install_and_import

# Import pandas (mặc định semi)
pd = install_and_import("pandas")

# Import numpy (im lặng hoàn toàn)
np = install_and_import("numpy", quiet=True)

# Import xgboost (log đầy đủ)
xgb = install_and_import("xgboost", quiet=False)
```

### Import nhiều thư viện cùng lúc

```python
from installer import bulk_install_and_import, show_versions

mods = bulk_install_and_import(["numpy", "pandas", "sklearn", "xgboost"])

np = mods["numpy"]
pd = mods["pandas"]
sklearn = mods["sklearn"]
xgb = mods["xgboost"]

show_versions(mods)
```

---

## 📋 Ví dụ output

```
pandas chưa có, đang cài (bán im lặng)...
numpy: 1.26.4
pandas: 2.2.1
sklearn: 1.4.2
xgboost: 2.1.0
```

---

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 🤝 Đóng góp

1. Fork repo
2. Tạo branch mới (`git checkout -b feature/your-feature`)
3. Commit thay đổi (`git commit -m 'Add some feature'`)
4. Push lên branch (`git push origin feature/your-feature`)
5. Tạo Pull Request
