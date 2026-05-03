# KkoScanner

**KkoScanner** is an experimental TCP scanner developed as a personal learning project.

The goal of this repository is not to replace tools such as Nmap, but to understand some of the technical principles behind network scanning, TCP handshakes, socket handling, and the architectural challenges involved in building a scalable scanner.

## Project Status

**Status:** Work in Progress / Educational Project

At the current stage, the scanner is functional only in limited scenarios and on a small number of ports. The project has been temporarily paused while I continue studying how to manage a large number of concurrent handshake attempts in a consistent and scalable way.

This means that the code should be considered experimental and incomplete.

## Purpose

This project was created to practice and understand:

- TCP scanning logic
- Basic SYN / open port detection concepts
- Low-level networking behavior
- Socket management
- Python scripting for security-related tooling
- The difference between using existing tools and understanding how they work internally

## What This Project Is

KkoScanner is:

- a learning-oriented security project
- an exercise in Python and networking fundamentals
- a practical attempt to understand how port scanners are structured
- a work in progress that reflects an ongoing learning path

## What This Project Is Not

KkoScanner is not:

- a replacement for Nmap
- a production-ready security tool
- a complete vulnerability scanner
- a mature penetration testing framework
- intended for unauthorized scanning or misuse

## Current Limitations

Some known limitations include:

- limited scalability across large port ranges
- incomplete handling of many simultaneous handshake attempts
- no mature concurrency model yet
- limited error handling and timeout management
- limited reporting/output features
- no guarantee of accuracy across different targets or network conditions

These limitations are part of the learning process and are intentionally documented rather than hidden.

## Roadmap

Future improvements may include:

- better port range handling
- improved timeout logic
- cleaner module organization
- more consistent handshake management
- concurrency or asynchronous scanning experiments
- clearer output formatting
- safer execution controls
- improved documentation

## Ethical Use

This project is intended only for educational use and authorized testing environments.

Do not use this tool against systems, networks, or services without explicit permission.

## Author

**Francesco Viviani / KkoViv**

- GitHub: [KkoViv](https://github.com/KkoViv)
- LinkedIn: [Francesco Viviani](https://www.linkedin.com/in/francesco-viviani-b95a38379/)
- X: [@KkoViv](https://x.com/KkoViv)
