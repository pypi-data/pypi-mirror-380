#!/usr/bin/env bash
# Get a metric value from the filling log file
# runs in both local and remote setups
# Local Usage: ./metric_from_log.sh local weldline
# Remote Usage: ./metric_from_log.sh remote weldline

set -e
casename=$(basename "$PWD")
mode="$1"
casecwd=""
logfile=""
cmdprefix=""

case "$mode" in
    local)
        casecwd="$PWD"
        logfile="$casecwd/log.blockUCoupledIMFoam.filling"
        if [ ! -f "$logfile" ]; then echo nan; exit 1; fi
        ;;
    remote)
        casecwd="/home/slurmuser/trials/$(basename "$PWD")"
        logfile="$casecwd/log.blockUCoupledIMFoam.filling"
        docker exec slurm-head bash -c "if [ ! -f $logfile ]; then echo nan; exit 1; fi"
        cmdprefix="docker exec slurm-head "
        ;;
    *)
        echo "Unknown mode: $mode"
        echo "Supported modes are: local, remote"
        exit 1
        ;;
esac

case $2 in
    weldline)
        awk_script='/^Weldline formed/ { if ($3 > max) max = $3; found = 1 } END { if (found) print max; else print "nan" }'
        $cmdprefix bash -c "awk -v max=-100 '$awk_script' $logfile"
    ;;
    balancedFilling)
        awk_script='/^Balanced filling/ { if ($4 > max) max = $4; found = 1 } END { if (found) print max; else print "nan" }' 
        $cmdprefix bash -c "awk -v max=-100 '$awk_script' $logfile"
    ;;
    maxInletPressure)
        awk_script='/^max pressure at inlets/ { if ($6 > max) max = $6; found = 1 } END { if (found) print max; else print "nan" }' 
        $cmdprefix bash -c "awk '$awk_script' $logfile"
    ;;
    fillTime)
        awk_script='/^Objective fillTime/ { if ($4 > max) max = $4; found = 1 } END { if (found && max>0) print max; else print "nan" }' 
        $cmdprefix bash -c "awk '$awk_script' $logfile"
    ;;
    *)
        echo 'Unknown metric: `'"$2"'`'
        echo "Supported metrics: weldline, balancedFilling, maxInletPressure, fillTime"
        exit 1
    ;;
esac
