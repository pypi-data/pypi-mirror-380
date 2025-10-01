import shutil
from pathlib import Path
from tqdm import tqdm
import zipfile
import tarfile
import py7zr
import subprocess

# ----------------------------
# Dateien kopieren
# ----------------------------
def copy_file(src: Path, dst: Path):
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    total_size = src.stat().st_size
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst, tqdm(total=total_size, unit='B', unit_scale=True, desc=f'Copy {src.name}') as pbar:
        while buf := fsrc.read(1024*1024):
            fdst.write(buf)
            pbar.update(len(buf))

# ----------------------------
# Komprimieren
# ----------------------------
def compress_zip(src: Path, dst: Path):
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_file():
        with zipfile.ZipFile(dst, 'w') as zipf:
            zipf.write(src, arcname=src.name)
    else:
        with zipfile.ZipFile(dst, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            for file in tqdm(list(src.rglob('*')), desc=f'Compressing {src.name}'):
                zipf.write(file, arcname=file.relative_to(src))

def compress_tar(src: Path, dst: Path):
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(dst, "w:gz") as tar:
        for file in tqdm(list(src.rglob('*')), desc=f'Compressing {src.name}'):
            tar.add(file, arcname=file.relative_to(src))

def compress_7z(src: Path, dst: Path):
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with py7zr.SevenZipFile(dst, 'w') as archive:
        files = list(src.rglob('*')) if src.is_dir() else [src]
        for file in tqdm(files, desc=f'Compressing {src.name}'):
            archive.write(file, arcname=file.relative_to(src) if src.is_dir() else file.name)

# ----------------------------
# ISO erstellen
# ----------------------------
def create_iso(src: Path, dst: Path):
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["genisoimage", "-o", str(dst), "-J", "-R", str(src)]
    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        print(f"Fehler beim Erstellen des ISO-Images: {e}")

# ----------------------------
# Archiv extrahieren
# ----------------------------
def extract_archive(src: Path, dst: Path):
    src, dst = Path(src), Path(dst)
    dst.mkdir(parents=True, exist_ok=True)
    suffix = src.suffix.lower()

    if suffix == '.zip':
        with zipfile.ZipFile(src, 'r') as zipf:
            for file in tqdm(zipf.namelist(), desc=f'Extracting {src.name}'):
                zipf.extract(file, path=dst)
    elif suffix in ['.tar', '.gz', '.tgz', '.tar.gz']:
        with tarfile.open(src, 'r:*') as tar:
            for member in tqdm(tar.getmembers(), desc=f'Extracting {src.name}'):
                tar.extract(member, path=dst)
    elif suffix == '.7z':
        with py7zr.SevenZipFile(src, 'r') as archive:
            allfiles = archive.getnames()
            for _ in tqdm(allfiles, desc=f'Extracting {src.name}'):
                archive.extract(path=dst)
    else:
        raise ValueError(f"Archivtyp {suffix} wird nicht unterstützt.")


# from hyperxar import extract_archive

# # ZIP extrahieren
# extract_archive("archive.zip", "unzipped_folder")

# # TAR.GZ extrahieren
# extract_archive("archive.tar.gz", "untarred_folder")

# # 7z extrahieren
# extract_archive("archive.7z", "7z_unpacked")
