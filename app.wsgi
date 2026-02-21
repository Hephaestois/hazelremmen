import sys
sys.path.insert(0, "/var/www/hazelremmen")
sys.path.insert(0, "/var/www/hazelremmen/templates")

print(sys.path)

from app import application
