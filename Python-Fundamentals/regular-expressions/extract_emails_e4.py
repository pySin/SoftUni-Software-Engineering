# Extract emails
# pattern = "\\b[a-z0_9][a-z0_9._-]+@\w+.[a-z.]+\\b"
# pattern = "\\b(([a-z0-9][a-z0-9._-]+@)([a-z.]+)+([a-z.]+)+[a-z])"
# pattern = "\\b(([a-z0-9][a-z0-9._-]+@)([a-z.]+)\.([a-z.]+)+[a-z])"
# pattern = "(^|\s)\\b([a-z0-9][a-z0-9._-]+@([a-z-]+)\.([a-z.-]+))"

import re

pattern = "(^|\s)\\b(([a-z0-9][a-z0-9._-]+@)([a-z-]+)\.([a-z.-]+)[a-z])"
text = input()


def occurrences(reg_pattern, reg_text):
    result = re.findall(reg_pattern, reg_text)
    return result


for match in occurrences(pattern, text):
    print(match[1])

# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.
# Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.
