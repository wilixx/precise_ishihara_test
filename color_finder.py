'''
Author: Allen Guo<1309476338@qq.com>
Instruction:
Given a rgb color [r, g, b], e.g. [100, 54, 55],
this module can get a list of colors with the same simulation 
result with the given color.

'''


import numpy as np
import colormath
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
color1=np.array([164.,  62.,  58.],np.float16)
print color1
color1=color1/255
def color_finder(color1):

    color2=np.array((np.random.randint(256, size=3)),np.float16)
    print color2
    color2=color2/255
    
    print color1,color2
    
    '''To simulate
    '''
    cvd_matrix=cb_matrices["t"]
    
    color1_sim = np.matmul(cvd_matrix,np.matmul(rgb2lms,color1))
    # color1_sim = np.around(np.matmul(lms2rgb,color1_sim)*255)
    color1_sim = np.matmul(lms2rgb,color1_sim)
    
    color2_sim = np.matmul(cvd_matrix,np.matmul(rgb2lms,color2))
    # color1_sim = np.around(np.matmul(lms2rgb,color1_sim)*255)
    color2_sim = np.matmul(lms2rgb,color2_sim)
    
    print "color1_sim,color2_sim",color1_sim,color2_sim
    
    # color1=(color1[0],color1[1],color1[2])
    # color2=(color2[0],color2[1],color2[2])
    # color1= rgb2lab(color1)
    # color2= rgb2lab(color2)
    
    color1_lab=rgb2lab([[color1]])[0][0]
#     color1_lab=color1[0][0]
    color1_sim_lab=rgb2lab([[color1_sim]])[0][0]
#     color1_sim_lab=color1_sim[0][0]
    
    color2_lab=rgb2lab([[color2]])[0][0]
#     color2=color2[0][0]
    color2_sim_lab=rgb2lab([[color2_sim]])[0][0]
#     color2_sim=color2_sim[0][0]
    
    
    print color1_lab,"\n",color2_lab,"\n"
    
    # (color1[0],color1[1],color1[2])
    # color2=rgb2lab(color2[0],color2[1],color2[2])
    delta_E_rgb = delta_e.deltaE_cie76(color1_lab, color2_lab)
    delta_E_sim = delta_e.deltaE_cie76(color1_sim_lab, color2_sim_lab)
    
    # delta_e_cie1976(color1, color2)
    ratio_now = delta_E_rgb/delta_E_sim
    print delta_E_rgb,delta_E_sim
    print ratio_now
    
    return np.around(color1*255),np.around(color2*255),np.around(color1_sim*255),np.around(color2_sim*255),ratio_now

colorset1=[]
colorset2=[]
colorsim1=[]
colorsim2=[]
ratio_now=[]
for i in range(10000):
    c1,c2,s1,s2,r=color_finder(color1)
    if (r>50):
        colorset1.append(c1)
        colorset2.append(c2)
        
        colorsim1.append(s1)
        colorsim2.append(s2)
        ratio_now.append(r)
    else:
        pass

print len(colorset1)
print len(colorset2)
print len(ratio_now)

print colorset1
print colorset2

print colorsim1
print colorsim2
print ratio_now

        







