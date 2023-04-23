import os
from bs4 import BeautifulSoup
from md2pdf.core import md2pdf

HEADER = """
<div style="text-align: center;font-size: 200%;">PARHAM KAZEMI</div>

<table>
  <tr>
    <td>pkazemi@bcgsc.ca</td>
    <td>linkedin.com/in/p-kazemi</td>
    <td>github.com/parham-k</td>
  </tr>
</table>
"""

BASE_DIR = os.path.dirname(__file__)
CV_MD_PATH = os.path.join(BASE_DIR, "cv.md")
CSS_PATH = os.path.join(BASE_DIR, "assets", "css", "cv.css")
CV_PDF_PATH = os.path.join(BASE_DIR, "assets", "CV-ParhamKazemi.pdf")

with open(CV_MD_PATH) as md_file:
    soup = BeautifulSoup(md_file, "html.parser")
    cv = HEADER + str(soup.find("div", id="cv"))[28:-8]

md2pdf(CV_PDF_PATH, md_content=cv, css_file_path=CSS_PATH)
