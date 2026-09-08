class Codec:
    """
    A codec for encoding and decoding a list of strings into a single string.
    Uses a 'length-prefix' strategy to handle arbitrary characters safely.
    """

    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: length + '#' + string
        Example: ["hello", "world"] -> "5#hello5#world"
        """
        encoded_str = ""
        for s in strs:
            # Prefix each string with its length and a delimiter '#'
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string back to a list of strings.
        Parses the length prefix to know exactly how many characters to read.
        """
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter '#'
            j = s.find('#', i)
            
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Extract the string based on the length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move the pointer to the start of the next length prefix
            i = end
            
        return res