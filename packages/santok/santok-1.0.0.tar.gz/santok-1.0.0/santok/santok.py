#!/usr/bin/env python3
"""
SanTOK Tokenization Engine - A Complete Text Tokenization Module
Convert your tokenizer into a reusable Python module
"""

class TextTokenizationEngine:
    """
    A complete text tokenization system with mathematical analysis
    """
    
    def __init__(self, random_seed=12345, embedding_bit=False, normalize_case=True, remove_punctuation=False, collapse_repetitions=0):
        """
        Initialize the tokenization engine with configuration parameters
        
        Args:
            random_seed (int): Deterministic seed for reproducible tokenization
            embedding_bit (bool): Enable embedding bit for additional variation in calculations
            normalize_case (bool): Convert input text to lowercase for case-insensitive processing
            remove_punctuation (bool): Strip punctuation and special characters from input
            collapse_repetitions (int): Collapse repeated character sequences (0=disabled, 1=run-aware, N=collapse to N)
        """
        self.random_seed = random_seed
        self.embedding_bit = embedding_bit
        self.normalize_case = normalize_case
        self.remove_punctuation = remove_punctuation
        self.collapse_repetitions = collapse_repetitions
        
        # Initialize alphabet table for fast lookup
        self._init_alphabetic_table()
    
    def _init_alphabetic_table(self):
        """Initialize alphabet table for fast alphabetic value lookup"""
        self._alphabet_table = []
        for i in range(26):
            self._alphabet_table.append((i % 9) + 1)
    
    def _normalize_case(self, text):
        """Convert text to lowercase for case-insensitive processing"""
        result = ""
        for char in text:
            if 65 <= ord(char) <= 90:  # A-Z
                result += chr(ord(char) + 32)  # Convert to lowercase
            else:
                result += char
        return result
    
    def _remove_punctuation(self, text):
        """Remove punctuation and special characters, preserve alphanumeric characters and whitespace"""
        result = ""
        for char in text:
            if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122) or (48 <= ord(char) <= 57) or char == ' ':
                result += char
        return result
    
    def _normalize_whitespace(self, text):
        """Normalize whitespace by collapsing multiple consecutive spaces into single space"""
        result = ""
        prev_was_space = False
        for char in text:
            if char == ' ':
                if not prev_was_space:
                    result += char
                    prev_was_space = True
            else:
                result += char
                prev_was_space = False
        return result
    
    def _preprocess_text(self, text):
        """
        Preprocess input text according to configuration parameters
        
        Args:
            text (str): Raw input text to preprocess
            
        Returns:
            str: Preprocessed text ready for tokenization
        """
        processed_text = text
        
        if self.normalize_case:
            processed_text = self._normalize_case(processed_text)
        
        if self.remove_punctuation:
            processed_text = self._remove_punctuation(processed_text)
        
        processed_text = self._normalize_whitespace(processed_text)
        
        return processed_text
    
    def _calculate_weighted_sum(self, text):
        """
        Calculate weighted character sum using position-based multiplication
        
        Args:
            text (str): Input text for weighted sum calculation
            
        Returns:
            int: Weighted sum value
        """
        total = 0
        i = 1
        for char in text:
            total += ord(char) * i
            i += 1
        return total
    
    def _compute_digital_root(self, n):
        """
        Compute digital root using 9-centric reduction algorithm
        
        Args:
            n (int): Integer value to reduce to digital root
            
        Returns:
            int: Digital root value (1-9)
        """
        if n <= 0:
            return 9
        return ((n - 1) % 9) + 1
    
    def _compute_hash(self, text):
        """
        Compute hash value using polynomial rolling hash algorithm
        
        Args:
            text (str): Input text for hash computation
            
        Returns:
            int: Computed hash value
        """
        h = 0
        for char in text:
            h = h * 31 + ord(char)
        return h
    
    def _generate_frontend_digit(self, text):
        """
        Generate frontend digit using weighted sum and hash-based methods
        
        Args:
            text (str): Input text for frontend digit generation
            
        Returns:
            int: Frontend digit value (1-9)
        """
        # Method 1: Weighted sum + digital root
        weighted_sum = self._calculate_weighted_sum(text)
        weighted_digit = self._compute_digital_root(weighted_sum)
        
        # Method 2: Hash + modulo 10
        hash_value = self._compute_hash(text)
        hash_digit = hash_value % 10
        
        # Combination: (Weighted_Digit × 9 + Hash_Digit) % 9 + 1
        combined_digit = (weighted_digit * 9 + hash_digit) % 9 + 1
        return combined_digit
    
    def _tokenize_by_whitespace(self, text):
        """
        Tokenize input text by whitespace delimiters
        
        Args:
            text (str): Input text for whitespace-based tokenization
            
        Returns:
            list: List of token strings
        """
        tokens = []
        current_token = ""
        
        for char in text:
            if char == ' ':
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
        
        if current_token:
            tokens.append(current_token)
        
        return tokens
    
    def _tokenize_by_character(self, text):
        """
        Tokenize input text into individual character units
        
        Args:
            text (str): Input text for character-level tokenization
            
        Returns:
            list: List of character token strings
        """
        return list(text)
    
    def _tokenize_by_word_boundary(self, text):
        """
        Tokenize input text by word boundaries (alphabetic characters only)
        
        Args:
            text (str): Input text for word-based tokenization
            
        Returns:
            list: List of word token strings
        """
        tokens = []
        current_word = ""
        
        for char in text:
            if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):  # A-Z or a-z
                current_word += char
            else:
                if current_word:
                    tokens.append(current_word)
                    current_word = ""
        
        if current_word:
            tokens.append(current_word)
        
        return tokens
    
    def _tokenize_by_subword(self, text, chunk_size=3):
        """
        Tokenize input text into subword units of specified size
        
        Args:
            text (str): Input text for subword tokenization
            chunk_size (int): Maximum size of each subword unit
            
        Returns:
            list: List of subword token strings
        """
        tokens = []
        words = self._tokenize_by_word_boundary(text)
        
        for word in words:
            for i in range(0, len(word), chunk_size):
                chunk = word[i:i+chunk_size]
                if chunk:
                    tokens.append(chunk)
        
        return tokens
    
    def _compute_statistical_features(self, tokens, frontend_digits):
        """
        Compute statistical features from tokenized data and frontend digit values
        
        Args:
            tokens (list): List of tokenized text units
            frontend_digits (list): List of corresponding frontend digit values
            
        Returns:
            dict: Dictionary containing computed statistical features
        """
        if not frontend_digits:
            return {
                'length_factor': 0,
                'balance_index': 0,
                'entropy_index': 0
            }
        
        # Length Factor: Number of tokens modulo 10
        length_factor = len(tokens) % 10
        
        # Balance Index: Mean of frontend digits modulo 10
        mean_value = sum(frontend_digits) / len(frontend_digits)
        balance_index = int(mean_value) % 10
        
        # Entropy Index: Variance of frontend digits modulo 10
        variance = sum((x - mean_value) ** 2 for x in frontend_digits) / len(frontend_digits)
        entropy_index = int(variance) % 10
        
        return {
            'length_factor': length_factor,
            'balance_index': balance_index,
            'entropy_index': entropy_index,
            'mean': mean_value,
            'variance': variance
        }
    
    def tokenize(self, text, tokenization_method="whitespace", compute_features=True):
        """
        Main tokenization method for text processing
        
        Args:
            text (str): Input text to tokenize
            tokenization_method (str): Tokenization strategy ("whitespace", "word", "character", "subword")
            compute_features (bool): Whether to compute and return statistical features
            
        Returns:
            dict: Dictionary containing tokens, frontend digits, and features
        """
        # Preprocess input text
        preprocessed_text = self._preprocess_text(text)
        
        # Apply tokenization based on method
        if tokenization_method == "whitespace":
            tokens = self._tokenize_by_whitespace(preprocessed_text)
        elif tokenization_method == "word":
            tokens = self._tokenize_by_word_boundary(preprocessed_text)
        elif tokenization_method == "character":
            tokens = self._tokenize_by_character(preprocessed_text)
        elif tokenization_method == "subword":
            tokens = self._tokenize_by_subword(preprocessed_text)
        else:
            raise ValueError(f"Unsupported tokenization method: {tokenization_method}")
        
        # Generate frontend digits for each token
        frontend_digits = [self._generate_frontend_digit(token) for token in tokens]
        
        # Compute statistical features if requested
        features = None
        if compute_features:
            features = self._compute_statistical_features(tokens, frontend_digits)
        
        return {
            'original_text': text,
            'preprocessed_text': preprocessed_text,
            'tokens': tokens,
            'frontend_digits': frontend_digits,
            'features': features,
            'tokenization_method': tokenization_method,
            'configuration': {
                'random_seed': self.random_seed,
                'embedding_bit': self.embedding_bit,
                'normalize_case': self.normalize_case,
                'remove_punctuation': self.remove_punctuation,
                'collapse_repetitions': self.collapse_repetitions
            }
        }
    
    def analyze_text(self, text, tokenization_methods=None):
        """
        Analyze text using multiple tokenization strategies
        
        Args:
            text (str): Input text for analysis
            tokenization_methods (list): List of tokenization methods to apply
            
        Returns:
            dict: Dictionary containing analysis results for each tokenization method
        """
        if tokenization_methods is None:
            tokenization_methods = ["whitespace", "word", "character", "subword"]
        
        analysis_results = {}
        for method in tokenization_methods:
            analysis_results[method] = self.tokenize(text, method)
        
        return analysis_results
    
    def generate_summary(self, text):
        """
        Generate comprehensive summary statistics for text analysis
        
        Args:
            text (str): Input text for summary generation
            
        Returns:
            dict: Dictionary containing summary statistics
        """
        tokenization_result = self.tokenize(text, "whitespace")
        
        return {
            'text_length': len(text),
            'token_count': len(tokenization_result['tokens']),
            'unique_tokens': len(set(tokenization_result['tokens'])),
            'frontend_digits': tokenization_result['frontend_digits'],
            'statistical_features': tokenization_result['features']
        }


