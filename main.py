import plot as p

# IP-Address and Port
__HOST = '169.254.173.4'
__PORT = 502

if __name__ == '__main__':
    # Initialise the live Plot
    p.livePlot(__HOST, __PORT)