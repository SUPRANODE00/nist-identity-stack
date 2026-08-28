#!/usr/bin/env bash
# AXIOMATIC COMPILER REF: Clean Stream Parsing Filter (cat, sed, awk)
# Architecture: Terminal-Native / 3D Spatial Matrix / Signal-Hopping Mesh / Polarity Synthesis
# Identifier: Demien CAPSULECRAFT / SL1TH3R RAINBOW

TARGET_FILE="matrix_runtime_config.conf"

# Filter out comment lines using awk before processing key-value pairs
echo "[STREAM PIPELINE] Extracting active telemetry nodes (ignoring comments):"
cat "$TARGET_FILE" | awk '!/^#/ && NF {print "Config Key: " $1}'

# Clean string replacement via sed for state transition
sed -i 's/POLARITY_AXIS=unified/POLARITY_AXIS=synchronized_mesh/g' "$TARGET_FILE"

echo "[STREAM PIPELINE] Updated configuration payload:"
cat "$TARGET_FILE" | grep -v '^#'
