import re # Import regex library to detect and match specific patterns in the sample log.
from collections import Counter # To count the amount of times IPs, URLs and User-Agents appear.  

def main():
    # For telling Pyton what parts of the log line I want to collect.
    log_Pattern = r'(?P<ip>\S+) - \S+ - \[(?P<date_Time>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) \d+ "(?P<referrer>.*?)" "(?P<user_Agent>.*?)" \d+'

    #Open the log file and real all lines.
    with open('sample-log.log') as l:
        logs = l.readlines() # Save the lines from the file into a list.

    #Creation of counters to count the amountof times IP, User-Agent, and URLs appear.
    ip_Counter = Counter()
    user_AgentCounter = Counter()
    url_Counter = Counter()

    # Go through ecah line from the log file
    for line in logs:
        match = re.match(log_Pattern, line) # Try to match the log pattern to the line.
        if match: #If it matches we collect the the information we need and add a +1 count for each one.
            ip = match.group("ip") 
            user_Agent = match.group("user_Agent")
            url = match.group("url")
            ip_Counter[ip] += 1
            user_AgentCounter[user_Agent] += 1
            url_Counter[url] += 1

    # Print the IP, User-Agents and URLs for the top 20 most common of them, the amount of times they appear and in a readable format.
    print("Most Common IPs: ")
    for ip, count in ip_Counter.most_common(20):
        print(f"  {ip} - {count} times")

    print("\nMost Common User-Agents: ")
    for ua, count in user_AgentCounter.most_common(20):
        print(f"  {ua} - {count} times")

    print("\nMost Common URLs: ")
    for url, count in url_Counter.most_common(20):
        print(f"  {url} - {count} times")

# This makes sure the script runs only when directly executed
if __name__ == "__main__":
    main()
