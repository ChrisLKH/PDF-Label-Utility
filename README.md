# 📦 PDF Label Utility

A simple Python utility for manipulating PDF labels: rotate pages, add text overlays, and merge multiple labels into one file. Ideal for generating printable 4x6 labels for logistics, inventory, or packaging workflows.

---

## ✨ Features

- 🔄 **Rotate PDF** pages by any angle (e.g., 180° for upside-down printing)
- 📝 **Add custom text** to any position on a 4x6 label
- 📚 **Merge multiple labels** into one clean, printable PDF

---

## 📂 File Structure

```
pdf-label-utils/
│
├── pdf_label_utils.py       # Main utility functions
├── example_usage.py         # Example of how to use the utilities
├── requirements.txt         # Required Python packages
└── README.md                # This file
```

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/pdf-label-utils.git
cd pdf-label-utils
pip install -r requirements.txt
```

**Dependencies:**
- `PyPDF2`
- `reportlab`

Install manually if needed:

```bash
pip install PyPDF2 reportlab
```

---

## 🚀 Usage Examples

### Rotate a PDF by 180 degrees:
```python
from pdf_label_utils import rotate_pdf
rotate_pdf("label.pdf", "label_rotated.pdf", 180)
```

### Add text to a PDF label:
```python
from pdf_label_utils import add_text_to_label
add_text_to_label("label.pdf", "label_text.pdf", "Order #12345", 50, 150)
```

### Merge multiple label PDFs:
```python
from pdf_label_utils import merge_labels
merge_labels(["label1.pdf", "label2.pdf"], "combined_labels.pdf")
```

---

## 📏 Label Size

- All operations assume a 4x6 inch label (common in thermal printing).
- Coordinates `(x, y)` in `add_text_to_label()` are in **points** (1 inch = 72 points).

---


## 📄 License

MIT License

---
