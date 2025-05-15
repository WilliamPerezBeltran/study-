import cv2
import numpy as np
import statistics
import argparse
import math
import pdb


class ProcessPetals():
	def __init__(self, origin_image):
		self.origin_image = origin_image

	def less_contours(self,contours):
		info=[]
		for c in range(len(contours)):
			areas=[]		
			cont_our=contours[c]
			if cv2.contourArea(cont_our)>1000:
				areas.append(c)
				areas.append(cv2.contourArea(cont_our))
				info.append(areas)
		info=sorted(info,key=lambda info:info[1])
		
		return(info)

	def centroid(self,c):
	   good=False
	   M_p=cv2.moments(c)
	   cx=0
	   cy=0
	   if M_p['m00']!=0:
	   	cx=int(M_p['m10']/M_p['m00'])
	   	cy=int(M_p['m01']/M_p['m00'])
	   	good=True
	   
	   return cx,cy,good


	def get_petal_contours(self,img,liminf_fungi,limsup_fungi,liminf_petal,limsup_petal):
		hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		fungi_mask=cv2.inRange(hsv_img,liminf_fungi,limsup_fungi)
		petal_mask=cv2.inRange(hsv_img,liminf_petal,limsup_petal)
		fungi_mask=cv2.medianBlur(fungi_mask,3)
		petal_mask=cv2.medianBlur(petal_mask,3)
		petals_total=cv2.bitwise_or(fungi_mask,petal_mask)
		for k in range(0,1):
			petals_total=cv2.medianBlur(petals_total,11)
		
		contours_total_petal,hierarchy=cv2.findContours(petals_total,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		npet=0
		ratio_tray=[]
		for pet in contours_total_petal:
			
			if cv2.contourArea(pet)>80:
				petal_data=[]
				npet=npet+1
				x_p,y_p,w_p,h_p=cv2.boundingRect(pet)
				c_x_p,c_y_p,flag=self.centroid(pet)
							
				ind_petal_petal=cv2.inRange(hsv_img[y_p:y_p+h_p,x_p:x_p+w_p],liminf_petal,limsup_petal)
				ind_petal_fungi=cv2.inRange(hsv_img[y_p:y_p+h_p,x_p:x_p+w_p],liminf_fungi,limsup_fungi)
				contours_ind_petal,hierarchy=cv2.findContours(ind_petal_petal,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
				contours_ind_fungi,hierarchy=cv2.findContours(ind_petal_fungi,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
				area_p=0
				for pp_1 in contours_ind_petal:
					cv2.drawContours(img[y_p:y_p+h_p,x_p:x_p+w_p],[pp_1],-1,(0,0,255),2)
					area_p=area_p+cv2.contourArea(pp_1)
				area_f=0							
				for ff_1 in contours_ind_fungi:
					cv2.drawContours(img[y_p:y_p+h_p,x_p:x_p+w_p],[ff_1],-1,(0,255,255),2)
					area_f=area_f+cv2.contourArea(ff_1)
				petal_data.append(npet)
				petal_data.append(round((area_f/(area_f+area_p))*100,2))
				petal_data.append(round((area_p/(area_f+area_p))*100,2))
				petal_data.append(0)
				petal_data.append(0)			
				cv2.putText(img, str(npet), (c_x_p,c_y_p), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
				ratio_tray.append(petal_data)
		sum_h=0
		sum_p=0
		if len(ratio_tray)>0:
			for d in ratio_tray:
				sum_h=sum_h+d[1]
				sum_p=sum_p+d[2]
			sum_h=sum_h/len(ratio_tray)
			sum_p=sum_p/len(ratio_tray)
			#nums_v=[]
			num_h=round((sum_h/100)*5,2)
			num_p=round((sum_p/100)*5,2)
			for n_r in ratio_tray:
				n_r[3]=num_h
				n_r[4]=num_p
		
		return ratio_tray,img

	def order_by_origin(self,cnt,idx):
		a=[]
		for x in idx:
			b=[]
			x_cnt=cnt[x]
			cxc,cyc,g=self.centroid(x_cnt)
			d=math.sqrt(cxc*cxc+cyc*cyc)
			b.append(x)
			b.append(d)
			a.append(b)
		
		a=sorted(a,key=lambda a:a[1])
		
		return ([z[0] for z in a ])


	def get_result(self):			
		ap = argparse.ArgumentParser()
		ap.add_argument("-i", "--image", required = True, help = "Path to the image")
		ap.add_argument("-f", "--folder", required = True, help = "Folder destination")
		args = vars(ap.parse_args())
		img=cv2.imread(args["image"])
		print(img.shape)
		img_last_rgb=cv2.resize(img,(1280,960))
		liminf_boxes=(0,0,0)
		limsup_boxes=(124,139,118)
		liminf_fungi=(0,86,6)
		limsup_fungi=(64,255,255)
		liminf_petal=(36,109,26)
		limsup_petal=(183,255,255)

		box_mask=cv2.inRange(img_last_rgb,liminf_boxes,limsup_boxes)
		filtered_boxes=cv2.medianBlur(box_mask,3)
		for i in range(0,20):
			filtered_boxes=cv2.medianBlur(filtered_boxes,3)
		contours_boxes,hierarchy_boxes=cv2.findContours(filtered_boxes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		i=0
		file_info=open(args["folder"]+"results_"+args["image"]+".csv","+w")
		file_info.write("tratamiento,repeticion,individuo,hongo,petalo,NUM_hongo,NUM_petalo\n")
		for m_c in contours_boxes:
		   area_box=cv2.contourArea(m_c)
		   if area_box>10000:
		   	x,y,w,h=cv2.boundingRect(m_c)
		   	c_x,c_y,flag=self.centroid(m_c)
		   	dummy=filtered_boxes[y:y+h,x:x+w]
		   	actual_img=img_last_rgb[y:y+h,x:x+w]
		   	copy_actual_img=actual_img.copy()
		   	i=i+1
		   	
		   	contours_inner,hierarchy_inner=cv2.findContours(dummy,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		   	matrix=self.less_contours(contours_inner)

		   	idx=[]
		   	for y in range(0,3):
		   		try:
		   			idx.append(matrix[y][0])
		   		except:
		   			print("Error:no hubo detección de bandeja")
		   			
		   	idx=self.order_by_origin(contours_inner,idx)
		   	j=0
		   		
		   	for i_c in idx:
		   		cnt_i=contours_inner[i_c]
		   		if cv2.contourArea(cnt_i)>100:
		   			x_1,y_1,w_1,h_1=cv2.boundingRect(cnt_i)
		   			j=j+1
		   			c_x_1,c_y_1,flag=self.centroid(cnt_i)
		   			ratio_matrix,cropped=self.get_petal_contours(copy_actual_img[y_1:y_1+h_1,x_1:x_1+w_1],liminf_fungi,limsup_fungi,liminf_petal,limsup_petal)
		   			actual_img[y_1:y_1+h_1,x_1:x_1+w_1]=cropped
		   			get_data_result = []
		   			for data in ratio_matrix:
		   				file_info.write(str(i)+","+str(j)+","+str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n")
		   				print(str(i)+","+str(j)+","+str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n")
		   				print(i,j,data[0],data[1],data[2],data[3],data[4])
		   				get_data_result.append({
		   					"treatment":i, "repetition":j, "individual":data[0], "fungus":data[1], "petal":data[2], "num_fungus":data[3], "NUM_petal":data[4]
		   					})

		   			
		   			cv2.putText(actual_img, str(j), (c_x_1,c_y_1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
		   			
		   			cv2.putText(img_last_rgb, str(i), (int(c_x-w/2),int(c_y-h/2+20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

   			return {"array":get_data_result,"image_result":img_last_rgb}

			# pdb.set_trace()
			# return {"array":get_data_result,"image_result":img_last_rgb}
		   



   
# print(i)
# cv2.imwrite(args["folder"]+"resultado"+args["image"],img_last_rgb)
# file_info.close()
# print("Done..")

# 	




ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-f", "--folder", required = True, help = "Folder destination")
args = vars(ap.parse_args())
img=cv2.imread(args["image"])

petalos = ProcessPetals(img)
data = petalos.get_result()
pdb.set_trace()