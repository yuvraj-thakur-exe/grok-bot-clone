#!/usr/bin/env bash
set -euo pipefail

# Acquire exact pinned upstream commits for inspection only.
# Never installs dependencies, runs upstream scripts, imports source or changes ORBIT app code.
# OpenMausBot enterprise/ is excluded from the worktree by sparse checkout.
# Usage: bash scripts/clone_upstreams.sh [selectors...]

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -n "${ORBIT_UPSTREAM_DIR:-}" ]]; then
  DEST="$ORBIT_UPSTREAM_DIR"
elif [[ -n "${ORBIT_HOME:-}" ]]; then
  DEST="$ORBIT_HOME/01-upstream-checkouts"
else
  DEST="$ROOT/upstream"
fi
mkdir -p "$DEST"

clone_pinned() {
  local name="$1" url="$2" sha="$3" exclude_enterprise="${4:-false}" target="$DEST/$1"
  if [[ -d "$target/.git" ]]; then
    local origin
    origin="$(git -C "$target" remote get-url origin)"
    if [[ "$origin" != "$url" ]]; then
      echo "ERROR: $target has unexpected origin: $origin" >&2
      return 2
    fi
    git -C "$target" fetch --filter=blob:none --depth=1 origin "$sha"
  elif [[ -e "$target" ]]; then
    echo "ERROR: target exists but is not a Git checkout: $target" >&2
    return 2
  else
    git clone --filter=blob:none --no-checkout --depth=1 "$url" "$target"
    git -C "$target" fetch --filter=blob:none --depth=1 origin "$sha"
  fi

  if [[ "$exclude_enterprise" == "true" ]]; then
    git -C "$target" sparse-checkout init --no-cone
    printf '%s\n' '/*' '!/enterprise/' | git -C "$target" sparse-checkout set --no-cone --stdin
  fi

  git -C "$target" checkout --detach "$sha"
  local actual
  actual="$(git -C "$target" rev-parse HEAD)"
  [[ "$actual" == "$sha" ]] || { echo "ERROR: SHA mismatch for $name" >&2; return 3; }
  if [[ "$exclude_enterprise" == "true" && -e "$target/enterprise" ]]; then
    echo "ERROR: restricted enterprise/ path unexpectedly present in $target" >&2
    return 4
  fi
  printf 'READY %-30s %s\n' "$name" "$actual"
}

