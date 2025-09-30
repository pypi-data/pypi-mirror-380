# Synthetic Data Pipeline

AI-powered synthetic data generation pipeline with web search and topic extraction.

## Installation

Install the package using pip:

    pip install synthetic-data-pipeline

## Requirements

- Python >= 3.8
- API Keys for: Gemini, Tavily, ScraperAPI

## Quick Start

**Step 1: Create Configuration File**

Create a `.env` file in your project directory:

    GEMINI_API_KEY=your_gemini_api_key_here
    TAVILY_API_KEY=your_tavily_api_key_here
    SCRAPERAPI_API_KEY=your_scraper_api_key_here
    OUTPUT_DIR=/path/to/your/output

Note: The `.env` file must be in the directory where you run your scripts.

**Step 2: Use in Python Code**

Basic usage example:

    from synthetic_data_pipeline import generate_synthetic_data
    
    result = generate_synthetic_data("Generate 100 QA pairs about Python")

Advanced usage with custom parameters:

    generate_synthetic_data(
        user_query="prompt",
        refined_queries_count=20,
        search_results_per_query=5,
        rows_per_subtopic=5
    )

**Step 3: Use CLI**

Command line usage:

    synthetic-data "Generate data about machine learning"

## Configuration

**Environment Variables**

| Variable | Required | Description |
|----------|----------|-------------|
| GEMINI_API_KEY | Yes | Google Gemini API key |
| TAVILY_API_KEY | Yes | Tavily search API key |
| SCRAPERAPI_API_KEY | Yes | ScraperAPI key |
| OUTPUT_DIR | Yes | Output directory path |

**Custom Output Location**

Set via environment variable in `.env`:

    OUTPUT_DIR=/custom/path

Or via code:

    generate_synthetic_data("prompt")

Or via CLI:

    synthetic-data "prompt"

## API Reference

### `generate_synthetic_data(user_query: str, refined_queries_count: Optional[int] = None, search_results_per_query: Optional[int] = None, rows_per_subtopic: Optional[int] = None, gemini_model_name: Optional[str] = None)`

Generate synthetic data based on a natural language prompt. The `user_query` is parsed to automatically determine the number of samples, data type, language, and a detailed description of the data to be generated.

**Parameters:**
- `user_query` (str): **Required**. A natural language description of the data you want to generate. This query should implicitly or explicitly contain:
    - **Number of samples**: The total count of data entries to generate (e.g., "100").
    - **Data type**: The structure or format of the data (e.g., "QA pairs", "product reviews", "customer support conversations").
    - **Language**: The desired language for the generated data (e.g., "English", "French", "Egyptian_Arabic").
    - **Description**: A detailed explanation of the data's content and context.
- `refined_queries_count` (int, optional): Number of refined search queries to generate. Defaults to a value from `.env` or internal settings.
- `search_results_per_query` (int, optional): Number of web search results to consider per refined query. Defaults to a value from `.env` or internal settings.
- `rows_per_subtopic` (int, optional): Number of synthetic data rows to generate per extracted subtopic. Defaults to a value from `.env` or internal settings.
- `gemini_model_name` (str, optional): The name of the Gemini model to use (e.g., "gemini-pro", "gemini-1.5-flash"). Defaults to "gemini-2.5-flash" or a value from `.env`.

**Returns:**
- `dict`: A dictionary containing the status of the data generation, the output location of the generated files, and other relevant metadata.

**Example:**
```python
from synthetic_data_pipeline import generate_synthetic_data

result = generate_synthetic_data(
    user_query="Generate 50 customer reviews in French for a high-end restaurant, including ratings and short text comments.",
    refined_queries_count=15,
    search_results_per_query=7,
    rows_per_subtopic=3
)
print(f"Generated data saved to: {result['output_location']}")
```

## Development

**Local Installation**

    git clone https://github.com/yourusername/synthetic-data-pipeline
    cd synthetic-data-pipeline
    pip install -e .

## License

MIT License - see LICENSE file for details.

## Support

- Issues: GitHub Issues
- Email: omarjooo595@gmail.com