"""
File Processor - Multi-format file processing for AI applications

Supports JSON, JSONL, CSV, TXT formats with metadata extraction.
"""

import json
import csv
import os
import asyncio
from pathlib import Path
from typing import Dict, List, Any, Iterator, Optional, Union, AsyncIterator
import logging
import aiofiles

logger = logging.getLogger(__name__)


class FileProcessor:
    """Process various file formats to extract structured data"""
    
    def __init__(self, supported_extensions: Optional[set] = None):
        """
        Initialize file processor
        
        Args:
            supported_extensions: Set of supported file extensions (default: .json, .jsonl, .csv, .txt)
        """
        self.supported_extensions = supported_extensions or {'.json', '.jsonl', '.csv', '.txt'}
    
    async def process_file_async(self, file_path: Union[str, Path]) -> AsyncIterator[Dict[str, Any]]:
        """
        Process a file and yield structured data
        
        Args:
            file_path: Path to the file to process
            
        Yields:
            Dict containing data and metadata
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return
        
        extension = file_path.suffix.lower()
        
        try:
            if extension == '.json':
                async for item in self._process_json_async(file_path):
                    yield item
            elif extension == '.jsonl':
                async for item in self._process_jsonl_async(file_path):
                    yield item
            elif extension == '.csv':
                async for item in self._process_csv_async(file_path):
                    yield item
            elif extension == '.txt':
                async for item in self._process_txt_async(file_path):
                    yield item
            else:
                logger.warning(f"Unsupported file type: {extension}")
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
    
    async def _process_json_async(self, file_path: Path) -> AsyncIterator[Dict[str, Any]]:
        """Process JSON file"""
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            try:
                content = await f.read()
                data = json.loads(content)
                
                # Handle different JSON structures
                if isinstance(data, list):
                    # Array of items
                    for i, item in enumerate(data):
                        yield {
                            'data': item,
                            'source_file': str(file_path),
                            'index': i,
                            'metadata': await self._extract_file_metadata_async(file_path)
                        }
                elif isinstance(data, dict):
                    # Single item or structured data
                    if self._is_multi_item_structure(data):
                        # Multiple items in a structure
                        items = self._extract_items_from_structure(data)
                        for i, item in enumerate(items):
                            yield {
                                'data': item,
                                'source_file': str(file_path),
                                'index': i,
                                'metadata': await self._extract_file_metadata_async(file_path)
                            }
                    else:
                        # Single item
                        yield {
                            'data': data,
                            'source_file': str(file_path),
                            'index': 0,
                            'metadata': await self._extract_file_metadata_async(file_path)
                        }
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in {file_path}: {e}")
    
    async def _process_jsonl_async(self, file_path: Path) -> AsyncIterator[Dict[str, Any]]:
        """Process JSONL (JSON Lines) file"""
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            i = 0
            async for line in f:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    data = json.loads(line)
                    yield {
                        'data': data,
                        'source_file': str(file_path),
                        'index': i,
                        'metadata': await self._extract_file_metadata_async(file_path)
                    }
                    i += 1
                except json.JSONDecodeError as e:
                    logger.error(f"Invalid JSON line {i+1} in {file_path}: {e}")
                    i += 1
    
    async def _process_csv_async(self, file_path: Path) -> AsyncIterator[Dict[str, Any]]:
        """Process CSV file"""
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            # Read sample to detect delimiter
            sample = await f.read(1024)
            await f.seek(0)
            
            delimiter = ','
            if '\t' in sample and sample.count('\t') > sample.count(','):
                delimiter = '\t'
            
            # Read all content and process with csv module
            content = await f.read()
            lines = content.splitlines()
            
            if not lines:
                return
            
            reader = csv.DictReader(lines, delimiter=delimiter)
            metadata = await self._extract_file_metadata_async(file_path)
            
            for i, row in enumerate(reader):
                yield {
                    'data': dict(row),
                    'source_file': str(file_path),
                    'index': i,
                    'metadata': metadata
                }
    
    async def _process_txt_async(self, file_path: Path) -> AsyncIterator[Dict[str, Any]]:
        """Process text file"""
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            content = (await f.read()).strip()
            
            if not content:
                return
            
            # Try to split into multiple sections if separated by blank lines
            sections = content.split('\n\n')
            
            for i, section in enumerate(sections):
                section = section.strip()
                if section:
                    yield {
                        'data': {'content': section},
                        'source_file': str(file_path),
                        'index': i,
                        'metadata': await self._extract_file_metadata_async(file_path)
                    }
    
    def _is_multi_item_structure(self, data: dict) -> bool:
        """Check if dict contains multiple items in known structures"""
        # Common patterns for multi-item structures
        multi_item_keys = ['conversations', 'items', 'data', 'records', 'entries']
        return any(key in data and isinstance(data[key], list) for key in multi_item_keys)
    
    def _extract_items_from_structure(self, data: dict) -> List[Any]:
        """Extract items from structured data"""
        multi_item_keys = ['conversations', 'items', 'data', 'records', 'entries']
        for key in multi_item_keys:
            if key in data and isinstance(data[key], list):
                return data[key]
        return [data]  # Fallback to single item
    
    async def _extract_file_metadata_async(self, file_path: Path) -> Dict[str, Any]:
        """Extract metadata from file path and stats"""
        stat = file_path.stat()
        
        return {
            'filename': file_path.name,
            'file_size': stat.st_size,
            'created_time': stat.st_ctime,
            'modified_time': stat.st_mtime,
            'directory': str(file_path.parent),
            'extension': file_path.suffix
        }
    
    def _extract_file_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Sync version of metadata extraction"""
        return asyncio.run(self._extract_file_metadata_async(file_path))
    
    def scan_directory(self, directory: Union[str, Path], recursive: bool = True) -> Iterator[Path]:
        """
        Scan directory for supported files
        
        Args:
            directory: Directory to scan
            recursive: Whether to scan subdirectories
            
        Yields:
            Path objects for supported files
        """
        directory = Path(directory)
        
        if not directory.exists():
            logger.error(f"Directory not found: {directory}")
            return
        
        if recursive:
            pattern = "**/*"
        else:
            pattern = "*"
        
        for file_path in directory.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower() in self.supported_extensions:
                yield file_path
    
    def get_directory_stats(self, directory: Union[str, Path]) -> Dict[str, Any]:
        """Get statistics about files in directory"""
        directory = Path(directory)
        
        stats = {
            'total_files': 0,
            'by_extension': {},
            'total_size': 0,
            'directories': set()
        }
        
        for file_path in self.scan_directory(directory):
            stats['total_files'] += 1
            stats['total_size'] += file_path.stat().st_size
            stats['directories'].add(str(file_path.parent))
            
            ext = file_path.suffix.lower()
            stats['by_extension'][ext] = stats['by_extension'].get(ext, 0) + 1
        
        stats['directories'] = len(stats['directories'])
        return stats
    
    async def process_directory_async(self, directory: Union[str, Path], recursive: bool = True) -> AsyncIterator[Dict[str, Any]]:
        """Process all supported files in a directory concurrently"""
        semaphore = asyncio.Semaphore(5)  # Limit concurrent file processing
        
        async def process_single_file(file_path):
            async with semaphore:
                results = []
                async for item in self.process_file_async(file_path):
                    results.append(item)
                return results
        
        tasks = []
        for file_path in self.scan_directory(directory, recursive):
            tasks.append(process_single_file(file_path))
        
        # Process files concurrently
        for completed_task in asyncio.as_completed(tasks):
            results = await completed_task
            for item in results:
                yield item
    
    # Sync compatibility wrappers
    def process_file(self, file_path: Union[str, Path]) -> Iterator[Dict[str, Any]]:
        """Sync wrapper for process_file_async"""
        async def _collect_results():
            results = []
            async for item in self.process_file_async(file_path):
                results.append(item)
            return results
        
        results = asyncio.run(_collect_results())
        yield from results
    
    def process_directory(self, directory: Union[str, Path], recursive: bool = True) -> Iterator[Dict[str, Any]]:
        """Sync wrapper for process_directory_async"""
        async def _collect_results():
            results = []
            async for item in self.process_directory_async(directory, recursive):
                results.append(item)
            return results
        
        results = asyncio.run(_collect_results())
        yield from results