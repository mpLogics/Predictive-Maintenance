# Predictive-Maintenance
These days, we have manufacturing machines loaded with sensors that provide critical usage data, which record a variety of values such as temperature, velocity and acceleration between regular time intervals. These sensors may also provide a computed damage accumulation measure, which is helpful for predictive maintenance which monitors asset performance during normal operation to anticipate and predict failures. This also allows maintenance teams to correct the issue before a failure occurs. 
Rather than running a part to failure or replacing it when it still has life because of protocols, predictive maintenance helps organizations optimize their strategies by conducting maintenance only when completely necessary.

There are multiple approaches for effective predictive maintainence:
- Slot-wise Prediction : Analyze and predict damage accumulation before every slot. Then allot slot.
- 2-day Prediction : Analyze and predict damage accumulation for finite number of days and schedule maintenance accordingly so as to minimize reduction of working hours.
- (Chosen approach) Weekly Prediction : Analyze and predict damage accumulation for the next week and schedule maintenance accordingly.

The chosen approach enables the user to monitor day-wise analysis, calculate weekly average, greater buffer time for machine repair, considering the off timings and weekends.

The following image shows the working model for calculation of damage accumulation:
![image](https://user-images.githubusercontent.com/99707960/154849880-d85d29a8-a14c-4ccc-8eed-fee6c2417b38.png)

The damage accumulation thus calculated will be used to predict the wear and tear of the machine, and further predict as to when it will stop working or would need an immediate repair work.
This process is advantegous considering the outcome _tends to no downtime_ with the machine and productivity increases.

This Repo also contains a **SAM(Student Activity Management) Scheduler**. 
It helps in finding a slot for people who want to work on a particular machine. It takes the following inputs:
- Number of projects required to be done on the machine, with the project names obviously
- Time required by each project
- Deadline for each project
- Number of days the machine would be operational
- Number of hours the machine would be working in a day

With all the above info it prioritizes the different tasks and assigns 1 hour slot to each and every project accordingly. It can also be helpful to find out whether the number of projects with their particular deadlines are feasible or not. As it may happen some of the project require a lot of time and because of deadline issues, it may not be possible to accomodate all of the projects. So the associated people could take decisions early on, rather than starting the work and finding out near the deadline.
