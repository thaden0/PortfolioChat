# 🤖 Developer Information ChatBot

This application implements a Retrieval-Augmented Generation (RAG) system using Llama 3.2 via Ollama, with Qdrant as the vector database. The chatbot answers questions about a developer based on information stored in a text file.

## Features
- Fully local RAG implementation
- Powered by Llama 3.2 through Ollama
- Vector search using Qdrant
- Interactive playground interface
- No external API dependencies
- Answers questions about developer background, skills, and experience

## How to get Started?

1. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install and start Qdrant vector database locally:**
```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

3. **Install Ollama and pull required models:**
```bash
ollama pull llama3.2
ollama pull openhermes
```

4. **Create your developer information file:**
Create a file named `developer_info.txt` in this directory with information about the developer. This can include:
- Background and experience
- Skills and technologies
- Projects and achievements
- Education and certifications
- Contact information
- Any other relevant details

5. **Run the Developer ChatBot:**
```bash
python developer_chatbot.py
```

6. **Open your web browser** and navigate to the URL provided in the console output to interact with the chatbot through the playground interface.

## Usage Examples

Once running, you can ask questions like:
- "What programming languages does this developer know?"
- "Tell me about their work experience"
- "What projects have they worked on?"
- "What is their educational background?"
- "What are their key skills and expertise?"

## Configuration

- **Model**: Change the model in `developer_chatbot.py` by modifying `Ollama(id="llama3.2")`
- **File Path**: Update `file_path="developer_info.txt"` to point to your developer information file
- **Collection Name**: Modify `collection_name` to change the vector database collection name

## Troubleshooting

- **Qdrant Connection Issues**: Ensure Qdrant is running on `http://localhost:6333/`
- **Ollama Issues**: Make sure Ollama is installed and the required models are pulled
- **File Not Found**: Ensure `developer_info.txt` exists in the same directory as the script
