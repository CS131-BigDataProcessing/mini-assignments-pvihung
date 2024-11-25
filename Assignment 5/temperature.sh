#!/bin/bash
TEMP=$1
if [ "$TEMP" -lt 55 ]; then
        echo "freezing"
elif [ "$TEMP" -ge 55 ] && [ "$TEMP" -lt 67 ]; then
        echo "cold"
elif [ "$TEMP" -ge 67 ] && [ "$TEMP" -lt 85 ]; then
        echo "nice"
elif [ "$TEMP" -ge 85 ]; then
        echo "hot"
fi

