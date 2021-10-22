import matplotlib.pyplot as plt
def plot(teacher_score_li, final_score_li):
	radius = [x for x in range(1, 25)]
	#teacher_score_li = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
	#final_score_li = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
	plt.plot(radius, teacher_score_li, label='Teacher-Score')
	plt.plot(radius, final_score_li, marker='o', linestyle='--', color='r', label='Threshold-Score')
	plt.xlabel('Teacher-Score')
	plt.ylabel('Scores')
	plt.title('Project Accuracy')
	plt.legend()
	plt.show()



