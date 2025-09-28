# TraceMind Recipes v1

The `recipes-v1` format captures declarative flow and policy definitions that can be
loaded directly by the TraceMind runtime. This document describes the canonical
field set, validation rules, and working examples that you can copy into your
project.

## 1. Flow Recipe Schema

Each flow recipe is stored as a JSON document with the following top-level structure:

```json
{
  "flow": {
    "id": "string",
    "version": "string",
    "description": "string",
    "tags": ["string"],
    "entry": "step-id",
    "steps": [ ... ],
    "edges": [ ... ]
  }
}
```

Field details:

| Field | Type | Rules |
| --- | --- | --- |
| `flow.id` | string | Required. Lowercase slug (letters, digits, `_`, `-`). Must be unique across flows. |
| `flow.version` | string | Required. Semantic version or content hash. Used when generating `flow_rev`. |
| `flow.description` | string | Optional. Free-text summary displayed in tooling. |
| `flow.tags` | array of string | Optional. Zero or more short labels for discovery. |
| `flow.entry` | string | Required. References a step `id`; execution starts here. |
| `flow.steps` | array | Required. Each element defines one step (see below). |
| `flow.edges` | array | Required. Describes directed edges between steps. Must form a DAG. |

### 1.1 Step Objects

Each item in `flow.steps` has the shape:

```json
{
  "id": "string",
  "kind": "task" | "switch" | "parallel" | "finish",
  "config": { "...": "..." },
  "hooks": {
    "before": "dotted.path",
    "run": "dotted.path",
    "after": "dotted.path",
    "on_error": "dotted.path"
  },
  "timeout_ms": 30000
}
```

Field semantics:

| Field | Type | Rules |
| --- | --- | --- |
| `id` | string | Required. Unique per flow. Slug format recommended. |
| `kind` | enum | Required. One of `task`, `switch`, `parallel`, `finish`. |
| `config` | object | Optional. Kind-specific configuration. See below. |
| `hooks.before` | string | Optional. Import path to async/sync callable executed before the step. |
| `hooks.run` | string | Required for `task`, `switch`, `parallel`. Callable that returns the step output. |
| `hooks.after` | string | Optional. Callable invoked after success. |
| `hooks.on_error` | string | Optional. Callable invoked on exceptions. |
| `timeout_ms` | integer | Optional. Per-step timeout budget in milliseconds. |

Kind-specific expectations:

* **task** – `config` is free-form; runtime passes step state into `hooks.run`.
* **switch** – `config` supports `{ "cases": { "label": "edge-id" }, "default": "edge-id" }`. The `run` hook returns a case label.
* **parallel** – `config` supports `{ "branches": ["step-id", ...], "mode": "all" | "race" }`.
* **finish** – terminal marker; no `run` hook.

### 1.2 Edge Objects

Each edge is defined as:

```json
{
  "from": "step-id",
  "to": "step-id",
  "when": "optional-condition"
}
```

Rules:

* `from` and `to` must reference valid step ids.
* Multiple edges originating from a `switch` step should have distinct `when` labels matching `config.cases`. The default branch may omit `when`.
* The combined set of edges must form a directed acyclic graph (DAG).

## 2. Policy Recipe Schema

Policy recipes use a parallel structure:

```json
{
  "policy": {
    "id": "string",
    "strategy": "epsilon" | "ucb" | "custom",
    "params": { "epsilon": 0.1 },
    "hooks": {
      "choose": "dotted.path",
      "update": "dotted.path"
    }
  }
}
```

* `policy.id` – required slug.
* `policy.strategy` – required string describing the tuning strategy. Built-ins expect `epsilon` or `ucb`; `custom` defers to `hooks`.
* `policy.params` – optional key/value payload passed into the strategy implementation.
* `policy.hooks.choose` / `policy.hooks.update` – optional overrides for custom routing logic. If omitted, built-in logic uses `params`.

## 3. Validation Rules

Loaders MUST enforce the following:

1. **Uniqueness:** step ids are unique and referenced edges exist.
2. **Reachability:** every step is reachable from `flow.entry`; unreachable nodes raise an error.
3. **Acyclic:** `flow.edges` must encode a DAG. Cycles (direct or indirect) are rejected.
4. **Config shape:** `switch` steps require `config.cases`. `parallel` steps require `config.branches`.
5. **Hook resolution:** when present, hook strings should resolve to importable callables.
6. **Policy consistency:** `policy.strategy` must match available handlers; unknown strategies require explicit hooks.

Violations should raise a descriptive error before the flow/policy is registered. The runtime uses the `RecipeLoader` class to enforce these checks before creating a `FlowSpec`.

## 4. Copyable Examples

### 4.1 Linear Three-Step Flow

```json
{
  "flow": {
    "id": "checkout-linear",
    "version": "1.0.0",
    "description": "Three sequential tasks: prepare -> charge -> finish",
    "tags": ["demo", "linear"],
    "entry": "prepare",
    "steps": [
      {"id": "prepare", "kind": "task", "hooks": {"run": "tm.examples.recipes.prepare"}},
      {"id": "charge", "kind": "task", "hooks": {"run": "tm.examples.recipes.charge"}},
      {"id": "done", "kind": "finish"}
    ],
    "edges": [
      {"from": "prepare", "to": "charge"},
      {"from": "charge", "to": "done"}
    ]
  }
}
```

### 4.2 Switch Flow with Conditional Branches

