# 🛡️ Multi-Agent SOC - AI Powered Security Operations Center

## 📌 Overview

Multi-Agent SOC is an AI-powered Security Operations Center assistant that analyzes security logs, detects potential threats, evaluates severity, recommends responses, and generates automated SOC incident reports.

The system uses specialized AI agents coordinated through a **LangGraph-based workflow** to simulate a real SOC investigation pipeline.

---

# 🚨 Problem Statement

Organizations generate thousands of security events every day from sources such as servers, endpoints, firewalls, and authentication systems.

Manually analyzing these logs is time-consuming and can delay threat detection and response.

This project addresses this challenge by creating an automated multi-agent SOC assistant that can:

* Analyze security logs
* Detect suspicious activities
* Classify threat severity
* Recommend mitigation actions
* Generate structured incident reports

---

# 💡 Solution Architecture

The system follows a multi-agent architecture where each agent performs a specialized security task.

```
                 User Security Log
                        |
                        ▼
                 FastAPI Backend
                        |
                        ▼
              LangGraph SOC Workflow
                        |
        ┌───────────────┴───────────────┐
        ▼                               ▼

   Log Analysis Agent             Threat Agent

                                        |
                                        ▼

                              Threat Decision Router

                              /              \

                             /                \

                    No Threat              Threat Found

                         |                    |
                         ▼                    ▼

                     Report              Malware Agent
                                              |
                                              ▼
                                        Severity Agent
                                              |
                                              ▼
                                        Response Agent
                                              |
                                              ▼
                                    Coordinator AI Agent
                                              |
                                              ▼
                                      Report Generator
```

---

# 🤖 AI Agents

## 1. Log Analysis Agent

Responsibilities:

* Reads incoming security logs
* Extracts important information
* Performs initial analysis

## 2. Threat Intelligence Agent

Responsibilities:

* Detects possible attacks
* Identifies threats such as:

  * Brute force attacks
  * Malware activity
  * Phishing attempts
  * Ransomware

## 3. Malware Analysis Agent

Responsibilities:

* Checks malware-related indicators
* Identifies suspicious activity

## 4. Severity Agent

Responsibilities:

* Classifies incident priority:

  * 🟢 Low
  * 🟡 Medium
  * 🟠 High
  * 🔴 Critical

## 5. Response Agent

Responsibilities:

* Provides recommended security actions:

Examples:

* Block suspicious IPs
* Lock compromised accounts
* Isolate infected systems

## 6. Coordinator AI Agent

Responsibilities:

* Combines outputs from all agents
* Uses LLM reasoning
* Creates a professional SOC incident summary

## 7. Report Generator

Responsibilities:

* Generates structured incident reports
* Saves reports automatically

---

# 🔄 LangGraph Workflow

The project uses LangGraph for agent orchestration.

Each security capability is represented as a workflow node.

Current workflow:

```
START
 |
Log Agent
 |
Threat Agent
 |
 ├───────────────┐
 |               |
No Threat     Threat Found
 |               |
Report       Malware Agent
                  |
             Severity Agent
                  |
             Response Agent
                  |
          Coordinator AI Agent
                  |
               Report
                  |
                 END
```

The conditional routing allows the system to avoid unnecessary analysis for normal security events.

---

# 🛠️ Technologies Used

## Backend

* Python
* FastAPI

## AI / Agent Framework

* LangGraph
* LangChain
* Groq LLM

## Frontend

* HTML
* Jinja Templates

## Environment

* Python Virtual Environment
* GitHub

---

# 📂 Project Structure

```
Multi-Agent-SOC/

│
├── agents/
│   ├── coordinator.py
│   ├── log_agent.py
│   ├── threat_agent.py
│   ├── malware_agent.py
│   ├── severity_agent.py
│   └── response_agent.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   ├── workflow.py
│   └── runner.py
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── reports/
│   └── generated_reports/
│
├── requirements.txt
└── README.md
```

---

# 🚀 Running the Application

## 1. Clone repository

```
git clone <repository-url>
```

## 2. Activate virtual environment

Windows:

```
.\.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

## 4. Add environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

## 5. Start application

```
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

# 📝 Example Security Event

Input:

```
Multiple failed login attempts detected from IP 192.168.1.45. Possible brute force attack.
```

Output:

```
Threat:
Possible Brute Force Attack

Severity:
High

Response:
Block suspicious IP
Enable MFA
Monitor login attempts

SOC Report Generated Successfully
```

---

# 🔮 Future Enhancements

Planned improvements:

* Integration with real SIEM platforms
* Real-time log streaming
* Threat intelligence API integration
* Malware file scanning
* Database storage
* User authentication
* Advanced LangGraph agent routing

---

# 👨‍💻 Project Goal

The goal of this project is to demonstrate how autonomous AI agents and workflow orchestration can improve cybersecurity monitoring and incident response.
