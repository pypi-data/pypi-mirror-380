def help():
    """
    🧾 Quick Reference Guide
    ============================

    📌 STRUCTURE LOCKING
    --------------------
    - On first `w()` or `a()`, structure is saved (1D/2D + row length if 2D).
    - Future writes/appends must match the saved structure.
    - To reset structure: clear the file with `w("file", [])`.

    ================================
    ⚙️ CORE FUNCTIONS (Usage & Parameters)
    ================================

    ▶ w(txt_name, write_list, is2d=None)
       Overwrites file with data.
       - txt_name: file name (str)
       - write_list: data (1D or 2D list)
       - is2d: set True/False only when file is new or reset

    ▶ r(txt_name, index=None, set_new=[], notify_new=True) → list | None
       Reads file content.
       - index: int/list/tuple to return specific rows/items
       - set_new: default value if file doesn't exist
       - notify_new: print alert if new file is auto-created

    ▶ a(txt_name, append_list, is2d=None) → list
       Appends data to existing file.
       - append_list: data to append (must match existing structure)
       is2d: set True/False only when file is new or reset

    ▶ d(txt_name, del_list=[], index=None, cutoff=None, keep=None,
         reverse=False, size=None) → (int, list)
       Deletes rows based on matching values or limits.
       - del_list: values to delete (["*"] clears all)
       - index: index to match in 2D rows
       - cutoff: max deletions per value
       - keep: rows to retain per value
       - reverse: process list in reverse
       - size: trim final output to last N rows

    ▶ backup(txt_name, display=True)
       Manual backup to "Backup 💾".
       - Use "*" to back up all files.

    ▶ snapshot(txt_name, unit, gap, trim=None, begin=0, display=True)
       Time-based auto-backup to "Snapshot 📸".
       - unit: 's', 'm', 'h', 'd', 'mo', 'y'
       - gap: minimum time between snapshots
       - trim: max rows to include in snapshot
       - begin: day start hour (for daily snapshots)

    ▶ debug(txt_name, is2d=None, clean=None, length=None, display=True)
       Scans file for invalid rows.
       - clean=True: auto-fixes and rewrites valid rows
       - length: expected row length (for 2D)
       - is2d: force structure detection if unknown

    ▶ remove(txt_name, display=True)
       Deletes file and all backups permanently.

    ▶ hide(txt_name, display=True) / unhide(txt_name, display=True)
       Hides/unhides a file. Use "*" for all files.

    ▶ listdir(display=True) → list
       Lists all existing files.

    ▶ info(txt_name, display=True) / describe(txt_name, display=True)
       Shows file stats: type, size, shape, validation, etc.

    ======================
    🧠 NOTES
    ======================
    - Data stored as `.txt` with automatic backups and structure checks.
    - Always use list format (1D or 2D) for data.
    - `is2d` is only needed when creating/resetting a file.
    - All changes are synced across backups automatically.

    🔚 End of Guide
    """
    print(help.__doc__)
