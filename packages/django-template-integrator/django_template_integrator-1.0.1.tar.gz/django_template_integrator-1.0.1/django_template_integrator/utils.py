"""Helper utilities for file operations and path handling."""

import os
import shutil
from pathlib import Path


def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    Path(directory).mkdir(parents=True, exist_ok=True)


def is_asset_file(filepath):
    """Check if file is a static asset (CSS, JS, images, fonts)."""
    asset_extensions = {
        '.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico',
        '.woff', '.woff2', '.ttf', '.eot', '.otf', '.webp', '.bmp'
    }
    return Path(filepath).suffix.lower() in asset_extensions


def is_html_file(filepath):
    """Check if file is an HTML file."""
    return Path(filepath).suffix.lower() in {'.html', '.htm'}


def get_asset_type(filepath):
    """Determine asset type (css, js, img, fonts) from file path or extension."""
    path_lower = str(filepath).lower()
    ext = Path(filepath).suffix.lower()
    
    if '/css/' in path_lower or ext == '.css':
        return 'css'
    elif '/js/' in path_lower or '/javascript/' in path_lower or ext == '.js':
        return 'js'
    elif ext in {'.woff', '.woff2', '.ttf', '.eot', '.otf'}:
        return 'fonts'
    elif ext in {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp', '.bmp'}:
        return 'img'
    else:
        return 'assets'


def copy_file_to_static(src_file, django_project_path, relative_path):
    """Copy a file to the appropriate location in Django static directory."""
    asset_type = get_asset_type(src_file)
    
    static_dir = Path(django_project_path) / 'static' / asset_type
    ensure_dir(static_dir)
    
    filename = Path(src_file).name
    dest_file = static_dir / filename
    
    shutil.copy2(src_file, dest_file)
    
    return f'{asset_type}/{filename}'


def clean_temp_dir(temp_dir):
    """Remove temporary extraction directory."""
    if Path(temp_dir).exists():
        shutil.rmtree(temp_dir)
