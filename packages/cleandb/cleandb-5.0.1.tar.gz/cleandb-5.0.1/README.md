🧾 CleanDB — A Data Cleaning and Quality Solution for Messy Data, Bug Prevention, and Leakage Control

A lightweight, Python-native, zero-dependency utility for managing structured .txt files. 
Ideal for structured data storage where full database integration is overkill. Uses simple 1D/2D list logic.


📦 Features:
- ✅ Structured Data Enforcement (1D/2D)
- ✍️ Write, Read, Append, and Delete Operations with Built-in Validation
- 🔍 Sql select style Read filtering
- 🧹 Selective Deletes & Trimming
- 🎗️ Multi-Console Safe for Concurrent Access
- 💾 Manual Backups or Timed Snapshots
- 🧪 Debug Tool & Auto-Clean Invalid Rows
- 🗂️ Clean Folder & Versioned File Organization
- 🔐 File Hiding and Visibility Controls
- 🗃️ No External Dependencies
- 💪 Strong anti-corruption and Tamper mechanism


Why Use This Package?

For Data Professionals (Analysts, Scientists, Engineers):
- Build quick dashboards and visualizations from real-time text data.
- Process and clean scraped or pipeline data without needing a database.
- Track, audit, and version small datasets during experimentation.
- Validate incoming data and auto-correct format issues on the fly.
- Run fast, repeatable data operations locally without SQL overhead.

For General Developers:
- Great for automation scripts, bots, or microservices.
- Ideal for prototyping features without setting up a database.
- Use as a flat-file backend for small apps or CLI tools.
- Snapshot and backup data safely without extra libraries.
- Handle concurrent access and reduce race-condition bugs automatically.


📦 Installation:
    pip install cleandb

♻️ Upgrade:
    pip install --upgrade cleandb


🚀 Quick Usage:

    import cleandb as db

    db.w("tasks", [["Read", "Done"], ["Code", "Pending"]])
    db.a("tasks", [["Test", "Pending"]])
    db.r("tasks")
    db.d("tasks", del_list=["Done"], index=1)
    db.backup("tasks")
    db.snapshot("tasks", unit="h", gap=6)


🧰 Function Overview:

🔄 Write:
    w(txt_name, write_list, is2d=None)
    Overwrites data and validates structure. Use [] to reset file and structure.

📖 Read:
    r(txt_name, index=None, set_new=[], notify_new=True)
    Reads data or returns `set_new` if file doesn't exist.

➕ Append:
    a(txt_name, append_list, is2d=None)
    Appends new data to file. Must match existing structure.

❌ Delete:
    d(txt_name, del_list=[], index=None, cutoff=None, keep=None, reverse=False, size=None)
    Deletes rows by value. Supports:
        - cutoff: Max deletions per value
        - keep: Keep N rows per value
        - reverse: Reverse traversal
        - size: Trim file to last N rows

💾 Backup:
    backup(txt_name, display=True)
    Creates manual backup. Use '*' to back up all files.

⏱ Snapshot:
    snapshot(txt_name, unit, gap, trim=None, begin=0, display=True)
    Creates a time-based snapshot if gap is met.
    Units: 's', 'm', 'h', 'd', 'mo', 'y'

🧹 Debug:
    debug(txt_name, is2d=None, clean=None, length=None, display=True)
    Scans file for validation issues and optionally fixes them.

🧨 Remove:
    remove(txt_name, display=True)
    Permanently deletes file and all backups.

🙈 Hide / Unhide:
    hide(txt_name, display=True)
    unhide(txt_name, display=True)
    Hides or unhides files. Use '*' for all files.

📋 List Files:
    listdir(display=True)
    Lists all stored file names.

ℹ️ File Info:
    info(txt_name, display=True)
    describe(txt_name, display=True)
    Shows metadata about file: type, shape, size, etc.


🧠 Notes:
- Structure Locking: On first write/append, the shape (1D/2D) and row length (for 2D) is saved.
- Use w("file", []) to reset the file and clear the structure lock.
- Only list data is supported (1D or 2D).
- All changes sync automatically across backups.
- Files are validated before every write operation.

