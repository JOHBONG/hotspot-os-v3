# HotspotOS V3

## Overview
A modern MikroTik hotspot management SaaS platform for ISPs and hotspot operators in Africa. Features voucher management, reseller controls, hotspot/route monitoring, payment integrations, analytics, and AI-powered automation.

## Stack
- **Frontend:** Next.js, TailwindCSS
- **Backend:** FastAPI (Python), REST API, JWT auth, RBAC
- **Database:** PostgreSQL
- **Cache/Queues:** Redis, Celery
- **Integrations:** MikroTik RouterOS, WhatsApp API, M-Pesa, Flutterwave, etc.
- **Deployment:** Docker containers, VPS/Cloud support

## Core Features
- Multi-role (Admin, Reseller, Operator)
- Real-time dashboard, router & user sessions
- Voucher generation (bulk, QR, PDF, branded)
- Reseller system, wallet, package management
- Payment workflows, WhatsApp notifications, AI tools
- Security, analytics, multi-tenant roadmap

## Directory Structure
- `/backend` — FastAPI app, models, migrations
- `/frontend` — Next.js UI
- `/db` — schema, seeds

## Quickstart
1. Copy `.env.example` to `.env`.
2. Run `docker-compose up --build`.
3. Access frontend and backend on default ports.

## Roadmap
1. Auth & dashboard → router integration
2. Vouchers, packages, sync → payments & WhatsApp
3. Analytics & AI → multi-tenant SaaS

---
