# StopWeb

Block websites temporarily to help you stay focused. Works by editing your system's hosts file.

I built this because I kept getting distracted by social media and news sites when trying to work. Simple solution: block them for a few hours.

## What it does

- Blocks websites for a set amount of time (default: 1 day)
- Automatically unblocks them when time's up  
- Works on Mac, Linux, and Windows
- Lets you see what's currently blocked
- Can unblock sites early if needed

## Install

```bash
pip install stopweb
```

## Basic usage

Block Facebook for a day:
```bash
sudo stopweb facebook.com
```

Block YouTube for 2 hours:
```bash
sudo stopweb --duration 2h youtube.com
```

Block multiple sites at once:
```bash
sudo stopweb facebook.com youtube.com reddit.com
```

See what's blocked:
```bash
sudo stopweb --list
```

Unblock a site early:
```bash
sudo stopweb --remove facebook.com
```

Remove all blocks:
```bash
sudo stopweb --clear
```

## Time formats

- `30m` - 30 minutes
- `2h` - 2 hours  
- `1d` - 1 day
- `1w` - 1 week

## How it works

StopWeb edits your hosts file to redirect blocked sites to localhost (127.0.0.1). 

On Mac/Linux that's `/etc/hosts`, on Windows it's `C:\Windows\System32\drivers\etc\hosts`.

It adds lines like:
```
127.0.0.1    facebook.com    # StopWeb: expires 2024-01-15 14:30:00
```

When the time expires, it removes those lines automatically.

## Notes

- Requires sudo/admin privileges (needs to edit system files)
- You might need to clear your browser cache after blocking/unblocking
- Creates a backup of your hosts file before making changes
- If something goes wrong, your original hosts file is saved as `hosts.stopweb_backup`

## Why not just use browser extensions?

Browser extensions can be easily disabled when you're feeling weak. Editing the hosts file is more permanent - you'd have to remember the exact command to undo it.

Plus this works system-wide, not just in your browser.