# Pins are also recorded in config/upstreams/upstream-lock.yaml.
clone_product_base() { clone_pinned openmausbot https://github.com/milind-soni/OpenMausBot.git 3f81576655ca45af91bfaaa63dc37251222828eb true; }
clone_openclaw() { clone_pinned openclaw https://github.com/openclaw/openclaw.git 7283c5182497e1ac5f95668de9f39ad3a9df3b11; }
clone_hermes() { clone_pinned hermes_agent https://github.com/NousResearch/hermes-agent.git 27afd192c2215d1e7363c38a2db77d0ab3f9db49; }
clone_self_evolution() { clone_pinned hermes_agent_self_evolution https://github.com/NousResearch/hermes-agent-self-evolution.git 0a929e3aa20e15cf04dc7c28492a7d41a5139125; }
clone_skills_index() { clone_pinned awesome_openclaw_skills https://github.com/VoltAgent/awesome-openclaw-skills.git 5492fcd98f7c52c69e1b2fa58790faf4fc90ce13; }
clone_openhands() { clone_pinned openhands_software_agent_sdk https://github.com/OpenHands/software-agent-sdk.git 51ad22388a154d48353fac7a82cfd5255dbeefc1; }
clone_opensandbox() { clone_pinned opensandbox https://github.com/opensandbox-group/OpenSandbox.git 5a85d1d24ad15a78dce1e1ae59503b87fc58cdde; }
clone_stagehand() { clone_pinned stagehand https://github.com/browserbase/stagehand.git 310957518a931c1a84c5968b13282cc30acd1be9; }
clone_browser_use() { clone_pinned browser_use https://github.com/browser-use/browser-use.git b49a68e4060acb226da8f784194fef301c53a6d7; }
clone_mem0() { clone_pinned mem0 https://github.com/mem0ai/mem0.git f1791daa86d469249c9b002f62644d58a1eb96a0; }
clone_letta() { clone_pinned letta_code https://github.com/letta-ai/letta-code.git 9176d8c0b16f408e9240422a98379a423e2176c3; }
clone_langgraph() { clone_pinned langgraph https://github.com/langchain-ai/langgraph.git e5e37b5d70dbfd93c7006bd90a658c6179a95946; }
clone_dspy() { clone_pinned dspy https://github.com/stanfordnlp/dspy.git efcb1e4232b90705a414e4b4e7cf47b503764c53; }
clone_temporal() { clone_pinned temporal https://github.com/temporalio/temporal.git 74c71f963b99f366f2adf8c503ecd785b0d8b4dc; }
clone_otel() { clone_pinned opentelemetry_js https://github.com/open-telemetry/opentelemetry-js.git ee94b842fd734e23064539c5f8069e0af0e92b9a; }
clone_llamaindex() { clone_pinned llamaindex https://github.com/run-llama/llama_index.git 444fdf0684707de62ebb447d658dba137dd9cb99; }
clone_qdrant() { clone_pinned qdrant https://github.com/qdrant/qdrant.git 222b2e44ab1c3f17e8246396ead6558e45041df7; }

clone_pydantic_ai() { clone_pinned pydantic_ai https://github.com/pydantic/pydantic-ai.git 0f7648a1b0685389ea368ea4f7b754b393cea8c7; }
clone_ollama() { clone_pinned ollama https://github.com/ollama/ollama.git d63b702609c4300a2ca07be2bdb0adb9834725e5; }
clone_llama_cpp() { clone_pinned llama_cpp https://github.com/ggml-org/llama.cpp.git f477f795cb071baf5b8af6488378366a72034ac4; }
clone_docling() { clone_pinned docling https://github.com/docling-project/docling.git 1d9a79c85028d4a2917e8026de338158f5d9fa88; }
clone_faster_whisper() { clone_pinned faster_whisper https://github.com/SYSTRAN/faster-whisper.git 846467d436117e44d54ad74f555d85c75834edb0; }
clone_graphiti() { clone_pinned graphiti https://github.com/getzep/graphiti.git 024b83679e48e41d59a7d1714ac0870aff2e4676; }
clone_mcp_python_sdk() { clone_pinned mcp_python_sdk https://github.com/modelcontextprotocol/python-sdk.git 77001c96f9507be0f4d009b83210a384a5e08bda; }
clone_openai_agents_python() { clone_pinned openai_agents_python https://github.com/openai/openai-agents-python.git 27c75c5f9c5fd957d28c04fb7e9eeacaad4630a9; }
clone_composio() { clone_pinned composio https://github.com/ComposioHQ/composio.git e970677aa69f4526009bb535a58d006ca7368e9a; }



clone_playwright() { clone_pinned playwright https://github.com/microsoft/playwright.git 07c7069cdbb1f5c7331d3f4d2abd864dcfde745a; }
clone_markitdown() { clone_pinned markitdown https://github.com/microsoft/markitdown.git ed178952a6672abdfd35b5f9e76a80b6cefc086e; }
clone_chroma() { clone_pinned chroma https://github.com/chroma-core/chroma.git 1a3ac2c7c623adbd03ed2508dc27b98cdf26016d; }
clone_tei() { clone_pinned text_embeddings_inference https://github.com/huggingface/text-embeddings-inference.git da9a9ce190444ef4326e1fbab15d298f0a1016c7; }
clone_transformers() { clone_pinned transformers https://github.com/huggingface/transformers.git a6f5c8676b158c367dc3389f68dde7a97fb619d6; }
clone_sherpa_onnx() { clone_pinned sherpa_onnx https://github.com/k2-fsa/sherpa-onnx.git 347ec768a01ca53e766780f7759b14e145b643e6; }
clone_semantic_kernel() { clone_pinned semantic_kernel https://github.com/microsoft/semantic-kernel.git df1cb33d0d32699c8d6a2e5b3ea7e5f8990d86d5; }
clone_home_assistant() { clone_pinned home_assistant https://github.com/home-assistant/core.git c97172ccafa1672d9854d9b862598d4640999b0d; }
clone_microsoft_agent_framework() { clone_pinned microsoft_agent_framework https://github.com/microsoft/agent-framework.git 924a6e50ec0336f3c965ee8b1151c54085888b6e; }


# v0.8: evaluation, serving, RAG and local analytics candidates.
clone_vllm() { clone_pinned vllm https://github.com/vllm-project/vllm.git d76fe936a1c4bb40abaf1b06aba37d849e95bdb2; }
clone_sglang() { clone_pinned sglang https://github.com/sgl-project/sglang.git cbbc6b67f48008a8b739f4667d7b14abb89088cf; }
clone_promptfoo() { clone_pinned promptfoo https://github.com/promptfoo/promptfoo.git 2a6fdf9b2e1600ffa2a204e70e9fea7cb0c14cff; }
clone_haystack() { clone_pinned haystack https://github.com/deepset-ai/haystack.git 0ad74747ffd7d9f9b092db97ba2e222080992c2e; }
clone_duckdb() { clone_pinned duckdb https://github.com/duckdb/duckdb.git d4eea3f208d42ca4ee522aca23f5ea76f902b0ca; }
clone_garak() { clone_pinned garak https://github.com/NVIDIA/garak.git 892779207cbc38f65a738ef9cbdfbc1e83aa0b55; }


# v0.9: graph RAG, structured output guardrails and scalable vector DB alternative.
clone_graphrag() { clone_pinned graphrag https://github.com/microsoft/graphrag.git 34b2b67ae4601ad0b47bcd179fbe3f2a23aa0857; }
clone_guardrails() { clone_pinned guardrails https://github.com/guardrails-ai/guardrails.git 06d0ff2c5f9bcb493d976b76f885e37e41ce845d; }
clone_milvus() { clone_pinned milvus https://github.com/milvus-io/milvus.git 686b129ca584fe2e8ae88b06ead95ffa03bad56a; }

# v1.0: additional coding agents, typed agent framework and search backend candidates.
clone_google_adk() { clone_pinned google_adk https://github.com/google/adk-python.git dd7161f7a2b88cd7ae482cc2acd8423675ac027c; }
clone_openai_codex() { clone_pinned openai_codex https://github.com/openai/codex.git c9b4267c370a755da12ec1c8648c2451163212b7; }
clone_gemini_cli() { clone_pinned gemini_cli https://github.com/google-gemini/gemini-cli.git 62bab5b232c15b925d31e655ce844ab939c882b7; }
clone_opensearch() { clone_pinned opensearch https://github.com/opensearch-project/OpenSearch.git 0b131ddecfe5be4cef617acda803e8c824c8c875; }
clone_swe_agent() { clone_pinned swe_agent https://github.com/SWE-agent/SWE-agent.git 3ea751c087f32b16e039a2233dd6eefecef325d5; }
clone_faiss() { clone_pinned faiss https://github.com/facebookresearch/faiss.git 29782a03747addd1122bf040b6c3488c8d669fe9; }


if [[ "$#" -eq 0 ]]; then set -- --product-base; fi
for selection in "$@"; do
  case "$selection" in
    --product-base) clone_product_base ;;
    --all-supplied) echo "NOTE: source acquisition may require substantial disk/network."; clone_product_base; clone_openclaw; clone_hermes; clone_self_evolution; clone_skills_index ;;
    --openclaw) clone_openclaw ;;
    --hermes) clone_hermes ;;
    --self-evolution) clone_self_evolution ;;
    --skills-index) clone_skills_index ;;
    --openhands-sdk) clone_openhands ;;
    --opensandbox) clone_opensandbox ;;
    --stagehand) clone_stagehand ;;
    --browser-use) clone_browser_use ;;
    --mem0) clone_mem0 ;;
    --letta) clone_letta ;;
    --langgraph) clone_langgraph ;;
    --dspy) clone_dspy ;;
    --temporal) clone_temporal ;;
    --otel) clone_otel ;;
    --llamaindex) clone_llamaindex ;;
    --qdrant) clone_qdrant ;;
    --pydantic-ai) clone_pydantic_ai ;;
    --ollama) clone_ollama ;;
    --llama-cpp) clone_llama_cpp ;;
    --docling) clone_docling ;;
    --faster-whisper) clone_faster_whisper ;;
    --graphiti) clone_graphiti ;;
    --mcp-python-sdk) clone_mcp_python_sdk ;;
    --openai-agents-python) clone_openai_agents_python ;;
    --composio) clone_composio ;;
    --all-new-candidates)
      clone_pydantic_ai; clone_ollama; clone_llama_cpp; clone_docling; clone_faster_whisper;
      clone_graphiti; clone_mcp_python_sdk; clone_openai_agents_python; clone_composio ;;
    --playwright) clone_playwright ;;
    --markitdown) clone_markitdown ;;
    --chroma) clone_chroma ;;
    --text-embeddings-inference) clone_tei ;;
    --transformers) clone_transformers ;;
    --sherpa-onnx) clone_sherpa_onnx ;;
    --semantic-kernel) clone_semantic_kernel ;;
    --home-assistant) clone_home_assistant ;;
    --microsoft-agent-framework) clone_microsoft_agent_framework ;;
    --all-v07-new)
      clone_playwright; clone_markitdown; clone_chroma; clone_tei; clone_transformers;
      clone_sherpa_onnx; clone_semantic_kernel; clone_home_assistant; clone_microsoft_agent_framework ;;
    --vllm) clone_vllm ;;
    --sglang) clone_sglang ;;
    --promptfoo) clone_promptfoo ;;
    --haystack) clone_haystack ;;
    --duckdb) clone_duckdb ;;
    --garak) clone_garak ;;
    --all-v08-new) clone_vllm; clone_sglang; clone_promptfoo; clone_haystack; clone_duckdb; clone_garak ;;
    --graphrag) clone_graphrag ;;
    --guardrails) clone_guardrails ;;
    --milvus) clone_milvus ;;
    --all-v09-new) clone_graphrag; clone_guardrails; clone_milvus ;;
    --google-adk) clone_google_adk ;;
    --openai-codex) clone_openai_codex ;;
    --gemini-cli) clone_gemini_cli ;;
    --opensearch) clone_opensearch ;;
    --swe-agent) clone_swe_agent ;;
    --faiss) clone_faiss ;;
    --all-v10-new) clone_google_adk; clone_openai_codex; clone_gemini_cli; clone_opensearch; clone_swe_agent; clone_faiss ;;
    --help|-h)
      cat <<'HELP'
