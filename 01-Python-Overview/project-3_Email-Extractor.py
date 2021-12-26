"""
Developer: Mr. Skywalker
Purpose: Project-3, E-Mail Extractor
Stardate: 12020.--

"""

# take email input
email = input('\n\tEnter Your E-Mail Address: ').strip().lower()


# slice into username and domainname
username = email[:email.index('@')]
domainname = email[email.index('@') + 1:]

# Show output
output = (
    f"\n\tYour username: {username} \n\tYour domain is: {domainname}\n")
print(output)


'''
# Logic

variable[start: end: step]    

'''
