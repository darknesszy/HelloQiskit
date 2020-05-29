import os
from qiskit import IBMQ, __version__
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Login to IBM Quantum.
if IBMQ.stored_account().get('token') == None:
    IBMQ.save_account(os.environ['IBMQ_TOKEN'])
    print('You are now logged in...')

print(__version__)