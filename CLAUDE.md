# Tech Interview Prep: Merging Customer Data for Market Analysis

## Assignment Context
- Course: AD311 Intermediate Application Development 1
- Task: Merge two sorted integer arrays (customerData1 and customerData2) into a single sorted array stored in-place in customerData1
- Scenario: Data analytics company interview — consolidating customer records from different databases

## Problem Summary
Given two sorted arrays `customerData1` (length m+n, last n elements are 0) and `customerData2` (length n), merge customerData2 into customerData1 in non-decreasing order in-place.

## Deliverables Required
- Merge function in `solution.py`
- ASCII diagram/flowchart of the approach
- Clarifying questions documented
- Pytest unit tests: 3+ normal cases, 3+ edge cases
- Time and space complexity analysis
- Optimized solution with trade-off explanation

## Workflow (from parent CLAUDE.md)
- Generate naive solution first, then optimize
- Analyze time/space complexity for both versions
- Create pytest unit tests (3+ normal, 3+ edge cases)
- Create simple ASCII diagrams for whiteboard explanation

## Style (from parent CLAUDE.md)
- Use Pythonic idioms
- Include docstrings with complexity analysis

## Constraints
- Must be presentable as a live coding interview (talk through decisions)
- Communicate clearly throughout - explain why you make each decision