```json
{
  "flow": {
    "id": "fraud-review",
    "version": "2024.05.01",
    "description": "Route risky orders to manual review",
    "tags": ["switch", "risk"],
    "entry": "score",
    "steps": [
      {"id": "score", "kind": "task", "hooks": {"run": "tm.examples.recipes.score"}},
      {
        "id": "router",
        "kind": "switch",
        "config": {"cases": {"manual": "manual", "auto": "approve"}, "default": "auto"},
        "hooks": {"run": "tm.examples.recipes.route"}
      },
      {"id": "manual", "kind": "task", "hooks": {"run": "tm.examples.recipes.manual_review"}},
      {"id": "approve", "kind": "task", "hooks": {"run": "tm.examples.recipes.auto_approve"}},
      {"id": "complete", "kind": "finish"}
    ],
    "edges": [
      {"from": "score", "to": "router"},
      {"from": "router", "to": "manual", "when": "manual"},
      {"from": "router", "to": "approve", "when": "auto"},
      {"from": "manual", "to": "complete"},
      {"from": "approve", "to": "complete"}
    ]
  }
}
```

### 4.3 Parallel (all) with Patch Step

```json
{
  "flow": {
    "id": "document-process",
    "version": "1.2.3",
    "description": "Extract fields in parallel and merge into payload",
    "tags": ["parallel", "patch"],
    "entry": "ingest",
    "steps": [
      {"id": "ingest", "kind": "task", "hooks": {"run": "tm.examples.recipes.ingest"}},
      {
        "id": "fanout",
        "kind": "parallel",
        "config": {"branches": ["extract_text", "classify"], "mode": "all"},
        "hooks": {"run": "tm.examples.recipes.run_parallel"}
      },
      {"id": "extract_text", "kind": "task", "hooks": {"run": "tm.examples.recipes.extract_text"}},
      {"id": "classify", "kind": "task", "hooks": {"run": "tm.examples.recipes.classify"}},
      {"id": "patch", "kind": "task", "hooks": {"run": "tm.examples.recipes.patch_payload"}},
      {"id": "finish", "kind": "finish"}
    ],
    "edges": [
      {"from": "ingest", "to": "fanout"},
      {"from": "fanout", "to": "extract_text"},
      {"from": "fanout", "to": "classify"},
      {"from": "extract_text", "to": "patch"},
      {"from": "classify", "to": "patch"},
      {"from": "patch", "to": "finish"}
    ]
  }
}
```

### Policy Example (epsilon)

```json
{
  "policy": {
    "id": "epsilon-demo",
    "strategy": "epsilon",
    "params": {"epsilon": 0.2}
  }
}
```

### Policy Example (custom strategy)

```json
{
  "policy": {
    "id": "custom-routing",
    "strategy": "custom",
    "params": {"weights": {"arm-a": 0.7, "arm-b": 0.3}},
    "hooks": {
      "choose": "demo.policies.custom.choose",
      "update": "demo.policies.custom.update"
    }
  }
}
```

## 5. Running Recipes

1. Place one of the flow examples above into a file such as `flows/checkout-linear.yaml`. Converting the JSON block to YAML is optional—the loader accepts both. Example YAML:

   ```yaml
   flow:
     id: checkout-linear
     version: "1.0.0"
     entry: prepare
     steps:
   - id: prepare
     kind: task
     hooks:
        run: tm.examples.recipes.prepare
    - id: charge
      kind: task
      hooks:
        run: tm.examples.recipes.charge
       - id: done
         kind: finish
     edges:
       - {from: prepare, to: charge}
       - {from: charge, to: done}
   ```

2. Execute the recipe with the helper API:

   ```python
   from tm.run_recipe import run_recipe

   result = run_recipe("flows/checkout-linear.yaml", {"payload": {"order_id": "123"}})
   print(result)
   ```

   The response follows `{"status", "run_id", "output", "exec_ms"}`. A successful run returns `status="ok"`; invalid recipes (for example, missing hooks) surface `status="error"` with the validation message.

3. Policies can be loaded via `PolicyLoader` and applied to a `BanditTuner`:

   ```python
   from tm.ai.policy_registry import PolicyLoader, apply_policy
   from tm.ai.tuner import BanditTuner

   loader = PolicyLoader()
   loader.load("policies/epsilon-demo.json")
   tuner = BanditTuner()
   await apply_policy(tuner, "epsilon-demo")
   ```

## 6. Overlay Validation Workflow

TraceMind ships an overlay checker that compares runtime traces against exported flow artifacts:

1. Ensure your FlowRuntime is initialized via `tm.app.wiring_flows`. This automatically exports per-revision artifacts under `artifacts/flows/<flow_id>@<flow_rev>.{json,dot}`.
2. After running a few requests, invoke the checker:

   ```bash
   python scripts/trace_overlay_checker.py \
     --trace-dir data/trace \
     --artifacts-dir artifacts/flows \
     --runs 10
   ```

3. A report similar to the following is printed:

   ```json
   {
     "runs_analyzed": 10,
     "events": 42,
     "anomalies": [],
     "anomaly_rate": 0.0
   }
   ```

   Non-zero anomaly counts usually indicate a step name mismatch, a missing revision artifact, or a branch label emitted by a switch helper that is not covered by `config.cases`.

With these steps you can copy any of the recipe examples, run them through the loader, and verify their trace coverage using the overlay checker.

All of the flow snippets respect the schema above and can be ingested by a loader
that enforces the validation rules. You can attach additional metadata (for
example, runtime policies) alongside these documents as needed.
