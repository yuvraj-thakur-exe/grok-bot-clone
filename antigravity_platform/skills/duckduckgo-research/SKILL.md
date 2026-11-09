---
name: duckduckgo-research
description: >-
  Performs web search, browser-based content extraction, and information gathering using DuckDuckGo.
  Use this skill whenever the user asks to search the web via DuckDuckGo, browse web pages,
  collect online research, scrape article text, or gather structured intelligence from web sources.
---

# DuckDuckGo Research & Web Browsing Skill

This skill provides an automated workflow to search DuckDuckGo, visit target web pages, extract readable body text (stripping ads and clutter), and collect structured information into reports or datasets.

---

## Capabilities & Tooling

The skill includes a dedicated helper script located at:
`C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py`

Key capabilities:
- **Fast Web Search**: Queries DuckDuckGo without requiring API keys or authentication.
- **Content Extraction**: Follows search result URLs and extracts clean, readable text.
- **Browser Automation (Playwright)**: Supports headless Chromium rendering for JavaScript-heavy single-page applications (SPAs).
- **Multiple Formats**: Outputs formatted Markdown or structured JSON.

---

## Quick Reference / Commands

### 1. Simple Keyword Search
To retrieve the top 5 search results (titles, direct URLs, and snippets):
```powershell
python "C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py" --query "your search keywords" -n 5
```

### 2. Deep Search & Full Page Content Collection
To search and automatically fetch readable article content from the top results:
```powershell
python "C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py" --query "your search keywords" -n 3 --fetch
```

### 3. Extract Readable Content from a Specific URL
To inspect and collect text from a specific webpage:
```powershell
python "C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py" --url "https://example.com/article"
```

### 4. JavaScript / Single-Page App Rendering (Playwright)
For dynamic websites that require JavaScript execution:
```powershell
python "C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py" --url "https://example.com" --browser
```

### 5. Export Results to Markdown or JSON
Save output directly to disk for analysis:
```powershell
# Save as Markdown
python "C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py" --query "topic" -n 5 -o "research_report.md"

# Save as JSON
python "C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\scripts\ddg_research.py" --query "topic" -n 5 --fetch -o "data.json"
```

---

## Research Workflow Best Practices

1. **Query Formulation**: Use concise, targeted keywords. Avoid conversational filler in the search query.
2. **Fetch and Verify**: When factual accuracy or code details are required, use `--fetch` to inspect the source text rather than relying solely on snippets.
3. **Structured Synthesis**:
   - Organize findings into logical sections (e.g., Overview, Key Features, Limitations, Sources).
   - Always retain and cite the original source URLs.
4. **Artifact Creation**: For multi-page or comprehensive research, compile findings into a dedicated Markdown artifact in the conversation artifact directory.

