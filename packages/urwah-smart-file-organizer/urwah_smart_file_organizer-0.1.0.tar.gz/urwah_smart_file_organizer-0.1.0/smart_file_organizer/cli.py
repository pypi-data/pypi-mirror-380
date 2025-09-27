import argparse
from pathlib import Path
from .file_handler import FileHandler
from .organizer import Organizer
from .duplicate_detector import DuplicateDetector
from .logger import Logger
from .classifier import FileClassifier   # ✅ import classifier

def main():
    parser = argparse.ArgumentParser(prog="smart-file-organizer")
    parser.add_argument("--path", required=True, help="Directory to organize")
    parser.add_argument("--check-duplicates", action="store_true", help="Detect duplicate files")
    parser.add_argument("--ml-similarity", action="store_true", help="Use perceptual image hashing (optional)")
    parser.add_argument("--log-path", default=None, help="Folder to save logs (default: PATH)")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually move files")
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists() or not root.is_dir():
        print("❌ ERROR: path does not exist or is not a directory:", root)
        return

    fh = FileHandler(root)
    dup = DuplicateDetector(use_ml=args.ml_similarity)
    org = Organizer(root, dry_run=args.dry_run)
    logger = Logger()
    classifier = FileClassifier()   # ✅ use classifier

    files = list(fh.scan_files())
    if not files:
        print("⚠️ No files found in:", root)
        return

    for f in files:
        category = classifier.classify(f)   # ✅ proper classification
        if args.check_duplicates:
            is_dup, other, reason, file_hash = dup.check(f)
        else:
            is_dup, other, reason, file_hash = (False, None, None, None)

        if is_dup:
            dest = org.move_to_duplicates(f)
            logger.add(f, dest, "duplicate", reason=reason, file_hash=file_hash)
            print(f"[DUPLICATE] {f} -> {dest} ({reason})")
        else:
            dest = org.move_file(f, category)
            logger.add(f, dest, "moved", reason=category, file_hash=file_hash)
            print(f"[MOVED] {f} -> {dest}")

    log_folder = Path(args.log_path) if args.log_path else root
    report = logger.save(log_folder, name="smart_file_organizer_report.csv")
    print("✅ Report saved to:", report)


if __name__ == "__main__":
    main()
