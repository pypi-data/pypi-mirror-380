class FileClassifier:
    CATEGORIES = {
        "Documents": {".pdf", ".docx", ".txt", ".xls", ".xlsx"},
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp"},
        "Audio": {".mp3", ".wav", ".aac"},
        "Video": {".mp4", ".avi", ".mov", ".mkv"},
        "Archives": {".zip", ".rar", ".7z"},
        "Code": {".py", ".js", ".html", ".css", ".java", ".cpp"},
    }

    def classify(self, path):
        ext = path.suffix.lower()
        for cat, exts in self.CATEGORIES.items():
            if ext in exts:
                return cat
        return "Others"
