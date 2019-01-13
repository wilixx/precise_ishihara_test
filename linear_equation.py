import numpy as np
from scipy import linalg

# rgb2lms = np.array([[2, -4, 4], [34, 3, -1], [1, 1, 1]])
rgb2lms = np.array([[17.8824, 43.5161, 4.11935],
                        [3.45565, 27.1554, 3.86714],
                        [0.0299566, 0.184309, 1.46709]])

# inv_r2l = np.linalg.inv(rgb2lms)

lms2rgb = np.array([[8.09444479e-02, -1.30504409e-01, 1.16721066e-01],
                        [-1.02485335e-02, 5.40193266e-02, -1.13614708e-01],
                        [-3.65296938e-04, -4.12161469e-03, 6.93511405e-01]])

# print "inv_r2l:",inv_r2l

lms_sim = np.array([[1, 0, 0], 
                    [0.494207, 0, 1.24827], 
                    [0, 0, 1]])

# inv_lms2sim = np.linalg.inv(lms_sim)
# print "inv_lms2sim:",inv_lms2sim


color=np.array([110,32,45])
print "given_color:",color

lms = np.matmul(rgb2lms,color)
# lms = np.matmul(color, rgb2lms)
print "lms_color:",lms

color_back = linalg.solve(rgb2lms, lms)
print "color_back:",color_back


# new_rgb=np.matmul(lms2rgb,lms)
# 
# print "new_rgb:",new_rgb
# 
# color2= np.matmul(inv_r2l,lms)

# color2=np.linalg.solve(lms, rgb2lms)

# print "color2:",color2

sim_color=np.matmul(lms_sim,lms)
print "sim_color:", sim_color

# color_another = linalg.solve(lms_sim, sim_color)

# color_another = np.linalg.lstsq(rgb2lms, lms)
color_another = np.linalg.lstsq(lms_sim, sim_color)[0]

color_pair=np.linalg.lstsq(rgb2lms, color_another)[0]
print "color_another:",color_another
print "color_pair:",color_pair



# lms2=np.linalg.solve(lms_sim, sim_color)
# print "lms2:",lms2

# b = np.array([8, 30, 108])
# b = np.array([8, 30, 108])
# x = np.linalg.solve(a, b)


