#!/bin/bash
# MIMIC-IV ECG Job Status Monitor
# Usage: ./job_status.sh [--watch] [--interval SECONDS]

# Default settings
WATCH_MODE=false
INTERVAL=5
AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION:-"us-east-2"}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --watch|-w)
            WATCH_MODE=true
            shift
            ;;
        --interval|-i)
            INTERVAL="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: $0 [--watch] [--interval SECONDS]"
            echo "  --watch, -w       Live monitoring mode (refreshes every $INTERVAL seconds)"
            echo "  --interval, -i    Set refresh interval for watch mode (default: 5)"
            echo "  --help, -h        Show this help"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Function to convert UTC to Eastern Time
utc_to_et() {
    if command -v date >/dev/null 2>&1; then
        # Try different date format approaches
        if date -d "$1" >/dev/null 2>&1; then
            # GNU date (Linux)
            TZ=America/New_York date -d "$1" "+%Y-%m-%d %H:%M:%S ET"
        elif date -j -f "%Y-%m-%d %H:%M:%S" "$1" >/dev/null 2>&1; then
            # BSD date (macOS)
            TZ=America/New_York date -j -f "%Y-%m-%d %H:%M:%S" "$1" "+%Y-%m-%d %H:%M:%S ET"
        else
            echo "$1 (UTC)"
        fi
    else
        echo "$1 (UTC)"
    fi
}

