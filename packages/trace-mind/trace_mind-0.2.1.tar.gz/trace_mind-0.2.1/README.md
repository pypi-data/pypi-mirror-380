# TraceMind

**TraceMind** – A lightweight, event-sourced smart agent framework.
It records and reflects every transaction, supports pipeline-based field analysis, static flow export, and interactive summaries/diagnosis/plans.
Designed with a clean DDD structure, minimal dependencies, and safe container execution.

> Current release: **v0.2.1** — see [CHANGES.md](CHANGES.md) for highlights.

---

Agent Evolution Timeline
─────────────────────────────────────────────
(1) Client + Server        (2) Digital Twin         (3) Autonomous Agent
    ───────────────        ───────────────          ────────────────────
    • Proxy / Adapter      • Mirror of entity       • Observer
    • Sip, Websocket       • Present + feedback     • Executor
    • Hide protocol        • IoT, Telecom           • Collaborator
      complexity           • State visualization    • AI-driven autonomy
                           • Simulation / feedback  • Coordination in MAS

 Value: simplify access    Value: insight + control Value: autonomy + learning

---

## ✨ Features

* **Event Sourcing Core**: append-only event store powered by the Binary Segment Log (`tm/storage/binlog.py`). JSONL and SQLite remain optional adapters planned for future expansion.
* **DDD Structure**: clear separation of domain, application, and infrastructure layers.
* **Pipeline Engine**: field-driven processing (Plan → Rule → Step), statically analyzable.
* **Tracing & Reflection**: every step produces auditable spans.
* **Smart Layer**:

  * Summarize: human-readable summaries of recent events.
  * Diagnose: heuristic anomaly detection with suggested actions.
  * Plan: goal → steps → optional execution.
  * Reflect: postmortem reports and threshold recommendations.
* **Visualization**:

  * Static: export DOT/JSON diagrams of flows.
  * Dynamic: SSE dashboard with live DAG and insights panel.
* **Protocols**:

  * MCP (Model Context Protocol) integration (JSON-RPC 2.0) – see the
    [latest specification](https://modelcontextprotocol.io/specification/latest)
    and the [community GitHub org](https://github.com/modelcontextprotocol).
    Example flow recipe:
    ```python
    from tm.recipes.mcp_flows import mcp_tool_call

    spec = mcp_tool_call("files", "list", ["path"])
    runtime.register(_SpecFlow(spec))
    ```
* **Interfaces**:

  * REST API: `/api/commands/*`, `/api/query/*`, `/agent/chat`.
  * Metrics: `/metrics` (Prometheus format).
  * Health checks: `/healthz`, `/readyz`.

---

## 📂 Architecture (ASCII Overview)

```
                +----------------+
                |   REST / CLI   |
                +----------------+
                         |
                    [Commands]
                         v
                +----------------+
                |  App Service   |
                +----------------+
                         |
                  +------+------+
                  |             |
             [Event Store]   [Event Bus]
                  |             |
          +-------+        +----+-----------------+
          |                |                      |
     [Projections]   [Pipeline Engine]      [Smart Layer]
                          |              (Summarize/Diagnose/Plan/Reflect)
                          v
                      [Trace Store]
```

---

## 📚 Documentation

- [Flow & policy recipes](docs/recipes-v1.md)
- [Helpers reference](docs/helpers.md)
- [Policy lifecycle & MCP integration](docs/policy.md)
- [Publishing guide](docs/publish.md)

---

## 🚀 Quick Start

### Requirements

* Python 3.11+
* Standard library only (no third-party dependencies by default)

### Run in development

```bash
# clone
git clone https://github.com/<your-username>/trace-mind.git
cd trace-mind

# install and scaffold a demo project
pip install -e .
tm init demo
cd demo

# execute the sample flow
tm run flows/hello.yaml -i '{"name":"world"}'
```

### Run in container

```bash
docker build -t trace-mind ./docker

docker run --rm -it \
  --read-only \
  -v $(pwd)/data:/data \
  -p 8080:8080 \
  trace-mind
```

---

## 🧩 Roadmap

* [ ] More connectors (file bridge, http bridge, kafka bridge)
* [ ] Richer dashboard with interactive actions
* [ ] Adaptive thresholds in Reflector
* [ ] Optional LLM integration for natural summaries

---

## 📜 License

MIT (for personal and experimental use)
