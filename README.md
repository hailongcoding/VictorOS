# JarvisOS
<h3 style="color:cyan">Credits to OpenJarvis</h3><br>
<h2 style="color:yellow">project is on development</h2>

> An AI Operating System built on top of OpenJarvis.

---

# Vision

JarvisOS is **not** another chatbot.

It is **not** another AI wrapper.

It is **not** another desktop assistant.

JarvisOS aims to become a complete **AI Operating System** that lives on the user's computer and acts as a persistent intelligent partner.

Instead of asking an AI to answer one prompt at a time, the user works with a system that can:

- Think
- Plan
- Remember
- Observe
- Automate
- Execute
- Learn
- Cooperate

all as one continuous operating environment.

The long-term goal is to build something that feels similar to **J.A.R.V.I.S.** from Iron Man—not by copying the character, but by creating an intelligent operating system capable of coordinating many specialized AI systems into one unified assistant.

---

# Purpose

OpenJarvis already provides powerful AI building blocks:

- Intelligence
- Agents
- Memory
- Tools
- Learning
- Model Routing

JarvisOS sits **above OpenJarvis**.

Its purpose is to coordinate these capabilities into a persistent operating system.

OpenJarvis is the AI framework.

JarvisOS is the operating system.

---

# Philosophy

Everything in JarvisOS follows one simple rule:

> Every class should have one responsibility.

Examples:

Kernel
- Boots the system.
- Connects services.

Director
- Understands requests.
- Creates execution plans.

Runtime
- Owns execution lifecycle.

Executor
- Executes plans.

Brain
- Talks to AI.

Workers
- Perform specialized tasks.

No component should perform another component's responsibility.

Architecture comes before features.

---

# Long-Term Goals

JarvisOS should eventually be capable of:

## Natural Conversation

The assistant should feel like a continuous companion instead of a prompt-response chatbot.

---

## Multiple AI Cooperation

Different AI systems should cooperate automatically.

Examples:

Conversation AI

↓

Coding AI

↓

Research AI

↓

Vision AI

↓

Automation AI

The user talks to one assistant.

JarvisOS coordinates many.

---

## Persistent Memory

Jarvis should remember:

- Projects
- Conversations
- Preferences
- Files
- Habits
- Long-term goals

Memory should survive reboots.

---

## Desktop Automation

Jarvis should operate the computer like a human.

Examples:

- Open applications
- Move windows
- Click buttons
- Fill forms
- Download files
- Upload files
- Organize folders
- Control browsers

Applications without APIs should still be usable through computer vision and desktop automation.

---

## Vision

Jarvis should understand:

- Screens
- Images
- Windows
- Buttons
- Documents
- PDFs
- Videos

Vision allows Jarvis to interact with software exactly as a human would.

---

## Voice

Eventually the primary interface should become:

"Hey Jarvis..."

instead of typing.

Jarvis should be able to continue working while listening for new requests.

---

## Background Tasks

Jarvis should execute long-running jobs without blocking conversation.

Example:

User:

> Build me a website.

Jarvis:

> Certainly. I'm working on it now.

The website continues building in the background while the conversation continues.

---

## Skills

Jarvis should become extensible through plugins.

Examples:

- Home Automation
- Finance
- Email
- Calendar
- Discord
- Telegram
- Browsers
- IDEs
- Office software

New skills should require minimal changes to the core architecture.

---

# Architecture Principles

JarvisOS prefers:

- Composition over inheritance
- Clear contracts
- Small services
- Stable interfaces
- Expandable runtime
- Registry-based architecture
- Dependency injection
- Separation of concerns

Architecture should remain understandable even after years of development.

---

# Current Architecture

```
User
        │
        ▼
Kernel
        │
        ▼
Director
        │
        ▼
ExecutionPlan
        │
        ▼
Runtime
        │
        ▼
Worker Registry
        │
        ▼
Workers
        │
        ▼
Executor
        │
        ▼
Brain
        │
        ▼
OpenJarvis
```

---

# Development Philosophy

JarvisOS is designed to evolve without constantly rewriting the foundation.

Infrastructure is built first.

Capabilities are added second.

Every milestone should make Jarvis more capable without breaking previous architecture.

The goal is not simply to build software.

The goal is to build an intelligent operating system.

---

# Roadmap

Core Architecture

- [x] Kernel
- [x] Brain
- [x] Director
- [x] Contracts
- [x] Execution Plan
- [x] Runtime
- [x] Executor
- [x] Worker System

Capabilities

- [ ] Worker Registry
- [ ] AI Cooperation
- [ ] Background Execution
- [ ] Vision
- [ ] Desktop Automation
- [ ] Persistent Memory
- [ ] Voice
- [ ] Skills
- [ ] Plugin System
- [ ] Always-On Assistant

---

# Final Goal

One day, the interaction should be as natural as:

User:

> "Jarvis, download today's images from the IMAGE group on Zalo, upload them to the company website, summarize today's meetings, remind me about unfinished tasks, and continue generating the dashboard we discussed yesterday."

Jarvis:

> "Certainly. I'm already uploading the images. The dashboard is 62% complete. You have two unfinished tasks from yesterday, and your next meeting begins in 18 minutes."

The user should feel like they are working alongside an intelligent partner—not operating a chatbot.