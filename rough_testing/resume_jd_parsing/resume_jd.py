import re
from pdfminer.high_level import extract_pages, extract_text
import sys

sys.stdout.reconfigure(encoding='utf-8')

#Function to Extract Resume text from Resume
def extractResumeText(pdf=""):
    resume_text = extract_text(pdf)
    return resume_text

#Function to Extract JD text from Resume
def extractJDText(pdf=""):
    jd_text = extract_text(pdf)
    return jd_text

resume = extractResumeText("rough_testing/resume_jd_parsing/Charles_Resume_Final.pdf")
jd = extractJDText("rough_testing/resume_jd_parsing/AEH JD Updated.pdf")

print(resume)
print("\n")
print(jd)