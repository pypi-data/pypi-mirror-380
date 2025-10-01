"""Command-line interface for Django Template Integrator."""

import argparse
import sys
from pathlib import Path
from .core import DjangoTemplateIntegrator
from . import __version__


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Django Template Integrator - Automate frontend template integration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m django_template_integrator.cli template.zip mysite/
  python -m django_template_integrator.cli medical-template.zip /path/to/django/project
  
This tool will:
  1. Extract the ZIP template
  2. Move CSS/JS/images/fonts to Django static/ directory
  3. Move HTML files to Django templates/ directory
  4. Rewrite asset paths to Django {% static %} tags
  5. Add {% load static %} to all HTML files
        """
    )
    
    parser.add_argument(
        'zip_file',
        help='Path to the frontend template ZIP file'
    )
    
    parser.add_argument(
        'django_project',
        help='Path to the Django project directory'
    )
    
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Suppress output messages'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'Django Template Integrator {__version__}'
    )
    
    args = parser.parse_args()
    
    zip_path = Path(args.zip_file)
    django_path = Path(args.django_project)
    
    if not zip_path.exists():
        print(f"❌ Error: ZIP file not found: {zip_path}", file=sys.stderr)
        sys.exit(1)
    
    if not django_path.exists():
        print(f"❌ Error: Django project directory not found: {django_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        integrator = DjangoTemplateIntegrator(
            zip_path,
            django_path,
            verbose=not args.quiet
        )
        
        integrator.integrate()
        
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ Integration failed: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
