from pathlib import Path
from .utils import IMAGE_EXTS, DOC_EXTS, VIDEO_EXTS, PDF_EXTS

class FileHandler:
    def __init__(self, root):
        self.root = Path(root)

    def scan_files(self):
        for p in self.root.rglob("*"):
            if p.is_file():
                yield p

    def classify(self, path):
        ext = path.suffix.lower()
        if ext in IMAGE_EXTS:
            return "Images"
        if ext in DOC_EXTS:
            return "Documents"
        if ext in VIDEO_EXTS:
            return "Videos"
        if ext in PDF_EXTS:
            return "PDFs"
        return "Others"
