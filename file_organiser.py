import os
import shutil

# --- Configure this ---
FOLDER_TO_ORGANISE = r"C:\Users\korisnik\Downloads"  # Change this to your folder

# --- File type categories ---
FILE_TYPES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents":  [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":      [".mp3", ".wav", ".aac"],
    "Archives":   [".zip", ".rar", ".tar", ".gz"],
    "Scripts":    [".py", ".js", ".html", ".css"],
}

def organise_folder(folder):
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return

    moved = 0

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        # Skip folders
        if os.path.isdir(filepath):
            continue

        ext = os.path.splitext(filename)[1].lower()
        destination_folder = None

        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                destination_folder = os.path.join(folder, category)
                break

        if not destination_folder:
            destination_folder = os.path.join(folder, "Other")

        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(filepath, os.path.join(destination_folder, filename))
        print(f"Moved: {filename} → {os.path.basename(destination_folder)}")
        moved += 1

    print(f"\nDone! {moved} files organised.")

organise_folder(FOLDER_TO_ORGANISE)
