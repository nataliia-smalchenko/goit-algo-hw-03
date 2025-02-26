from pathlib import Path
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Коріювання файлів із сортуванням за типом.")
    parser.add_argument("source_dir", help="Шлях до вхідної папки")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Шлях до папки призначення (за замовчуванням: dist)")
    parser.add_argument("logging", nargs="?", default=False, help="Логування скопійованих файлів (за замовчуванням: False)")
    return parser.parse_args()

def copy_files_recursively(source_path: Path, destination_path: Path, logging=False):
    if source_path.is_dir():
        for child in source_path.iterdir():
            copy_files_recursively(child, destination_path)
    elif source_path.is_file():
        file_extension = source_path.suffix[1:]
        target_dir = destination_path / file_extension

        if not target_dir.exists():
            target_dir.mkdir(parents=True)

        target_path = target_dir / source_path.name
        try:
            shutil.copy(source_path, target_path)
            if logging:
                print(f"Файл {source_path.name} успішно скопійовано до {target_path}")
        except PermissionError:
            print(f"Помилка доступу до каталогу: {source_path}")
        except OSError as e:
            print(f"Помилка копіювання файлу {source_path}: {e}")

args = parse_arguments()
source_dir = Path(args.source_dir)
destination_dir = Path(args.destination_dir)

if not source_dir.exists():
    print(f"Вхідна папка {source_dir} не існує")
else:
    copy_files_recursively(source_dir, destination_dir)