"""
Web Scraping Tool for AI Orchestrator
Uses BeautifulSoup for content extraction
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

class WebScraper:
    """Simple web scraper for research and information gathering"""
    
    def __init__(self, respect_robots=True):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.respect_robots = respect_robots
    
    def fetch_page(self, url: str) -> str:
        """Fetch and extract main content from a webpage"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Remove script and style elements
            for script in soup(['script', 'style', 'nav', 'header', 'footer']):
                script.decompose()
            
            # Get main content
            main = soup.find('main') or soup.find('article') or soup.body
            if not main:
                main = soup
            
            # Extract text
            text = main.get_text(separator='\n', strip=True)
            
            # Clean up whitespace
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            content = '\n'.join(lines[:100])  # Limit to first 100 lines
            
            return content
            
        except Exception as e:
            return f"Error fetching page: {e}"
    
    def extract_links(self, url: str, same_domain_only=True) -> list:
        """Extract all links from a page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            links = []
            
            parsed_base = urlparse(url)
            
            for link in soup.find_all('a', href=True):
                href = link['href'].strip()
                full_url = urljoin(url, href)
                parsed = urlparse(full_url)
                
                # Filter same domain if requested
                if same_domain_only and parsed.netloc != parsed_base.netloc:
                    continue
                
                # Skip non-http links
                if not parsed.scheme.startswith('http'):
                    continue
                
                links.append({
                    'url': full_url,
                    'text': link.get_text(strip=True)[:100]
                })
            
            return links[:20]  # Limit to 20 links
            
        except Exception as e:
            return []
    
    def search_code(self, url: str, pattern: str = None) -> dict:
        """Search for code blocks on a page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Find code blocks
            code_blocks = []
            
            # Common code block tags
            for tag in ['code', 'pre', 'div[class*="code"]', 'div[class*="highlight"]']:
                for element in soup.select(tag):
                    code = element.get_text(strip=True)
                    if code:
                        code_blocks.append({
                            'code': code[:2000],  # Limit length
                            'language': element.get('class', ['unknown'])[0] if element.get('class') else 'unknown'
                        })
            
            return {
                'url': url,
                'code_blocks': code_blocks[:10],  # Limit to 10 blocks
                'total_found': len(code_blocks)
            }
            
        except Exception as e:
            return {'error': str(e)}


# CLI interface for testing
if __name__ == "__main__":
    import sys
    
    scraper = WebScraper()
    
    if len(sys.argv) < 2:
        print("Usage: python web_scraper.py <url> [search_pattern]")
        print("Example: python web_scraper.py https://example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    pattern = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"\n🔍 Fetching: {url}\n")
    
    if pattern:
        result = scraper.search_code(url, pattern)
        print(f"Found {result.get('total_found', 0)} code blocks")
        for block in result.get('code_blocks', [])[:3]:
            print(f"\n```{block['language']}")
            print(block['code'][:500])
            print("```")
    else:
        content = scraper.fetch_page(url)
        print(content[:2000])
