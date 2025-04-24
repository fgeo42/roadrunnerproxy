import os
from proxy.common.flag import Flags
from proxy.core.entrypoint import start

# Get the dynamic port from Heroku
port = int(os.environ.get("PORT", 8899))

flags = Flags(
    port=port,
    hostname='0.0.0.0',
    num_workers=1,
)

start(flags)
