import os
import json
from PIL import Image

json_dir='./vott-json-export/export.json'
if os.path.exists(json_dir):
    with open(json_dir) as json_f:
        json_data=json.load(json_f)

        ids=[]
        for assets in json_data["assets"]:
            ids.append(assets)

        for tag in json_data["tags"]:
            name=tag["name"]

            if not(os.path.isdir('./cropped_image./{}'.format(name))):
                os.makedirs(os.path.join('./cropped_image./{}'.format(name)))
                
        i=1
        for id in ids:
            asset=json_data["assets"]["{}".format(id)]
            img_dir='./vott-json-export/'+asset["asset"]["name"]

            j=1
            for region in asset["regions"]:
                
                tag=region["tags"][0]

                '''
                point=region["points"]
                point_left_below=point[0]
                point_right_above=point[2]

                x1=int(point_left_below["x"])
                y1=int(point_left_below["y"])
                x2=int(point_right_above["x"])
                y2=int(point_right_above["y"])
                '''

                bbox=region["boundingBox"]

                x=bbox["left"]
                y=bbox["top"]
                w=bbox["width"]
                h=bbox["height"]


                with Image.open(img_dir) as img:
                    area=(x, y, x+w, y+h)
                    cropped_img=img.crop(area)

#                    try:
                    cropped_img.save('./cropped_image/{}/cropped_frame{:05d}_{:02d}.bmp'.format(tag,i,j))
#                    except SystemError:
#                       print('\nError occured!\n\nregion_id:{}\ntag:{}\npoint:\n\tx1:{}\n\ty1:{}\n\tx2:{}\n\ty2:{}\n'\
#                            .format(region["id"],tag,x1,y1,x2,y2))
                    print('success to crop {:05d}_{:02d}'.format(i,j))

                j+=1

            i+=1