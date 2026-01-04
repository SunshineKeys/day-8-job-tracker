# Job Application Tracker — Day 8 Capstone Project

A Python CLI tool for tracking job applications with persistent storage. Built as the capstone of my 8-day Python sprint to solve a real problem I'm facing right now: staying organized during my job search.

When you're applying to dozens of positions, it's easy to lose track of where you applied, when you applied, and what happened next. This tool keeps everything organized in one place.

## 🎯 The Problem This Solves

Job hunting is chaotic. Between Indeed, LinkedIn, company websites, and referrals, it's hard to remember:
- Where did I apply last week?
- Which companies haven't responded yet?
- When should I follow up?
- What's my application-to-interview ratio?

This tracker centralizes everything so you can stay organized and make data-driven decisions about your job search.

## ✨ Features

**Application Management:**
- Add job applications with company name, title, location, status, and notes
- View all applications in a clean, organized format
- Persistent JSON storage (your data survives restarts)
- Update application status as you progress through the process

**Built for Real Use:**
- Simple CLI interface (no setup, just run it)
- Handles missing or corrupted data gracefully
- Fast to use (add an application in 30 seconds)
- Works offline (no API keys or internet required)

## 🚀 Quick Start
```bash
# Clone and run
git clone https://github.com/SunshineKeys/day-8-job-tracker.git
cd day-8-job-tracker
python job_tracker.py
```

**Menu options:**
1. Add new application
2. View all applications
3. Update application status
4. Exit

## 📊 Example Usage
```
=== Job Application Tracker ===

1) Add application
2) View all applications
3) Exit

Choose: 1

Company name: Principal Financial
Job title: Junior Python Developer
Location/Remote: Des Moines, IA
Status (applied/interviewing/rejected/offer): applied
Notes: Applied via LinkedIn Easy Apply

✓ Application added!
```

## 💡 Real-World Value

**For Job Seekers:**
- Stay organized across multiple job boards
- Track follow-up dates (7 days after application)
- Measure your success rate (applications → interviews)
- Keep notes on salary ranges, interview dates, contacts

**For Technical Interviews:**
- Demonstrates I solve my own problems with code
- Shows understanding of data persistence
- Proves I can build tools I actually use
- Reinforces practical CLI and file handling skills

## 🛠 Technical Details

**Built with:**
- Python (standard library only — no dependencies!)
- JSON for persistent storage
- Dictionary/list data structures
- Defensive error handling for corrupted files
- Clean CLI menu system

**Design Decisions:**
- **JSON over database:** Simpler for single-user CLI tool
- **Status field:** Tracks application lifecycle
- **Notes field:** Flexible for any additional context
- **Local storage:** Works offline, no API dependencies

**Handles Edge Cases:**
- Missing `applications.json` file (creates automatically)
- Corrupted JSON data (alerts user, doesn't crash)
- Empty input validation
- Graceful exit without losing data

## 🔮 Future Enhancements

If I expand this after landing a job:
- Export to CSV for spreadsheet analysis
- Filter by status (show only "interviewing")
- Add timestamps (date applied, last updated)
- Reminder system (follow up after 7 days)
- Statistics dashboard (applications per week, success rate)
- Integration with job board APIs (auto-import from LinkedIn)

## 🎓 Why This Project Matters

This is my Day 8 capstone — the final project in my 8-day Python sprint. I chose to build something I'll actually use while job hunting.

It demonstrates that I can:
- Identify real problems and build practical solutions
- Work with persistent data storage
- Handle user input and edge cases
- Build tools that solve my own needs (then extend them for others)
- Ship complete, working projects

More importantly, I'm **using this tool right now** to track applications as I apply to Python developer roles. When interviewers ask "Tell me about a project you built," I can say: "I built the tool I'm using to track this very application."

That's the kind of meta problem-solving that gets you hired.

## 📬 Connect

**Megan Merrigan**  
🔗 [GitHub](https://github.com/SunshineKeys) | [LinkedIn](https://linkedin.com/in/megan-merrigan-a824a1265)

*Part of my 8-day Python portfolio sprint — Day 8 of 8 complete.*  
*Building tools that demonstrate job-ready skills for technical support, DevOps, and development roles.*
