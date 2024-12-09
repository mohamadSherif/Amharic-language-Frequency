# amharic_helper.py

class AmharicAlphabet:
    def __init__(self):
        self.alphabet = {
            'ሀ': ['ሀ', 'ሁ', 'ሂ', 'ሃ', 'ሄ', 'ህ', 'ሆ'],
            'ለ': ['ለ', 'ሉ', 'ሊ', 'ላ', 'ሌ', 'ል', 'ሎ'],
            'ሐ': ['ሐ', 'ሑ', 'ሒ', 'ሓ', 'ሔ', 'ሕ', 'ሖ'],
            'መ': ['መ', 'ሙ', 'ሚ', 'ማ', 'ሜ', 'ም', 'ሞ'],
            'ሠ': ['ሠ', 'ሡ', 'ሢ', 'ሣ', 'ሤ', 'ሥ', 'ሦ'],
            'ረ': ['ረ', 'ሩ', 'ሪ', 'ራ', 'ሬ', 'ር', 'ሮ'],
            'ሰ': ['ሰ', 'ሱ', 'ሲ', 'ሳ', 'ሴ', 'ስ', 'ሶ'],
            'ሸ': ['ሸ', 'ሹ', 'ሺ', 'ሻ', 'ሼ', 'ሽ', 'ሾ'],
            'ቀ': ['ቀ', 'ቁ', 'ቂ', 'ቃ', 'ቄ', 'ቅ', 'ቆ'],
            'በ': ['በ', 'ቡ', 'ቢ', 'ባ', 'ቤ', 'ብ', 'ቦ'],
            'ተ': ['ተ', 'ቱ', 'ቲ', 'ታ', 'ቴ', 'ት', 'ቶ'],
            'ቸ': ['ቸ', 'ቹ', 'ቺ', 'ቻ', 'ቼ', 'ች', 'ቾ'],
            'ኀ': ['ኀ', 'ኁ', 'ኂ', 'ኃ', 'ኄ', 'ኅ', 'ኆ'],
            'ነ': ['ነ', 'ኑ', 'ኒ', 'ና', 'ኔ', 'ን', 'ኖ'],
            'ኘ': ['ኘ', 'ኙ', 'ኚ', 'ኛ', 'ኜ', 'ኝ', 'ኞ'],
            'አ': ['አ', 'ኡ', 'ኢ', 'ኣ', 'ኤ', 'እ', 'ኦ'],
            'ከ': ['ከ', 'ኩ', 'ኪ', 'ካ', 'ኬ', 'ክ', 'ኮ'],
            'ኸ': ['ኸ', 'ኹ', 'ኺ', 'ኻ', 'ኼ', 'ኽ', 'ኾ'],
            'ወ': ['ወ', 'ዉ', 'ዊ', 'ዋ', 'ዌ', 'ው', 'ዎ'],
            'ዐ': ['ዐ', 'ዑ', 'ዒ', 'ዓ', 'ዔ', 'ዕ', 'ዖ'],
            'ዘ': ['ዘ', 'ዙ', 'ዚ', 'ዛ', 'ዜ', 'ዝ', 'ዞ'],
            'ዠ': ['ዠ', 'ዡ', 'ዢ', 'ዣ', 'ዤ', 'ዥ', 'ዦ'],
            'የ': ['የ', 'ዩ', 'ዪ', 'ያ', 'ዬ', 'ይ', 'ዮ'],
            'ደ': ['ደ', 'ዱ', 'ዲ', 'ዳ', 'ዴ', 'ድ', 'ዶ'],
            'ጀ': ['ጀ', 'ጁ', 'ጂ', 'ጃ', 'ጄ', 'ጅ', 'ጆ'],
            'ገ': ['ገ', 'ጉ', 'ጊ', 'ጋ', 'ጌ', 'ግ', 'ጎ'],
            'ጠ': ['ጠ', 'ጡ', 'ጢ', 'ጣ', 'ጤ', 'ጥ', 'ጦ'],
            'ጨ': ['ጨ', 'ጩ', 'ጪ', 'ጫ', 'ጬ', 'ጭ', 'ጮ'],
            'ጰ': ['ጰ', 'ጱ', 'ጲ', 'ጳ', 'ጴ', 'ጵ', 'ጶ'],
            'ጸ': ['ጸ', 'ጹ', 'ጺ', 'ጻ', 'ጼ', 'ጽ', 'ጾ'],
            'ፀ': ['ፀ', 'ፁ', 'ፂ', 'ፃ', 'ፄ', 'ፅ', 'ፆ'],
            'ፈ': ['ፈ', 'ፉ', 'ፊ', 'ፋ', 'ፌ', 'ፍ', 'ፎ'],
            'ፐ': ['ፐ', 'ፑ', 'ፒ', 'ፓ', 'ፔ', 'ፕ', 'ፖ']
        }
        
        self.vowel_forms = {
            0: "Base form (ə)",
            1: "First form (u)",
            2: "Second form (i)",
            3: "Third form (a)",
            4: "Fourth form (e)",
            5: "Fifth form (ɨ)",
            6: "Sixth form (o)"
        }

    def get_letter_family(self, base_letter):
        """Get all forms of a given base letter"""
        return self.alphabet.get(base_letter, [])

    def get_all_base_letters(self):
        """Get all base letters"""
        return list(self.alphabet.keys())

    def get_vowel_form(self, vowel_index):
        """Get all letters of a specific vowel form"""
        if 0 <= vowel_index <= 6:
            return [family[vowel_index] for family in self.alphabet.values()]
        return []

    def get_vowel_name(self, vowel_index):
        """Get the name of a vowel form"""
        return self.vowel_forms.get(vowel_index, "Invalid vowel form")

    def find_letter_family(self, letter):
        """Find which family a letter belongs to"""
        for base_letter, family in self.alphabet.items():
            if letter in family:
                return base_letter, family
        return None, None

    def get_letter_position(self, letter):
        """Get the vowel position of a letter in its family"""
        base_letter, family = self.find_letter_family(letter)
        if family:
            try:
                position = family.index(letter)
                return position, self.vowel_forms[position]
            except ValueError:
                return None, None
        return None, None

# Example usage:
if __name__ == "__main__":
    amharic = AmharicAlphabet()
    
    # Example operations
    print(f"Base letters: {amharic.get_all_base_letters()}")
    print(f"'መ' family: {amharic.get_letter_family('መ')}")
    print(f"Third form (a) letters: {amharic.get_vowel_form(3)}")
    print(f"Letter 'ሙ' belongs to family: {amharic.find_letter_family('ሙ')[0]}")
    position, vowel_type = amharic.get_letter_position('ሙ')
    print(f"Letter 'ሙ' is in position {position} ({vowel_type})")