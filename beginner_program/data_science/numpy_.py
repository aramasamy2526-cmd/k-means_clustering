# # # import numpy as np
# # # list_a = [21,53,15,74,35,72]
# # # list_b = [31,67,34,14,63,21]
# # # list_c = [43,53,23,56,73,85]
# # # array_con = np.array([list_a,list_b,list_c], dtype=int)
# # # print(array_con.dtype)  
# # # sort_array = np.sort(array_con)
# # # print(sort_array)
# # # # x = array_con > 50
# # # # print(x)
# # # # print(array_con[x])
# # # # a = np.arange(1,10)
# # # # print(array_con)
# # # # x = np.where(array_con > 55)
# # # # print(x)
# # # # print(array_con[x])

# # import numpy as np

# # student_mark = [78, 92, 36, 64, 89]
# # student_mark_arr = np.array(student_mark)
# # total_marks = np.sum(student_mark_arr)
# # print(total_marks)

# # additional_marks = [2, 2, 5, 10, 1]
# # additional_marks_arr = np.array(additional_marks)
# # #student_mark_arr += additional_marks_arr
# # student_mark_arr_s = np.sub(student_mark_arr,additional_marks_arr)
# # print(student_mark_arr_s)

# # import numpy as np
# # #Students marks in 4 subjects
# # students_marks = np.array([[67, 45],[90, 92],[66, 72],[32, 40]])
# # mult_arr = [5,1]
# # mult_st = np.add(students_marks,mult_arr)
# # print(mult_st)

# # from skimage.io import imread
# # from skimage import data_dir
# # import matplotlib.pyplot as plt
# # import numpy as np
# # import os

# # # Read your own image
# # img = imread('img.PNG')

# # plt.imshow(img)
# # plt.title("Original Image")
# # plt.show()

# # print(img)
# # print((type(img), img.ndim, img.shape))


# # # Read astronaut image
# # img = imread(os.path.join(data_dir, 'astronaut.png'))

# # plt.imshow(img)
# # plt.title("Astronaut Original")
# # plt.show()

# # # Slice rocket area
# # img_slice = img.copy()
# # img_slice = img_slice[0:300, 360:480]

# # plt.imshow(img_slice)
# # plt.title("Sliced Rocket")
# # plt.show()

# # # Zero out rocket region in original
# # img[0:300, 360:480, :] = 0
# # plt.imshow(img)
# # plt.title("Original with Rocket Removed")
# # plt.show()

# # # Remove specific red-range pixels
# # mask = np.greater_equal(img_slice[:,:,0], 100) & np.less_equal(img_slice[:,:,0], 150)
# # img_slice[mask] = 0

# # plt.imshow(img_slice)
# # plt.title("Sliced Rocket After Red Filter")
# # plt.show()

# # # Paste processed slice back
# # img[0:300, 360:480, :] = img_slice
# # plt.imshow(img)
# # plt.title("Final Merged Image")
# # plt.show()
# import numpy as np
# # arr = np.linspace(0,5)
# # print(arr)
# # print('Length of arr: ',len(arr))
# # #Number of values = 3
# # print(np.linspace(0,10,4))
# # print(np.ones(3))
# #2D
# # print(np.zeros([2,3]))
# # print(np.full(5,8))
# # print(np.full([3,3],"nupy"))
# # print(np.eye(2,2))

# # print("printing randam number", np.random.rand(5))
# # print("printing randam number from 0 to 10 five numbers", np.random.randint(0,10,size = 5))
# # print("printing randam number from 0 to 100 storing in matrix", np.random.randint(0,10,size =[3,5] ))

# # x = np.random.choice([1,3,5,6,2,7], size = [3,3])
# # print(x)

# # steps = [6012, 7079, 6886, 7230, 4598, 5564, 6971, 7763, 8032, 9569]
# # steps_arr = np.array(steps)
# # walks_2000 = np.array([2000])
# # add_daily_walk = np.add(steps_arr,walks_2000, dtype = "int")
# # x = np.where(add_daily_walk > 9000)

# # print(add_daily_walk)
# # print(add_daily_walk[x])
# # print(np.sort(add_daily_walk[x]))
