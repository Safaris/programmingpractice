#solution to problem found at http://www.reddit.com/r/dailyprogrammer/comments/29i9jw/6302014_challenge_169_easy_90_degree_2d_array/
#By Sean Safari
def rotate(n):
    n2=[[row[(i)] for row in reversed(n)] for i in range(len(n))]
    return n2

#matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix=[[1,2,3,4,5,6,7,8,9,0],[0,9,8,7,6,5,4,3,2,1],[1,3,5,7,9,2,4,6,8,0],[0,8,6,4,2,9,7,5,3,1],
        [0,1,2,3,4,5,4,3,2,1],[9,8,7,6,5,6,7,8,9,0],[1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2],
        [9,8,7,6,7,8,9,8,7,6],[0,0,0,0,0,0,0,0,0,0]]
degreenum=int(input("Enter degree of rotation \n"))
mod=degreenum%90
num=int(degreenum/90)
print(num)
if mod!=0:
    print("Degree entered not a multiple of 90 degrees. Exiting.")
else:
    for i in range(0,num,1):
        matrix=rotate(matrix)
    for i in range(len(matrix)):
        print(matrix[i])