# Function to display status
show_status() {
    echo ""
    echo "=============================================="
    echo "🔍 MIMIC-IV ECG Job Status Monitor"
    echo "=============================================="
    echo "$(date '+%Y-%m-%d %H:%M:%S ET') | Refresh: ${INTERVAL}s"
    echo ""
    
    # Check running processes first
    echo "📋 RUNNING JOBS"
    echo "----------------------------------------------"
    
    # Check for different types of download processes
    MIMIC_PROCESSES=$(ps aux | grep mimic_to_s3.sh | grep -v grep || true)
    AWS_SYNC_PROCESSES=$(ps aux | grep "aws s3 sync" | grep -v grep || true)
    PULL_PROCESSES=$(ps aux | grep pull_from_s3.sh | grep -v grep || true)
    
    MIMIC_COUNT=0
    AWS_COUNT=0  
    PULL_COUNT=0
    
    if [ -n "$MIMIC_PROCESSES" ] && [ "$MIMIC_PROCESSES" != "" ]; then
        MIMIC_COUNT=$(echo "$MIMIC_PROCESSES" | wc -l)
    fi
    
    if [ -n "$AWS_SYNC_PROCESSES" ] && [ "$AWS_SYNC_PROCESSES" != "" ]; then
        AWS_COUNT=$(echo "$AWS_SYNC_PROCESSES" | wc -l)
    fi
    
    if [ -n "$PULL_PROCESSES" ] && [ "$PULL_PROCESSES" != "" ]; then
        PULL_COUNT=$(echo "$PULL_PROCESSES" | wc -l)
    fi
    
    TOTAL_PROCESSES=$((MIMIC_COUNT + AWS_COUNT + PULL_COUNT))
    
    if [ "$TOTAL_PROCESSES" -gt 0 ]; then
        echo "✅ $TOTAL_PROCESSES active download processes"
        echo ""
        echo "Process Details:"
        
        if [ "$MIMIC_COUNT" -gt 0 ]; then
            echo "MIMIC-to-S3 processes:"
            echo "$MIMIC_PROCESSES" | while read line; do
                PID=$(echo "$line" | awk '{print $2}')
                START_TIME=$(echo "$line" | awk '{print $9}')
                CPU=$(echo "$line" | awk '{print $3}')
                MEM=$(echo "$line" | awk '{print $4}')
                echo "  PID $PID | CPU: $CPU% | MEM: $MEM% | Started: $START_TIME"
            done
        fi
        
        if [ "$AWS_COUNT" -gt 0 ]; then
            echo "AWS S3 Sync processes:"
            echo "$AWS_SYNC_PROCESSES" | while read line; do
                PID=$(echo "$line" | awk '{print $2}')
                START_TIME=$(echo "$line" | awk '{print $9}')
                CPU=$(echo "$line" | awk '{print $3}')
                MEM=$(echo "$line" | awk '{print $4}')
                echo "  PID $PID | CPU: $CPU% | MEM: $MEM% | Started: $START_TIME | Type: S3 Sync"
            done
        fi
        
        if [ "$PULL_COUNT" -gt 0 ]; then
            echo "Pull-from-S3 processes:"
            echo "$PULL_PROCESSES" | while read line; do
                PID=$(echo "$line" | awk '{print $2}')
                START_TIME=$(echo "$line" | awk '{print $9}')
                CPU=$(echo "$line" | awk '{print $3}')
                MEM=$(echo "$line" | awk '{print $4}')
                echo "  PID $PID | CPU: $CPU% | MEM: $MEM% | Started: $START_TIME | Type: Pull Script"
            done
        fi
        echo ""
        
        # Job health assessment  
        if [ "$AWS_COUNT" -gt 0 ]; then
            echo "💚 JOB STATUS: HEALTHY"
            echo "   AWS S3 sync is actively downloading files. No intervention needed!"
        else
            LATEST_UPLOAD=$(tail -1 /workspace/logs/mimic_s3_progress.txt 2>/dev/null | awk '{print $1, $2}')
            if [ -n "$LATEST_UPLOAD" ]; then
                LATEST_ET=$(utc_to_et "$LATEST_UPLOAD")
                CURRENT_TIME=$(date +%s)
                LATEST_TIME=$(date -d "$LATEST_UPLOAD" +%s 2>/dev/null || echo "$CURRENT_TIME")
                TIME_DIFF=$((CURRENT_TIME - LATEST_TIME))
                
                if [ $TIME_DIFF -lt 300 ]; then  # Less than 5 minutes
                    echo "💚 JOB STATUS: HEALTHY"
                    echo "   The job is working well - both CSV processing and file uploads"
                    echo "   are progressing normally. No intervention needed!"
                elif [ $TIME_DIFF -lt 900 ]; then  # Less than 15 minutes
                    echo "🟡 JOB STATUS: SLOW"
                    echo "   Job is running but uploads seem slower than usual."
                    echo "   Last upload: $LATEST_ET"
                else
                    echo "🔴 JOB STATUS: STALLED"
                    echo "   No recent uploads detected. Job may need attention."
                    echo "   Last upload: $LATEST_ET"
                fi
            else
                echo "🟡 JOB STATUS: STARTING"
                echo "   Processes running but no uploads logged yet."
            fi
        fi
    else
        echo "❌ No download jobs currently running"
        echo "   To restart: cd /workspace/runpod-mm-cardiotox-inference && nohup ./scripts/mimic_to_s3.sh lvef > /workspace/logs/lvef_background.log 2>&1 &"
    fi
    
    echo ""
    echo "📊 PROGRESS SUMMARY"
    echo "----------------------------------------------"
    
    if [ "$AWS_COUNT" -gt 0 ]; then
        # AWS S3 Sync Progress
        CURRENT_FILES=$(find /workspace/physionet.org -type f \( -name "*.dat" -o -name "*.hea" \) 2>/dev/null | wc -l)
        ESTIMATED_TOTAL=138381  # Total files from full dataset download (as reported)
        PERCENT_DOWNLOAD=$(echo "scale=1; $CURRENT_FILES * 100 / $ESTIMATED_TOTAL" | bc 2>/dev/null || echo "0")
        REMAINING_FILES=$((ESTIMATED_TOTAL - CURRENT_FILES))
        
        echo "S3 Sync Progress: $CURRENT_FILES/$ESTIMATED_TOTAL files (~${PERCENT_DOWNLOAD}%)"
        echo "Files downloaded since sync started: ~$((CURRENT_FILES - 354))"
        echo "Estimated remaining: $REMAINING_FILES files"
        
        # Progress bar for S3 sync
        BAR_LENGTH=50
        FILLED_LENGTH=$(echo "$PERCENT_DOWNLOAD * $BAR_LENGTH / 100" | bc 2>/dev/null || echo "0")
        printf "Progress: ["
        for ((i=0; i<FILLED_LENGTH; i++)); do printf "="; done
        for ((i=FILLED_LENGTH; i<BAR_LENGTH; i++)); do printf " "; done
        printf "] %.1f%%\n" "$PERCENT_DOWNLOAD"
        
        echo ""
        echo "AWS Sync Status: ACTIVE (CPU: $(ps -p 4187877 -o %cpu --no-headers 2>/dev/null || echo "N/A")%)"
        
    elif [ "$MIMIC_COUNT" -gt 0 ]; then
        # Original MIMIC upload progress (legacy)
        if [ -f "/workspace/logs/lvef_background.log" ]; then
            LATEST_PROGRESS=$(grep "Progress:" /workspace/logs/lvef_background.log | tail -1)
            if [ -n "$LATEST_PROGRESS" ]; then
                CURRENT_RECORDS=$(echo "$LATEST_PROGRESS" | cut -d' ' -f2 | cut -d'/' -f1)
                TOTAL_RECORDS=$(echo "$LATEST_PROGRESS" | cut -d' ' -f2 | cut -d'/' -f2)
                PROGRESS_TIME=$(echo "$LATEST_PROGRESS" | sed 's/.*(\(.*\)).*/\1/')
                PERCENT_CSV=$(echo "scale=1; $CURRENT_RECORDS * 100 / $TOTAL_RECORDS" | bc -l 2>/dev/null || echo "0")
                
                echo "CSV Processing: $CURRENT_RECORDS/$TOTAL_RECORDS records (${PERCENT_CSV}%)"
                echo "Last update: $PROGRESS_TIME"
            fi
        fi
    else
        echo "No active downloads detected"
    fi
    
    echo ""
    echo "🛠️  QUICK ACTIONS"
    echo "----------------------------------------------"
    echo "Monitor live: tail -f /workspace/logs/mimic_s3_progress.txt"
    echo "CSV progress: tail -f /workspace/logs/lvef_background.log"
    echo "Stop job:     pkill -f mimic_to_s3.sh"
    echo "Check errors: cat /workspace/logs/mimic_s3_errors.log"
    
    if [ "$WATCH_MODE" = true ]; then
        echo ""
        echo "🔄 Live monitoring enabled. Press Ctrl+C to exit."
        echo "=============================================="
    fi
}

# Function for live monitoring
live_monitor() {
    echo "🔄 Starting live monitoring (Ctrl+C to exit)..."
    echo ""
    
    trap 'echo ""; echo "Monitoring stopped."; exit 0' INT
    
    while true; do
        show_status
        sleep "$INTERVAL"
    done
}

# Main execution
if [ "$WATCH_MODE" = true ]; then
    live_monitor
else
    show_status
    echo ""
    echo "💡 TIP: Use --watch for live monitoring: ./job_status.sh --watch"
fi
