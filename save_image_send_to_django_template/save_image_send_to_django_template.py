import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import base64 
from io import BytesIO
import sys , glob



#define a list to add all pandas queries
img_list = []
fig_list = []
images = []
i = 0


#load csv file into DataFrame
df = pd.read_csv(r'C:/Users/Jyothi/Desktop/waageesh/Python_open_source_codes/save_image_send_to_django_template/course.csv')

#define a virtual figure to save all plots
fig_1 = plt.figure()

#add all pandas queries to list which are used for plot
pandas_queries = [df.groupby('Category')['Status'].count() , df.groupby('Category')['Status'].count()]

#plot and save those plots as images for all pnadas queries
for query in pandas_queries:
    fig_list.append('fig_'+str(i))
    fig_list[i] = plt.figure()
    query.plot.bar()
    fig_list[i].savefig('media/abc_' + str(i) + '.png')
    i +=1

#loop through all images and saving them as base64 string
for img in glob.glob('media/*.png'):
    img = open(img , 'rb')
    img_list.append(base64.b64encode(img.read()))

#loop through all encoded img strings to parse them, that is understandable by html page
for img in img_list:
    images.append(urllib.parse.quote(img))

# -------------------------
# return all parsed images
# return images    
# -------------------------

#check gengerated images exist or not
print(len(img_list[0]) , len(img_list[1]) )
print(img_list[0] == img_list[1] )

# return saved img_list(encoded string format of images) to html page
#def get(self, request):
#    file_path = os.path.abspath('train.csv')
#    list_of_files = glob.glob('/'.join( file_path.split('/')[0:-1])+str('/media')+str('/*')) # * means all if need specific format then *.csv
#    latest_file_url = list_of_files
#    img, img2, img3 =  self.plot_data(latest_file_url)
#    return render(request , 'plot.html' , {'data' : img, 'data2' : img2, 'data3' : img3})

