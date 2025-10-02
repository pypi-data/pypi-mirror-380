# CV Document Chunker

A Python package for parsing PDF document layouts using YOLO models, chunking content based on layout, performing  table parsing with Docling integration, and optionally performing OCR.

## Features

- Convert PDF documents to images for processing.
- Detect document layout elements (e.g., paragraphs, tables, figures) using YOLO.
- Process and refine bounding boxes.
- Chunk document content based on detected layout.
- **Advanced Table Parsing**: Intelligent table detection and parsing using Docling integration.
- **Table Classification**: Classify tables as "good" (hierarchically parseable) or "bad" (requiring vision models).
- **Table Content Analysis**: Generate table summaries, identify key columns, and classify table content.
- **(Optional)** Perform OCR on detected elements using Azure Document Intelligence or Tesseract.
- Save structured document data (layouts, chunks, OCR text, parsed tables) in JSON format.
- Generate paragraph embeddings using OpenAI, Azure OpenAI, or Hugging Face APIs.
- **Hierarchical Document Structure**: Build document hierarchy based on layout analysis.

## Installation

### Prerequisites

- Python 3.10+
- Pip package manager
- (Optional but Recommended) CUDA-capable GPU for YOLO model inference acceleration.

### Steps

1.  **Install the Package:**
    ```bash
    pip install kiwi-pdf-chunker
    ```

## User-Provided Data

This package requires the user to provide certain data externally:

1.  **Input Directory (`input/`):** Place the PDF documents you want to process in a directory (e.g., `input/`). You will need to provide the path to your input file(s) when using the package.
2.  **Models Directory (`models/`):** Download the necessary YOLO model(s) (e.g., `doclayout_yolo_docstructbench_imgsz1024.pt`) and place them in a dedicated directory (e.g., `models/`). The path to this directory (or the specific model file) will be needed by the parser.

## Usage

**Basic Usage:**

```python
from kiwi_pdf_chunker.main import PDFParser

# --- User Configuration ---
input_pdf_path = "path/to/your/input/document.pdf" # Path to user's PDF
model_path = "path/to/your/models/doclayout_yolo.pt" # Path to user's model
output_dir = "path/to/your/output/" # Directory to save results

# Basic parser with OCR
parser = PDFParser(
    yolo_model_path=model_path,
    ocr=True,
    azure_ocr_endpoint="your_azure_endpoint",
    azure_ocr_key="your_azure_key"
)

results = parser.parse_document(input_pdf_path, output_dir=output_dir)
```

**Advanced Usage with Table Classification and Embeddings:**

```python
from kiwi_pdf_chunker import PDFParser

# Advanced parser with table classification and embeddings
parser = PDFParser(
    yolo_model_path=model_path,
    ocr=True,
    azure_ocr_endpoint="your_azure_endpoint",
    azure_ocr_key="your_azure_key",
    embed=True,
    classify_tables=True,
    openai_api_key="your_openai_key",  # For embeddings
    azure_openai_api_key="your_azure_openai_key",  # For table classification
    azure_openai_api_version="2024-02-15-preview",
    azure_openai_endpoint="your_azure_openai_endpoint",
    debug_mode=True
)

results = parser.parse_document(
    input_pdf_path, 
    output_dir=output_dir,
    generate_annotations=True,
    save_bounding_boxes=True,
    use_tesseract=False  # Use Azure OCR instead of Tesseract
)
```

**Using Hugging Face for Embeddings:**

```python
parser = PDFParser(
    yolo_model_path=model_path,
    ocr=True,
    embed=True,
    hf_token="your_huggingface_token",
    hf_endpoint="your_huggingface_endpoint",
    classify_tables=True,
    azure_openai_api_key="your_azure_openai_key",
    azure_openai_endpoint="your_azure_openai_endpoint"
)
```

## Constructor Parameters

The `PDFParser` class accepts the following parameters:

### Core Parameters
- `yolo_model_path` (str, optional): Path to the YOLO model file. If None, uses the default path from config.
- `debug_mode` (bool, optional): Enable debug mode with additional logging and outputs. Defaults to False.
- `container_threshold` (int, optional): Minimum number of contained boxes required to remove a container box.
- `hierarchy` (bool, optional): Enable hierarchy generation. Defaults to True.

### OCR Parameters
- `ocr` (bool, optional): Enable OCR processing. Defaults to False.
- `azure_ocr_endpoint` (str, optional): Azure Document Intelligence endpoint URL.
- `azure_ocr_key` (str, optional): Azure Document Intelligence API key.

### Embedding Parameters
- `embed` (bool, optional): If True, generate embeddings for extracted text. Defaults to False.
- `embedding_model` (str, optional): Name of the OpenAI model for embeddings. Defaults to "text-embedding-3-small".
- `openai_api_key` (str, optional): API key for standard OpenAI service.
- `azure_openai_api_key` (str, optional): API key for Azure OpenAI service.
- `azure_openai_api_version` (str, optional): API version for Azure OpenAI service.
- `azure_openai_endpoint_embedding` (str, optional): Endpoint URL for Azure OpenAI service for text embeddings.
- `hf_token` (str, optional): Hugging Face API token for embeddings.
- `hf_endpoint` (str, optional): Hugging Face endpoint URL for embeddings.

### Table Classification Parameters
- `classify_tables` (bool, optional): If True, classify tables in the document. Defaults to False.
- `table_categories` (list, optional): List of table categories for classification.
- `azure_openai_endpoint` (str, optional): Endpoint URL for Azure OpenAI service for table classification.

## Understanding the Output

After running the parser, the following outputs will typically be available in the specified `output_dir`:

1.  **`boxes.json`**: JSON file containing the detected document structure (element labels, coordinates, confidence).
2.  **`tables.json`**: JSON file containing parsed table data with hierarchical structure for "good" tables and vision model output for "bad" tables.
3.  **`table_screenshots/`**: Directory containing screenshots of detected tables for debugging and verification.
4.  **`annotations/`**: Directory containing annotated images showing the detected elements for each page (if `generate_annotations=True`).
5.  **`boxes/`**: Directory containing individual images for each detected element, organized by page number (if `save_bounding_boxes=True`). This is required for OCR.
6.  **`text.json`**: (Only if `ocr=True`) JSON file containing the extracted text for each element, sorted according to the structure defined in `boxes.json`.
7.  **`embeddings.json`**: (Only if `embed=True`) JSON file containing embeddings for each text element.
8.  **`hierarchy.json`**: (Only if `hierarchy=True`) JSON file containing the document hierarchy structure.

### Table Parsing Features

The library provides advanced table parsing capabilities:

- **Automatic Table Detection**: Uses Docling integration for superior table detection.
- **Table Classification**: Automatically classifies tables as "good" (hierarchically parseable) or "bad" (requiring vision models).
- **Hierarchical Table Parsing**: For "good" tables, builds hierarchical tree structures preserving table relationships.
- **Vision Model Parsing**: For "bad" tables, uses vision models to extract structured data.
- **Table Content Analysis**: When `classify_tables=True`, provides:
  - Table content classification
  - Table summaries
  - Key column identification

If debug mode is enabled (`debug_mode=True`), additional debug images might be saved, typically in a `debug/` subdirectory within the `output_dir`, showing intermediate steps of the parsing process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.