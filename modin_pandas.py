from time import time  # used for our benchmarking

import modin.pandas as pd  # the star of today's show!

PROGRAM_START = time()

df = pd.read_csv("data/large.csv", sep=',',
                 header='infer', usecols=['val1', 'val2'])
PROGRAM_CSV_READ = time()

# first computation
df['sum'] = df['val1'] + df['val2']

PROGRAM_COMPUTATION1 = time()

print(f"Time to read CSV file:\t{PROGRAM_CSV_READ-PROGRAM_START}\n"
      f"Time to perform first computation:\t{PROGRAM_COMPUTATION1-PROGRAM_CSV_READ}\n")

print(df)
