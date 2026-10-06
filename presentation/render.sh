#!/bin/bash
# macOS only: export the deck to PDF through Microsoft PowerPoint, then rasterize slides for review.
# PowerPoint is sandboxed, so the round trip goes through its container directory.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
C=~/Library/Containers/com.microsoft.Powerpoint/Data
cp "$HERE/MACE_Agentic_Discovery.pptx" "$C/deck.pptx"; rm -f "$C/deck.pdf"
osascript -e "with timeout of 170 seconds
tell application \"Microsoft PowerPoint\"
  open POSIX file \"$C/deck.pptx\"
  delay 4
  save active presentation in (POSIX file \"$C/deck.pdf\") as save as PDF
  delay 2
  close active presentation saving no
end tell
end timeout"
mv "$C/deck.pdf" "$HERE/MACE_Agentic_Discovery.pdf"; rm -f "$C/deck.pptx"
mkdir -p "$HERE/render" && rm -f "$HERE"/render/slide-*.jpg
pdftoppm -jpeg -r 80 "$HERE/MACE_Agentic_Discovery.pdf" "$HERE/render/slide"
