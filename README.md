
# Codeforces Competitive Programming Portfolio
Automated repository powered by GitHub Actions and a custom Python script to track, classify, and organize my accepted (AC) solutions on the Codeforces platform.
## Stats and Profile
<p align="left">
  <img src="https://cf-readme-stats.vercel.app/api?username=imanol-e-p&theme=dark" alt="Codeforces Stats" height="200"/>
</p>

> Note: This card automatically fetches my current rank, peak rating, and the total number of solved problems directly from the official Codeforces API.
> 
## Tech Stack
 * Primary Language: C++ (GCC 20 / C++17)
 * Automation: GitHub Actions (CI/CD)
 * Scripting: Python 3.x (Codeforces REST API consumption)
## Repository Structure
The workflow automatically fetches and organizes solved problems into a hierarchical structure based on the contest ID and problem difficulty:
.
├── .github/
│   └── workflows/sync_codeforces.yml   # Process automation
├── Concurso_1900/
│   ├── A_Problem_Name/
│   │   └── A.cpp                       # Structured solution
│   └── B_Problem_Name/
│       └── B.cpp
└── README.md                           # This file

### How the Automation Works
Every 6 hours, an Ubuntu virtual environment configured via GitHub Actions runs a Python script that makes an HTTP request to codeforces.com/api/user.status. The script filters submissions with an OK verdict, generates the corresponding directories, and automatically pushes the changes back to this repository whenever new solved problems are detected.
