import os
from contextlib import ExitStack
from pathlib import Path

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import OpenAI

BROCHURES_DIR = Path("brochures")


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def get_brochure_paths() -> list[Path]:
    return sorted(BROCHURES_DIR.glob("*.pdf"))


def main() -> None:
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")
    credential = None

    try:
        # Get configuration settings
        load_dotenv()
        azure_openai_endpoint = get_required_env("AZURE_OPENAI_ENDPOINT")
        model_deployment = get_required_env("MODEL_DEPLOYMENT")

        # Initialize the OpenAI client
        credential = DefaultAzureCredential()
        token_provider = get_bearer_token_provider(
            credential, "https://ai.azure.com/.default"
        )
        openai_client = OpenAI(base_url=azure_openai_endpoint, api_key=token_provider)

        # Create vector store and upload files
        brochure_paths = get_brochure_paths()
        if not brochure_paths:
            print("No PDF files found in the brochures folder.")
            return

        print("Creating vector store and uploading files...")
        vector_store = openai_client.vector_stores.create(name="travel-brochures")

        with ExitStack() as stack:
            file_streams = [
                stack.enter_context(path.open("rb")) for path in brochure_paths
            ]
            file_batch = openai_client.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id,
                files=file_streams,
            )

        print(f"Vector store created with {file_batch.file_counts.completed} files.")

        # Track conversation state
        last_response_id = None

        # Loop until the user wants to quit
        while True:
            input_text = input('\nEnter a question (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a question.")
                continue

            # Get a response using tools
            stream = openai_client.responses.create(
                model=model_deployment,
                instructions="""
You are a travel assistant that provides information on travel services available from Margie's Travel.
Answer questions about services offered by Margie's Travel using the provided travel brochures.
Search the web for general information about destinations or current travel advice.
""",
                input=input_text,
                previous_response_id=last_response_id,
                tools=[
                    {
                        "type": "file_search",
                        "vector_store_ids": [vector_store.id],
                    },
                    {
                        "type": "web_search",
                    },
                ],
                stream=True,
            )
            print("Assistant: ", end="", flush=True)
            for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
                elif event.type == "response.completed":
                    last_response_id = event.response.id
            print()

    except Exception as ex:
        print(ex)

    finally:
        if credential is not None:
            credential.close()


if __name__ == "__main__":
    main()
