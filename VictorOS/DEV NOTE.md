JARVISOS MISSION

We are NOT rebuilding OpenJarvis.

We are building the experience around it.

OpenJarvis is the brain.
JarvisOS is the companion.

============================

Desktop UI
Floating assistant
Voice wake word
Windows integration
Notifications
Animations
Personal personality
Relationship layer
Custom plugins
Your own workflow

============================

If a feature already exists inside OpenJarvis,
we USE it.

If OpenJarvis provides an SDK/API,
we WRAP it.

If OpenJarvis improves,
we BENEFIT.

JarvisOS should focus on making OpenJarvis
feel like a real personal assistant.


--LEFT OFF 1--
🚀 JARVISOS MASTER CONTEXT (v0.1)
Project Name

JarvisOS

Vision

JarvisOS is NOT a chatbot.

JarvisOS is NOT another AI wrapper.

JarvisOS is an AI Operating System.

OpenJarvis is used as the AI Framework underneath.

JarvisOS sits above OpenJarvis and coordinates everything.

Think of it like this:

Windows
    ↓
Applications

JarvisOS
    ↓
AI Systems

or

OpenJarvis
=
AI Framework

JarvisOS
=
Operating System

OpenJarvis already provides modular primitives—Intelligence, Engine, Agents, Memory, Tools, and Learning—using a registry-driven architecture. JarvisOS is intentionally designed to orchestrate those primitives rather than reimplement them.

Ultimate Goal

Eventually the user should be able to say things like:

"Jarvis, open Zalo, download the newest images from IMAGE group, upload them to the company website, summarize today's emails, then remind me at 4 PM if anything is missing."

Jarvis should:

understand
plan
choose AI
use vision
control desktop
use browser
use memory
execute background tasks
keep talking while tasks continue
Philosophy

JarvisOS owns:

orchestration
runtime
desktop
scheduling
workers
plugins
skills
memory integration
personality

OpenJarvis owns:

inference
engines
agents
learning
tools
model execution

We never duplicate OpenJarvis.

We build above it.

Development Philosophy

Always prefer:

Extend

instead of

Duplicate

Before creating a new class always ask:

Does this responsibility already exist?

Every class should own exactly one responsibility.

Architecture

Current architecture

User

↓

Kernel

↓

Director

↓

ExecutionPlan

↓

Runtime

↓

Worker Registry

↓

Worker

↓

Executor

↓

Brain

↓

OpenJarvis
Responsibilities
Kernel

Owns:

boot
shutdown
wiring services

Never:

executes AI
chooses models
plans tasks
Director

Owns:

classify request
choose model
build ExecutionPlan
send plan to Runtime

Never:

execute models directly
own desktop logic
ExecutionPlan

Contract only.

Contains

prompt

task

model

agent

Nothing else.

Runtime

Owns execution lifecycle.

Current:

IDLE

RUNNING

Future:

BACKGROUND

WAITING

BUSY

SHUTTING_DOWN

Future responsibilities:

scheduler
background jobs
AI cooperation
worker orchestration
Worker

Abstract interface.

Every worker implements

execute(plan)

Current:

DefaultWorker

Future:

ConversationWorker

CodingWorker

VisionWorker

ResearchWorker

AutomationWorker

MemoryWorker

VoiceWorker

WorkerRegistry

Current goal:

No hardcoded workers.

Today:

"default"

Future:

conversation

coding

vision

research

automation

This mirrors OpenJarvis's registry-first architecture, where new engines, agents, and tools register themselves instead of requiring changes throughout the framework.

Executor

Owns exactly one thing:

execute(plan)

Never:

schedule
classify
store tasks
Brain

Owns AI interaction.

Current:

OpenJarvisAdapter

Future:

Multiple adapters.

Model Routing

Current:

Conversation

↓

Qwen 3.5 4B

Future:

Conversation

↓

Tiny conversation model

Coding

↓

Coding model

Vision

↓

Vision model

Reasoning

↓

Reasoning model

Research

↓

Research model

Long-Term AI Cooperation

Eventually

Conversation AI

↓

Coding AI

↓

Vision AI

↓

Research AI

↓

Automation AI

All cooperate under Runtime.

Desktop Automation

Planned.

Will use

OCR
Vision
Mouse
Keyboard
Browser
Windows APIs

No API required.

Can automate software visually.

Voice

Future

Wake word:

Hey Jarvis

Conversation continues while background workers keep executing.

Memory

Future

Jarvis remembers:

projects
people
preferences
files
conversations
long-term context
Skills

Future plugins.

Example:

Calendar

Browser

Email

Discord

Zalo

File System

Git

VS Code
Runtime Vision

Eventually

Runtime

├── Scheduler

├── Worker Registry

├── Background Queue

├── Task Manager

├── Vision

├── Memory

├── Automation

├── AI Cooperation
Current Progress

Completed

✅ Kernel

✅ Contracts

✅ Brain

✅ OpenJarvis Integration

✅ Director

✅ ExecutionPlan

✅ Executor

✅ Task

✅ TaskManager v1

✅ Runtime v1

✅ Runtime State

✅ Worker Interface

✅ Default Worker

✅ Worker Registry
Estimated Progress

Core architecture:

~75% complete

Remaining core work:

Task → Worker selection
Runtime orchestration
Multi-worker dispatch

Then capability phase:

AI cooperation
Vision
Desktop automation
Persistent memory
Voice
Skills
Always-on assistant
Coding Rules
Never duplicate responsibilities.
Prefer extending existing architecture.
Always inspect current files before telling the user to modify them.
Never assume code still matches an earlier step—the project evolves continuously.
Keep Kernel thin.
Keep Executor tiny.
Runtime is the heart.
Director plans.
Workers perform specialized execution.
JarvisOS orchestrates; OpenJarvis provides AI primitives.
Project Notes
The project is local only (not connected to GitHub yet).
There will be a dedicated cleanup/refactor phase later to remove obsolete first-version files and keep the codebase clean.
The user consistently values architecture over quick hacks and prefers responsibility-driven design.
Every milestone should move JarvisOS closer to feeling like an AI Operating System, not just adding more code.
Where we actually left off

This is important because I do not want to repeat my earlier mistake.

We should not continue modifying Runtime immediately.

Instead, the next session should begin by reviewing the current implementations of:

services/runtime/runtime.py
services/runtime/worker_registry.py
services/director/director.py

and verify that the Worker Registry is correctly wired into the current codebase.

Only after that should we implement Task → Worker Selection, where BrainTask determines which worker the Runtime retrieves from the registry.