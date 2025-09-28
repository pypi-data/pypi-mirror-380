"""Content fetching and parsing utilities for AWS website"""

import asyncio
import re
from typing import Dict, List, Optional, Any, Set
from urllib.parse import urljoin, urlparse, parse_qs
import httpx
from bs4 import BeautifulSoup, Tag
from readability import Document
import logging
from datetime import datetime
from markdownify import markdownify as md

logger = logging.getLogger(__name__)


class AWSContentFetcher:
    """Fetches and parses content from aws.amazon.com"""
    
    def __init__(self):
        self.base_url = "https://aws.amazon.com"
        self.session = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; AWS-Content-MCP/1.0)",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
            }
        )
        self._content_cache: Dict[str, Dict[str, Any]] = {}
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()
    
    async def search_aws_content(self, query: str, content_type: str = "all") -> List[Dict[str, Any]]:
        """Search for AWS content based on query and type"""
        try:
            search_results = []
            
            # Search different sections based on content type
            if content_type in ["all", "blogs"]:
                blog_results = await self._search_blogs(query)
                search_results.extend(blog_results)
            
            if content_type in ["all", "products"]:
                product_results = await self._search_products(query)
                search_results.extend(product_results)
            
            if content_type in ["all", "solutions"]:
                solution_results = await self._search_solutions(query)
                search_results.extend(solution_results)
            
            if content_type in ["all", "pricing"]:
                pricing_results = await self._search_pricing(query)
                search_results.extend(pricing_results)
            
            # Remove duplicates based on URL
            seen_urls = set()
            unique_results = []
            for result in search_results:
                if result["url"] not in seen_urls:
                    seen_urls.add(result["url"])
                    unique_results.append(result)
            
            return unique_results[:20]  # Limit to top 20 results
            
        except Exception as e:
            logger.error(f"Error searching AWS content: {e}")
            return []
    
    async def _search_blogs(self, query: str) -> List[Dict[str, Any]]:
        """Search AWS blogs"""
        try:
            # AWS Blog search
            search_url = f"{self.base_url}/blogs/"
            response = await self.session.get(search_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Find blog posts
            blog_posts = soup.find_all(['article', 'div'], class_=re.compile(r'blog|post|article'))
            
            for post in blog_posts[:10]:
                title_elem = post.find(['h1', 'h2', 'h3', 'h4'], class_=re.compile(r'title|heading'))
                link_elem = post.find('a', href=True)
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    if query.lower() in title.lower():
                        url = urljoin(self.base_url, link_elem['href'])
                        
                        # Get excerpt
                        excerpt_elem = post.find(['p', 'div'], class_=re.compile(r'excerpt|summary|description'))
                        excerpt = excerpt_elem.get_text(strip=True)[:200] + "..." if excerpt_elem else ""
                        
                        results.append({
                            "title": title,
                            "url": url,
                            "type": "blog",
                            "excerpt": excerpt,
                            "source": "AWS Blog"
                        })
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching blogs: {e}")
            return []
    
    async def _search_products(self, query: str) -> List[Dict[str, Any]]:
        """Search AWS products and services"""
        try:
            # AWS Products page
            products_url = f"{self.base_url}/products/"
            response = await self.session.get(products_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Find product cards/sections
            products = soup.find_all(['div', 'section'], class_=re.compile(r'product|service|card'))
            
            for product in products[:15]:
                title_elem = product.find(['h1', 'h2', 'h3', 'h4'])
                link_elem = product.find('a', href=True)
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    if query.lower() in title.lower() or query.lower() in product.get_text().lower():
                        url = urljoin(self.base_url, link_elem['href'])
                        
                        # Get description
                        desc_elem = product.find(['p', 'div'], class_=re.compile(r'description|summary'))
                        description = desc_elem.get_text(strip=True)[:200] + "..." if desc_elem else ""
                        
                        results.append({
                            "title": title,
                            "url": url,
                            "type": "product",
                            "excerpt": description,
                            "source": "AWS Products"
                        })
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching products: {e}")
            return []
    
    async def _search_solutions(self, query: str) -> List[Dict[str, Any]]:
        """Search AWS solutions"""
        try:
            solutions_url = f"{self.base_url}/solutions/"
            response = await self.session.get(solutions_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Find solution cards
            solutions = soup.find_all(['div', 'section'], class_=re.compile(r'solution|card'))
            
            for solution in solutions[:10]:
                title_elem = solution.find(['h1', 'h2', 'h3', 'h4'])
                link_elem = solution.find('a', href=True)
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    if query.lower() in title.lower() or query.lower() in solution.get_text().lower():
                        url = urljoin(self.base_url, link_elem['href'])
                        
                        desc_elem = solution.find(['p', 'div'], class_=re.compile(r'description|summary'))
                        description = desc_elem.get_text(strip=True)[:200] + "..." if desc_elem else ""
                        
                        results.append({
                            "title": title,
                            "url": url,
                            "type": "solution",
                            "excerpt": description,
                            "source": "AWS Solutions"
                        })
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching solutions: {e}")
            return []
    
    async def _search_pricing(self, query: str) -> List[Dict[str, Any]]:
        """Search AWS pricing information"""
        try:
            pricing_url = f"{self.base_url}/pricing/"
            response = await self.session.get(pricing_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Find pricing sections
            pricing_sections = soup.find_all(['div', 'section'], class_=re.compile(r'pricing|price'))
            
            for section in pricing_sections[:10]:
                title_elem = section.find(['h1', 'h2', 'h3', 'h4'])
                link_elem = section.find('a', href=True)
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    if query.lower() in title.lower() or query.lower() in section.get_text().lower():
                        url = urljoin(self.base_url, link_elem['href'])
                        
                        desc_elem = section.find(['p', 'div'], class_=re.compile(r'description|summary'))
                        description = desc_elem.get_text(strip=True)[:200] + "..." if desc_elem else ""
                        
                        results.append({
                            "title": title,
                            "url": url,
                            "type": "pricing",
                            "excerpt": description,
                            "source": "AWS Pricing"
                        })
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching pricing: {e}")
            return []
    
    async def get_full_content(self, url: str) -> Dict[str, Any]:
        """Get full content from a specific AWS URL"""
        try:
            # Check cache first
            if url in self._content_cache:
                cached = self._content_cache[url]
                # Cache for 1 hour
                if (datetime.now() - cached["timestamp"]).seconds < 3600:
                    return cached["content"]
            
            response = await self.session.get(url)
            response.raise_for_status()
            
            # Use readability to extract main content
            doc = Document(response.text)
            main_content = doc.content()
            
            # Parse with BeautifulSoup for better structure
            soup = BeautifulSoup(main_content, 'html.parser')
            
            # Extract structured information
            title = soup.find(['h1', 'title'])
            title_text = title.get_text(strip=True) if title else "No title found"
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()
            
            # Get clean text content
            text_content = soup.get_text()
            
            # Convert to markdown for better formatting
            markdown_content = md(str(soup), heading_style="ATX")
            
            # Extract metadata
            meta_description = ""
            original_soup = BeautifulSoup(response.text, 'html.parser')
            meta_desc = original_soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                meta_description = meta_desc.get('content', '')
            
            # Extract publication date if available
            pub_date = None
            date_elem = original_soup.find(['time', 'span'], class_=re.compile(r'date|published'))
            if date_elem:
                pub_date = date_elem.get_text(strip=True)
            
            content_data = {
                "url": url,
                "title": title_text,
                "content": text_content,
                "markdown_content": markdown_content,
                "meta_description": meta_description,
                "publication_date": pub_date,
                "word_count": len(text_content.split()),
                "extracted_at": datetime.now().isoformat()
            }
            
            # Cache the result
            self._content_cache[url] = {
                "content": content_data,
                "timestamp": datetime.now()
            }
            
            return content_data
            
        except Exception as e:
            logger.error(f"Error fetching content from {url}: {e}")
            return {
                "url": url,
                "error": str(e),
                "extracted_at": datetime.now().isoformat()
            }
    
    async def analyze_content_similarity(self, content1: str, content2: str) -> float:
        """Analyze similarity between two pieces of content"""
        try:
            # Simple similarity based on common words
            words1 = set(content1.lower().split())
            words2 = set(content2.lower().split())
            
            if not words1 or not words2:
                return 0.0
            
            intersection = words1.intersection(words2)
            union = words1.union(words2)
            
            return len(intersection) / len(union) if union else 0.0
            
        except Exception as e:
            logger.error(f"Error analyzing content similarity: {e}")
            return 0.0
    
    async def get_aws_service_overview(self) -> Dict[str, Any]:
        """Get overview of all AWS services"""
        try:
            products_url = f"{self.base_url}/products/"
            response = await self.session.get(products_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            services = {}
            categories = soup.find_all(['div', 'section'], class_=re.compile(r'category|group'))
            
            for category in categories:
                category_title = category.find(['h1', 'h2', 'h3'])
                if category_title:
                    cat_name = category_title.get_text(strip=True)
                    
                    service_links = category.find_all('a', href=True)
                    category_services = []
                    
                    for link in service_links:
                        service_name = link.get_text(strip=True)
                        service_url = urljoin(self.base_url, link['href'])
                        
                        if service_name and '/products/' in service_url:
                            category_services.append({
                                "name": service_name,
                                "url": service_url
                            })
                    
                    if category_services:
                        services[cat_name] = category_services
            
            return {
                "services_by_category": services,
                "total_services": sum(len(services) for services in services.values()),
                "extracted_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error getting AWS service overview: {e}")
            return {"error": str(e)}