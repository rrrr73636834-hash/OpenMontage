#!/usr/bin/env bash
set -euo pipefail
mkdir -p logs
python3 make_video.py business_collapse "Corporate Mandate Collapse" 18 --use-kaggle > logs/business_collapse.log 2>&1 &
python3 make_video.py ancient_stoicism "Marcus Aurelius Wisdom" 20 --use-kaggle > logs/ancient_stoicism.log 2>&1 &
python3 make_video.py sleep_stories "Moonlit Forest Lullaby" 8 --use-kaggle > logs/sleep_stories.log 2>&1 &
wait
echo "Batch completed. Logs: logs/business_collapse.log logs/ancient_stoicism.log logs/sleep_stories.log"
