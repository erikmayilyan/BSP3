import re

CATEGORY_PATTERNS = {
  "academic": [
    r"\bexam(s)?\b",
    r"\bgrade(s)?\b",
    r"\bgrading\b",
    r"\bmark(s)?\b",
    r"\bretake\b",
    r"\bappeal a grade\b",
    r"\btranscript\b",
    r"\bects\b",
  ],
  "admissions": [
    r"\bapply\b",
    r"\bapplication\b",
    r"\badmission(s)?\b",
    r"\benrol(l)?(ment)?\b",
    r"\bre-enrol(ment)?\b",
    r"\bvisiting student\b",
    r"\bincoming student\b",
    r"\blanguage certificate\b",
  ],
  "campus": [
    r"\bcampus\b",
    r"\blibrary\b",
    r"\baccommodation\b",
    r"\bsports activities\b",
    r"\bstudent association\b",
    r"\bget to\b.*\btrain\b",
  ],
  "it": [
    r"\bwi-?fi\b",
    r"\bmoodle\b",
    r"\bpassword\b",
    r"\breset\b",
    r"\buniversity email\b",
    r"\bemail account\b",
    r"\bconnect\b",
  ],
  "language": [
    r"\blanguage\b",
    r"\bfrench\b",
    r"\benglish\b",
    r"\bgerman\b",
    r"\btoefl\b",
    r"\bacademic writing\b",
  ],
  "mobility": [
    r"\berasmus\b",
    r"\bexchange\b",
    r"\bpartner universities\b",
    r"\bsemester abroad\b",
    r"\babroad\b",
  ],
  "organisation": [
    r"\brector\b",
    r"\bstudent administration\b",
    r"\binternational relations office\b",
    r"\bopening hours\b",
    r"\bcontact\b.*\boffice\b",
  ],
  "programmes": [
    r"\bbachelor\b",
    r"\bmaster\b",
    r"\bdegree\b",
    r"\bprogramme(s)?\b",
    r"\bcourse catalogue\b",
    r"\bminor\b",
    r"\bpart-time\b",
  ],
  "research": [
    r"\bresearch\b",
    r"\bphd\b",
    r"\bsupervisor\b",
    r"\blaborator(y|ies)\b",
    r"\bpublications\b",
  ],
  "support": [
    r"\bmental health\b",
    r"\bcareer centre\b",
    r"\binternship(s)?\b",
    r"\bdisability\b",
    r"\bpeer support\b",
    r"\bcounselling\b",
    r"\bcounseling\b",
  ],
  "tuition": [
    r"\btuition\b",
    r"\bscholarship(s)?\b",
    r"\bfinancial support\b",
    r"\binstalments?\b",
    r"\binstallments?\b",
    r"\bfees\b",
  ],
}

def analyze_request(user_request: str) -> dict:
  request = user_request.lower()

  categories = []

  for category, patterns in CATEGORY_PATTERNS.items():
    for pattern in patterns:
      if re.search(pattern, request):
        categories.append(category)
        break

  if not categories:
    categories = ["other"]

  description = (
    f"The student is asking about {', '.join(categories)}"
  )

  return {
    "categories": categories,
    "description": description,
  }