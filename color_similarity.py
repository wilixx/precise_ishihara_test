import numpy as np
import colormath
import colorspacious
from colorspacious import cspace_convert
from colormath.color_objects import LabColor

from colormath.color_conversions import convert_color

from colormath.color_diff import delta_e_cie1976
# import colorsys
# from skimage.color.colorconv import rgb2lab
from skimage.color import rgb2lab
from skimage.color import delta_e
# from precise_ishihara_test.linear_equation import lms_sim

cb_matrices = {
        "d": np.array([[1, 0, 0], [0.494207, 0, 1.24827], [0, 0, 1]]),
        "p": np.array([[0, 2.02344, -2.52581], [0, 1, 0], [0, 0, 1]]),
        "t": np.array([[1, 0, 0], [0, 1, 0], [-0.395913, 0.801109, 0]]),
    }
rgb2lms = np.array([[17.8824, 43.5161, 4.11935],
                        [3.45565, 27.1554, 3.86714],
                        [0.0299566, 0.184309, 1.46709]])

lms2rgb = np.array([[8.09444479e-02, -1.30504409e-01, 1.16721066e-01],
                        [-1.02485335e-02, 5.40193266e-02, -1.13614708e-01],
                        [-3.65296938e-04, -4.12161469e-03, 6.93511405e-01]])



color1=np.array((np.random.randint(256, size=3)),np.float16)
print color1
color1=color1/255
# color1=np.array((np.random.randint(256, size=3)),np.float16)/255
color2=np.array((np.random.randint(256, size=3)),np.float16)

print color2
color2=color2/255
# color2=np.random.randint(256, size=3)/255
print color1,color2

'''To simulate
'''

color1_sim = np.matmul(cb_matrices["d"],np.matmul(rgb2lms,color1))
# color1_sim = np.around(np.matmul(lms2rgb,color1_sim)*255)
color1_sim = np.matmul(lms2rgb,color1_sim)

color2_sim = np.matmul(cb_matrices["d"],np.matmul(rgb2lms,color2))
# color1_sim = np.around(np.matmul(lms2rgb,color1_sim)*255)
color2_sim = np.matmul(lms2rgb,color2_sim)

print "color1_sim,color2_sim",color1_sim,color2_sim

# color1=(color1[0],color1[1],color1[2])
# color2=(color2[0],color2[1],color2[2])
# color1= rgb2lab(color1)
# color2= rgb2lab(color2)

color1=rgb2lab([[color1]])
color1=color1[0][0]

color1_sim=rgb2lab([[color1_sim]])
color1_sim=color1_sim[0][0]

color2=rgb2lab([[color2]])
color2=color2[0][0]

color2_sim=rgb2lab([[color2_sim]])
color2_sim=color2_sim[0][0]


print color1,"\n",color2,"\n"

# (color1[0],color1[1],color1[2])
# color2=rgb2lab(color2[0],color2[1],color2[2])
delta_E_rgb = delta_e.deltaE_cie76(color1, color2)
delta_E_sim = delta_e.deltaE_cie76(color1_sim, color2_sim)

# delta_e_cie1976(color1, color2)

print delta_E_rgb,delta_E_sim
print delta_E_rgb/delta_E_sim

'''
cvd_space = {"name": "sRGB1+CVD",
                "cvd_type": "deuteranomaly",
                "severity": 50}
   
color1_sim=cspace_convert(color1, "sRGB1", cvd_space)

# cspace_convert(arr, start, end)
color1_sim=cspace_convert(color1_sim, cvd_space, "sRGB1")
print color1_sim 
# color2_sim
'''

