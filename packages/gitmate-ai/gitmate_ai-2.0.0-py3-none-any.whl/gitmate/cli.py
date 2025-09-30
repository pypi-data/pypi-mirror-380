def main():
    import os
    import re
    import argparse
    import json
    from pathlib import Path
    from datetime import datetime

    from rich.console import Console
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich.text import Text

    from langchain_core.prompts import ChatPromptTemplate
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_openai import ChatOpenAI
    from langchain_anthropic import ChatAnthropic

    console = Console()

    # 🧠 Argument Parser
    parser = argparse.ArgumentParser(description="GitMate - AI Git Terminal Assistant")
    parser.add_argument("--model", type=str, choices=["openai", "gemini", "claude"], help="LLM model to use")
    parser.add_argument("--api-key", type=str, help="API key for the selected model")
    args = parser.parse_args()

    # 🌐 Select LLM Provider
    model_choice = args.model
    if not model_choice:
        console.print("\n🤖 [bold cyan]Welcome to GitMate! Choose your LLM model:[/]")
        console.print("1. [green]OpenAI (ChatGPT)[/]")
        console.print("2. [blue]Google Gemini[/]")
        console.print("3. [magenta]Anthropic Claude[/]")
        selected = Prompt.ask("Enter choice [1/2/3]", choices=["1", "2", "3"], default="2")
        model_choice = {"1": "openai", "2": "gemini", "3": "claude"}[selected]

    api_key = args.api_key  # default: None

    # -------------------------------------------
    # Config File Support
    # -------------------------------------------
    CONFIG_FILE = Path.home() / ".gitmate-config.json"
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as cf:
                config = json.load(cf)
        except json.JSONDecodeError:
            config = {}
    else:
        config = {}

    # 🔑 API Key + LLM Initialization
    if model_choice == "openai":
        api_key = config.get("openai_api_key") or api_key
        if not api_key:
            api_key = Prompt.ask("🔑 [bold green]Enter your OpenAI API Key[/]").strip()
        os.environ["OPENAI_API_KEY"] = api_key
        config["openai_api_key"] = api_key
        llm = ChatOpenAI(model="gpt-4o", temperature=0.3)
        provider_name = "OpenAI GPT-4o"

    elif model_choice == "gemini":
        api_key = config.get("gemini_api_key") or api_key
        if not api_key:
            api_key = Prompt.ask("🔑 [bold blue]Enter your Google Gemini API Key[/]").strip()
        os.environ["GOOGLE_API_KEY"] = api_key
        config["gemini_api_key"] = api_key
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
        provider_name = "Google Gemini 2.0"

    elif model_choice == "claude":
        api_key = config.get("claude_api_key") or api_key
        if not api_key:
            api_key = Prompt.ask("🔑 [bold magenta]Enter your Claude API Key[/]").strip()
        os.environ["ANTHROPIC_API_KEY"] = api_key
        config["claude_api_key"] = api_key
        llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.3)
        provider_name = "Claude 3 Sonnet"

    else:
        console.print("[red]❌ Invalid model selection[/]")
        return

    # Save/update config
    with open(CONFIG_FILE, "w", encoding="utf-8") as cf:
        json.dump(config, cf, indent=4)

    # -------------------------------------------
    # Log File Setup
    # -------------------------------------------
    LOG_FILE = f"git_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"GitMate Session Started - {datetime.now()}\n")
        log.write(f"Provider: {provider_name}\n")
        log.write("=" * 50 + "\n")

    console.print(f"\n🎯 [bold cyan]GitMate Terminal Started with {provider_name}[/]")
    console.print(f"💾 [green]Logging to:[/] {LOG_FILE}")
    console.print("📝 Type your commands. Type [yellow]`exit`[/] or [yellow]`quit`[/] to stop.")
    console.print("🤖 Type [magenta]`@bot your question`[/] to ask GitMate.")
    console.print("🚀 GitMate will explain and suggest commands, but will NOT execute them.\n")

    # -------------------------------------------
    # Invoke Bot
    # -------------------------------------------
    def invoke_bot(question, history):
        console.print("🤖 [yellow]Thinking...[/]")

        prompt = ChatPromptTemplate.from_template(
    """You are GitMate — an AI git assistant.

Here is the git session log so far:
{history}

The user asked:
{question}

### Instructions:
1. Explain in plain English (2-3 sentences max).
2. Only include commands if they are truly necessary.
3. If commands are included, format exactly:

GitMate suggests N command(s):
1. command_1
2. command_2

4. Start numbering at 1. Each command must be ready to copy-paste.
5. Do NOT execute commands automatically.
6. At the end of commands, indicate their relationship:
   - **Alternative commands** (like checking multiple files): "You can run **any one** of these commands."
   - **Sequential commands** (like add → commit → push): "You should run these commands **in order** to accomplish the task."
"""
        )

        chain = prompt | llm
        answer = chain.invoke({"history": history, "question": question})
        response_text = answer.content.strip()

        console.print(Panel(response_text, title="🤖 GitMate", border_style="green"))

        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(f"\n>>> @bot {question}\n")
            log.write(f"🤖 {response_text}\n")
            log.flush()

        return response_text

    # -------------------------------------------
    # Main Loop
    # -------------------------------------------
    while True:
        try:
            cmd = Prompt.ask("[bold blue]>>>[/]").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n👋 [bold red]Exiting.[/]")
            break

        if cmd.lower() in {"exit", "quit"}:
            break
        if not cmd:
            continue

        if cmd.startswith("@bot"):
            question = cmd.replace("@bot", "", 1).strip()
            with open(LOG_FILE, "r", encoding="utf-8") as lf:
                history_lines = lf.readlines()
            recent_history = "".join(history_lines[-100:])

            invoke_bot(question, recent_history)
            continue

        # Normal shell command
        os.system(cmd)

    console.print(f"\n✅ [bold green]Session saved to {LOG_FILE}[/]")


if __name__ == "__main__":
    main()
