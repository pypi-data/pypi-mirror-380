<p align="center">
  <a href="https://arize.com/ax">
    <img src="https://storage.googleapis.com/arize-assets/arize-logo-white.jpg" width="600" />
  </a>
  <br/>
  <a target="_blank" href="https://pypi.org/project/arize/">
    <img src="https://img.shields.io/pypi/v/arize?color=blue">
  </a>
  <a target="_blank" href="https://pypi.org/project/arize/">
      <img src="https://img.shields.io/pypi/pyversions/arize">
  </a>
  <a target="_blank" href="https://arize-ai.slack.com/join/shared_invite/zt-2w57bhem8-hq24MB6u7yE_ZF_ilOYSBw#/shared-invite/email">
    <img src="https://img.shields.io/badge/slack-@arize-blue.svg?logo=slack">
  </a>
</p>

---

## Overview

A helper package to interact with Arize AI APIs.

Arize is an AI engineering platform. It helps engineers develop, evaluate, and observe AI applications and agents. 

Arize has both Enterprise and OSS products to support this goal: 
- [Arize AX](https://arize.com/) — an enterprise AI engineering platform from development to production, with an embedded AI Copilot
- [Phoenix](https://github.com/Arize-ai/phoenix) — a lightweight, open-source project for tracing, prompt engineering, and evaluation
- [OpenInference](https://github.com/Arize-ai/openinference) — an open-source instrumentation package to trace LLM applications across models and frameworks

We log over 1 trillion inferences and spans, 10 million evaluation runs, and 2 million OSS downloads every month. 

## Key Features
- [**_Tracing_**](https://docs.arize.com/arize/observe/tracing) - Trace your LLM application's runtime using OpenTelemetry-based instrumentation.
- [**_Evaluation_**](https://docs.arize.com/arize/evaluate/online-evals) - Leverage LLMs to benchmark your application's performance using response and retrieval evals.
- [**_Datasets_**](https://docs.arize.com/arize/develop/datasets) - Create versioned datasets of examples for experimentation, evaluation, and fine-tuning.
- [**_Experiments_**](https://docs.arize.com/arize/develop/datasets-and-experiments) - Track and evaluate changes to prompts, LLMs, and retrieval.
- [**_Playground_**](https://docs.arize.com/arize/develop/prompt-playground)- Optimize prompts, compare models, adjust parameters, and replay traced LLM calls.
- [**_Prompt Management_**](https://docs.arize.com/arize/develop/prompt-hub)- Manage and test prompt changes systematically using version control, tagging, and experimentation.

## Installation

Install Arize (version 8 is currently under alpha release) via `pip` or `conda`:

```bash
pip install arize==8.0.0ax 
```
where `x` denotes the specific alpha release. Install the `arize-otel` package for auto-instrumentation of your LLM library:

```bash
pip install arize-otel
```

## Usage
  
### Instrumentation

See [arize-otel in PyPI](https://pypi.org/project/arize-otel/):

```python
from arize.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor

# Setup OpenTelemetry via our convenience function
tracer_provider = register(
    space_id=SPACE_ID,
    api_key=API_KEY,
    project_name="agents-cookbook",
)

# Start instrumentation
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```


### Logging Spans, Evaluations, and Annotations

Use `arize.spans` to interact with spans: log spans into Arize, update the span's evaluations, annotations and metadata in bulk. 

> **WARNING**: This is currently under an alpha release. Install with `pip install arize==8.0.0ax` where the `x` denotes the specific alpha version. Check the [pre-releases](https://pypi.org/project/arize/#history) page in PyPI.

```python
from arize import ArizeClient

client = ArizeClient(api_key=API_KEY)
SPACE_ID = "<your-space-id>"
PROJECT_NAME = "<your-project-name>"

client.spans.log(
    space_id=SPACE_ID,
    project_name=PROJECT_NAME,
    dataframe=spans_df,
    evals_df=evals_df, # Optionally pass the evaluations together with the spans
)

client.spans.update_evaluations(
    dataframe=evals_df,
    project_name="your-llm-project",
)

client.spans.update_annotations(
    dataframe=annotations_df,
    project_name="your-llm-project",
)

client.spans.update_metadata(
    dataframe=annotations_df,
    project_name="your-llm-project",
)
```

## Community

Join our community to connect with thousands of AI builders.

- 🌍 Join our [Slack community](https://arize-ai.slack.com/join/shared_invite/zt-11t1vbu4x-xkBIHmOREQnYnYDH1GDfCg?__hstc=259489365.a667dfafcfa0169c8aee4178d115dc81.1733501603539.1733501603539.1733501603539.1&__hssc=259489365.1.1733501603539&__hsfp=3822854628&submissionGuid=381a0676-8f38-437b-96f2-fc10875658df#/shared-invite/email).
- 📚 Read our [documentation](https://docs.arize.com/arize).
- 💡 Ask questions and provide feedback in the _#arize-support_ channel.
- 𝕏 Follow us on [𝕏](https://twitter.com/ArizeAI).
- 🧑‍🏫 Deep dive into everything [Agents](http://arize.com/ai-agents/) and [LLM Evaluations](https://arize.com/llm-evaluation) on Arize's Learning Hubs.

Copyright 2025 Arize AI, Inc. All Rights Reserved.
