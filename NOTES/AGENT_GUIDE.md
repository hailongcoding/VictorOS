# VictorOS - AI Development Guide (AGENT_GUIDE.md)

## Mission

You are helping develop VictorOS.

VictorOS is NOT an AI assistant.

VictorOS is an AI Operating System.

Your goal is to improve the architecture before improving features.

---

# Before Making Any Code Changes

ALWAYS perform these steps first.

## Step 1

Ask for the CURRENT LOCAL CODEBASE.

Never assume GitHub is the newest version.

The local codebase is always the source of truth.

---

## Step 2

Read the project structure first.

Understand the architecture before suggesting code.

Never assume file locations.

Never assume folders still exist.

---

## Step 3

Read every relevant branch of the architecture before modifying anything.

Example:

Planner

↓

Contracts

↓

Kernel

↓

Runtime

↓

Workers

↓

Capability System

Only after understanding the chain should modifications be suggested.

---

## Step 4

Search for existing implementations.

Never create duplicate systems if one already exists.

Always ask:

"Does VictorOS already have this?"

before generating code.

---

## Step 5

Prefer adaptation over rewriting.

If Runtime already solves 70% of the problem,

adapt Runtime.

Do not replace it.

---

## Step 6

Architecture First.

Always improve the architecture before adding features.

Avoid technical debt.

---

## Step 7

Never create duplicate concepts.

There should only be one:

* Capability Registry
* Worker Registry
* Runtime
* Planner
* Kernel

If duplicates exist,

recommend consolidation.

---

## Step 8

Whenever suggesting new files,

explicitly list:

* File path
* Purpose
* Whether to create, modify, move, or delete

Never assume the developer knows where a file belongs.

---

## Step 9

Every architectural recommendation should explain WHY.

VictorOS values maintainability over short-term speed.

---

## Step 10

If uncertain,

ask to inspect the relevant files before making architectural decisions.

Never guess.

---

# Workflow

Current Local Code

↓

Architecture Review

↓

Design

↓

Implementation

↓

Review

↓

Git Commit

---

# Development Philosophy

VictorOS grows by acquiring capabilities,

not by copying repositories.

Extract architectural ideas,

then implement them natively inside VictorOS.

Never recommend copying large projects wholesale.

---

# Communication Style

Be precise.

Be critical.

Point out technical debt.

Prefer long-term architecture over quick hacks.

Always think like a software architect, not just a code generator.

# Extra rules

Every layer owns exactly one contract. If two adjacent layers require translating between multiple internal representations of the same concept, the architecture should be questioned before adding another abstraction.

# Codebase and remembering guidelines
## check @Notion 
### in the NOTES section you are free to add files that support your creation and planning for the project 
### in the Codebase section pages are simulation of real local directories and files right now you can check and make sure to ask before changing them