from __future__ import annotations

import asyncio
import importlib


def module(name: str):
    return importlib.import_module(name)


def test_token_window_evicts_oldest_message_and_pins_system():
    lesson = module("phase1.01_token_budget")
    window = lesson.TokenWindow(14, "be concise")
    window.add("user", "first message about memory")
    window.add("assistant", "second message about memory")
    window.add("user", "latest question")
    assert window.messages[0].role == "system"
    assert window.messages[-1].content == "latest question"
    assert window.token_count <= 14


def test_summary_chain_keeps_recent_turns():
    lesson = module("phase1.02_summarization")
    chain = lesson.SummarizationChain(max_tokens=8, keep_recent=1)
    chain.add("user", "I like retrieval")
    chain.add("assistant", "Use chunks")
    chain.add("user", "Keep citations")
    assert chain.summary
    assert len(chain.recent) == 1


def test_vector_memory_round_trip(tmp_path):
    lesson = module("phase1.03_memory")
    memory = lesson.VectorMemory(2)
    memory.add("near", [1, 0], source="a")
    memory.add("far", [0, 1], source="b")
    assert memory.search([1, 0])[0][0].text == "near"
    path = tmp_path / "memory.json"
    memory.save(path)
    assert lesson.VectorMemory.load(path).items[0].text == "near"


def test_embeddings_are_normalized_and_similar_text_is_retrievable():
    lesson = module("phase2.04_embeddings")
    embedder = lesson.HashingEmbedder(32)
    vector = embedder.embed("agent tool")
    assert abs(float((vector * vector).sum()) - 1) < 1e-8
    assert lesson.cosine_similarity(vector, embedder.embed("agent tool")) == 1.0


def test_chunking_respects_fixed_size():
    lesson = module("phase2.05_chunking")
    chunks = lesson.fixed_chunks("abcdefghij", size=4, overlap=1)
    assert [chunk.text for chunk in chunks] == ["abcd", "defg", "ghij"]


def test_hybrid_search_and_mmr_return_bounded_results():
    lesson = module("phase2.06_vector_search")
    docs = ["python agent tools", "retrieval documents", "agent tools and retrieval"]
    assert lesson.hybrid_search("agent", docs, 2)[0].text in docs
    embedder = module("phase2.04_embeddings").HashingEmbedder(16)
    vectors = embedder.encode(docs)
    assert len(lesson.mmr(embedder.embed("agent"), vectors, 2)) == 2


def test_function_calling_validates_before_execute():
    lesson = module("phase3.07_function_calling")
    spec = lesson.ToolSpec("add", "add", {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}}, "required": ["a", "b"]}, lambda a, b: a + b)
    assert lesson.execute_tool_call({"name": "add", "arguments": {"a": 2, "b": 3}}, {"add": spec}) == 5
    try:
        lesson.execute_tool_call({"name": "add", "arguments": {"a": "no", "b": 3}}, {"add": spec})
    except lesson.ToolCallError:
        pass
    else:
        raise AssertionError("invalid argument was executed")


def test_registry_and_mcp_server():
    registry = module("phase3.08_tool_registry").ToolRegistry()
    registry.register("echo", "echo", lambda text: text)
    assert registry.dispatch("echo", text="ok") == "ok"
    server = module("phase3.09_mcp_server").build_server()
    result = server.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "word_count", "arguments": {"text": "one two"}}})
    assert result["result"]["content"][0]["text"] == "2"


def test_react_agent_stops_on_final():
    lesson = module("phase4.10_react_agent")
    agent = lesson.ReActAgent({"lookup": lambda value: "answer"}, lesson.demo_policy)
    assert agent.run("question") == "I found: answer"


def test_planning_and_reflection():
    tree = module("phase4.11_tree_of_thought")
    best = tree.tree_search(tree.Thought("root"), lambda _: [tree.Thought("bad", 1), tree.Thought("good", 3)], depth=1)
    assert best.text == "good"
    reflection = module("phase4.12_self_reflection")
    history = reflection.reflect("task", lambda _, __: "draft", lambda _, __: "ok", lambda answer, _: answer)
    assert len(history) == 1


def test_async_message_passing():
    assert asyncio.run(module("phase5.13_message_passing").conversation()) == ["analyst: RAG", "writer: Analysis of RAG"]


def test_supervisor_and_consensus():
    orchestration = module("phase5.14_orchestration")
    supervisor = orchestration.Supervisor({"a": lambda task, _: "A", "b": lambda task, state: state["first"] + "B"})
    assert supervisor.run([orchestration.Task("first", "a"), orchestration.Task("second", "b", ("first",))])["second"] == "AB"
    consensus = module("phase5.15_consensus")
    assert consensus.majority_vote(["b", "a", "a"]) == "a"
    assert consensus.borda_count([["a", "b"], ["b", "a"]]) == "a"


def test_production_helpers():
    obs = module("phase6.16_observability")
    assert asyncio.run(obs.collect_stream("hello")) == "hello"
    ledger = obs.CostLedger(0.1, 0.2)
    assert ledger.record(2, 3) == 0.8
    guard = module("phase6.17_evals_guardrails")
    assert "REDACTED_EMAIL" in guard.redact_pii("a@example.com")
    deployment = module("phase6.18_deployment")
    assert deployment.build_manifest("x", ["python"], "x")["version"] == "0.1.0"


def test_indic_boundaries():
    mixed = module("phase7.19_code_mixed_rag")
    assert mixed.detect_script("नमस्ते") == "devanagari"
    assert mixed.transliterate_devanagari("मौसम आज") == "mausam aaj"
    regional = module("phase7.20_regional_tool_use")
    call = regional.normalize_tool_call("मौसम in Delhi", "hi")
    assert call.name == "weather" and call.arguments["city"] == "Delhi"
