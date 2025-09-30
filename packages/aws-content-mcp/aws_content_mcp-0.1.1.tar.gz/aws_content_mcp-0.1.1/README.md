# AWS Content MCP Server

A comprehensive Model Context Protocol (MCP) server for retrieving and analyzing content from aws.amazon.com. This server provides dynamic, real-time access to AWS blogs, product information, solutions, pricing, and other content without hallucination.

## Features

- **Dynamic Content Retrieval**: Real-time fetching from aws.amazon.com
- **Comprehensive Search**: Search across blogs, products, solutions, and pricing
- **Full Content Analysis**: Extract complete content with detailed analysis
- **Duplicate Detection**: Identify similar content and prevent duplication
- **Content Comparison**: Compare different AWS content pieces
- **Service Overview**: Get comprehensive AWS service listings
- **No Hallucination**: All information is fetched directly from AWS sources

## Installation

### Using uvx (Recommended)

```bash
uvx aws-content-mcp
```

### Using pip

```bash
pip install aws-content-mcp
```

### From Source

```bash
git clone https://github.com/yourusername/aws-content-mcp.git
cd aws-content-mcp
pip install -e .
```

## Usage

### As MCP Server

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "aws-content": {
      "command": "uvx",
      "args": ["aws-content-mcp"]
    }
  }
}
```

### Available Tools

#### 1. search_aws_content
Search for AWS content across different categories.

**Parameters:**
- `query` (required): Search query
- `content_type` (optional): "all", "blogs", "products", "solutions", or "pricing"

**Example:**
```json
{
  "query": "serverless computing",
  "content_type": "blogs"
}
```

#### 2. get_full_aws_content
Get complete content from a specific AWS URL with detailed analysis.

**Parameters:**
- `url` (required): AWS URL to fetch content from

**Example:**
```json
{
  "url": "https://aws.amazon.com/blogs/compute/serverless-computing-with-lambda/"
}
```

#### 3. analyze_aws_blog_ideas
Analyze blog ideas for duplication and provide content recommendations.

**Parameters:**
- `topic` (required): Blog topic to analyze
- `check_duplicates` (optional): Whether to check for duplicates (default: true)

**Example:**
```json
{
  "topic": "machine learning on AWS",
  "check_duplicates": true
}
```

#### 4. get_aws_service_overview
Get comprehensive overview of all AWS services organized by category.

**Parameters:** None

#### 5. compare_aws_content
Compare two pieces of AWS content for similarity and differences.

**Parameters:**
- `url1` (required): First AWS URL to compare
- `url2` (required): Second AWS URL to compare

## Use Cases

### 1. Content Research
- Research AWS services and solutions
- Find relevant blog posts and documentation
- Get pricing information for AWS services

### 2. Blog Content Planning
- Check for duplicate blog ideas
- Analyze existing content on topics
- Get recommendations for unique angles

### 3. Competitive Analysis
- Compare different AWS solutions
- Analyze content similarities
- Track AWS product updates

### 4. Documentation Discovery
- Find comprehensive service documentation
- Discover best practices and guides
- Access latest AWS announcements

## Architecture

The MCP server consists of several key components:

### Content Fetcher (`content_fetcher.py`)
- Handles HTTP requests to aws.amazon.com
- Parses HTML content using BeautifulSoup
- Extracts clean content using readability
- Implements caching for performance
- Provides content similarity analysis

### Server (`server.py`)
- Implements MCP protocol
- Defines available tools and their schemas
- Handles tool execution and error management
- Formats responses for optimal readability

## Technical Details

### Dependencies
- `mcp`: Model Context Protocol implementation
- `httpx`: Async HTTP client for web requests
- `beautifulsoup4`: HTML parsing and content extraction
- `readability-lxml`: Main content extraction
- `markdownify`: HTML to Markdown conversion
- `pydantic`: Data validation and serialization

### Content Processing Pipeline
1. **Search**: Query AWS website sections
2. **Extract**: Use readability to get main content
3. **Parse**: Structure content with BeautifulSoup
4. **Clean**: Remove navigation, ads, and scripts
5. **Format**: Convert to Markdown for better readability
6. **Cache**: Store results for performance

### Error Handling
- Comprehensive error catching and logging
- Graceful degradation for network issues
- Informative error messages for users
- Retry logic for transient failures

## Development

### Setup Development Environment

```bash
git clone https://github.com/yourusername/aws-content-mcp.git
cd aws-content-mcp
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/
isort src/
```

### Type Checking

```bash
mypy src/
```

## Publishing to PyPI

### Build Package

```bash
python -m build
```

### Upload to PyPI

```bash
python -m twine upload dist/*
```

## Configuration

The server can be configured through environment variables:

- `AWS_CONTENT_CACHE_TTL`: Cache time-to-live in seconds (default: 3600)
- `AWS_CONTENT_MAX_RESULTS`: Maximum search results (default: 20)
- `AWS_CONTENT_TIMEOUT`: HTTP request timeout (default: 30)

## Limitations

- Only works with publicly accessible aws.amazon.com content
- Rate limited by AWS website response times
- Content structure may change as AWS updates their website
- Some dynamic content may not be fully captured

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- GitHub Issues: https://github.com/yourusername/aws-content-mcp/issues
- Documentation: https://github.com/yourusername/aws-content-mcp/wiki

## Changelog

### v0.1.0
- Initial release
- Basic content fetching and search
- Blog analysis and duplicate detection
- Service overview functionality
- Content comparison tools