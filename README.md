# ieuk-task-2025
This repo contains the log file for completing the 2025 IEUK Engineering task! The log file is too big to view in browser so you'll need to download it to your local machine. 

## Download Task
### Via Github UI 
https://github.com/user-attachments/assets/81972137-bf32-42c1-bc7d-dc65a0b9398f

### Via Git
You'll need to install Git and the Git LFS extension (which can be found [here](https://git-lfs.com/)). If you're unfamiliar with Git, I wouldn't worry about this—just download the log file via the UI.

-----------------------------------------------------------------------------------------------------------------------------

# Log Analysis Script – IEUK 2025 Project

This project was developed during the **Bright Network Internship Experience UK 2025** (Technology & Engineering stream), in response to a real-world engineering challenge set by **Lloyds Banking Group**.

## Project Overview

The challenge involved investigating performance issues on a fictional music media start-up’s website, which was repeatedly crashing due to suspected non-human (bot) traffic.  
Our goal was to:
- Analyze raw server logs
- Identify unusual or repetitive IP activity
- Recommend improvements to restore performance and improve reliability

This repository contains the log analysis script, a sample log file, and a report outlining key findings.

---

## What This Script Does

- Reads a raw server log file line by line
- Counts and ranks the most frequent IP addresses
- Flags IPs, URLs, and user-agents with unusually high access counts (potential bot activity)
- Outputs a simple summary of the most suspicious patterns found

---

## How to Run

Make sure you have **Python 3** installed.

1. If you dont have the complete log file, download the log file from the link below:
   🔗 [Download Full Log File](https://drive.google.com/file/d/1c1FrvuUXGkcK-2zA8H_YNBZgqtNi4s0M/view?usp=sharing)

2. Save it in the same folder as your script or note its location.

3. Run the script using:

```bash
python log_analysis.py

