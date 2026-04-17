import sys
import os
import time
import re
import json

# Add parent directory to path so we can import backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.config import supabase_admin
from backend.services.groq_service import GroqService

# Defined here for the script, though we'll also have them in the frontend
OBJECTIVES = [
    {"num": "1.1", "title": "Security Controls"},
    {"num": "1.2", "title": "Cryptography Concepts"},
    {"num": "1.3", "title": "Authentication & Authorization"},
    {"num": "1.4", "title": "PKI & Certificate Management"},
    {"num": "2.1", "title": "Malware & Ransomware"},
    {"num": "2.2", "title": "Social Engineering & Phishing"},
    {"num": "2.3", "title": "Application Attacks"},
    {"num": "2.4", "title": "Network Attacks"},
    {"num": "2.5", "title": "Threat Intelligence & OSINT"},
    {"num": "2.6", "title": "Vulnerability Scanning & Penetration Testing"},
    {"num": "3.1", "title": "Cloud Security"},
    {"num": "3.2", "title": "Network Segmentation & Topology"},
    {"num": "3.3", "title": "Zero Trust Architecture"},
    {"num": "3.4", "title": "Virtualization & Containerization"},
    {"num": "3.5", "title": "Secure Infrastructure Design"},
    {"num": "3.6", "title": "ICS/SCADA & Embedded Systems"},
    {"num": "4.1", "title": "Identity & Access Management (IAM)"},
    {"num": "4.2", "title": "Endpoint Security & EDR"},
    {"num": "4.3", "title": "Firewalls, IDS/IPS & Network Security"},
    {"num": "4.4", "title": "SIEM & Log Monitoring"},
    {"num": "4.5", "title": "Incident Response"},
    {"num": "4.6", "title": "Digital Forensics"},
    {"num": "4.7", "title": "Data Loss Prevention (DLP)"},
    {"num": "5.1", "title": "Risk Management & Assessment"},
    {"num": "5.2", "title": "Compliance, Regulations & Frameworks"},
    {"num": "5.3", "title": "Data Privacy & Classification"},
    {"num": "5.4", "title": "Business Continuity & Disaster Recovery"},
    {"num": "5.5", "title": "Vendor & Third-Party Risk Management"},
    {"num": "5.6", "title": "Security Policies & Awareness Training"}
]


def clean_json_response(raw_text):
    """
    Removes Markdown code blocks and extra whitespace 
    to ensure json.loads can read the string.
    """
    clean_text = re.sub(r'```json\n?|```', '', raw_text).strip()
    return clean_text

def run_generation():
    groq = GroqService()
    
    for obj in OBJECTIVES:
        try:
            print(f"Generating questions for {obj['num']}: {obj['title']}...")
            
            # FIXED: Changed to generate_exam_questions to match your service file
            raw_response = groq.generate_exam_questions(obj['num'], obj['title'])
            
            # Clean and Parse the string into a Python List
            clean_text = clean_json_response(raw_response)
            questions_list = json.loads(clean_text)
            
            # Insert into Supabase
            for q in questions_list:
                data = {
                    "domain_number": obj['num'],
                    "domain_title": obj['title'],
                    "question": q['question'],
                    "options": q['options'],
                    "correct_index": q['correct_index'],
                    "explanation": q['explanation'],
                    "difficulty": q.get('difficulty', 'medium'),
                    "verified": False
                }
                
                supabase_admin.table("questions").insert(data).execute()
                
            print(f"✅ Successfully generated {len(questions_list)} questions for {obj['num']}\n")
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON Parsing Error for {obj['num']}: {e}")
            print(f"Raw response was: {raw_response[:100]}...") 
        except Exception as e:
            print(f"❌ Error processing {obj['num']}: {e}")

if __name__ == "__main__":
    run_generation()