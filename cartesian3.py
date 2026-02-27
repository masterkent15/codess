import numpy as np
a1 = float(input ("a1 = "))
a2 = float(input ("a2 = "))
a3 = float(input ("a3 = "))
a4 = float(input ("a4 = "))
a5 = float(input ("a5 = "))
a6 = float(input ("a6 = "))
a7 = float(input ("a7 = "))
#joint variable
d1 = float(input ("d1 = "))
d2 = float(input ("d2 = "))
d3 = float(input ("d3 = "))
t4 = float(input ("t4 = "))
t5 = float(input ("t5 = "))
t6 = float(input ("t6 = "))

T4 = (t4/180)*np.pi
T5 = (t5/180)*np.pi
T6 = (t6/180)*np.pi


PT = [[(0/180)*np.pi, (270/180)*np.pi, 0, a1],
      [(270/180)*np.pi, (270/180)*np.pi, 0, a2+d1], 
      [(90/180)*np.pi, (270/180)*np.pi, 0, a3+d2], 
      [(0/180)*np.pi, (0/180)*np.pi, 0, a4+d3],
      [(270/180)*np.pi+t4,(270/180)*np.pi, 0, a5],
      [(90/180)*np.pi+t5, (90/180)*np.pi, 0, 0],
      [(0/180)*np.pi+t6, (0/180)*np.pi, 0, a6+a7]]
      

i = 0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i = 1
H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i = 2
H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i = 3
H3_4 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 4
H4_5 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i = 5
H5_6 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
i = 6
H6_7 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]


H0_1 = np.array(H0_1)
print("H0_1 = ")
print(H0_1)

H1_2 = np.array(H1_2)
print("H1_2 = ")
print(H1_2)

H2_3 = np.array(H2_3)
print("H2_3 = ")
print(H2_3)

H3_4 = np.array(H3_4)
print("H3_4 = ")
print(H3_4)

H4_5 = np.array(H4_5)
print("H4_5 = ")
print(H4_5)

H5_6 = np.array(H5_6)
print("H5_6 = ")
print(H5_6)

H6_7 = np.array(H6_7)
print("H6_7 = ")
print(H6_7)

H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)
H0_4 = np.dot(H0_3,H3_4)
H0_5 = np.dot(H0_4,H4_5)
H0_6 = np.dot(H0_5,H5_6)
H0_7 = np.dot(H0_6,H6_7)
print ("H0_7 = ")
print(np.around(H0_7,3))