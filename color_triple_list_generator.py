'''
Author: Allen Guo<1309476338@qq.com>
Instruction:
To generator a list of color triplets of different color visual deficiency types.
 

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


def color_selection():
    color1=np.array((np.random.randint(256, size=3)),np.float16)
    print color1
    color1=color1/255
    
    color2=np.array((np.random.randint(256, size=3)),np.float16)
    print color2
    color2=color2/255
    
    print color1,color2
    color1_lab=rgb2lab([[color1]])[0][0]
    color2_lab=rgb2lab([[color2]])[0][0]
    
    print color1_lab,"\n",color2_lab,"\n"
    delta_E_rgb = delta_e.deltaE_cie76(color1_lab, color2_lab)

    '''To simulate d
    '''
    matrix_cvd = cb_matrices["d"]
    d_sim={}
    d_sim['color1_sim'] = np.matmul(lms2rgb,np.matmul(matrix_cvd,np.matmul(rgb2lms,color1)))
    d_sim['color2_sim'] = np.matmul(lms2rgb,np.matmul(matrix_cvd,np.matmul(rgb2lms,color2)))
    
    print "color1_sim,color2_sim",d_sim['color1_sim'],d_sim['color2_sim']
    
    color1_sim_lab=rgb2lab([[d_sim['color1_sim']]])[0][0]
    color2_sim_lab=rgb2lab([[d_sim['color2_sim']]])[0][0]
    
    d_sim['delta_E_sim'] = delta_e.deltaE_cie76(color1_sim_lab, color2_sim_lab)
    
    d_sim['ratio_now'] = delta_E_rgb/d_sim['delta_E_sim']
    
    print d_sim
    print d_sim['ratio_now']

    
    '''To simulate d
    '''
    matrix_cvd = cb_matrices["p"]
    p_sim={}
    p_sim['color1_sim'] = np.matmul(lms2rgb,np.matmul(matrix_cvd,np.matmul(rgb2lms,color1)))
    p_sim['color2_sim'] = np.matmul(lms2rgb,np.matmul(matrix_cvd,np.matmul(rgb2lms,color2)))
    
    print "color1_sim,color2_sim",p_sim['color1_sim'],p_sim['color2_sim']
    
    color1_sim_lab=rgb2lab([[p_sim['color1_sim']]])[0][0]
    color2_sim_lab=rgb2lab([[p_sim['color2_sim']]])[0][0]
    
    p_sim['delta_E_sim'] = delta_e.deltaE_cie76(color1_sim_lab, color2_sim_lab)
    
    p_sim['ratio_now'] = delta_E_rgb/p_sim['delta_E_sim']
    
    print p_sim
    print p_sim['ratio_now']
    
    
    '''To simulate t
    '''
    matrix_cvd = cb_matrices["t"]
    t_sim={}
    t_sim['color1_sim'] = np.matmul(lms2rgb,np.matmul(matrix_cvd,np.matmul(rgb2lms,color1)))
    t_sim['color2_sim'] = np.matmul(lms2rgb,np.matmul(matrix_cvd,np.matmul(rgb2lms,color2)))
    
    print "color1_sim,color2_sim",t_sim['color1_sim'],t_sim['color2_sim']
    
    color1_sim_lab=rgb2lab([[t_sim['color1_sim']]])[0][0]
    color2_sim_lab=rgb2lab([[t_sim['color2_sim']]])[0][0]
    
    t_sim['delta_E_sim'] = delta_e.deltaE_cie76(color1_sim_lab, color2_sim_lab)
    
    t_sim['ratio_now'] = delta_E_rgb/t_sim['delta_E_sim']
    
    print t_sim
    print t_sim['ratio_now']
    
    return np.around(color1*255),np.around(color2*255),d_sim,p_sim,t_sim
#     return np.around(color1*255),np.around(color2*255),np.around(d_sim['color1_sim']*255),np.around(d_sim['color2_sim']*255),d_sim['ratio_now']

colorset1=[]
colorset2=[]
colorsim1_d=[]
colorsim2_d=[]

colorsim1_p=[]
colorsim2_p=[]

colorsim1_t=[]
colorsim2_t=[]

colorsim_=[]
ratio_now=[]
for i in range(10000):
    c1,c2,d,p,t = color_selection()
    if ((d['ratio_now']>2) and  (p['ratio_now']>2) and (t['ratio_now']>2) ):
#     if ((d['ratio_now']>10) and  (p['ratio_now']>5)):
        colorset1.append(c1)
        colorset2.append(c2)
        
        colorsim1_d.append(np.around(d['color1_sim']*255))
        colorsim2_d.append(np.around(d['color2_sim']*255))
        colorsim1_p.append(np.around(p['color1_sim']*255))
        colorsim2_p.append(np.around(p['color2_sim']*255))
        colorsim1_t.append(np.around(t['color1_sim']*255))
        colorsim2_t.append(np.around(t['color2_sim']*255))
        
        ratio_now.append(t['ratio_now'])
    else:
        pass

print len(colorset1)
print len(colorset2)
print len(ratio_now)

print colorset1
print colorset2

print colorsim1_d
print colorsim2_d

print colorsim1_p
print colorsim2_p

print colorsim1_t
print colorsim2_t
# print ratio_now

        







