from faker import Faker

fake = Faker()

print(fake.name())          # Name
print(fake.first_name())    # First Name
print(fake.last_name())     # Last Name
print(fake.email())         # Email
print(fake.phone_number())  # Phone Number
print(fake.address())       # Address
print(fake.city())          # City
print(fake.country())       # Country
print(fake.company())       # Company
print(fake.job())           # Job
print(fake.date())          # Random Date
print(fake.text())          # Random Paragraph
print(fake.password())      # Password



