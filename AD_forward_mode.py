import numpy as np

# f = sin(x2 / x1) + (x2 / x1) - exp(x2) * ((x2 / x1) - exp(x2))

def forward_mode(x1,x2):
    v_m1 = x1
    v_0 = x2

    dv_m1 = 1 # to figure out the tiny change of output when we change x1 but not x2
    dv_0 = 0 

    v_1 = v_m1 / v_0
    dv_1 = (dv_m1 * v_0 - v_m1 * dv_0) / v_0 ** 2
    
    v_2 = np.sin(v_1)
    dv_2 = np.cos(v_1) * dv_1

    v_3 = np.exp(v_0)
    dv_3= np.exp(v_0) * v_0

    v_4 = v_1 - v_3
    dv_4 = dv_1 - dv_3


    v_5 = v_2 + v_4
    dv_5 = dv_2 + dv_4

    # v6 = v5 * v4
    v_6 = v_5 * v_4
    dv_6 = dv_5 * v_4 + v_5 * dv_4

    f = v_6
    df_dx1 = dv_6

    return f, df_dx1

# Example: evaluate at x1 = 1.0, x2 = 2.0
x1 = 1.0
x2 = 2.0

f, df_dx1 = forward_mode(x1, x2)

print (f"f(x1,x2)= {f}")
print(f"∂f/∂x1 = {df_dx1}")