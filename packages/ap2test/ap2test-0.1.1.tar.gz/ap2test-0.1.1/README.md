# AP2Test - Agent Payments Protocol Testing CLI

A command-line tool for testing AP2 (Agent Payments Protocol) payment flows.

## Overview

AP2Test helps developers test their AI agent payment implementations by simulating the complete mandate flow:
- **Intent Mandates** - Define agent authorization constraints
- **Cart Mandates** - Capture specific purchase approvals
- **Payment Mandates** - Execute cryptographically-signed transactions

## Installation

pip install ap2test

## Examples

# View detailed audit trail
ap2test audit

# Check current status
ap2test status

# Create a custom intent
ap2test create-intent --amount 1000 --merchant store_xyz --category electronics

# Create a custom cart
ap2test create-cart --items "Laptop:899:1,Mouse:49:1" --merchant store_xyz

# Execute with crypto payment
ap2test execute-payment --method stablecoin

# Export audit as JSON
ap2test audit --format json

# Clear all data when done testing
ap2test reset
