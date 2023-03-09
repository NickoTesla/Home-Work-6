import os
import shutil
import string
import unicodedata
# Списки розширень файлів
image_exts = ('JPEG', 'PNG', 'JPG', 'SVG')
video_exts = ('AVI', 'MP4', 'MOV', 'MKV')
document_exts = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
music_exts = ('MP3', 'OGG', 'WAV', 'AMR')
archive_exts = ('ZIP', 'GZ', 'TAR')
# Словник зі списками файлів різних типів
file_dict = {
    'images': [],
    'videos': [],
    'documents': [],
    'music': [],
    'archives': []
}
# Список розширень файлів, які вдалось знайти
found_exts = []
# Список невідомих розширень файлів
unknown_exts = []


def normalize(filename):
    """Функція для нормалізації назви файлу"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = unicodedata.normalize(
        'NFKD', filename).encode('ASCII', 'ignore')
    filename = filename.decode('ASCII')
    filename = ''.join(c for c in filename if c in valid_chars)
    return filename


def sort_files(folder):
    """Функція для сортування файлі
