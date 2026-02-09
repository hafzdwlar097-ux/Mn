import importlib

tools = {
    "Cortex (LLMs)": "transformers",
    "Sensory (Vision)": "ultralytics",
    "Creation (Image)": "diffusers",
    "Audio (Speech)": "TTS",
    "Guardian (Security)": "scapy",
    "Architect (Agents)": "crewai"
}

print("--- AETHER SOVEREIGN: SYSTEM DIAGNOSTIC ---")
for name, lib in tools.items():
    try:
        importlib.import_module(lib)
        print(f"✅ {name}: Operational")
    except ImportError:
        print(f"❌ {name}: Pending Installation on this device")

print("\n--- 102 TOOLS MAPPING IS ACTIVE ON GITHUB ---")
