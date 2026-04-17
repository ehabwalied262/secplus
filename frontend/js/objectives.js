const SY701_OBJECTIVES = {
    "1.0 General Security Concepts": [
        { id: "1.1", title: "Security Controls" },
        { id: "1.2", title: "Cryptography Concepts" },
        { id: "1.3", title: "Authentication & Authorization" },
        { id: "1.4", title: "PKI & Certificate Management" }
    ],
    "2.0 Threats, Vulnerabilities & Mitigations": [
        { id: "2.1", title: "Malware & Ransomware" },
        { id: "2.2", title: "Social Engineering & Phishing" },
        { id: "2.3", title: "Application Attacks" },
        { id: "2.4", title: "Network Attacks" },
        { id: "2.5", title: "Threat Intelligence & OSINT" },
        { id: "2.6", title: "Vulnerability Scanning & Penetration Testing" }
    ],
    "3.0 Security Architecture": [
        { id: "3.1", title: "Cloud Security" },
        { id: "3.2", title: "Network Segmentation & Topology" },
        { id: "3.3", title: "Zero Trust Architecture" },
        { id: "3.4", title: "Virtualization & Containerization" },
        { id: "3.5", title: "Secure Infrastructure Design" },
        { id: "3.6", title: "ICS/SCADA & Embedded Systems" }
    ],
    "4.0 Security Operations": [
        { id: "4.1", title: "Identity & Access Management (IAM)" },
        { id: "4.2", title: "Endpoint Security & EDR" },
        { id: "4.3", title: "Firewalls, IDS/IPS & Network Security" },
        { id: "4.4", title: "SIEM & Log Monitoring" },
        { id: "4.5", title: "Incident Response" },
        { id: "4.6", title: "Digital Forensics" },
        { id: "4.7", title: "Data Loss Prevention (DLP)" }
    ],
    "5.0 Security Program Management & Oversight": [
        { id: "5.1", title: "Risk Management & Assessment" },
        { id: "5.2", title: "Compliance, Regulations & Frameworks" },
        { id: "5.3", title: "Data Privacy & Classification" },
        { id: "5.4", title: "Business Continuity & Disaster Recovery" },
        { id: "5.5", title: "Vendor & Third-Party Risk Management" },
        { id: "5.6", title: "Security Policies & Awareness Training" }
    ]
};

// Export for use in other scripts (since we aren't using modules, we use global scope)
window.SY701_OBJECTIVES = SY701_OBJECTIVES;