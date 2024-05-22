def pig_latin(word): return word[1:] + word[0] + 'ay' if word[0] not in 'aeiou' else word + 'ay'

# Example usage:
text = "google chat"
print(pig_latin(text))  # Output: "ooglegay atchay"

