from pathlib import Path

from ordeq_pymupdf import PymupdfFile


def test_pdf_file(tmp_path: Path, resources_dir: Path):
    dataset = PymupdfFile(path=resources_dir / "example.pdf")
    pdf_file = dataset.load()
    assert pdf_file.metadata is not None
    assert pdf_file.metadata["creator"] == "TeX"
    assert pdf_file.metadata["producer"] == "pdfTeX-1.40.23"

    page = pdf_file[0]
    page.set_rotation(180)  # flip the page

    dataset = PymupdfFile(path=tmp_path / "example.pdf")
    dataset.save(pdf_file)

    # similar file contents, only metadata should be different
    output = (tmp_path / "example.pdf").read_bytes()[:1000]
    reference = (resources_dir / "output.pdf").read_bytes()[:1000]
    assert output == reference