Selectors (multiple allowed):
  --product-base      OpenMausBot public OSS product-shell candidate (enterprise/ excluded)
  --all-supplied      All five repositories supplied by the user
  --openclaw          OpenClaw runtime
  --hermes            Hermes Agent runtime
  --self-evolution    Hermes self-evolution research code
  --skills-index      VoltAgent skill discovery catalogue
  --openhands-sdk     OpenHands coding-agent SDK
  --opensandbox       OpenSandbox runtime
  --stagehand         Stagehand browser automation SDK
  --browser-use       Browser Use Python browser agent
  --mem0              Mem0 memory layer
  --letta             Letta Code
  --langgraph         LangGraph workflow framework
  --dspy              DSPy optimizer
  --temporal          Temporal workflow engine
  --otel              OpenTelemetry JS
  --llamaindex        LlamaIndex ingestion/RAG framework
  --qdrant            Qdrant vector database
  --pydantic-ai       Typed Python agent framework
  --ollama            Local model serving runtime
  --llama-cpp         Low-level GGUF inference runtime
  --docling           Document parsing and ingestion
  --faster-whisper    Speech-to-text worker
  --graphiti          Temporal knowledge graph memory
  --mcp-python-sdk    Python MCP SDK
  --openai-agents-python Python handoffs/guardrails SDK
  --composio          Connected-app toolkit/auth catalogue
  --playwright        Cross-browser automation baseline
  --markitdown        Document/Office-to-Markdown conversion
  --chroma            Alternative vector database
  --text-embeddings-inference Embedding inference server
  --transformers      Model architecture/tokenizer library
  --sherpa-onnx       Offline ASR/TTS/VAD pipeline
  --semantic-kernel   Multi-language agent/plugin SDK
  --home-assistant    Home automation connector research
  --microsoft-agent-framework Specialist multi-agent SDK
  --all-v07-new       All nine additional v0.7 candidates
  --vllm              GPU inference server (benchmark against SGLang)
  --sglang            GPU inference server (benchmark against vLLM)
  --promptfoo         Prompt/agent/RAG evaluation and red-team test harness
  --haystack          Alternative retrieval/RAG pipeline
  --duckdb            Embedded local analytics database
  --garak             LLM security/red-team probes for authorized targets
  --all-v08-new       All six v0.8 additions
  --graphrag          Graph-based RAG and knowledge graph extraction
  --guardrails        Structured output validation and guardrail pipeline
  --milvus            Distributed vector database alternative
  --all-v09-new       All three v0.9 additions
  --google-adk        Google Agent Development Kit Python framework
  --openai-codex      OpenAI Codex terminal coding-agent source
  --gemini-cli        Gemini CLI agent and extension source
  --opensearch        Distributed lexical/hybrid search backend
  --swe-agent         Issue-to-code worker and SWE benchmark candidate
  --faiss             Vector ANN similarity-search library
  --all-v10-new       All six v1.0 additions
  --all-new-candidates All nine v0.6/v0.7 candidate additions

Example:
  bash scripts/clone_upstreams.sh --product-base --openhands-sdk --opensandbox --stagehand
HELP
      ;;
    *) echo "Unknown option: $selection (use --help)" >&2; exit 64 ;;
  esac
done

echo "Pinned upstream source checkouts are under: $DEST"
echo "No dependencies were installed. No upstream scripts were executed. No code was merged."
echo "Review each upstream license, NOTICE, nested package, security posture and tests before reuse."
