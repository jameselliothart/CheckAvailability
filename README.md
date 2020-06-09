# Check Availability

## Purpose

Checks whether an item is in stock and sends a linux notification with the status.

This is a workaround to the Notify Me functionality on Home Depot's site not working.
Could be used for other sites with missing Notify Me functionality for out of stock items.

## Usage

Schedule a cron job with `crontab -e` to run execute.sh every so often.
