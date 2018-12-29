
'''
Test calculation based on approximation formula
'''

# Given following WSG84 coordinates
phi = 460238.87
lambda_ = 84349.79
h_wgs = 650.60 
print('WGS84 coordinates')
print('phi: %s° %s\' %s\"' % (str(phi)[0:2], str(phi)[2:4], str(phi)[4:]))
print('lambda: %s° %s\' %s\"' % (str(lambda_)[0:2], str(lambda_)[2:4], str(lambda_)[4:]))

# 1. Tranform in sexagesimal seconds
phi = 46 * 60*60 + 2 * 60 + 38.87
lambda_ = 8 * 60*60 + 43 * 60 + 49.79

# 2. Calculate values relative to bern
phi_bar = (phi - 169028.66) / 10000
lambda_bar = (lambda_ - 26782.5) /10000

# 3. Transform coordinates in LV95 (E, N, h)
E_m = 2600072.37 \
        + 211455.93 * lambda_bar \
        - 10938.51 * lambda_bar * phi_bar \
        - 0.36 * lambda_bar * phi_bar ** 2 \
        - 44.54 * lambda_bar ** 3
N_m = 1200147.07 \
        + 308807.95 * phi_bar \
        + 3745.25 * lambda_bar **2 \
        + 76.63 * phi_bar **2 \
        - 194.56 * lambda_bar**2 * phi_bar \
        + 119.79 * phi_bar **3

# ... and then in LV03 (y, x, h)
y_m = E_m - 2000000.00
x_m = N_m - 1000000.00
h_ch_m = h_wgs - 49.55 \
            + 2.73 * lambda_bar \
            + 6.94 * phi_bar

print('Swiss coordinates:')
print('y : %s' % y_m)
print('x : %s' % x_m)
print('h_ch : %s' % h_ch_m)