import matplotlib.pyplot as plt
import matplotlib.image as mpimg

folder_name="Milan2007"
first_image=folder_name + "/" + "09.Kaka.png"

imagine=mpimg.imread(first_image)
figure, axis = plt.subplots(1, 1)
axis.imshow(imagine)
plt.show()

