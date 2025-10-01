# hyperxar

Python3 Modul zum Kopieren, Komprimieren, Extrahieren und ISO-Erstellen mit Fortschrittsanzeige.

## Installation

```bash
pip install git+https://github.com/deinusername/hyperxar.git


from hyperxar import copy_file, compress_zip, compress_tar, compress_7z, create_iso, extract_archive

copy_file("source.txt", "target.txt")
compress_zip("my_folder", "archive.zip")
compress_tar("my_folder", "archive.tar.gz")
compress_7z("my_folder", "archive.7z")
create_iso("my_folder", "image.iso")
extract_archive("archive.zip", "unzipped_folder")
````