
import pandas as pd
from collections import defaultdict

def generate_glossary():
    df = pd.read_excel("SonoVerse.xlsx")
    df = df.sort_values(by=["Organ", "Term"])

    grouped = defaultdict(list)
    for _, row in df.iterrows():
        organ = row["Organ"]
        term = row["Term"]
        variant = row["Variant/Detail"]
        link = row["YouTube Link"] if pd.notna(row["YouTube Link"]) else None
        note = row["Notes"] if pd.notna(row["Notes"]) else ""
        grouped[organ].append({"term": term, "variant": variant, "link": link, "note": note})

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SonoVerse Glossary</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body { font-family: Arial, sans-serif; background-color: #f0f4f8; margin: 0; padding: 0; text-align: center; }
header { background-color: #003366; padding: 40px 20px; color: white; display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap; }
h1 { margin: 0; font-size: 2.2em; }
.subtitle { font-size: 1.2em; color: #cce0ff; margin: 0; }
.logo { max-width: 100px; width: 100%; height: auto; }
.title-block { text-align: left; }
#searchInput, #organSelect {
    padding: 10px; width: 100%; font-size: 1em; margin: 20px 0;
    border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;
}
.section { margin-bottom: 40px; text-align: left; max-width: 800px; margin-left: auto; margin-right: auto; }
h2 { color: #003366; margin-top: 30px; }
ul { list-style: none; padding-left: 0; }
li { margin-bottom: 10px; }
a { text-decoration: none; color: #0066cc; }
.coming { color: gray; }
@media (max-width: 768px) {
    h2 { font-size: 1.2em; }
    li { font-size: 0.95em; }
}
</style>
<script>
function searchGlossary() {
    var input = document.getElementById("searchInput").value.toLowerCase();
    var selectedOrgan = document.getElementById("organSelect").value;
    var sections = document.querySelectorAll(".section");
    sections.forEach(function(section) {
        var organ = section.getAttribute("data-organ");
        var items = section.querySelectorAll("li");
        var sectionVisible = false;
        items.forEach(function(item) {
            var text = item.textContent.toLowerCase();
            var match = (text.includes(input) && (selectedOrgan === "all" || selectedOrgan === organ));
            item.style.display = match ? "" : "none";
            if (match) sectionVisible = true;
        });
        section.style.display = sectionVisible ? "" : "none";
    });
}
</script>
</head>
<body>
<header>
    <img src="sonoverse_icon_only1.png" alt="SonoVerse Logo" class="logo">
    <div class="title-block">
        <h1>SonoVerse</h1>
        <p class="subtitle">Visual Ultrasound Glossary</p>
    </div>
</header>
<select id="organSelect" onchange="searchGlossary()">
<option value="all">Filter by organ (All)</option>
'''

    for organ in sorted(grouped.keys()):
        html += f"<option value='{organ}'>{organ}</option>"

    html += '''
</select>
<input type="text" id="searchInput" onkeyup="searchGlossary()" placeholder="Search for terms...">
'''

    for organ in sorted(grouped.keys()):
        html += f"<div class='section' data-organ='{organ}'><h2>{organ}</h2><ul>"
        for entry in grouped[organ]:
            display = f"{entry['term']} – {entry['variant']}"
            if entry["link"]:
                html += f"<li><a href='{entry['link']}' target='_blank'>{display}</a></li>"
            else:
                html += f"<li class='coming'>{display} (coming soon)</li>"
        html += "</ul></div>"

    html += "</body></html>"

    with open("glossary.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    generate_glossary()
