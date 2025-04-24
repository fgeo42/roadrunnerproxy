import os
import sys
from proxy import main

# Set the dynamic port from Heroku's environment
port = os.environ.get("PORT", "8899")

# Simulate running from CLI: pass args to proxy.main
sys.argv = ["proxy.py", "--hostname", "0.0.0.0", "--port", port]

main()
