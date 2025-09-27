import hashlib
from pathlib import Path

try:
    from PIL import Image
    import imagehash
    HAVE_IMAGEHASH = True
except Exception:
    HAVE_IMAGEHASH = False

class DuplicateDetector:
    def __init__(self, use_ml=False, sim_threshold=5):
        self.hash_map = {}   # sha256 -> first_path
        self.use_ml = use_ml and HAVE_IMAGEHASH
        self.sim_threshold = sim_threshold
        self.image_hashes = {}  # path -> phash

    def sha256(self, path: Path):
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def check(self, path: Path):
        file_hash = self.sha256(path)
        if file_hash in self.hash_map:
            return True, self.hash_map[file_hash], "exact", file_hash
        self.hash_map[file_hash] = path
        # optional image similarity using perceptual hash
        if self.use_ml and path.suffix.lower() in {'.jpg','.jpeg','.png','.bmp','.gif'}:
            try:
                ph = imagehash.phash(Image.open(path))
                for other_path, other_ph in self.image_hashes.items():
                    if abs(ph - other_ph) <= self.sim_threshold:
                        return True, other_path, "phash", file_hash
                self.image_hashes[path] = ph
            except Exception:
                pass
        return False, None, None, file_hash
