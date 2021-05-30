# Powerlifting Training Log

# Project Overview
This powerlifting training log will be a site where users can come, sign into their profiles which they create, and then upload their training sessions to a database. Powerlifters love data, so the handling and management of this data will be a key consideration of the site. Regarding this, there are several metrics which will be calculated following each session such as the peak intensity of 1 repetition maximum, the total volume load in that particular session , training load, and estimated 1 repetition maximum on a set by set basis. These metrics will allow users to make informed decisions regarding their training. Another key consideration for the site will be making the site easy to use on mobile, as lots of the users will want to upload their session as soon as they have completed it, while still in the gym. Finally, I want the user to enjoy coming to log their training as this can be a cumbersome task on similar logging apps, therefore, ease of use and a beautiful design will be critical to the success of this project. 
# UX
## 5 Planes of UX
### Surface Plane
This site is being created to meet the needs of powerlifters specifically. As a powerlifter myself and a sports science graduate, I understand the importance of data as it relates to sport performance and training. Being precise with the stimulus that is applied during each training session will allow for more predictable results and a lower likelihood of injury. Also a grearter history of data will allow for more accurate predictions of future responses to training. Furthermore, powerlifters compete in the three main lifts which are the squat, the bench press, and the deadlift. While these are only three exercises, there are actually so many modifications of these exercises which most powerlifters regularly train. Keeping track of your performance in a distant variation of the main lift is a very important thing which is quite hard to do. Therefore, this app will be an easy way to look back over your performance in these more obscure lifts such as the 3 1 0 tempo, beltless, high bar squat. It will also allow the user to easily see their performance in the main lift which in this case is the low bar squat with a belt. 
### Scope Plane
#### Features
1) This project will require a registration, sign in, and sign out functionality. The ability to sign in is critical to allow the user to be able to look back at their old data which is the whole purpose of this app. 
2) This project will require the ability to run calculations on the data given to it and populate tables with this newly generated data. These data will be interpreted by the user 
3) The CRUD accronym will apply here, so the user will be able to create, read, update and delete their own data. 
4) There will be an admin user who can overlook all of the data stored in the database. 
5) The data entry form must be user friendly and be relatively intuitive
### Structure
The main landing page of the site will be the sign in page. Users will then be redirected to their personal dashboard, which will have some information on prior sessions if they have any. The only real place users will be able to go from here is either the sign out page or the log session page. The log session page will be intuitive and have several pages of forms which the user has to navigate through to log a session successfully. Following this they will be shown their session recap and be redirected to their dashboard. There may be another page which will offer them coaching advice/ general information on what to do with the metrics supplied by the app. 
### Skeleton 
### Surface





### User stories
On opening the app the user will be immediately prompted to sign in or register. Then the user will be redirected to their personal dashboard which will have details on their prior sessions. There will be a large button asking them if they would like to log a new session. On the session logging screen they will be asked for the start and end times of the session and a few words of a description which will be optional. Next they are asked what their first exercise was, they will then select the modifiers that apply to that exercise. Finally they will be asked how many sets they completed and then they will click the next button. On the next page they will input the reps completed, the weight, and the RPE which stands for rating of perceived exertion which is a very well known metric in powerlifting circles. They will repeat these steps for the other exercises they completed during that session. Then they will just click the log session button to finish inputting the session. They will receive a flash message at this point thanking them for logging the session and they will be shown the advanced metrics I discussed above, which will act like a session recap. 