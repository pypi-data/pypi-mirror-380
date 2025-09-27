from pathlib import Path
import shutil
from smart_file_organizer.file_handler import FileHandler
from smart_file_organizer.duplicate_detector import DuplicateDetector
from smart_file_organizer.organizer import Organizer

def test_scan_and_classify(tmp_path):
    p = tmp_path / "a.jpg"
    p.write_bytes(b"dummy")
    fh = FileHandler(tmp_path)
    files = list(fh.scan_files())
    assert len(files) == 1
    assert fh.classify(p) == "Images"

def test_hash_duplicates(tmp_path):
    a = tmp_path / "f1.txt"
    b = tmp_path / "f2.txt"
    a.write_bytes(b"hello")
    b.write_bytes(b"hello")
    dd = DuplicateDetector()
    is_dup1, *_ = dd.check(a)
    assert is_dup1 is False
    is_dup2, other, *_ = dd.check(b)
    assert is_dup2 is True
    assert other == a
