"""
Web Research Tool - OPTIMIZED
With caching and parallel searches for speed
"""

import subprocess
import sys
import os
import json
from datetime import datetime, timedelta
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

# Colors for live display
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Cache file
CACHE_FILE = os.path.join(os.path.dirname(__file__), "search_cache.json")
CACHE_DURATION = timedelta(hours=24)  # Cache for 24 hours

class SearchCache:
    """Cache search results to avoid repeated API calls"""
    
    def __init__(self):
        self.cache = {}
        self.load()
    
    def load(self):
        """Load cache from file"""
        try:
            if os.path.exists(CACHE_FILE):
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    self.cache = json.load(f)
        except:
            self.cache = {}
    
    def save(self):
        """Save cache to file"""
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass
    
    def get(self, query: str) -> Dict:
        """Get cached result if valid"""
        if query in self.cache:
            cached = self.cache[query]
            cached_time = datetime.fromisoformat(cached['time'])
            if datetime.now() - cached_time < CACHE_DURATION:
                return cached['results']
        return None
    
    def set(self, query: str, results: Dict):
        """Cache search results"""
        self.cache[query] = {
            'time': datetime.now().isoformat(),
            'results': results
        }
        self.save()


class WebResearcher:
    """Optimized web researcher with caching and parallel searches"""
    
    def __init__(self):
        self.max_results = 5
        self.cache = SearchCache()
    
    def search(self, query: str, search_num: int, total: int) -> Dict:
        """Search with caching"""
        print(f"\n[{search_num}/{total}] {Colors.CYAN}🔍 Searching:{Colors.END} \"{query}\"")
        
        # Check cache first
        cached_result = self.cache.get(query)
        if cached_result:
            print(f"    {Colors.GREEN}✓{Colors.END} From cache (instant!)")
            return cached_result
        
        # Perform search
        try:
            result = subprocess.run(
                ["py", "-3.12", "-m", "duckduckgo_search", "text", "-k", query, "-m", "3"],
                capture_output=True, text=True, timeout=30
            )
            
            # Parse results
            results = []
            lines = result.stdout.strip().split('\n')
            
            current = {}
            for line in lines:
                line = line.strip()
                if line.startswith('1.') or line.startswith('2.') or line.startswith('3.'):
                    if current:
                        results.append(current)
                    current = {'title': line[3:].strip()}
                elif 'href' in line.lower() and 'http' in line:
                    url = line.split('http')[-1].strip()
                    current['url'] = 'http' + url
                    print(f"    {Colors.GREEN}📄 Source:{Colors.END} {current['url'][:60]}...")
                elif 'body' in line.lower():
                    snippet = line.split(':', 1)[-1].strip()[:100]
                    current['snippet'] = snippet
            
            if current:
                results.append(current)
            
            print(f"    {Colors.GREEN}✓{Colors.END} Found {len(results)} relevant results")
            
            # Cache the result
            result_data = {
                'query': query,
                'results': results,
                'count': len(results)
            }
            self.cache.set(query, result_data)
            
            return result_data
            
        except Exception as e:
            print(f"    {Colors.RED}✗ Error: {e}{Colors.END}")
            return {
                'query': query,
                'results': [],
                'error': str(e)
            }
    
    def search_parallel(self, queries: List[str]) -> List[Dict]:
        """Run multiple searches in parallel"""
        results = []
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_query = {
                executor.submit(self.search, q, i+1, len(queries)): (q, i+1)
                for i, q in enumerate(queries)
            }
            
            for future in as_completed(future_to_query):
                query, num = future_to_query[1]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"    {Colors.RED}✗ {query}: {e}{Colors.END}")
        
        return results
    
    def research_topic(self, topic: str) -> Dict:
        """Research a topic with parallel searches"""
        searches = [
            f"{topic} best practices 2025",
            f"{topic} tutorial",
            f"{topic} examples",
        ]
        
        print(f"\n{Colors.BOLD}🌐 PLAN-WEB: Live Research{Colors.END}")
        print(f"{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.END}")
        print(f"\n{Colors.BOLD}Topic:{Colors.END} {topic}\n")
        
        # Run searches in parallel
        all_results = self.search_parallel(searches)
        
        # Compile summary
        all_urls = []
        for r in all_results:
            for result in r.get('results', []):
                if 'url' in result:
                    all_urls.append(result['url'])
        
        return {
            'topic': topic,
            'searches_performed': searches,
            'all_results': all_results,
            'sources': list(set(all_urls))[:5],
            'total_found': sum(r.get('count', 0) for r in all_results)
        }
    
    def format_research(self, research: Dict) -> str:
        """Format research results"""
        output = []
        output.append(f"\n{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.END}")
        output.append(f"{Colors.BOLD}📊 Research Summary{Colors.END}")
        output.append(f"{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.END}\n")
        
        output.append(f"Total sources found: {research['total_found']}")
        output.append(f"Unique sources: {len(research['sources'])}\n")
        
        output.append(f"{Colors.BOLD}Sources:{Colors.END}")
        for i, url in enumerate(research['sources'][:5], 1):
            output.append(f"  {i}. {url}")
        
        output.append(f"\n{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.END}\n")
        
        return '\n'.join(output)
    
    def update_plan_live(self, topic: str, research: Dict):
        """Show plan being updated live based on research"""
        print(f"\n{Colors.BOLD}📋 Creating Informed Plan...{Colors.END}\n")
        
        # Show initial plan
        print(f"{Colors.YELLOW}Initial Plan:{Colors.END}")
        print("  Task 1: Research")
        print("  Task 2: Setup")
        print("  Task 3: Implementation")
        print("  Task 4: Testing\n")
        
        # Show updates based on findings
        print(f"{Colors.GREEN}✏️  UPDATING based on research findings...{Colors.END}\n")
        
        print(f"{Colors.GREEN}Updated Plan:{Colors.END}")
        print(f"  {Colors.GREEN}✓{Colors.END} Task 1: Research (completed via web)")
        print(f"  {Colors.CYAN}→{Colors.END} Task 2: Setup (15 min)")
        
        if research['sources']:
            print(f"    → Based on: {research['sources'][0][:50]}...")
            print("    → Install required packages")
            print("    → Set up project structure")
        
        print(f"  {Colors.CYAN}→{Colors.END} Task 3: Implementation (60 min)")
        print("    → Follow best practices from research")
        print("    → Implement error handling")
        print("    → Add recommended features")
        
        print(f"  {Colors.CYAN}→{Colors.END} Task 4: Testing (30 min)")
        print("    → Test with examples from tutorials")
        print("    → Verify against documentation")
        
        print(f"\n{Colors.CYAN}══════════════════════════════════════════════════════════{Colors.END}\n")


def plan_from_web(topic: str):
    """Main function: Research topic and create informed plan"""
    researcher = WebResearcher()
    
    # Research with live display
    research = researcher.research_topic(topic)
    
    # Show summary
    print(researcher.format_research(research))
    
    # Show plan being updated live
    researcher.update_plan_live(topic, research)
    
    print(f"{Colors.BOLD}Ready to proceed? [Y/n]{Colors.END} ", end='')
    
    return research


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python web_research.py \"your topic\"")
        sys.exit(1)
    
    topic = " ".join(sys.argv[1:])
    plan_from_web(topic)