🛡 Good Practices:
- Always use the provided w, a, r, d, etc. functions for access.
- Don't manually edit .txt files — structure validation may fail.
- Schedule snapshot() calls during long-running processes.
- Use debug() if you're unsure why writes are failing.


🧪 Example Workflow:

    import cleandb as db

✍️ Note : set is2d only for write and append mode  when creating a new 1D list file 

👉 1D list Workflow:

    # Create a 1D file
    db.w("shopping_list", ["Apples", "Bread", "Milk"], is2d=False) 
    
    # Append a new item
    db.a("shopping_list", ["Eggs"])
    
    # Read all items
    print(db.r("shopping_list"))
    # ➜ ['Apples', 'Bread', 'Milk', 'Eggs']
    filtering
    print(db.r("shopping_list", index = 1))
    # ➜'Bread'
    
    # Delete an item
    db.d("shopping_list", "Milk")
    db.d("shopping_list", ['Bread', 'Eggs'])


👉 2D list Workflow:

    # Write a 2D file with [Task, Status, Priority]
    
    tasks = [
        ["Read Docs", "Done", "Low"],
        ["Fix Bug", "Pending", "High"],
        ["Write Tests", "Pending", "Medium"]
    ]
    db.w("task_board", tasks)
    
    # Append new rows (must match 3 columns)
    db.a("task_board", [["Deploy", "In Progress", "High"]])
    
    # Read all tasks (no filter)
    all_tasks = db.r("task_board")
    print(all_tasks)
    
    # Read filtered rows by column 1 (Status == "Pending")
    pending_tasks = db.r("task_board", index=1)
    pending_tasks = db.r("task_board", index= [0,1])
    print(pending_tasks)
    
    # Delete all rows where Priority (column 2) is "Low"
    db.d("task_board", ["Low"], index=2)
    db.d("task_board", ["Low"], index=2)

    db.d("task_board",  [["Read Docs", "Done", "Low"]] , index="*")
    select start * means all index

    db.d("task_board",  [["Read Docs"], ["Fix Bug]] , index= 1)
    db.d("task_board",  ["Done", "Low"],["Pending", "High"], index= [1,2])
    
    
    # Run debug to clean invalid rows and enforce 3 columns
    db.debug("task_board", is2d=True, clean=True, length=3)
    
    # Backup the current file state manually
    db.backup("task_board")
    
    # Create a snapshot if at least 6 hours passed since last snapshot
    db.snapshot("task_board", unit="h", gap=6 , trim = 12)


👉 Delete Features: cutoff, keep, and size Usage Example

    # Setup sample 2D data: [Task, Status]
    tasks = [
        ["Read Docs", "Done"],
        ["Fix Bug", "Pending"],
        ["Write Tests", "Pending"],
        ["Deploy", "Pending"],
        ["Fix Bug", "Done"],
        ["Write Tests", "Done"],
        ["Fix Bug", "Pending"],
        ["Deploy", "Done"],
    ]
    
    db.w("task_board", tasks)
    
    print(db.r("task_board"))
    
    # 1️⃣ cutoff: Delete up to N rows per value in del_list
    # Delete up to 2 rows where Status == "Pending" (index=1)
    db.d("task_board", del_list=["Pending"], index=1, cutoff=2)
    print(db.r("task_board"))
    
    # 2️⃣ keep: Keep only N rows per value in del_list, delete extras
    # Keep only 1 row where Task == "Fix Bug" (index=0), delete others
    db.d("task_board", del_list=["Fix Bug"], index=0, keep=1)
    print(db.r("task_board"))
    
    # 3️⃣ size: Trim file to last N rows (keep last 4 rows)
    db.d("task_board", size=4)


📂 Backup & Recovery:
- Backups are stored under 'Backup 💾/'
- Snapshots are stored under 'Snapshot 📸/'
- To restore, simply copy the file back to main data directory



📜 License:
This project is free to use, modify, and distribute. No warranty is provided.

🙋 Contribution:
Feel free to fork, improve, and send pull requests.

✅ End of README
"""
