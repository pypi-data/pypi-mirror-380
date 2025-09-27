import pandas as pd
from pathlib import Path

class Logger:
    def __init__(self):
        self.rows = []

    def add(self, original, destination, action, reason=None, file_hash=None):
        self.rows.append({
            "original": str(original),
            "destination": str(destination) if destination else "",
            "action": action,
            "reason": reason or "",
            "hash": file_hash or ""
        })

    def save(self, folder, name="report.csv", fmt="csv"):
        folder = Path(folder)
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / name
        df = pd.DataFrame(self.rows)
        if fmt == "csv":
            df.to_csv(path, index=False)
        else:
            df.to_json(path, orient="records")
        return path
