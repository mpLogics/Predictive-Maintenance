import numpy as np
import math

class scheduler():
    def __init__(self):
        self.duration = [11,14,10,8,15,12]
        self.deadlines = [5,3,3,4,5,2]
        self.project_names = [1,2,3,4,5,6]
        self.total_projects = len(self.duration)
        self.project_hrs = sum(self.duration)
        self.available = 15
        self.days = 5
        self.feasible = True
        self.project = []
        self.nfp = []
        self.operational_days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    
    def high_level_feasibility_check(self):
        if (self.project_hrs > self.available*self.days):
            print("The projects completion is not possible")
            self.feasible = False
    
    def low_level_feasibility_check(self):
        i=0
        while i<len(self.project):
            count = 1
            c = self.project[i][1]
            s = self.project[i][0]
            for j in range(i+1,len(self.project)):
                if (self.project[j][1] == c):
                    count+=1
                    s += self.project[j][0]
                else:
                    break
            if (s > self.available * count):
                self.feasible = False
                while self.project[i][1] == c:
                    self.nfp.append(i)
                    i+=1
            i+=1

        if not self.feasible:
            print("The following projects are not feasible:")
            for i in range(len(self.nfp)):
                print("Project",self.nfp[i]+1,",",end="")
            print()
        assert self.feasible
    
    def setup_project_matrix(self):
        for i in range(self.total_projects):
            self.project.append([self.duration[i], self.deadlines[i], self.project_names[i]])
        self.project.sort(key=lambda x : x[1])
        
    
    def allot_slots(self):
        self.high_level_feasibility_check()
        self.setup_project_matrix()
        self.low_level_feasibility_check()
        
        available_slots_per_day = [self.available] * self.days
        week_slots = np.array([["Empty"] * self.available] * self.days)
        i=0
        start = 0

        while i<len(self.project):
            c = self.project[i][1]
            group = []
            group.append(i)
            for j in range(i+1, len(self.project)):
                if (self.project[j][1] == c):
                    group.append(j)
                    i+=1
                else:
                    break
            hrs = 0
            for g in group:
                hrs += self.project[g][0]

            tday = 0
            while hrs>0:
                division = math.ceil(hrs/c)
                temp = []
                s = 0
                for g in range(len(group)):
                    if g != len(group)-1:
                        calc = math.ceil(self.project[group[g]][0]/hrs * division)
                        s += calc
                        temp.append([group[g], calc])
                    else:
                        temp.append([group[g], division - s])

                flag = True
                for t in temp:
                    x = self.available - available_slots_per_day[tday]
                    e = x
                    while e<self.available and e<x+t[1]:
                        week_slots[tday][e] = self.project[t[0]][2]
                        e+=1
                    if (x+t[1] <= self.available):
                        available_slots_per_day[tday] -= t[1]
                        hrs -= t[1]
                        self.project[t[0]][0] -= t[1]
                    else:
                        available_slots_per_day[tday] = 0
                        hrs -= (self.available-x)
                        self.project[t[0]][0] -= (self.available-x)
                    self.project[t[0]][1] -= 1
                c-=1
                tday+=1
            i+=1
        return week_slots
    
    def display_alloted_slots(self):
        weekly_slots = self.allot_slots()
        presentable_weekly_slots = []

        for i in range(len(weekly_slots)):
            temporary = []
            for j in range(len(weekly_slots[i])):
                if (weekly_slots[i][j]!="Empty"): temporary.append("P" + weekly_slots[i][j])
                else: temporary.append(weekly_slots[i][j])
            presentable_weekly_slots.append(temporary)

        for i in range(len(presentable_weekly_slots)):
            print(self.operational_days[i])
            print(presentable_weekly_slots[i])