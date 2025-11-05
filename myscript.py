import os

# Define the good and bad commits
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c "
badhash = "1d8748281263e8e7efe7b85c828cd3f600d96bfc "

# Start git bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Run git bisect with the test command
os.system("git bisect run python manage.py test")
