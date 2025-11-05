import os

# Define the good and bad commits
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"

# Start git bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Run git bisect with the test command
os.system("git bisect run python manage.py test")
