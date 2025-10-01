"""Core logic for Django template integration."""

import os
import re
import zipfile
from pathlib import Path
from bs4 import BeautifulSoup
from .utils import (
    ensure_dir, is_asset_file, is_html_file,
    copy_file_to_static, clean_temp_dir
)


class DjangoTemplateIntegrator:
    """Main integrator class that orchestrates the template integration process."""
    
    def __init__(self, zip_path, django_project_path, verbose=True):
        self.zip_path = Path(zip_path)
        self.django_project_path = Path(django_project_path)
        self.temp_dir = Path('tmp_template')
        self.verbose = verbose
        self.asset_mapping = {}
        
    def log(self, message):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(message)
    
    def extract_template(self):
        """Extract ZIP template to temporary directory with security validation.
        
        Note: This implementation blocks absolute paths and path traversal attacks.
        Symlink/hardlink entries are not explicitly rejected in v1.0.
        Only use this tool with trusted frontend template ZIPs.
        """
        self.log(f"📦 Extracting template from {self.zip_path}...")
        
        if not self.zip_path.exists():
            raise FileNotFoundError(f"ZIP file not found: {self.zip_path}")
        
        ensure_dir(self.temp_dir)
        temp_dir_resolved = self.temp_dir.resolve()
        
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            for zip_info in zip_ref.infolist():
                member = zip_info.filename
                member_path = Path(member)
                
                if member_path.is_absolute():
                    raise ValueError(f"Unsafe ZIP: absolute path detected: {member}")
                
                target_path = (temp_dir_resolved / member_path).resolve()
                
                try:
                    target_path.relative_to(temp_dir_resolved)
                except ValueError:
                    raise ValueError(f"Unsafe ZIP: path escape detected: {member}")
                
                zip_ref.extract(zip_info, self.temp_dir)
        
        self.log(f"✅ Template extracted to {self.temp_dir}")
    
    def find_all_files(self, directory):
        """Recursively find all files in a directory."""
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                files.append(Path(root) / filename)
        return files
    
    def move_assets_to_static(self):
        """Move all asset files to Django static directory."""
        self.log("\n📁 Moving assets to static directory...")
        
        all_files = self.find_all_files(self.temp_dir)
        asset_files = [f for f in all_files if is_asset_file(f)]
        
        for asset_file in asset_files:
            relative_path = asset_file.relative_to(self.temp_dir)
            django_static_path = copy_file_to_static(
                asset_file, 
                self.django_project_path, 
                relative_path
            )
            
            original_path_variants = [
                str(relative_path).replace('\\', '/'),
                str(relative_path.as_posix()),
                asset_file.name,
            ]
            
            for variant in original_path_variants:
                self.asset_mapping[variant] = django_static_path
            
            self.log(f"  ✓ Moved: {relative_path} → static/{django_static_path}")
        
        self.log(f"✅ Moved {len(asset_files)} asset files")
    
    def rewrite_html_paths(self, html_content, html_filename):
        """Rewrite asset paths in HTML to Django static template tags."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        tags_attrs = [
            ('link', 'href'),
            ('script', 'src'),
            ('img', 'src'),
            ('source', 'src'),
            ('source', 'srcset'),
            ('video', 'src'),
            ('audio', 'src'),
            ('embed', 'src'),
            ('object', 'data'),
        ]
        
        for tag_name, attr_name in tags_attrs:
            for tag in soup.find_all(tag_name):
                if tag.has_attr(attr_name):
                    original_path = tag[attr_name]
                    
                    if original_path.startswith(('http://', 'https://', '//', '#', 'data:')):
                        continue
                    
                    cleaned_path = original_path.lstrip('./')
                    
                    if cleaned_path.startswith('assets/'):
                        cleaned_path = cleaned_path.replace('assets/', '', 1)
                    
                    filename = Path(cleaned_path).name
                    
                    matched_path = None
                    for orig_path, static_path in self.asset_mapping.items():
                        if Path(orig_path).name == filename:
                            matched_path = static_path
                            break
                    
                    if matched_path:
                        tag[attr_name] = f"{{% static '{matched_path}' %}}"
        
        for tag in soup.find_all(style=True):
            style_content = tag['style']
            style_content = self.rewrite_css_urls(style_content)
            tag['style'] = style_content
        
        for style_tag in soup.find_all('style'):
            if style_tag.string:
                style_tag.string = self.rewrite_css_urls(style_tag.string)
        
        return str(soup)
    
    def rewrite_css_urls(self, css_content):
        """Rewrite url() references in CSS content."""
        def replace_url(match):
            url = match.group(1).strip('\'"')
            
            if url.startswith(('http://', 'https://', '//', 'data:', '#')):
                return match.group(0)
            
            filename = Path(url).name
            
            for orig_path, static_path in self.asset_mapping.items():
                if Path(orig_path).name == filename:
                    return f"url('{{% static '{static_path}' %}}')"
            
            return match.group(0)
        
        return re.sub(r'url\(([^)]+)\)', replace_url, css_content)
    
    def add_load_static(self, html_content):
        """Add {% load static %} tag at the beginning of HTML."""
        if '{% load static %}' not in html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            if soup.html:
                load_tag = soup.new_string('{% load static %}\n')
                soup.html.insert_before(load_tag)
                return str(soup)
            else:
                return '{% load static %}\n' + html_content
        
        return html_content
    
    def process_html_files(self):
        """Process all HTML files and save to Django templates directory."""
        self.log("\n📝 Processing HTML files...")
        
        templates_dir = self.django_project_path / 'templates'
        ensure_dir(templates_dir)
        
        all_files = self.find_all_files(self.temp_dir)
        html_files = [f for f in all_files if is_html_file(f)]
        
        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()
            
            html_content = self.rewrite_html_paths(html_content, html_file.name)
            
            html_content = self.add_load_static(html_content)
            
            output_filename = html_file.name
            output_path = templates_dir / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.log(f"  ✓ Processed: {html_file.name} → templates/{output_filename}")
        
        self.log(f"✅ Processed {len(html_files)} HTML files")
    
    def cleanup(self):
        """Clean up temporary extraction directory."""
        self.log("\n🧹 Cleaning up temporary files...")
        clean_temp_dir(self.temp_dir)
        self.log("✅ Cleanup complete")
    
    def integrate(self):
        """Run the complete integration process."""
        try:
            self.log("🚀 Starting Django Template Integration...\n")
            
            self.extract_template()
            
            self.move_assets_to_static()
            
            self.process_html_files()
            
            self.cleanup()
            
            self.log("\n🎉 Integration complete!")
            self.log(f"📂 Static files: {self.django_project_path / 'static'}")
            self.log(f"📂 Templates: {self.django_project_path / 'templates'}")
            
            return True
            
        except Exception as e:
            self.log(f"\n❌ Error during integration: {str(e)}")
            self.cleanup()
            raise
