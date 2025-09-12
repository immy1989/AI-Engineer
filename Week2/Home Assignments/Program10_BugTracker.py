class BugTracker:
    def __init__(self):
        # Dictionary to store bugs: {bug_id: {"description": ..., "severity": ..., "status": ...}}
        self.bugs = {}
    
    def add_bug(self, bug_id, description, severity):
        if bug_id in self.bugs:
            print(f"Bug ID {bug_id} already exists.")
        else:
            self.bugs[bug_id] = {
                "description": description,
                "severity": severity,
                "status": "Open"
            }

    def update_bug_status(self, bug_id, new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
        else:
            print(f"Bug ID {bug_id} not found.")

    def display_all_bugs(self):
        if not self.bugs:
            print("No bugs reported.")

        else:
            print("\n=== Bug List ===")
            for bug_id, details in self.bugs.items():
                print(f"Bug ID: {bug_id}")
                print(f"Description: {details['description']}")
                print(f"Severity: {details['severity']}")           
                print(f"Status: {details['status']}")

if __name__ == "__main__":
    tracker = BugTracker()
    
    # Adding bugs
    tracker.add_bug(101, "Null pointer exception in login module", "High")
    tracker.add_bug(102, "UI misalignment on dashboard", "Medium")
    tracker.add_bug(103, "Typo in help documentation", "Low")
    
    # Displaying all bugs
    tracker.display_all_bugs()
    
    # Updating bug status
    tracker.update_bug_status(102, "In Progress")
    tracker.update_bug_status(101, "Resolved")
    
    # Displaying all bugs after updates
    tracker.display_all_bugs()