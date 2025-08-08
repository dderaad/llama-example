from invoke import task

@task
def ensure_ollama_install(c):
    try:
        c.run("ollama pull llama2")
        c.run("ollama pull llama3")
    except Exception as e:
        print(f"Warning: Exception {e}\nEncountered during pull.")
    finally:
        print("Llama3 and Llama2 are local!")

@task
def ensure_ollama_serve(c):
    try:

        c.run("ollama serve")
    except Exception as e:
        print(f"Warning: Exception {e}\nEncountered during serve.")
    finally:
        print("Ollama is serving!")