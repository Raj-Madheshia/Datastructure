def matchfinding(males_ranking, female_ranking):\
    # transpose for making calculation easy
    males_ranking = [[males_ranking[j][i] for j in range(len(males_ranking))] for i in range(len(males_ranking[0]))] 
    
    l = len(males_ranking)
    selected_males = [0]*l
    assign_males =[-1]*l
    for i_index,i in enumerate(males_ranking):
        for index,j in enumerate(i):      
            if not selected_males[index]:
                if assign_males[j-1]==-1:
                    assign_males[j-1] = index+1
                    selected_males[index] =1
                else:
                    rank_by_female =female_ranking[j-1]
                    first = rank_by_female.index(assign_males[j-1])
                    second = rank_by_female.index(index+1)
                    if first > second :
                        
                        selected_males[j-1]=0
                        assign_males[j-1] =  index+1
                        selected_males[index] =1
            
    for index, i in enumerate(assign_males):
        print(index+1,">>>>>Match With<<<<<", i)
        
#a = [[1,3,4,3],[3,4,2,2],[2,1,3,1],[4,2,1,4]]
a =[[1,3,2,4],[3,4,1,2],[4,2,3,1],[3,2,1,4]]
b = [[2,1,3,4], [4,1,2,3], [1,3,2,4],[2,3,1,4]]

a =[[1,2,3,4], [4,3,2,1],[1,2,4,3],[1,3,4,2]]
b = [[3,1,4,2],[1,2,4,3],[1,2,3,4],[2,1,4,3]]
matchfinding(a,b)
