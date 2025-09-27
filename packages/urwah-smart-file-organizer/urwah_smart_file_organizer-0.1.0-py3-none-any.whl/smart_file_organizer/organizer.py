from pathlib import Path
import shutil

class Organizer:
    def __init__(self, base_path, dry_run=False):
        self.base = Path(base_path)
        self.organized_root = self.base / "Organized"
        self.duplicates_root = self.base / "Duplicates"
        self.dry_run = dry_run

    def move_file(self, src_path, category):
        dest_dir = self.organized_root / category
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src_path.name
        i = 1
        while dest.exists():
            dest = dest_dir / f"{src_path.stem}_{i}{src_path.suffix}"
            i += 1
        if not self.dry_run:
            shutil.move(str(src_path), str(dest))
        return dest

    def move_to_duplicates(self, src_path):
        self.duplicates_root.mkdir(parents=True, exist_ok=True)
        dest = self.duplicates_root / src_path.name
        i = 1
        while dest.exists():
            dest = self.duplicates_root / f"{src_path.stem}_{i}{src_path.suffix}"
            i += 1
        if not self.dry_run:
            shutil.move(str(src_path), str(dest))
        return dest
