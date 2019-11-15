# Moodify

This is a project done in the 3rd Semester of University for the course Social Computing.

With the help of crowdsourcing, we wanted to know if there is any correlation between gender, age, personality 
type and sentiment recognization in songs. Spotify is already known for categorizing songs into playlist according to moods, 
however, we wanted to analyze how many people agree with this categorization and if this categorization has any type of bias.


## Set up

The data was collected with the help of a survey on crowdflower (now figure-eight). The user was first asked some
introductionary question on their age and sex. They were also asked to take a short quiz which would categorize them
into a personality group. This should help us profile the workers.
Each song was a lenght of 30 seconds, and were taken out of four playlists of different moods from spotify.
After listening to the preview of the song, the user was then asked to put the song to the category/label he sees most
fit. Additonally, the user had to provide a reasoning, to what led them to believe what the song belongs in the category
of their choice. Here we decided to show some of the user one version of the task, and the other half a different one.
Half the users get to choose their reasoning from a fixed list, the other group had a free form text. We wanted to see, if
having a given list of reasoning would affect the choice of the user.

## Evaluation

The data was processed and evaluated in python. The data can be found in the folders Task1 and Task2, 
the combined data can be found in the folder Combined. The data was evaluated in Python and interactively plotted, so I highly suggest that one downloads and runs the code to access the dynamic version of the plots.

