
import numpy as np
import matplotlib.pyplot as plt



x_data  = np.random.random(2050)*100
y_data  = np.random.random(2050)*100


# SCATTER GRAPH 

print (x_data)
print (y_data)
plt.scatter(x_data ,y_data  )
# plt.scatter(x_data ,y_data , c="blue" ,s=150, marker="*" alpha=0.3 )



weight = [ 75,78,73,82,70, 85, 78,73,70,82,84,75,79,71.,76]
years = [2010 + i for i in range(15)] 

# PLOT GRAPH

plt.plot(years,weight)

plt.plot(years,weight  , "r--", lw="2")
plt.xlabel("years")
plt.ylabel("weight")

plt.bar(years,weight)

plt.hist(weight)
plt.pie(years,weight)





# PIE CHART 



langs = ["python ","c++", "c#","java"]
votes = ["42 ","25", "19","6"]
explodes =[0,0.1,0,0.1]


# plt.pie(votes , labels=langs ,explode=explodes,autopct="%0.2f%%", pctdistance=1.3  , startangle=180 )
plt.pie(votes , labels=langs )
plt.title("votes to the different languages ")





x1 = np.random.random(50)
y1 = np.random.random(50)
plt.figure(1)

plt.scatter(x1,y1)

plt.figure(2)
plt.plot(x1 ,y1)
plt.figure(3)
plt.bar(x1 ,y1)

# MULTIPLE GRAPH IN SINGLE WINDOW  


x = np.arange(50)


fig, axs = plt.subplots(2,2)
fig.suptitle('four function of maths')

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("sin wave")


axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title("cos wave")


axs[1,0].plot(x,np.tan(x))
axs[1,0].set_title("tan wave")


axs[1,1].plot(x, np.array(x))
axs[1,1].set_title("log wave")
plt.tight_layout()
# plt.savefig("fourplots.png",dpi="300")



# 3D GRAPH 


x1 = np.arange(0,50,0.01)
y1 = np.sin(np.random.randint(50))
z1 = np.cos(x1)


axes = plt.axes(projection="3d")

axes.plot(x1,y1,z1)
axes.set_xlabel("x-axis")
axes.set_ylabel("y-axis")
axes.set_zlabel("z-axis")

# 3D MESHGRID VIEW

axes = plt.axes(projection="3d")

x = np.arange(-1,10,.2)
y = np.arange(-1,10,.2)

a , b = np.meshgrid(x,y)

c = np.sin(a) * np.cos(b)
axes.plot_surface(a,b,c , cmap="Spectral")
plt.show()


