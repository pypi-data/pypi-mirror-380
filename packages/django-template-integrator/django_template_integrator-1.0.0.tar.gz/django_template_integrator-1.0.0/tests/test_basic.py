import shutil
import tempfile
import zipfile
from pathlib import Path

import pytest
from django_template_integrator.core import DjangoTemplateIntegrator


def create_test_zip(zip_path):
    """Helper to create a fake frontend template ZIP for testing."""
    with zipfile.ZipFile(zip_path, "w") as z:
        z.writestr(
            "index.html",
            '<html><head><link href="css/style.css"></head>'
            '<body><img src="img/logo.png"></body></html>'
        )
        z.writestr("css/style.css", "body {background: white;}")
        z.writestr("js/app.js", "console.log('test');")
        z.writestr("img/logo.png", "fakeimagebytes")


def test_full_integration_pipeline():
    temp_dir = tempfile.mkdtemp()
    zip_path = Path(temp_dir) / "template.zip"
    create_test_zip(zip_path)

    output_dir = Path(temp_dir) / "output"
    integrator = DjangoTemplateIntegrator(zip_path, output_dir)
    integrator.integrate()

    # ✅ Check files moved correctly
    assert (output_dir / "static/css/style.css").exists()
    assert (output_dir / "static/js/app.js").exists()
    assert (output_dir / "static/img/logo.png").exists()
    assert (output_dir / "templates/index.html").exists()

    # ✅ Check HTML content rewritten
    html_content = (output_dir / "templates/index.html").read_text()
    assert "{% load static %}" in html_content
    assert "{% static 'css/style.css' %}" in html_content
    assert "{% static 'img/logo.png' %}" in html_content

    shutil.rmtree(temp_dir)