# Convenience functions for simplified usage
def tokenize_text(text, tokenization_method="whitespace"):
    """
    Convenience function for text tokenization
    
    Args:
        text (str): Input text to tokenize
        tokenization_method (str): Tokenization strategy to apply
        
    Returns:
        dict: Tokenization results
    """
    tokenization_engine = TextTokenizationEngine()
    return tokenization_engine.tokenize(text, tokenization_method)

def analyze_text_comprehensive(text):
    """
    Convenience function for comprehensive text analysis
    
    Args:
        text (str): Input text for analysis
        
    Returns:
        dict: Comprehensive analysis results
    """
    tokenization_engine = TextTokenizationEngine()
    return tokenization_engine.analyze_text(text)

def generate_text_summary(text):
    """
    Convenience function for text summary generation
    
    Args:
        text (str): Input text for summary generation
        
    Returns:
        dict: Summary statistics
    """
    tokenization_engine = TextTokenizationEngine()
    return tokenization_engine.generate_summary(text)


# Example usage
if __name__ == "__main__":
    # Example usage
    print("SanTOK Tokenization Engine Module Example")
    print("=" * 50)
    
    # Create tokenization engine instance
    tokenization_engine = TextTokenizationEngine(random_seed=12345, embedding_bit=False)
    
    # Test text
    text = "Hello World! This is a test."
    
    # Basic tokenization
    result = tokenization_engine.tokenize(text, "whitespace")
    print(f"Original: {result['original_text']}")
    print(f"Preprocessed: {result['preprocessed_text']}")
    print(f"Tokens: {result['tokens']}")
    print(f"Frontend Digits: {result['frontend_digits']}")
    print(f"Features: {result['features']}")
    
    print("\n" + "=" * 50)
    
    # Multiple tokenization methods
    analysis = tokenization_engine.analyze_text(text)
    for method, result in analysis.items():
        print(f"{method}: {len(result['tokens'])} tokens")
    
    print("\n" + "=" * 50)
    
    # Generate summary
    summary = tokenization_engine.generate_summary(text)
    print(f"Summary: {summary}")
