import os
import shutil
from datetime import datetime

def archive_pdf(file_path, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Get the base name of the file
    file_name = os.path.basename(file_path)
    
    # Create a timestamped version of the file name to avoid overwriting
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archived_file_name = f"{timestamp}_{file_name}"
    
    # Construct the full path for the archived file
    archived_file_path = os.path.join(archive_dir, archived_file_name)
    
    # Move the file to the archive directory
    shutil.move(file_path, archived_file_path)
    print(f"Archived {file_path} to {archived_file_path}")

# Example usage
if __name__ == "__main__":
    archive_pdf('old_document.pdf')